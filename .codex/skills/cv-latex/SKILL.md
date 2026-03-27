---
name: cv-latex
description: Use when updating the LaTeX CV in this repository, compiling it, publishing the latest PDF, or creating a job-targeted CV variant from a job description. Applies to edits under cv/latex, tailoring the summary and bullets for a role, generating role-specific variants, and keeping assets/pdfs/cv.pdf aligned only when explicitly requested.
---

# CV LaTeX

Use this skill for CV work in this repository.

Start by reading:

- `cv/latex/README.md`
- `cv/latex/cv.tex`

Treat `cv/latex/cv.tex` as the master CV source.
Treat `assets/pdfs/cv.pdf` as a published artifact, not the editable source.

## Modes

### 1. Update the master CV

Use this when the user wants to refresh the canonical CV with new roles, achievements, skills, talks, or education details.

Rules:

- Edit the LaTeX source, not the published PDF.
- Preserve factual accuracy.
- Prefer specific evidence over broad claims.
- Keep the existing Friggeri CV structure unless the user asks for a redesign.

### 2. Create a job-targeted CV variant

Use this when the user provides or references a job description.

Rules:

- Do not overwrite `cv/latex/cv.tex` unless the user explicitly asks.
- Create the tailored variant under `cv/latex/variants/<role-slug>/`.
- Name the entrypoint `cv.tex` inside that variant directory unless there is a strong reason not to.
- Store the target role context inside the variant folder.
- Create `job-post.md` in the variant folder containing the source link, capture date if known, and the job description text used for tailoring.
- Create `fit-assessment.md` in the variant folder containing:
  - why the profile is a strong fit
  - where the fit is partial or weak
  - which CV changes were made to improve alignment
  - which claims were intentionally not made because the evidence is missing
- Build the variant by copying the master `cv.tex` and then adjusting relative LaTeX paths for the nested location.
- For variants stored one level below `cv/latex/variants/`, use `../../friggeri-cv` as the class path and `../../images/` as the graphics path unless the source layout changes.
- Tailor by reordering emphasis, refining summary text, tightening bullets, and foregrounding matching skills.
- Do not invent experience, tools, impact, certifications, or titles.
- If the job description asks for something unsupported by the source CV, say so clearly and handle it as a gap rather than fabricating.

## Tailoring Workflow

1. Read the job description and extract the actual requirements, not just keywords.
2. Map each requirement to evidence already present in the CV source or supplied by the user.
3. Decide whether the request should update the master CV or produce a role-specific variant.
4. For variants, preserve the master narrative but adjust emphasis:
   - headline and summary
   - ordering and wording of experience bullets
   - skill grouping and prominence
   - removal of lower-value detail when space is tight
5. Keep the final document credible and readable. Avoid keyword stuffing.

## File Conventions

- Master source: `cv/latex/cv.tex`
- Role-specific variants: `cv/latex/variants/<role-slug>/cv.tex`
- Job description snapshot: `cv/latex/variants/<role-slug>/job-post.md`
- Fit evaluation: `cv/latex/variants/<role-slug>/fit-assessment.md`
- Archived PDFs: `cv/latex/versions/`
- Published site PDF: `assets/pdfs/cv.pdf`

Only update `assets/pdfs/cv.pdf` when the user explicitly wants the website CV refreshed.

## Compile and Publish

When the environment supports it, compile from `cv/latex/` with:

- `latexmk -xelatex -interaction=nonstopmode -synctex=1 cv.tex`

For a variant, compile from that variant directory with the same command.

If the user asks to publish the new master PDF to the website, copy the compiled output to:

- `assets/pdfs/cv.pdf`

## Validation

- Check that the LaTeX still matches the document's existing structure and macros.
- Check links, line breaks, and role dates when editing content.
- If you cannot compile locally, say so explicitly.
- When tailoring to a role, record the positioning choices and evidence gaps in `fit-assessment.md`.
