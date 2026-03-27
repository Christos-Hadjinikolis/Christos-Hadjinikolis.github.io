---
name: site-design-review
description: Use when reviewing, critiquing, or redesigning the visual design of this Jekyll website. Applies to homepage hierarchy, typography, color system, imagery, navigation, page composition, consistency across sections/pages, and recommending or implementing a stronger visual direction.
---

# Site Design Review

Use this skill for visual design work in this repository.

## Scope

This skill is for design critique and redesign guidance, not just functional site maintenance.

Read the relevant files first:

- `_sass/jekyll-theme-prologue.scss`
- `_layouts/`
- `_includes/`
- `content/_sections/`
- `content/pages/`
- `content/index.md`

If screenshots are available, use them as the primary evaluation surface.

## Review Lens

Evaluate the site against:

- visual hierarchy
- typography quality and expressiveness
- spacing rhythm and alignment
- navigation clarity
- color palette coherence
- iconography consistency
- imagery quality and art direction
- distinction between homepage, blog, CV, and experience pages
- whether the site feels generic, dated, or overly template-driven

## Working Style

1. Start with concrete findings, not vague taste statements.
2. Separate structural issues from stylistic issues.
3. Prefer a clear visual direction over a collection of disconnected tweaks.
4. Preserve working content architecture unless the redesign calls for a justified structural change.
5. When proposing changes, explain the intended effect on perception:
   - more credible
   - more modern
   - more technical
   - more editorial
   - more distinctive

## Output Expectations

When reviewing:

- identify the top 3 to 5 visual problems
- explain why each problem matters
- propose one coherent redesign direction

When implementing:

- define or refine shared visual tokens first
- avoid one-off styling hacks unless fixing a clear bug
- make navigation, typography, and section rhythm more deliberate
- avoid generic “AI startup” aesthetics

## Repo-Specific Notes

- The site is based on Jekyll with a local Sass theme file.
- The current visual center of gravity lives in `_sass/jekyll-theme-prologue.scss`.
- Page content lives under `content/`, but visual consistency should be driven from shared layout and CSS layers.
- Internal docs under `_internal/` and `.codex/` must never become part of the site output.
