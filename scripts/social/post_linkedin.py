#!/usr/bin/env python3
import argparse
import json
import os
import sys
import urllib.error
import urllib.request


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


def parse_args():
    parser = argparse.ArgumentParser(description="Publish a post to LinkedIn via the Posts API.")
    parser.add_argument("--text", required=True, help="Post commentary text.")
    parser.add_argument("--article-url", help="Optional article URL for an article-style post.")
    parser.add_argument("--title", help="Article title when --article-url is used.")
    parser.add_argument("--description", help="Article description when --article-url is used.")
    parser.add_argument("--thumbnail-urn", help="Optional LinkedIn image URN for article thumbnail.")
    return parser.parse_args()


def build_payload(args, author_urn):
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
            "title": (args.title or args.article_url).strip(),
            "description": (args.description or "").strip(),
        }
        if args.thumbnail_urn:
            article["thumbnail"] = args.thumbnail_urn.strip()
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

    payload = json.dumps(build_payload(args, author_urn)).encode("utf-8")
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
            print(body)
            return 0
    except urllib.error.HTTPError as exc:
        error_body = exc.read().decode("utf-8", errors="replace")
        print(error_body, file=sys.stderr)
        return exc.code or 1


if __name__ == "__main__":
    raise SystemExit(main())
