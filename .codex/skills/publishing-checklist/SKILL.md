---
name: publishing-checklist
description: Use when preparing to publish or review changes for this repository's website or blog. Applies to pre-publish QA, content release checks, accidental page exposure checks, metadata review, and final verification before merging or deploying site changes.
---

# Publishing Checklist

Use this skill for final review before publishing website or blog changes in this repository.

## Checklist

1. Confirm the changed files are in the expected locations.
2. Check that internal-only docs are not publishable.
3. Review front matter on changed pages or posts.
4. Check navigation impact for any new or reordered pages or sections.
5. Check links, asset paths, and image references in changed content.
6. Check analytics/config changes for obvious mistakes.
7. Check that the 404 page, feed references, and canonical behavior still make sense when touched.

## Build Verification

When the environment supports it:

- Run `make build`.
- Run `make audit`.
- Inspect the top-level output in `_site/` for accidental repo docs or unexpected pages.

## Content Verification

For posts:

- Title is strong and not generic.
- Front matter is valid.
- `description`, canonical URL, and share image metadata are correct.
- `og_image` is suitable for social sharing and points to a real preview asset.
- Slug/date behavior is intentional.
- The post matches the editorial guidance in `_internal/authoring/`.
- If the post will be announced on LinkedIn/X, deploy the page first, then publish the social post, then add/embed the discussion thread in a follow-up pass if desired.

For site changes:

- The page appears where expected in nav.
- Hidden or internal content does not leak into rendered sections.
- Contact, analytics, and social links still reflect current intent.

## Reporting

When reviewing for publish readiness, lead with concrete blockers first.
If something cannot be verified because the local environment is broken, state that explicitly instead of implying a clean pass.
