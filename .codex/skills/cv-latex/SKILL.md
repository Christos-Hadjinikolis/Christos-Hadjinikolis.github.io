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
- Preserve the existing section set and overall structure unless the user explicitly asks for a redesign.
- Treat the baseline CV as already tightly optimised for two pages; tailor by replacing or tightening content, not by making the document longer.
- Keep the final variant to the same page count as the source CV unless the user explicitly asks otherwise.
- Only change the text content, not the underlying structure or formatting, unless the user explicitly asks for a redesign.
- Name the entrypoint `cv.tex` inside that variant directory unless there is a strong reason not to.
- Store the target role context inside the variant folder.
- Store role metadata under `cv/latex/variants/<role-slug>/_role-context/`.
- Create `job-post.md` inside that `_role-context/` folder containing the source link, capture date if known, and the job description text used for tailoring.
- If the user provides both a recruiter note and a public job description, record both and state which one controls positioning decisions.
- If the user says the real target seniority differs from the advertised title, tailor the emphasis to that actual target level while keeping factual role titles and claims honest.
- Create `fit-assessment.md` inside that `_role-context/` folder containing:
  - why the profile is a strong fit
  - where the fit is partial or weak
  - which CV changes were made to improve alignment
  - which claims were intentionally not made because the evidence is missing
- Build the variant by copying the master `cv.tex` and then adjusting relative LaTeX paths for the nested location.
- For variants stored one level below `cv/latex/variants/`, use `../../friggeri-cv` as the class path and `../../images/` as the graphics path unless the source layout changes.
- Tailor by reordering emphasis, refining summary text, tightening bullets, and foregrounding matching skills.
- Prefer Staff-, Lead-, or Principal-level framing only when the user's actual background supports that framing and the user explicitly indicates the target seniority.
- Do not invent experience, tools, impact, certifications, or titles.
- If the job description asks for something unsupported by the source CV, say so clearly and handle it as a gap rather than fabricating.

## Tailoring Workflow

1. Read the job description and extract the actual requirements, not just keywords.
2. Read the user's constraints and positioning notes first; treat them as binding unless they would force inaccurate claims.
3. Map each requirement to evidence already present in the CV source or supplied by the user.
4. Decide whether the request should update the master CV or produce a role-specific variant.
5. For variants, preserve the master narrative but adjust emphasis:
   - headline and summary
   - ordering and wording of experience bullets
   - skill grouping and prominence
   - removal of lower-value detail when space is tight
6. When seniority positioning is part of the ask, raise the leadership and ownership emphasis through wording, not by changing factual employment titles.
7. Keep the final document credible and readable. Avoid keyword stuffing.

## File Conventions

- Master source: `cv/latex/cv.tex`
- Role-specific variants: `cv/latex/variants/<role-slug>/cv.tex`
- Job description snapshot: `cv/latex/variants/<role-slug>/_role-context/job-post.md`
- Fit evaluation: `cv/latex/variants/<role-slug>/_role-context/fit-assessment.md`
- Archived PDFs: `cv/latex/versions/`
- Published site PDF: `assets/pdfs/cv.pdf`

Only update `assets/pdfs/cv.pdf` when the user explicitly wants the website CV refreshed.

## Cover Letters

- Keep cover letters to one printed page unless the user explicitly asks otherwise.
- Use professional A4 print CSS with explicit margins when generating HTML-backed `.doc` files.
- Justify body paragraphs (`text-align: justify; text-justify: inter-word; hyphens: auto;`) so the main prose aligns on both left and right edges.
- Keep contact details, date, salutation, and sign-off left-aligned unless the user asks for a different letter format.
- Verify page fit when tooling is available; if it cannot be rendered locally, say so.

## Compile and Publish

When the environment supports it, compile from `cv/latex/` with:

- `latexmk -xelatex -interaction=nonstopmode -synctex=1 cv.tex`

For a variant, compile from that variant directory with the same command.

If the user asks to publish the new master PDF to the website, copy the compiled output to:

- `assets/pdfs/cv.pdf`

## Validation

- Check that the LaTeX still matches the document's existing structure and macros.
- Check links, line breaks, and role dates when editing content.
- Confirm the variant still compiles to the intended page count, typically two pages.
- If you cannot compile locally, say so explicitly.
- When tailoring to a role, record the positioning choices and evidence gaps in `_role-context/fit-assessment.md`.
- After compiling a variant, clean unnecessary LaTeX intermediates so the variant folder keeps source, context, and final PDF artifacts only.
