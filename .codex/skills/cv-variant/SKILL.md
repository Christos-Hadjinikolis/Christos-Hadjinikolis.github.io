---
name: cv-variant
description: Use when creating or revising a truthful job-targeted CV variant from Christos Hadjinikolis's source LaTeX CV and a specific job description, and when requested producing a tailored cover letter. Applies to role-specific CV positioning, evidence-to-requirement mapping, claim audits, cover letters, LaTeX compilation under cv/latex, and preserving the master CV and published PDF unless explicitly asked to update them.
---

# CV Variant

Create the strongest truthful version of the user's actual experience for a specific role. Do not optimize for superficial similarity to the job advertisement.

## Source Boundaries

Start by reading:

- `cv/latex/README.md`
- `cv/latex/cv.tex`
- relevant files under `cv/latex/context/` when present and applicable
- existing variants for similar roles when they help preserve consistency
- the complete job description or user-provided role material

Treat `cv/latex/cv.tex` as the master CV source. Do not overwrite it unless the user explicitly asks for a master CV update.

Preserve the established Friggeri design using `cv/latex/friggeri-cv.cls`.
Use `cv/latex/variants/2026/09/permutable-ai-senior-engineering-leadership/cv.tex`
and its PDF as the design reference: charcoal header, sidebar, detailed experience,
and the full second-page career sections. Tailor content within that structure.
Do not substitute a generic single-column layout or remove career sections for
ATS optimisation unless the user explicitly requests that change. Compare the
rendered result with the reference PDF, not only with the source text.

Treat `assets/pdfs/cv.pdf` as the website-published artifact. Do not update it unless the user explicitly asks to publish or refresh the website CV.

Use repository/project evidence only when it is relevant and inspectable. If live company systems, Jira, Confluence, dashboards, or external pages are unavailable, state that limitation instead of treating them as verified.

## Truthfulness Rules

Truthfulness is the highest priority.

Never invent, exaggerate, or imply experience that is not supported by the source CV, career documents, repository/project evidence, or information the user explicitly provides.

Do not:

- turn familiarity into professional experience
- turn personal projects into enterprise production experience
- turn participation into ownership
- turn technical leadership into people management without evidence of people-management responsibility
- inflate team size, scope, seniority, impact, metrics, customer exposure, hiring responsibility, budget responsibility, or organisational influence
- claim technologies merely because they appear in the job description
- imply a product category or industry background where the evidence is only technically adjacent

Preserve uncertainty where the evidence is uncertain. If a requirement is a genuine gap, leave it as a gap.

## Evidence Mapping

Before editing, analyze the role into:

- core responsibilities
- essential requirements
- desirable requirements
- domain expectations
- leadership expectations
- technical expectations
- likely recruiter screening signals

Map each important requirement to concrete evidence and classify it internally as:

- `strong evidence`: direct and supported by the CV or supplied evidence
- `partial/adjacent evidence`: transferable but not the same thing
- `unsupported/gap`: no reliable support

Use strong evidence prominently. Use partial evidence carefully and accurately. Never disguise unsupported requirements.

Do not copy job-description phrases just for ATS matching. Use role terminology only where it accurately describes the user's experience.

## Professional Identity

Preserve the user's actual career shape: software engineering, ML engineering, production ML systems, distributed/event-driven systems, technical leadership, engineering management, architecture, research, and mentoring.

Change emphasis for the role, not the underlying history.

Job titles must remain truthful. If source material supports multiple legitimate descriptions of a role, choose the one best supported by the employment history and most useful to the application. Never manufacture a title.

When management is central to a role, foreground actual evidence of people leadership, delivery ownership, stakeholder alignment, mentoring, onboarding, operating model work, and engineering practice improvement. Do not imply manager-of-managers, budget ownership, hiring ownership, or large-org accountability unless explicitly supported.

## Translate Internal Jargon

Do not leak internal company terminology unless it is immediately explained and genuinely useful.

Translate internal project names, team names, acronyms, repositories, services, and organisation-specific labels into externally meaningful descriptions.

Examples:

- `Ithaca`, `Chronos`, `Motorway`, `Homework`, `Bon-voyage`, `DPT`, or `ADT` should usually become descriptions such as `real-time ML inference service`, `event-driven streaming pipeline`, `model-serving API`, `production data pipeline`, `forecasting system`, or `cross-functional engineering/product team`
- if the internal name is retained, explain it immediately in plain language

The reader should understand the significance of each accomplishment without knowing the user's employer's internal vocabulary.

## Writing Style

Write like an experienced engineer, not a marketing page.

Avoid:

- excessive adjectives
- corporate cliches
- generic leadership language
- breathless enthusiasm
- "passionate about"
- "thrilled" or "excited to apply"
- "perfect fit"
- "unique blend"
- "at the intersection of"
- "leveraging my extensive experience"
- unnecessary em dashes
- repetitive three-item rhetorical lists
- mirroring the company's marketing copy
- inflated claims

Prefer restrained, specific statements about what the user owned, changed, built, delivered, improved, or learned.

Use quantitative evidence where it is supported. Do not create numbers or convert vague outcomes into metrics.

## CV Variant Workflow

1. Read the user's positioning instructions and constraints first; treat them as binding unless they would force inaccurate claims.
2. Read the complete job description and source CV.
3. Inspect relevant context/evidence files and similar prior variants.
4. Build the requirement-to-evidence mapping.
5. Identify the strongest positioning and genuine gaps.
6. Create a dated role variant without overwriting the master CV.
7. Tailor the headline, professional summary, skill ordering, bullet selection, bullet wording, and older-career compression.
8. Preserve important differentiators such as education, research, teaching, talks, standards work, and career progression where they remain useful.
9. Run the claim audit before finalizing.
10. Compile and clean the variant when local tooling supports it.

Keep the CV concise and readable, normally around the same page count as the source CV unless the user asks otherwise. Treat a two-page baseline as already tight; tailor by replacing, reordering, or tightening content rather than adding bulk.

## File Conventions

Use the dated variant layout from `cv/latex/README.md`:

- master source: `cv/latex/cv.tex`
- role-specific variant: `cv/latex/variants/<YYYY>/<MM>/<role-slug>/cv.tex`
- job description snapshot: `cv/latex/variants/<YYYY>/<MM>/<role-slug>/_role-context/job-post.md`
- fit evaluation: `cv/latex/variants/<YYYY>/<MM>/<role-slug>/_role-context/fit-assessment.md`
- optional cover letter: `cv/latex/variants/<YYYY>/<MM>/<role-slug>/cover-letter.md`
- optional HTML-backed Word file: `cv/latex/variants/<YYYY>/<MM>/<role-slug>/cover-letter.doc`
- published site PDF: `assets/pdfs/cv.pdf`

For dated variants under `cv/latex/variants/<YYYY>/<MM>/<role-slug>/`, the expected LaTeX paths are:

- `\documentclass[]{../../../../friggeri-cv}`
- `\graphicspath{ {../../../../images/} }`

Store enough role context to explain the tailoring decision. Before committing, inspect `git status --short` and the ignore rules; role-context dossiers may include job-post snapshots or private notes and should be included only when that is intended.

## Fit Assessment

Create or update `_role-context/fit-assessment.md` for role variants. Include:

- the strongest positioning thesis
- strongest matches highlighted in the CV
- partial or adjacent matches
- unsupported gaps
- notable changes made from the master CV or prior variant
- claims deliberately not made because evidence was insufficient

This file is the working audit trail. Keep it useful and concrete.

## Cover Letters

Create a cover letter only when requested.

The cover letter should explain why the role makes sense given the trajectory of the user's career. Do not repeat the CV bullet-by-bullet.

Normally cover:

- why this technical/product problem is a coherent next step
- the strongest relevant evidence from the user's experience
- where the background is adjacent rather than exact, when that distinction matters
- why the company or team is specifically interesting without flattery

Keep it concise, typically 350-500 words unless the application or user specifies otherwise.

Do not pretend the user has always wanted to work for the company.

When producing `.doc` cover letters, use professional A4 print CSS with explicit margins, justified body paragraphs, and left-aligned contact details, date, salutation, and sign-off unless the user asks for a different format. Verify page fit when local tooling makes that practical.

## Compile

Compile from the relevant directory with:

```bash
latexmk -xelatex -interaction=nonstopmode -synctex=1 cv.tex
```

For variants, run the command from `cv/latex/variants/<YYYY>/<MM>/<role-slug>/`.

After a successful variant build, clean intermediates:

```bash
latexmk -c cv.tex
```

If local TeX tooling is unavailable or compilation fails for an environmental reason, report that explicitly and leave the source files in a reviewable state.

## Claim Audit

Before completion, audit every materially new or substantially rewritten claim.

Check:

- support exists in the source CV, career material, repo evidence, or user-supplied information
- no unexplained internal jargon remains
- no unsupported technology claims were introduced
- no personal/project experience is described as enterprise production experience
- no implied experience exceeds the evidence
- no management scope was inflated
- no dates, titles, education, or career sequence contradict source material
- no keyword stuffing or job-ad copy leaked into the prose
- the writing is specific, restrained, and human

If a claim cannot be established, omit it or flag it to the user rather than guessing.

## Final Report

After creating the files, briefly report:

- where the CV variant and cover letter were saved
- what positioning changed
- the strongest matches highlighted
- genuine gaps that remain
- anything deliberately not claimed because evidence was insufficient
- compilation result and page count, or why compilation could not be verified

Do not commit or push unless the user explicitly asks.
