---
name: blog-writing
description: Use when drafting, revising, or evaluating blog posts for this repository's ML-Affairs site. Applies to new post ideas, post outlines, editorial feedback, title refinement, and rewriting blog content to match the repo's stored content strategy and writing style.
---

# Blog Writing

Use this skill for blog work in this repository only.

Before writing or revising a post, read:

- `_internal/authoring/BLOG_CONTENT_STRATEGY.md`
- `_internal/authoring/BLOG_WRITING_STYLE.md`

When useful, also read 1 to 3 relevant existing posts from `content/_posts/` to match tone and structure.

## Workflow

1. Check whether the topic passes the editorial bar in `_internal/authoring/BLOG_CONTENT_STRATEGY.md`.
2. If the idea is weak, generic, or easy to fake with an LLM, say so directly and propose a sharper angle.
3. Draft or revise the post in the repo voice defined by `_internal/authoring/BLOG_WRITING_STYLE.md`.
4. Keep the writing grounded in lived experience, production trade-offs, failure modes, and operational reality.
5. Prefer concrete examples and earned opinions over trend summaries or generic tutorials.

## Output Rules

- New posts belong in `content/_posts/` with valid Jekyll front matter.
- Preserve an existing post's date and slug unless the user explicitly asks to change them.
- Use headings to structure arguments.
- When the visual treatment of blog posts matters, prefer a plain `title` for metadata and a rendered `title_html` for the on-page/blog-index heading.
- Use visual emphasis sparingly and consistently:
  - reserve color accents for technologies, frameworks, and core concepts that are central to the post
  - use at most 1 to 2 colored terms in a paragraph
  - prefer bold or italics for emphasis before adding more color
  - use bold for the clearest takeaways, named concepts, or strong claims
  - use italics for softer emphasis, contrast, or a reflective aside
  - do not stack bold, italics, and color on the same phrase unless there is a very strong reason
  - if a paragraph already has one visual emphasis cue, be skeptical about adding another
  - keep all accents accessible and readable on light backgrounds
- Follow the repo's blog accent conventions when they exist:
  - Python: dark blue text with muted gold support, not neon yellow
  - Flink / PyFlink: dark pink / raspberry
  - Kafka: warm amber/orange
  - AWS: AWS-style amber
  - Avro: brick red
  - Graph / streaming architecture concepts: teal or cyan family
- Avoid hype, startup marketing language, and generic AI thought leadership tone.
- Do not publish internal instructions or quote them into the post.

## Quality Bar

- The post should sound like Christos, not a generic assistant.
- The post should teach something non-obvious.
- The post should reconnect technical ideas to production conditions.
- The conclusion should land on a practical takeaway, not just a flourish.
