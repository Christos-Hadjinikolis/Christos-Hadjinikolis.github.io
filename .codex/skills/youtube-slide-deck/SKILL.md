---
name: youtube-slide-deck
description: Use when creating or revising HTML slide decks and narration notes for ML-Affairs YouTube-style technical videos. Applies to concept decks, animated explainer slides, screen-recording plans, and video-support visuals; do not use for normal blog prose or static social images.
---

# YouTube Slide Deck

Create slides as recording support, not as the full script. The viewer should be
able to understand the visual idea in a second or two while the presenter says
the detail aloud.

## Core Rules

- Put one idea on each slide. If a slide needs a paragraph to explain itself,
  move that paragraph into the notes and simplify the visual.
- Keep persistent branding minimal. Do not bake in YouTube-style subscribe
  buttons, clickable avatars, corner watermarks, or end-screen elements. Leave
  clean space for platform overlays in the final slide.
- Treat character art as optional punctuation. Never let mascots, avatars, or
  decorative marks compete with the workflow being explained.
- Prefer diagrams, motion, and live clips over dense bullets. A good slide
  should show a relationship, transition, contrast, or state change.
- For proof, cut to real tools. Do not simulate a product screen when the user
  can record the report, IDE, terminal, or browser directly.

## Motion

Use animation to express causality:

- draw arrows in the same direction the workflow moves
- reveal the current actor before its dependent actors
- pulse only the active event or handoff, not the whole slide
- avoid unrelated loops during narration unless they show a live process
- keep transitions short enough that the presenter can speak over them naturally

For graphs and workflows, use SVG paths with explicit coordinates and
`marker-end` arrowheads. Compute source and target centers first, then shorten
the visible path to the entity edge along that centerline so the arrow points at
the right object without covering its label.

Avoid hand-positioned rotated div arrows for important workflow diagrams. They
are acceptable only for intentionally rough background marks where precision is
not part of the message.

## Composition

Use a predictable hierarchy:

- short headline at the top
- one main visual field below it
- no more than a few labels inside the visual field
- narration, timing, and editor instructions in a side markdown file

Keep safe zones clean:

- avoid placing important content in the top-right corner
- avoid persistent lower-right badges, avatars, or buttons
- leave end-screen room on the closing slide instead of drawing custom links
- verify at 16:9 recording size, usually 1600x900 or 1920x1080

## Production Notes

For each video kit, include a markdown side document with:

- the core thesis
- a slide-by-slide narration script
- the intended animation beat per slide
- the exact live clips to record
- concrete repo-relative paths for reports, fixtures, tools, and commands
- explicit placeholders for clips that will be stitched in a video editor

If the user asks for a product/report/plugin showcase, prefer a short live
recording plan over screenshot stacks inside the deck. Slides should explain why
the viewer should care; recordings should prove the tool works.

## Verification

Before handing off:

- load the HTML deck in a browser-backed check; old HTML4 parsers may flag valid
  inline SVG as invalid
- capture representative slide screenshots after animation settle time
- inspect screenshots for text density, overlapping content, arrow endpoints,
  safe-zone problems, and baked-in YouTube overlay elements
- run the repository's normal build/audit checks when the deck lives inside this
  Jekyll site
