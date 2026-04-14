#!/usr/bin/env python3
"""Fail publication checks when post social preview images are missing."""

from __future__ import annotations

import datetime as dt
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
POST_DIRS = (ROOT / "content" / "_posts", ROOT / "content" / "review-room")
LOCAL_POST_IMAGE_RE = re.compile(r"assets/images/posts/[^'\"\)\s]+")
FRONT_MATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)
DATE_PREFIX_RE = re.compile(r"(\d{4}-\d{2}-\d{2})-")


def parse_front_matter(text: str) -> dict[str, str]:
    match = FRONT_MATTER_RE.match(text)
    if not match:
        return {}

    values: dict[str, str] = {}
    for raw_line in match.group(1).splitlines():
        if ":" not in raw_line or raw_line.startswith((" ", "\t", "-")):
            continue
        key, value = raw_line.split(":", 1)
        values[key.strip()] = value.strip().strip("'\"")
    return values


def post_date(path: Path, front_matter: dict[str, str]) -> dt.date | None:
    filename_date = DATE_PREFIX_RE.match(path.name)
    value = filename_date.group(1) if filename_date else front_matter.get("date")
    if not value:
        return None
    try:
        return dt.date.fromisoformat(value[:10])
    except ValueError:
        return None


def is_remote(path_value: str) -> bool:
    return path_value.startswith(("http://", "https://"))


def local_path_exists(path_value: str) -> bool:
    return (ROOT / path_value.lstrip("/")).exists()


def main() -> int:
    today = dt.date.today()
    failures: list[str] = []

    files: list[Path] = []
    for post_dir in POST_DIRS:
        if post_dir.exists():
            files.extend(sorted(post_dir.glob("*.md")))

    for path in files:
        text = path.read_text(encoding="utf-8")
        front_matter = parse_front_matter(text)
        if front_matter.get("layout") != "post":
            continue

        relative_path = path.relative_to(ROOT)
        current_post_date = post_date(path, front_matter)
        is_publishable_now = current_post_date is not None and current_post_date <= today
        has_social_post = any(
            front_matter.get(key)
            for key in ("linkedin_post_url", "linkedin_embed_url", "substack_post_url")
        )
        post_images = LOCAL_POST_IMAGE_RE.findall(text)
        has_article_image = bool(post_images)
        og_image = front_matter.get("og_image", "")

        needs_og_image = is_publishable_now or has_social_post or has_article_image
        if needs_og_image and not og_image:
            reason_parts = []
            if is_publishable_now:
                reason_parts.append("publishable now")
            if has_social_post:
                reason_parts.append("has social links")
            if has_article_image:
                reason_parts.append("contains article images")
            failures.append(
                f"{relative_path}: missing og_image ({', '.join(reason_parts)}). "
                "Set it explicitly; do not rely on the site avatar fallback."
            )
            continue

        if og_image and not is_remote(og_image) and not local_path_exists(og_image):
            failures.append(f"{relative_path}: og_image does not exist: {og_image}")

        if og_image.startswith("assets/images/site/") and has_article_image:
            failures.append(
                f"{relative_path}: og_image points at a site-level image while the "
                "article contains post imagery. Use a post-specific preview image."
            )

    if failures:
        print("Post social image audit failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    print("Post social image audit passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
