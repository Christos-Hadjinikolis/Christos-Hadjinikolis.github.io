#!/usr/bin/env python3
import argparse
import json
import mimetypes
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from html.parser import HTMLParser


def load_dotenv(path=".env"):
    if not os.path.exists(path):
        return
    with open(path, "r", encoding="utf-8") as handle:
        for raw_line in handle:
            line = raw_line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip())


class MetaTagParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.meta = {}

    def handle_starttag(self, tag, attrs):
        if tag.lower() != "meta":
            return
        attributes = {key.lower(): value for key, value in attrs if key and value}
        key = attributes.get("property") or attributes.get("name")
        content = attributes.get("content")
        if not key or not content:
            return
        self.meta.setdefault(key.lower(), content.strip())


def parse_args():
    parser = argparse.ArgumentParser(description="Publish a post to LinkedIn via the Posts API.")
    parser.add_argument("--delete-post-urn", help="Delete an existing LinkedIn post/share URN instead of creating one.")
    parser.add_argument("--text", help="Post commentary text.")
    parser.add_argument("--article-url", help="Optional article URL for an article-style post.")
    parser.add_argument("--title", help="Article title when --article-url is used.")
    parser.add_argument("--description", help="Article description when --article-url is used.")
    parser.add_argument("--thumbnail-urn", help="Optional LinkedIn image URN for article thumbnail.")
    parser.add_argument("--thumbnail-url", help="Optional public image URL to upload as the article thumbnail.")
    args = parser.parse_args()
    if not args.delete_post_urn and not args.text:
        parser.error("--text is required unless --delete-post-urn is used.")
    return args


def read_response_body(handle):
    return handle.read().decode("utf-8", errors="replace")


def request_json(url, *, method="GET", headers=None, data=None):
    request = urllib.request.Request(url, data=data, method=method, headers=headers or {})
    with urllib.request.urlopen(request) as response:
        body = read_response_body(response)
        return response, json.loads(body) if body else {}


def infer_article_metadata(article_url):
    request = urllib.request.Request(
        article_url,
        headers={"User-Agent": "Mozilla/5.0"},
        method="GET",
    )
    with urllib.request.urlopen(request) as response:
        html = read_response_body(response)

    parser = MetaTagParser()
    parser.feed(html)
    meta = parser.meta
    image_url = meta.get("og:image") or meta.get("twitter:image")
    if image_url:
        image_url = urllib.parse.urljoin(article_url, image_url)

    return {
        "title": meta.get("og:title") or meta.get("twitter:title"),
        "description": meta.get("og:description") or meta.get("twitter:description") or meta.get("description"),
        "image_url": image_url,
    }


def fetch_binary(url):
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0"},
        method="GET",
    )
    with urllib.request.urlopen(request) as response:
        content_type = response.headers.get_content_type() or mimetypes.guess_type(url)[0] or "application/octet-stream"
        return response.read(), content_type


def initialize_image_upload(token, author_urn, version):
    payload = json.dumps({"initializeUploadRequest": {"owner": author_urn}}).encode("utf-8")
    response, body = request_json(
        "https://api.linkedin.com/rest/images?action=initializeUpload",
        method="POST",
        data=payload,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Linkedin-Version": version,
            "X-Restli-Protocol-Version": "2.0.0",
        },
    )
    value = body.get("value", {})
    upload_url = value.get("uploadUrl")
    image_urn = value.get("image")
    if not upload_url or not image_urn:
        raise RuntimeError(f"Unexpected LinkedIn image upload initialization response: status={response.status}, body={body}")
    return upload_url, image_urn


def upload_image(upload_url, image_bytes, content_type):
    request = urllib.request.Request(
        upload_url,
        data=image_bytes,
        method="PUT",
        headers={
            "Content-Type": content_type,
            "Content-Length": str(len(image_bytes)),
        },
    )
    with urllib.request.urlopen(request):
        return


def resolve_thumbnail_urn(args, token, author_urn, version):
    if args.thumbnail_urn:
        return args.thumbnail_urn.strip(), None

    image_source_url = args.thumbnail_url.strip() if args.thumbnail_url else None
    inferred_metadata = None
    if args.article_url and not image_source_url:
        inferred_metadata = infer_article_metadata(args.article_url.strip())
        image_source_url = inferred_metadata.get("image_url")

    if not image_source_url:
        return None, inferred_metadata

    image_bytes, content_type = fetch_binary(image_source_url)
    upload_url, image_urn = initialize_image_upload(token, author_urn, version)
    upload_image(upload_url, image_bytes, content_type)
    return image_urn, inferred_metadata


def build_payload(args, author_urn, *, inferred_metadata=None, thumbnail_urn=None):
    payload = {
        "author": author_urn,
        "commentary": args.text.strip(),
        "visibility": "PUBLIC",
        "distribution": {
            "feedDistribution": "MAIN_FEED",
            "targetEntities": [],
            "thirdPartyDistributionChannels": [],
        },
        "lifecycleState": "PUBLISHED",
        "isReshareDisabledByAuthor": False,
    }

    if args.article_url:
        article = {
            "source": args.article_url.strip(),
            "title": (args.title or (inferred_metadata or {}).get("title") or args.article_url).strip(),
            "description": (args.description or (inferred_metadata or {}).get("description") or "").strip(),
        }
        if thumbnail_urn:
            article["thumbnail"] = thumbnail_urn.strip()
        payload["content"] = {"article": article}

    return payload


def main():
    load_dotenv()
    args = parse_args()

    token = os.getenv("LINKEDIN_ACCESS_TOKEN", "").strip()
    author_urn = os.getenv("LINKEDIN_AUTHOR_URN", "").strip()
    version = os.getenv("LINKEDIN_VERSION", "").strip()

    if not token:
        print("Missing LINKEDIN_ACCESS_TOKEN in .env or environment.", file=sys.stderr)
        return 1
    if not author_urn:
        print("Missing LINKEDIN_AUTHOR_URN in .env or environment.", file=sys.stderr)
        return 1
    if not version:
        print("Missing LINKEDIN_VERSION in .env or environment.", file=sys.stderr)
        return 1

    if args.delete_post_urn:
        encoded_urn = urllib.parse.quote(args.delete_post_urn.strip(), safe="")
        request = urllib.request.Request(
            f"https://api.linkedin.com/rest/posts/{encoded_urn}",
            method="DELETE",
            headers={
                "Authorization": f"Bearer {token}",
                "Linkedin-Version": version,
                "X-Restli-Protocol-Version": "2.0.0",
                "X-RestLi-Method": "DELETE",
            },
        )

        try:
            with urllib.request.urlopen(request) as response:
                print(json.dumps({"status": response.status, "deleted": args.delete_post_urn.strip()}))
                return 0
        except urllib.error.HTTPError as exc:
            error_body = exc.read().decode("utf-8", errors="replace")
            print(error_body, file=sys.stderr)
            return exc.code or 1

    try:
        thumbnail_urn, inferred_metadata = resolve_thumbnail_urn(args, token, author_urn, version)
    except urllib.error.HTTPError as exc:
        error_body = exc.read().decode("utf-8", errors="replace")
        print(error_body, file=sys.stderr)
        return exc.code or 1
    except urllib.error.URLError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    payload = json.dumps(
        build_payload(args, author_urn, inferred_metadata=inferred_metadata, thumbnail_urn=thumbnail_urn)
    ).encode("utf-8")
    request = urllib.request.Request(
        "https://api.linkedin.com/rest/posts",
        data=payload,
        method="POST",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Linkedin-Version": version,
            "X-Restli-Protocol-Version": "2.0.0",
        },
    )

    try:
        with urllib.request.urlopen(request) as response:
            body = response.read().decode("utf-8")
            result = {
                "status": response.status,
                "x_restli_id": response.headers.get("x-restli-id"),
                "location": response.headers.get("location"),
                "thumbnail_urn": thumbnail_urn,
                "inferred_thumbnail_url": (inferred_metadata or {}).get("image_url"),
                "body": body,
            }
            print(json.dumps(result))
            return 0
    except urllib.error.HTTPError as exc:
        error_body = exc.read().decode("utf-8", errors="replace")
        print(error_body, file=sys.stderr)
        return exc.code or 1


if __name__ == "__main__":
    raise SystemExit(main())
