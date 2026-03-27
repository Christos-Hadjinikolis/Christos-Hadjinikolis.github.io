# Christos-Hadjinikolis.github.io

Personal website and blog built with Jekyll and the `jekyll-theme-prologue` theme.

## Stack

- Jekyll 4
- Ruby 3.1+ (`.ruby-version` pins `3.1.2`)
- Bundler 2

## Repository Layout

- `content/_sections/`: homepage sections
- `content/_posts/`: blog posts
- `content/pages/`: standalone site pages
- `content/reading/`: reading-list page source
- `content/index.md`: homepage entrypoint
- `_layouts/` and `_includes/`: Jekyll templates and shared partials
- `_internal/`: non-published internal docs and authoring guides
- `assets/`: images, PDFs, CSS, and JavaScript
- `Makefile`: local development shortcuts

## Local Development

### Prerequisites

- Ruby 3.1 or newer available on your `PATH`
- Bundler 2 installed for that Ruby

On macOS, avoid the system Ruby at `/usr/bin/ruby`. This project will not install cleanly with Ruby 2.6.

Verify your environment:

```bash
ruby -v
bundle -v
```

### Quick Start

Install gems into `vendor/bundle` inside the repository:

```bash
make install
```

Start the site locally with live reload:

```bash
make serve
```

Open:

```text
http://127.0.0.1:4000
```

### Other Useful Commands

```bash
make help
make doctor
make build
make audit
make clean
make install-hooks
```

## Social Publishing

The repository includes a small social publishing scaffold under `scripts/social/`.

- `X` and `LinkedIn` have official post APIs and are the only platforms wired for direct publishing here.
- `Medium` is no longer a good foundation for new API integrations; Medium says it does not issue new integration tokens for the API.
- `Substack` still does not offer a public write API for publication posting, so treat it as a manual syndication target.

Secrets should live in a local `.env` file that is gitignored. Copy `.env.example` and fill in only the values you need.

See [scripts/social/README.md](scripts/social/README.md) for setup and usage.

## Troubleshooting

### Bundler says the lockfile requires Bundler 2

Install a Bundler 2 release for the active Ruby:

```bash
gem install bundler:2.1.4 --user-install
```

### `bundle install` fails with Ruby version errors

Your shell is likely using the macOS system Ruby. Switch to Ruby 3.1+ first, then rerun:

```bash
make install
```

### Preview build without serving

```bash
make build
```

The generated site will be written to `_site/`.

To quickly inspect the generated top-level files and catch accidental published repo docs:

```bash
make audit
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for the local workflow and contribution guidelines.
