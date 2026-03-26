# Contributing

## Prerequisites

- Ruby 3.1+ on your `PATH`
- Bundler 2

Check your environment before you start:

```bash
ruby -v
bundle -v
```

If `ruby -v` shows `/usr/bin/ruby` or Ruby 2.6 on macOS, switch to a newer Ruby before continuing.

## Setup

Install project dependencies into `vendor/bundle`:

```bash
make install
```

Run the site locally:

```bash
make serve
```

Create a production-style build:

```bash
make build
```

## Project Conventions

- Keep changes focused and easy to review.
- Preview content and layout changes locally before opening a PR.
- Put homepage content in `_sections/`.
- Put blog posts in `_posts/` with valid front matter.
- Put shared template changes in `_layouts/` or `_includes/`.
- Put internal-only notes or authoring guides in `_internal/` so Jekyll does not publish them.
- Keep large generated or vendored files out of commits.

## Before Opening a PR

- Run `make build`
- Review the affected pages locally
- Update docs when the local workflow changes

## Notes

- The bundle is installed into `vendor/bundle`.
- Local Bundler config is stored in `.bundle/`.
- Both paths are already ignored by Git.
