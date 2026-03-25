# Blog Writing Style Guide

This file captures the writing style used across the `ML-Affairs` blog and should be used as the working guide whenever we draft posts together.

It is based on the existing posts in [`_posts/`](/Users/chadjinik/Github/CH/Christos-Hadjinikolis.github.io/_posts), especially:

- personal and reflective posts such as `2020-07-28-just-do-it.md`
- experience-driven engineering posts such as `2020-08-11-agile-data-science.md`
- explanatory technical posts such as `2020-08-15-on-style-transfer.md`
- practical systems posts such as `2021-02-14-python-envs.md`
- production-focused ML posts such as `2022-05-31-dynamicio-at-ODSC.md`
- reflective systems/career posts such as `2023-10-31-Agile-In-Action.md`
- architecture-oriented posts such as `2023-11-07-Avro-Schema-Management.md`

This guide is not trying to freeze every habit from older posts. It keeps the strong parts of the voice and drops the weaker parts.

## Core Voice

The voice should feel like:

- thoughtful, experienced, and technically grounded
- warm and human, but not fluffy
- opinionated without becoming arrogant
- curious and reflective rather than performative
- practical and production-minded

The best version of the blog voice is:

- first-person singular: "I have seen...", "I care about...", "My experience tells me..."
- calm and conversational
- explanatory, with a teacher's instinct
- rooted in real systems, trade-offs, and delivery

It should not sound like:

- startup marketing copy
- generic "AI thought leadership"
- a research paper
- a corporate engineering blog written by committee
- a dry tutorial with no point of view

## What Makes The Writing Yours

### 1. Start from lived experience

Most strong posts begin with one of these:

- a real incident
- a concrete frustration
- a personal observation
- a story from work
- a broader reflection tied back to engineering

Examples of the pattern:

- "I was handed this notebook..."
- "Around two weeks ago I was approached..."
- "I am currently in Crete..."
- "If you call yourself an ML-Engineer then you've seen this before..."

This is important. The post should feel earned, not assembled.

### 2. Move quickly from story to idea

After the opening, get to the underlying point quickly.

Typical move:

1. open with a real situation
2. explain why it matters
3. name the actual problem
4. teach the reader something useful

Your posts work best when the personal anecdote is the entry point, not the whole piece.

### 3. Teach through structure

Your writing often uses progressive explanation:

- define the problem
- simplify the idea
- break it into parts
- deepen the technical detail
- reconnect to practical use

This is one of the strongest recurring traits in the blog.

Use headings generously. Favor a journey like:

- "The issue"
- "Why this matters"
- "How it works"
- "Where things go wrong"
- "What to do instead"

### 4. Blend engineering with metaphor carefully

You naturally use metaphor:

- navigation
- journeys
- bridges
- backstage heroes
- stories, music, ships, exploration

This works well when it supports the technical point.

Rule:

- one strong metaphor per section is enough
- do not let metaphor replace explanation
- if a metaphor cannot be tied back to the real system, remove it

### 5. Stay close to production reality

This is central to your writing identity.

When writing technical posts, keep bringing the reader back to:

- what breaks in production
- what the operational burden is
- who maintains the system
- how feedback loops work
- what happens when the model is wrong
- where the real bottleneck sits

Your posts should care about:

- latency
- observability
- reproducibility
- deployment
- data quality
- failure modes
- maintainability

That is the difference between your writing and generic ML blogging.

## Preferred Tone

Aim for this balance:

- 70% clear engineering explanation
- 20% personal reflection
- 10% stylistic flourish

The prose should be:

- readable
- moderately elegant
- never sterile
- never too clever for its own good

Good characteristics:

- rhetorical questions in moderation
- occasional emphasis
- direct statements when conviction matters
- specific nouns over vague abstractions

Avoid:

- too many exclamation marks
- hype phrases like "game-changing", "revolutionary", "unleashing"
- sounding breathless
- overusing "journey" or "exciting"
- ending every paragraph with a dramatic flourish

## Sentence-Level Guidance

### Keep

- medium-length sentences with some rhythm
- occasional longer sentence when building an argument
- plain language around technical ideas
- transitions like "So, here is the thing...", "Simply put...", "What this means is..."

### Reduce

- repeated filler phrases
- too many ellipses
- too many rhetorical build-ups before the point lands
- repeated "Remember to like my post..." style endings in new writing unless intentionally nostalgic

### Prefer

- "What matters here is..."
- "The issue is not X; the issue is Y."
- "In practice..."
- "This becomes a problem when..."
- "The real challenge is..."
- "This is where things get interesting."

## Post Types And How To Write Them

### A. Systems / engineering post

This should be the default modern mode.

Use when writing about:

- streaming systems
- MLOps
- architecture
- reliability
- production ML
- system design trade-offs

Recommended shape:

1. concrete problem from experience
2. why naive solutions fail
3. core concept or architecture
4. trade-offs and failure modes
5. practical takeaway

Tone:

- direct
- signal-first
- grounded in scars and lessons

### B. Explanatory technical post

Use when teaching a concept like Avro, style transfer, or Python environments.

Recommended shape:

1. introduce the concept through a practical problem
2. explain the basic mental model
3. walk through the technical mechanics step by step
4. give a concrete example or implementation path
5. end with a practical recommendation or next step

Tone:

- teacherly
- patient
- clear

### C. Reflective career / culture post

Use when discussing agile, team culture, standards, or engineering leadership.

Recommended shape:

1. lived experience or external prompt
2. what changed your thinking
3. where teams commonly get it wrong
4. what actually matters
5. a measured conclusion

Tone:

- reflective
- mature
- principled

## Strong Patterns To Preserve

- personal opening that earns the reader's attention
- practical framing around real problems
- layered explanation
- conviction about engineering rigor
- respect for experimentation, but only when tied to value
- visible empathy for practitioners dealing with messy systems

## Habits To Avoid In New Posts

These appear in older posts but should not be carried forward by default:

- overlong introductions before the technical thesis appears
- repeated social-media CTA blocks
- excessive exclamation marks
- slightly loose grammar or punctuation that makes sentences feel rushed
- sounding too apologetic before making a point
- overexplaining obvious ideas before getting to the real insight

In new posts, prefer the sharper modern version of your voice:

- less "blogging enthusiasm"
- more precision
- more systems thinking
- stronger narrative control

## Positioning Guidance

Future posts should reinforce your actual level:

- staff-level ML engineer
- systems builder
- real-time ML and streaming infrastructure practitioner
- someone who bridges modelling, infra, and product reality

That means posts should not frame you as:

- "just a data scientist"
- "just sharing a quick tutorial"
- "someone trying things out casually"

Instead, frame from ownership:

- what you changed
- what broke
- what you learned
- what trade-off mattered
- what should be done differently

## Recommended Default Template

Use this as the default drafting shape:

```md
---
title: ...
author: Christos Hadjinikolis
layout: post
og_image: ...
---

Opening paragraph:
- start from a real incident, frustration, or observation
- introduce the tension quickly

Hero image or diagram

## The Problem
- describe the real-world issue
- explain why naive solutions are insufficient

## Why This Is Hard
- name the operational, architectural, or organisational difficulty

## A Better Way To Think About It
- explain the mental model
- define the key system boundary or abstraction

## How It Works In Practice
- concrete implementation details
- diagrams, examples, code, or workflow

## Trade-offs And Failure Modes
- what can break
- what to measure
- what to watch operationally

## Closing Thoughts
- a compact conclusion
- one clear takeaway
```

## Editing Rules For Co-Writing

When drafting posts together:

- start with a real situation from your experience
- get to the thesis early
- keep the prose warm but controlled
- always connect technical content back to production reality
- prefer clarity over flourish when the two conflict
- keep one or two elegant turns of phrase, not ten
- write with authority, not with ego

If a draft sounds like "generic ML internet content", rewrite it.

If a draft sounds technically correct but emotionally flat, add a concrete lived example.

If a draft sounds reflective but does not teach anything useful, tighten it.

## One-Line Summary

The `ML-Affairs` voice is: personal but rigorous, reflective but practical, and always anchored in the hard reality of getting intelligent systems to work in production.
