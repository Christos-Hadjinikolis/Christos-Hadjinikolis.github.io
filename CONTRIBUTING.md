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

## CV / LaTeX Setup

The CV source lives under `cv/latex/` and is separate from the website PDF published at `assets/pdfs/cv.pdf`.

### Prerequisites

- Install a TeX distribution on macOS.
- Recommended: `MacTeX`
- Smaller alternative: `BasicTeX`

After installation, make sure TeX binaries are on your `PATH`:

```bash
echo 'export PATH="/Library/TeX/texbin:$PATH"' >> ~/.zshrc
exec zsh
```

Verify the toolchain:

```bash
which xelatex
which latexmk
xelatex --version
latexmk -v
```

### Compile the CV

From `cv/latex/`:

```bash
latexmk -xelatex -interaction=nonstopmode -synctex=1 cv.tex
```

To publish the latest compiled master CV to the website:

```bash
cp cv.pdf ../../assets/pdfs/cv.pdf
```

### IntelliJ IDEA Setup

Recommended plugins:

- `TeXiFy-IDEA`
- `PDF Viewer`

After installing MacTeX or BasicTeX:

1. Reopen IntelliJ.
2. Open the LaTeX file in `cv/latex/` or `cv/latex/variants/`.
3. If prompted to set up an SDK, choose `Add Native TeX Live SDK from disk...`
4. Point it to `/Library/TeX/texbin`
5. In TeXiFy settings, set the preferred compiler to `latexmk`

If IntelliJ reports that no LaTeX installation can be found, TeX is either not installed yet or `/Library/TeX/texbin` is not available to the IDE environment.

## Project Conventions

- Keep changes focused and easy to review.
- Preview content and layout changes locally before opening a PR.
- Put homepage content in `content/_sections/`.
- Put blog posts in `content/_posts/` with valid front matter.
- Put standalone site pages in `content/pages/` or another directory under `content/`.
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
