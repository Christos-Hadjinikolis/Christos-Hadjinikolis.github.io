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
    parser = argparse.ArgumentParser(description="Publish a post to X via the X API.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--text", help="Post body text.")
    group.add_argument("--text-file", help="Path to a UTF-8 file containing the post body.")
    return parser.parse_args()


def read_text(args):
    if args.text:
        return args.text.strip()
    with open(args.text_file, "r", encoding="utf-8") as handle:
        return handle.read().strip()


def main():
    load_dotenv()
    args = parse_args()
    text = read_text(args)
    token = os.getenv("X_ACCESS_TOKEN", "").strip()

    if not token:
        print("Missing X_ACCESS_TOKEN in .env or environment.", file=sys.stderr)
        return 1

    if not text:
        print("Post body is empty.", file=sys.stderr)
        return 1

    payload = json.dumps({"text": text}).encode("utf-8")
    request = urllib.request.Request(
        "https://api.x.com/2/tweets",
        data=payload,
        method="POST",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
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
