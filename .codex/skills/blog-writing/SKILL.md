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
5. When the post comes from a real pain point, open with that pain in concrete terms before broadening into framework or architecture discussion.
6. Name the practical reader early. The post should make clear who it is for, not just what it is about.
7. Prefer concrete examples and earned opinions over trend summaries or generic tutorials.
8. When source material exists (slides, notes, old reports, evaluations), mine it for concrete operational signals rather than just restating conclusions.
9. If visuals would genuinely improve a post, prefer tasteful supplied imagery or carefully chosen extracted assets that support the mood and topic without overwhelming the writing.
10. When a post is ready for distribution, prepare companion copy for X and LinkedIn by default.
11. Treat Medium and Substack as manual syndication targets unless the platform's official API situation clearly supports durable automation.
12. Every new post should include a concise, visible summary block near the top presented as an "At A Glance" section:
  - `tldr_why_read`
  - `tldr_persona`
  - `tldr_learn`
  - `tldr_takeaways`
13. Every new post should include `description` and `seo_keywords` front matter so the page has useful search metadata without resorting to hidden keyword stuffing.
14. For framework/platform posts, put the real adoption driver near the top and, when helpful, include a concrete next-step path such as a starter archetype, template, or agent prompt.

## Output Rules

- New posts belong in `content/_posts/` with valid Jekyll front matter.
- Preserve an existing post's date and slug unless the user explicitly asks to change them.
- Use headings to structure arguments.
- When the visual treatment of blog posts matters, prefer a plain `title` for metadata and a rendered `title_html` for the on-page/blog-index heading.
- Use `description`, `seo_keywords`, and the four summary fields in front matter.
- Infer `tldr_persona` from the post itself. The persona is your job to identify from the pain, stakes, and likely reader, not something to leave generic.
- Make the summary block earn its space:
  - `Why read` should communicate urgency or payoff
  - `Who it's for` should be concrete and useful
  - `What you'll learn` should name the real lesson
  - `Takeaways` should feel like memorable consequences, not filler bullets
- Do not add hidden keyword text to the page body for SEO. Prefer visible summaries, honest wording, and structured metadata.
- Include useful keywords in page metadata and natural prose so the post is discoverable without becoming spammy.
- Think in impact. A post should surface the non-obvious lesson quickly, then deepen it through story and explanation.
- Use visual emphasis sparingly and consistently:
  - reserve color accents for technologies, frameworks, and core concepts that are central to the post (be concistent across posts about colouring)
  - use at most 1 to 2 colored terms in a paragraph
  - prefer bold or italics for emphasis before adding more color
  - use bold for the clearest takeaways, named concepts, or strong claims
  - use italics for softer emphasis, contrast, or a reflective aside, or anything that is in quotes
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
- Use inline visuals only when they improve the post's reading experience:
  - prefer 0 to 2 visuals per post unless the post is explicitly image-heavy
  - bias toward curated imagery that feels intentional and visually appealing, not over-explained
  - if a diagram is used, it should be simple and genuinely necessary
  - avoid over-designed synthetic graphics that distract from the prose
  - when the user supplies images, prefer choosing the best ones and integrating them cleanly
- Avoid hype, startup marketing language, and generic AI thought leadership tone.
- Do not publish internal instructions or quote them into the post.
- For social distribution:
  - generate a short X version and a fuller LinkedIn version when useful
  - keep Medium and Substack copy reusable, but do not assume direct API publishing exists
  - use the repo's social scripts when they fit the task and credentials are configured

## Quality Bar

- The post should sound like Christos, not a generic assistant.
- The post should teach something non-obvious.
- The post should reconnect technical ideas to production conditions.
- The conclusion should land on a practical takeaway, not just a flourish.
- The summary block should make an impatient reader want to continue.
- A strong modern post should also give the reader a credible next step when that is useful: a repo, archetype, checklist, or agent prompt.
