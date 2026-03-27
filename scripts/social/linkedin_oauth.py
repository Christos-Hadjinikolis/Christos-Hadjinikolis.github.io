#!/usr/bin/env python3
import argparse
import base64
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request


ENV_PATH = ".env"


def load_dotenv(path=ENV_PATH):
    if not os.path.exists(path):
        return
    with open(path, "r", encoding="utf-8") as handle:
        for raw_line in handle:
            line = raw_line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip())


def upsert_env(key, value, path=ENV_PATH):
    lines = []
    found = False
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as handle:
            lines = handle.read().splitlines()
    for i, raw in enumerate(lines):
        stripped = raw.strip()
        if not stripped or stripped.startswith("#") or "=" not in raw:
            continue
        existing_key = raw.split("=", 1)[0].strip()
        if existing_key == key:
            lines[i] = f"{key}={value}"
            found = True
            break
    if not found:
        if lines and lines[-1].strip():
            lines.append("")
        lines.append(f"{key}={value}")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write("\n".join(lines) + "\n")


def require_env(name):
    value = os.getenv(name, "").strip()
    if not value:
        raise SystemExit(f"Missing {name} in .env or environment.")
    return value


def http_json(url, method="GET", data=None, headers=None):
    request = urllib.request.Request(url, data=data, method=method, headers=headers or {})
    with urllib.request.urlopen(request) as response:
        return json.loads(response.read().decode("utf-8"))


def decode_jwt_payload(token):
    parts = token.split(".")
    if len(parts) != 3:
        return {}
    payload = parts[1]
    payload += "=" * (-len(payload) % 4)
    try:
        decoded = base64.urlsafe_b64decode(payload.encode("utf-8")).decode("utf-8")
        return json.loads(decoded)
    except Exception:
        return {}


def parse_args():
    parser = argparse.ArgumentParser(description="LinkedIn OAuth helpers for local posting setup.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("auth-url", help="Print the LinkedIn authorization URL.")

    exchange = subparsers.add_parser("exchange-code", help="Exchange an auth code for an access token.")
    exchange.add_argument("--code", required=True, help="Authorization code returned by LinkedIn.")
    exchange.add_argument("--write-env", action="store_true", help="Write LINKEDIN_ACCESS_TOKEN into .env.")

    whoami = subparsers.add_parser("whoami", help="Resolve the authenticated member id and author URN.")
    whoami.add_argument("--write-env", action="store_true", help="Write LINKEDIN_AUTHOR_URN into .env.")

    return parser.parse_args()


def command_auth_url():
    client_id = require_env("LINKEDIN_CLIENT_ID")
    redirect_uri = require_env("LINKEDIN_REDIRECT_URI")
    scopes = os.getenv("LINKEDIN_SCOPES", "openid profile w_member_social").strip()
    params = {
        "response_type": "code",
        "client_id": client_id,
        "redirect_uri": redirect_uri,
        "scope": scopes,
    }
    print("https://www.linkedin.com/oauth/v2/authorization?" + urllib.parse.urlencode(params))


def command_exchange_code(args):
    client_id = require_env("LINKEDIN_CLIENT_ID")
    client_secret = require_env("LINKEDIN_CLIENT_SECRET")
    redirect_uri = require_env("LINKEDIN_REDIRECT_URI")

    payload = urllib.parse.urlencode(
        {
            "grant_type": "authorization_code",
            "code": args.code.strip(),
            "client_id": client_id,
            "client_secret": client_secret,
            "redirect_uri": redirect_uri,
        }
    ).encode("utf-8")

    try:
        response = http_json(
            "https://www.linkedin.com/oauth/v2/accessToken",
            method="POST",
            data=payload,
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )
    except urllib.error.HTTPError as exc:
        error_body = exc.read().decode("utf-8", errors="replace")
        print(error_body, file=sys.stderr)
        raise SystemExit(exc.code or 1)

    token = response.get("access_token", "").strip()
    refresh_token = response.get("refresh_token", "").strip()
    id_token = response.get("id_token", "").strip()
    id_payload = decode_jwt_payload(id_token) if id_token else {}
    person_id = id_payload.get("sub", "").strip()
    if args.write_env and token:
        upsert_env("LINKEDIN_ACCESS_TOKEN", token)
    if args.write_env and refresh_token:
        upsert_env("LINKEDIN_REFRESH_TOKEN", refresh_token)
    if args.write_env and id_token:
        upsert_env("LINKEDIN_ID_TOKEN", id_token)
    if args.write_env and person_id:
        upsert_env("LINKEDIN_AUTHOR_URN", f"urn:li:person:{person_id}")

    print(json.dumps(response, indent=2))


def command_whoami(args):
    token = require_env("LINKEDIN_ACCESS_TOKEN")
    id_token = os.getenv("LINKEDIN_ID_TOKEN", "").strip()
    if id_token:
        id_payload = decode_jwt_payload(id_token)
        person_id = id_payload.get("sub", "").strip()
        if person_id:
            author_urn = f"urn:li:person:{person_id}"
            result = {"person_id": person_id, "author_urn": author_urn, "raw": id_payload}
            if args.write_env:
                upsert_env("LINKEDIN_AUTHOR_URN", author_urn)
            print(json.dumps(result, indent=2))
            return

    headers = {"Authorization": f"Bearer {token}"}

    person_id = None
    payload = None

    try:
        payload = http_json("https://api.linkedin.com/v2/userinfo", headers=headers)
        person_id = payload.get("sub", "").strip()
    except urllib.error.HTTPError:
        payload = None

    if not person_id:
        try:
            payload = http_json("https://api.linkedin.com/v2/me", headers=headers)
            person_id = payload.get("id", "").strip()
        except urllib.error.HTTPError as exc:
            error_body = exc.read().decode("utf-8", errors="replace")
            print(error_body, file=sys.stderr)
            raise SystemExit(exc.code or 1)

    if not person_id:
        raise SystemExit("Could not determine LinkedIn member id from /v2/userinfo or /v2/me.")

    author_urn = f"urn:li:person:{person_id}"
    result = {"person_id": person_id, "author_urn": author_urn, "raw": payload}

    if args.write_env:
        upsert_env("LINKEDIN_AUTHOR_URN", author_urn)

    print(json.dumps(result, indent=2))


def main():
    load_dotenv()
    args = parse_args()
    if args.command == "auth-url":
        command_auth_url()
        return 0
    if args.command == "exchange-code":
        command_exchange_code(args)
        return 0
    if args.command == "whoami":
        command_whoami(args)
        return 0
    raise SystemExit(f"Unknown command: {args.command}")


if __name__ == "__main__":
    raise SystemExit(main())
