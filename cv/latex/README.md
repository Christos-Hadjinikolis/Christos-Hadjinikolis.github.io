# CV LaTeX Workspace

This directory is the source-of-truth home for the LaTeX code that generates the public CV PDF.

## Intended Structure

Move the contents of your existing `CV-latex` directory into this folder.

Current layout:

- `cv/latex/cv.tex`: primary entrypoint
- `cv/latex/friggeri-cv.cls`: custom class
- `cv/latex/bibliography.bib`: bibliography source
- `cv/latex/images/`: local image assets
- `cv/latex/versions/`: archived PDF versions
- `cv/latex/build/`: optional dedicated build output directory if you choose to use one

The public website should continue to serve the compiled PDF from:

- `assets/pdfs/cv.pdf`

That keeps the website asset separate from the editable source.

## Recommended Workflow

1. Edit the LaTeX source inside `cv/latex/`.
2. Compile locally from `cv.tex`.
3. Copy the final PDF to `assets/pdfs/cv.pdf`.
4. Commit both the source changes and the refreshed website PDF when needed.

## Prerequisites

On macOS, install a TeX distribution first.

Recommended:

- `MacTeX` if you want the full distribution
- `BasicTeX` if you want a smaller install and are comfortable adding packages later

You also want `latexmk` available in your shell, since it handles the repeated runs needed by LaTeX, BibTeX/Biber, and references.

## Compile From Terminal

From this directory:

```bash
latexmk -xelatex -interaction=nonstopmode -synctex=1 cv.tex
```

If you want a dedicated build directory instead of emitting files next to `cv.tex`:

```bash
latexmk -xelatex -interaction=nonstopmode -synctex=1 -outdir=build cv.tex
```

Clean build artifacts:

```bash
latexmk -C cv.tex
```

Publish the latest PDF to the site:

```bash
cp cv.pdf ../../assets/pdfs/cv.pdf
```

If you compile to `build/`, use:

```bash
cp build/cv.pdf ../../assets/pdfs/cv.pdf
```

## Working In IntelliJ IDEA

IntelliJ can be made usable for LaTeX, but it is not first-party LaTeX tooling. The right setup is:

1. Install the `TeXiFy-IDEA` plugin from JetBrains Marketplace.
2. Make sure a PDF viewer plugin is enabled in IntelliJ for in-IDE preview.
3. Ensure your TeX distribution binaries are on your shell `PATH`.
4. Open `cv/latex/` as a project or module root.

### Recommended Plugins

- `TeXiFy-IDEA`
- `PDF Viewer` if it is not already enabled in your IntelliJ installation

What `TeXiFy-IDEA` gives you:

- LaTeX syntax support
- inspections and quick fixes
- completion for commands, labels, citations, and environments
- compiler support for `pdfLaTeX`, `XeLaTeX`, `LuaLaTeX`, `latexmk`, `bibtex`, and `biber`
- forward/backward search support with a PDF viewer

### IntelliJ Setup Notes

After installing the plugin:

1. Open `Settings` -> `Plugins` and install `TeXiFy-IDEA`.
2. Restart IntelliJ if prompted.
3. Open `Settings` -> search for `TeXiFy`.
4. Set the preferred compiler to `latexmk` unless you have a reason not to.
5. Point the plugin at `cv.tex` if it does not detect it automatically.

### Recommended Compiler Choice

Use `latexmk` as the default compiler.

Reason:

- it handles multiple passes automatically
- it is the least fragile option for references and bibliographies
- it works well for CV-style documents where you want a repeatable build

### Suggested Run Configuration

If you prefer explicit control, add a shell-based run configuration that executes:

```bash
latexmk -xelatex -interaction=nonstopmode -synctex=1 cv.tex
```

## Troubleshooting

- If IntelliJ cannot compile, check that `latexmk` is available in the environment launched by IntelliJ.
- If fonts or packages are missing, install them in your TeX distribution first.
- If PDF preview does not sync correctly, verify that SyncTeX is enabled via `-synctex=1`.
- If bibliography entries do not appear, confirm whether the template expects `bibtex` or `biber`.
- This CV currently declares `%!TEX TS-program = xelatex`, so XeLaTeX should be treated as the default engine.

## Practical Repo Rule

Edit source here.

Do not treat `assets/pdfs/cv.pdf` as the editable source. It is only the published artifact used by the website.
