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
10. When visuals are useful, think in scenes, not decoration: identify 1 to 3 moments where an image would make the reader pause, smile, or understand the tension faster than prose alone.
11. For posts that suit a recurring concept avatar, generate image prompts that:
  - define the avatar once in a reusable base prompt
  - keep the avatar on a transparent or plain background when creating the reusable base asset
  - then reuse that avatar description inside scene prompts for future post visuals
  - keep the humor restrained, professional, and slightly self-aware rather than cartoonishly goofy
12. When preparing image prompts for the user, include:
  - one reusable avatar prompt
  - 1 to 3 scene prompts tied to specific moments in the post
  - a short note on where each image should be placed and what point it reinforces
13. When a post is ready for distribution, prepare companion copy for LinkedIn by default, and prepare X copy only when the user explicitly wants to use X.
14. When the user asks to publish or announce a post, follow this order unless they explicitly want something different:
  - finalize the post body, title, description, `og_image`, and share metadata
  - verify the post builds cleanly and the share image is a real PNG/JPEG-style preview asset, not just an on-page decorative image
  - commit and push the site changes so the live URL has the correct metadata
  - only then publish to LinkedIn using the live URL, and only add X if the user explicitly wants that channel
  - after the social post exists, add/embed the discussion link back into the article if desired
  - commit and push that embed/update as a second pass
15. Treat Medium and Substack as manual syndication targets unless the platform's official API situation clearly supports durable automation.
16. Every new post should include a concise, visible summary block near the top presented as an "At A Glance" section:
  - `tldr_why_read`
  - `tldr_persona`
  - `tldr_learn`
  - `tldr_takeaways`
17. Every new post should include `description` and `seo_keywords` front matter so the page has useful search metadata without resorting to hidden keyword stuffing.
18. For framework/platform posts, put the real adoption driver near the top and, when helpful, include a concrete next-step path such as a starter archetype, template, or agent prompt.
19. For comparison posts, include the author's real bias or prior preference when it matters, then show what experience changed or refined about that view.
20. When revising a strong post, sharpen the parts that are merely balanced into parts that are memorable:
  - challenge bad heuristics directly when the evidence supports it
  - call out failure modes, not just feature trade-offs
  - make the reader slightly uncomfortable about rewrite instinct, architectural cargo cults, or comfort-driven decisions
  - do not flatten real disagreement in the name of fairness
  - do not invent war stories or dramatize beyond the lived evidence
21. For opinionated technical posts, make sure the piece does more than explain:
  - it should force a perspective shift
  - it should contain at least one line that is quotable
  - it should name the cost curve of the preferred approach honestly
  - it should finish with a sharper consequence than "it depends"

## Output Rules

- New posts belong in `content/_posts/` with valid Jekyll front matter.
- Preserve an existing post's date and slug unless the user explicitly asks to change them.
- Use headings to structure arguments.
- When the visual treatment of blog posts matters, prefer a plain `title` for metadata and a rendered `title_html` for the on-page/blog-index heading.
- Use `description`, `seo_keywords`, and the four summary fields in front matter.
- When revisiting older posts, bring them up to the same emphasis standard as the stronger recent posts: summary block, title treatment, opening tension, and central-term highlighting should feel curated rather than accidental.
- Infer `tldr_persona` from the post itself. The persona is your job to identify from the pain, stakes, and likely reader, not something to leave generic.
- Make the summary block earn its space:
  - `Why read` should communicate urgency or payoff
  - `Who it's for` should be concrete and useful
  - `What you'll learn` should name the real lesson
  - `Takeaways` should feel like memorable consequences, not filler bullets
  - when a technology or language is central to the post, use the same accent treatment inside the summary block too
- Do not add hidden keyword text to the page body for SEO. Prefer visible summaries, honest wording, and structured metadata.
- Include useful keywords in page metadata and natural prose so the post is discoverable without becoming spammy.
- Think in impact. A post should surface the non-obvious lesson quickly, then deepen it through story and explanation.
- When a line carries the thesis of the post, isolate it. Strong posts usually have 1 to 3 sentences that deserve a real pause from the reader; present those as pull quotes or similarly elevated standalone moments, not as plain body text.
- When the post compares tools or architectures, be especially wary of familiarity bias. A good comparison should separate "this feels more natural to me" from "this is the better decision for the system."
- Avoid weak balancing language when the argument can support something clearer:
  - replace vague softeners like "too shallow" or "can become painful" when the actual point is stronger and defensible
  - prefer "misleading", "becomes the bottleneck", "dominant operational pain point", or similarly concrete phrasing when warranted
  - sharpen only as far as the lived evidence goes
- Use visual emphasis sparingly and consistently:
  - reserve color accents for technologies, frameworks, and core concepts that are central to the post
  - if a technology, framework, or language is central to the post, treat it consistently across the whole piece: title, summary block, section headings, opening argument, key body paragraphs, and conclusion
  - the archive matters too: when improving older posts, apply the same consistency standard instead of leaving legacy posts visually flat
  - central terms should usually use the repo's accent class in bold form, not drift between highlighted and plain text
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
  - when suggesting AI-generated visuals, tie each one to a specific narrative beat: rewrite instinct, operational pain, competing hypotheses, broken trust, or similar
  - recurring avatars should support recognition and tone, not become mascots that overpower the article
  - default to transparent-background avatar assets for reuse across future posts
- When preparing social distribution:
  - LinkedIn copy should open with the production pain, tension, or contrarian lesson, not a flat summary
  - the first 1 to 2 lines should earn attention quickly and make the value of clicking obvious
  - if the post will be shared as a link card, prefer a PNG or JPEG `og_image` over SVG and make sure the page has a real social preview image, not just an on-page decorative graphic
  - do not publish the social post until the page metadata is live on the deployed site, otherwise platforms may cache the wrong preview
- Avoid hype, startup marketing language, and generic AI thought leadership tone.
- Do not publish internal instructions or quote them into the post.
- For social distribution:
  - generate a fuller LinkedIn version by default
  - generate an X version only when the user explicitly wants that channel
  - when the user says to publish, use the local repo scripts after generating the copy if credentials are present
  - keep Medium and Substack copy reusable, but do not assume direct API publishing exists
  - use the repo's social scripts when they fit the task and credentials are configured

## Quality Bar

- The post should sound like Christos, not a generic assistant.
- The post should teach something non-obvious.
- The post should reconnect technical ideas to production conditions.
- The conclusion should land on a practical takeaway, not just a flourish.
- The best posts return to the tension they opened with and make the reader feel they finally understand the real question.
- The summary block should make an impatient reader want to continue.
- A strong modern post should also give the reader a credible next step when that is useful: a repo, archetype, checklist, or agent prompt.
- The strongest opinion pieces should not leave every reader comfortable:
  - they should challenge a default instinct
  - they should name at least one harmful or misleading simplification
  - they should still stay inside the bounds of what the author can honestly defend
