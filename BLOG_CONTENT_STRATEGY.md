# Blog Content Strategy Guide

This file captures the editorial instructions for what the `ML-Affairs` blog should write about, why the blog should exist, and how to decide whether a post is worth publishing.

Use this together with [`BLOG_WRITING_STYLE.md`](/Users/chadjinik/Github/CH/Christos-Hadjinikolis.github.io/BLOG_WRITING_STYLE.md):

- `BLOG_CONTENT_STRATEGY.md` decides whether a topic is worth writing and what angle it should take
- `BLOG_WRITING_STYLE.md` decides how the post should sound once the topic is chosen

## Why Anyone Should Read This Blog

In a world where LLMs can generate endless generic content, this blog should not compete on raw explanation alone.

People should read this blog for things that are hard to fake:

- judgment under real production constraints
- trade-offs made in messy systems
- failures, near-misses, and what they taught
- synthesis across modelling, infrastructure, and product
- opinions earned through building systems that actually run

The point of the blog is not:

- to summarize whatever is trending in AI
- to restate documentation
- to publish generic tutorials with no point of view
- to sound impressive

The point is:

- to explain what it takes to make intelligent systems work in the real world
- to write from experience, not simulation
- to offer signal, not volume

## Core Positioning

The blog should be positioned around:

- real-time, production-grade ML systems
- event-driven and streaming architectures
- the gap between experimentation and deployment
- reliability, observability, and graceful degradation
- decision systems operating under real-world constraints
- staff-level engineering judgment in ML systems

This is not a generic AI blog.

It is a systems blog written by someone who has operated across:

- data ingestion
- backend and infrastructure
- machine learning
- production serving
- business-facing decision systems

## What Makes The Blog Worth Reading

The differentiator is not "machine learning."

The differentiator is the combination of:

- systems thinking
- production realism
- architectural judgment
- domain-aware trade-offs
- a strong view on what actually matters once a system leaves the notebook

If a post could have been produced by an LLM with no real operational exposure, it is probably not worth publishing here.

## What To Write About

Prefer topics where there is asymmetric credibility from direct experience.

### 1. Production postmortems without drama

Write about:

- what almost broke
- what was misunderstood early
- what changed once a system hit production
- what the failure mode revealed about the design

These posts are valuable because they contain cost, consequence, and hindsight.

### 2. Architecture decisions

Write about:

- why a certain architecture was chosen
- where streaming is worth the complexity
- when batch is the better engineering decision
- how to think about backfills versus live inference
- where state, replayability, and determinism matter

These posts should show reasoning, not just outcomes.

### 3. ML systems reality

Write about:

- what "good enough" means in production
- how models degrade over time
- where observability matters most
- how to design for rollback, replay, and recovery
- why the bottleneck is often not the model

These posts should bring theory back to operating conditions.

### 4. Staff-level engineering in ML

Write about:

- how technical standards get established
- how quality scales through teams rather than individual heroics
- what changes when scope becomes cross-team
- how to think about ownership, interfaces, and long-term maintainability

These posts should reflect engineering leadership through systems and decisions.

### 5. Domain-constrained AI

Write about:

- how real-world constraints reshape model design
- why unconstrained prediction is often useless
- how business logic and model logic interact
- when accuracy is the wrong optimization target

These posts are especially strong when grounded in operational detail.

### 6. Opinionated essays with technical weight

Write about:

- where common ML advice breaks down
- which MLOps patterns are cargo cult
- why many AI demos are operationally unserious
- why deterministic systems are underrated

These posts should be argued carefully and backed by experience.

## What Not To Write

Avoid topics that are now easy to mass-produce and hard to differentiate.

Examples:

- "What is RAG?"
- "What is Kafka?"
- "Top 10 tips for MLOps"
- "Why AI is changing everything"
- generic framework tutorials
- paper summaries with no applied judgment
- commentary that only mirrors the current hype cycle

These topics are not forbidden, but they need an original angle rooted in experience. Without that, they are low-value.

## The Publishing Filter

Before drafting a post, ask:

1. Did I learn this by actually doing it?
2. Did it cost time, mistakes, or responsibility to learn?
3. Do I have a non-obvious opinion on it?
4. Can I explain where the standard advice breaks down?
5. Would this still be useful to someone who already knows the basics?

If the answer is mostly "no," the post is probably not worth writing.

## The Standard To Aim For

The blog should be:

- low-frequency
- high-signal
- experience-backed
- systems-oriented
- opinionated enough to be memorable

It should not aim to publish often just to stay active.

One strong post with real insight is worth more than ten competent summaries.

## Default Framing For Future Posts

When in doubt, bias future posts toward one of these angles:

- "Here is what production changed about the theory."
- "Here is where the obvious solution failed."
- "Here is the trade-off most people ignore."
- "Here is what operating the system taught me."
- "Here is what gets harder at scale, and why."

## One-Line Editorial Rule

Write the kind of post that only someone who has built and operated intelligent systems under real constraints could write.
