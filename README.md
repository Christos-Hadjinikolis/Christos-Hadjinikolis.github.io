# Christos-Hadjinikolis.github.io

Personal website and blog built with Jekyll and the `jekyll-theme-prologue` theme.

## Stack

- Jekyll 4
- Ruby 3.1+ (`.ruby-version` pins `3.1.2`)
- Bundler 2

## Repository Layout

- `_sections/`: homepage sections
- `_posts/`: blog posts
- `_layouts/` and `_includes/`: Jekyll templates and shared partials
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
make clean
```

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

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for the local workflow and contribution guidelines.


