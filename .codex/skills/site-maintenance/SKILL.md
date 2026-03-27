---
name: site-maintenance
description: Use when maintaining or modifying the structure, templates, styling, navigation, configuration, analytics, or content publishing behavior of this Jekyll website. Applies to layout fixes, page additions, homepage section changes, internal-doc exposure issues, and general repository hygiene for the site.
---

# Site Maintenance

Use this skill for structural or operational changes to this repository's Jekyll site.

## Repo Map

- `_config.yml`: site configuration
- `content/_sections/`: homepage sections
- `content/_posts/`: blog posts
- `content/pages/`: standalone pages
- `_layouts/` and `_includes/`: templates and shared partials
- `assets/`: CSS, JS, images, PDFs
- `_internal/`: private docs that must never become site pages

## Workflow

1. Inspect the relevant layout, include, and content files before editing.
2. Prefer fixing behavior at the config or template level over one-off content hacks.
3. Preserve the site's existing Jekyll/Prologue structure unless the user asks for a broader redesign.
4. Be alert for accidental publication of repo-only files.
5. When changing navigation or homepage sections, check both the header nav and rendered section list.

## Guardrails

- Do not put private docs in publishable locations.
- Treat `_internal/` as non-published content.
- Be careful with front matter, permalinks, and `order` values on pages and sections.
- Keep generated-site concerns in mind: URLs, feeds, 404 handling, analytics, and page discoverability.
- Prefer `relative_url` or `absolute_url` filters consistently when editing links in templates.

## Validation

When the environment supports it, use the Makefile targets:

- `make build`
- `make audit`

If local Ruby/Bundler is misconfigured, explain the limitation clearly and still verify as much as possible through source inspection.
