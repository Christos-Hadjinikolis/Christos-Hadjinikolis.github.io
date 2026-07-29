---
title: "Skeleton: Runtime Evidence Beats Architecture Guesswork"
title_html: "<span class='blog-title-accent blog-title-accent--signal'>Skeleton</span>: Runtime Evidence Beats Architecture Guesswork"
author: Christos Hadjinikolis
layout: post
published: false
date: 2026-08-01
canonical: false
description: "A draft placeholder for a post about Skeleton, runtime architecture replay, and why observing real execution gives developers better evidence than static diagrams or generic AI repository summaries."
seo_keywords: ["Skeleton", "skeleton-replay", "runtime tracing", "architecture replay", "Python architecture", "developer tools", "LLM-readable workflow", "software design", "architecture evidence"]
nav_tags: ["Architecture", "Python", "Developer Tools"]
tldr_why_read: "Read this if you have ever stared at a codebase diagram, an AI repository summary, or a static dependency graph and wondered whether it actually describes the system that runs."
tldr_persona: "Especially useful for Python engineers, staff engineers, and AI-assisted delivery teams who need evidence about runtime behaviour, not just a plausible story about source files."
tldr_learn: "Why <span class=\"blog-highlight blog-highlight--signal\">runtime evidence</span> changes architecture understanding, where static analysis becomes misleading, and how Skeleton turns one execution path into trace, snapshot, workflow, quality, and replay artifacts."
tldr_takeaways: ["Architecture understanding improves when it starts from observed behaviour", "Static structure is useful, but it is not the same as runtime evidence", "Skeleton should be framed as a developer-understanding tool, not a profiler", "The strongest advertisement is the pain: teams need trustworthy system evidence before they trust generated change"]
---
_Draft placeholder. Keep unpublished until the argument, screenshots, generated visuals, and social preview image are ready._

## Working Angle

Skeleton is not just a package announcement.

The stronger post is about a practical pain: modern teams, especially teams using AI coding tools, are producing and changing code faster than they can understand whether the system still behaves the way they think it does.

The post should make the case that architecture understanding needs runtime evidence:

- what actually ran
- which actors called each other
- what values crossed the boundary
- where I/O happened
- what can be shown to a human
- what can be handed to an LLM without asking it to guess from raw source alone

## Ideas To Collect

- Why static diagrams go stale.
- Why generic AI repo summaries sound confident but often miss the execution path.
- Why tracing is useful only if it becomes developer-facing evidence, not another telemetry dump.
- Why Skeleton should stay non-invasive: no decorators, no framework buy-in, no application-code rewrite.
- The four or five artifact surfaces worth explaining: `trace.jsonl`, `snapshot.json`, `workflow.md`, `architecture_quality.md`, `report.html`.
- How this connects to AI-assisted development: more generated change increases the need for stronger evidence.
- How this connects to production engineering: runtime behaviour is the thing that eventually matters.

## Possible Structure

1. Open with the frustration: a codebase can look understandable until you ask what actually happens when one real workflow runs.
2. Name the false comfort: static structure, diagrams, and AI summaries are useful, but they can be mistaken for evidence.
3. Introduce Skeleton as a runtime architecture replay tool for Python.
4. Show the artifact model.
5. Explain what makes the approach deliberately boring: `sys.setprofile`, project-local public calls, safe summaries, generated reports.
6. Discuss the trade-offs honestly: one run is not the whole system, tracing has overhead, and runtime evidence must be scoped.
7. Finish with the practical claim: the future of AI-assisted engineering needs more than code generation; it needs trustworthy evidence surfaces.

## Missing Before Publication

- Replace this placeholder with a full draft in the ML-Affairs voice.
- Add one post-specific `og_image` PNG or JPEG.
- Add `og_image_alt`.
- Decide whether to include generated visuals, screenshots from `report.html`, or both.
- Run the site audit before publishing.
- Prepare LinkedIn copy only after the final URL and preview image are ready.
