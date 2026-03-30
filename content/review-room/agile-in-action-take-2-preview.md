---
title: "What Agile Actually Means When You Ship ML Systems"
title_html: "What <span class='blog-title-accent blog-title-accent--agile'>Agile</span> Actually Means When You Ship <span class='blog-title-accent blog-title-accent--ml'>ML</span> Systems"
author: Christos Hadjinikolis
layout: post
hide: true
date: 2026-04-15
permalink: /review-room/post-2/
robots: noindex, nofollow, noarchive
canonical: false
og_image: assets/images/posts/2023/agile-in-action/2023-10-31-Turner.png
description: "A 2026 revisit of Agile in ML systems: balancing experimentation, determinism, replayability, and business constraints once models are truly in production."
seo_keywords: ["agile machine learning", "production ML", "ML systems", "streaming systems", "experimentation vs production", "replayability"]
tldr_why_read: "Read this if you are tired of vague <span class=\"blog-highlight blog-highlight--agile\">Agile</span> advice that falls apart the moment an <span class=\"blog-highlight blog-highlight--ml\">ML</span> system has to run in production."
tldr_persona: "Especially useful for <span class=\"blog-highlight blog-highlight--ml\">ML</span> leads, platform engineers, and teams operating real-time prediction systems under business and reliability constraints."
tldr_learn: "Why <span class=\"blog-highlight blog-highlight--agile\">Agile</span> in production <span class=\"blog-highlight blog-highlight--ml\">ML</span> is less about sprint ritual and more about safe change, replayability, state control, and decision quality."
tldr_takeaways: ["<span class=\"blog-highlight blog-highlight--agile\">Agile</span> in <span class=\"blog-highlight blog-highlight--ml\">ML</span> is about changing systems safely", "Replay and determinism matter more than ceremony", "Business constraints often matter more than raw model accuracy"]
---
*Preview copy shared privately for feedback before publication.*

<div class="image center">
  <img src="{{ 'assets/images/posts/2023/agile-in-action/2023-10-31-Turner.png' | relative_url }}" alt="Joseph Mallord William Turner | Dutch Boats in a Gale ('The Bridgewater Sea Piece') | National Gallery, London" />
  <p class="image-credit">Picture taken from <a href="https://www.nationalgallery.org.uk/paintings/joseph-mallord-william-turner-dutch-boats-in-a-gale-the-bridgewater-sea-piece" target="_blank" rel="noopener noreferrer">National Gallery, London</a></p>
</div>

Back in 2023, after speaking with Bill Raymond on Agile in Action, I wrote <a href="{% post_url 2023-10-31-Agile-In-Action %}">a post about bridging data science and engineering</a>.

I still recognise myself in that piece.

But I can also see what it was not saying yet.

At the time, I was focused on the gap between data scientists and engineers. Since then, the question that has mattered even more to me is what happens once that gap is crossed and the system has to live in production.

That is what this follow-up is about.

When I wrote about <span class="blog-highlight blog-highlight--agile">Agile</span> in data science a couple of years ago, the whole thing sounded clean. A bit too clean.

The reality is messier.

At Vortexa, we are not *"doing <span class="blog-highlight blog-highlight--agile">Agile</span>."* We are running a real-time <span class="blog-highlight blog-highlight--ml">ML</span> system that ingests tens of millions of AIS pings a day, pushes predictions in seconds, and then has to live with those decisions in front of customers.

That changes everything.

This post is what I actually learned after operating that kind of system, not what <span class="blog-highlight blog-highlight--agile">Agile</span> is *supposed* to be, but what survives once things hit production.

## The Problem

Most teams think <span class="blog-highlight blog-highlight--agile">Agile</span> is about managing uncertainty.

In <span class="blog-highlight blog-highlight--ml">ML</span> systems, uncertainty is the default state. That is not the problem.

The problem is this:

> You are making decisions with models that are wrong in ways you do not fully understand, inside systems that cannot afford to break.

And you are doing this continuously.

In our case:

- predictions run in real time, in seconds
- validation often comes hours or days later
- corrections are messy and sometimes manual
- downstream systems assume you are *mostly right*

So the question is not, *"how do we iterate fast?"*

It is this:

> How do we iterate without destabilising the system?

That is a much harder question, and it is the one most lightweight <span class="blog-highlight blog-highlight--agile">Agile</span> advice never really gets to.

## Why This Is Hard

There is a structural tension here that most <span class="blog-highlight blog-highlight--agile">Agile</span> writing ignores.

### 1. Experimentation vs determinism

Data scientists want:

- flexibility
- rapid iteration
- freedom to try things

Production systems want:

- determinism
- reproducibility
- controlled behaviour

You cannot fully optimise both at the same time.

If you bias too hard toward experimentation, you get non-reproducible pipelines and silent failures.

If you bias too hard toward engineering rigour, you slow exploration down so much that people stop learning.

Most teams oscillate between the two.

That oscillation is the real inefficiency.

### 2. Real time vs truth

In our stack, we predict destinations in seconds using streaming data, but the ground truth emerges later through batch pipelines, confirmed movements, and delayed signals.

That means:

- the system is always partially wrong
- corrections arrive late
- historical replays do not behave like live inference

So you effectively end up with two systems:

- one that predicts
- one that explains what actually happened

If those drift too far apart, you do not just lose accuracy. You lose credibility.

### 3. Business constraints beat model accuracy

A model that predicts the *most likely* port is useless if it violates real constraints like:

- regulatory rules
- physical feasibility
- known business rules

We learned this the hard way.

Raw model output is not a product.

It is an input to a decision system.

That system includes:

- rules
- overrides
- filters
- human corrections

Ignoring that layer is where many <span class="blog-highlight blog-highlight--ml">ML</span> systems fail. Not because the model is weak, but because the model was never the full system to begin with.

## A Better Way To Think About Agile In ML

After a few years of operating this kind of stack, my mental model changed.

<span class="blog-highlight blog-highlight--agile">Agile</span> is not a process.

It is a way of managing **three competing forces**.

### 1. Exploration

This is where you are trying to reduce uncertainty.

It is where:

- experiments live
- features get tested
- models evolve

But it should be **cheap and isolated**.

If your experimentation affects production behaviour too early, you are doing it wrong.

### 2. Stability

This is what many <span class="blog-highlight blog-highlight--ml">ML</span> teams underestimate.

Stability means:

- deterministic pipelines
- versioned state
- replayability
- controlled rollouts
- observability everywhere

If you cannot replay your system and get the same result, you are not in control.

And without control, iteration is dangerous.

### 3. Translation

This is the missing piece in most discussions.

A prediction is not useful unless it can be:

- interpreted
- constrained
- trusted

This is where:

- business logic lives
- filters get applied
- confidence thresholds matter
- hysteresis and smoothing reduce noise

This layer is where *accuracy* becomes *value*.

## How This Shows Up In Practice

Some patterns actually helped us.

### 1. Separate experimentation from serving

Models are trained and iterated in isolation.

Serving systems:

- load versioned artifacts
- do not contain training logic
- are designed for rollback first, improvement second

If you cannot roll back a model safely, you should not deploy it.

### 2. Treat state as a first-class problem

Streaming systems remember things.

And that memory bites you.

We had an incident where a subtle change in partitioning logic corrupted state and produced incorrect outputs at scale.

The fix was not just *"debug the bug."*

The fix was:

- version state explicitly
- make state reset a controlled operation
- accept that some changes require wiping history

If your system cannot safely forget, it will eventually lie.

### 3. Build for replay, not just real time

Real-time systems feel impressive.

But replay is where truth lives.

You need to be able to:

- re-run historical data
- validate changes against past behaviour
- explain differences

Without replay:

- you cannot debug
- you cannot trust improvements
- you cannot explain failures

### 4. Accept that *"good enough"* is contextual

There is no universal accuracy target.

A model can be:

- statistically strong
- operationally useless

What matters is:

- stability of predictions
- consistency over time
- behaviour under edge cases

We ended up introducing mechanisms like hysteresis just to stop predictions from flipping constantly.

That had more impact than improving raw accuracy.

### 5. Team structure matters more than process

One of the biggest improvements did not come from changing sprint rituals.

It came from aligning the team around:

- shared ownership of production
- no separation between modelling and engineering
- clear interfaces between components
- explicit trade-offs

If your team structure creates handoffs, your system will reflect those fractures.

## Where Most Agile Advice Breaks

A lot of <span class="blog-highlight blog-highlight--agile">Agile</span> advice assumes:

- work can be decomposed cleanly
- outcomes are predictable per iteration
- progress is visible through story completion

None of that really holds in production <span class="blog-highlight blog-highlight--ml">ML</span> systems.

You can:

- complete a sprint
- ship code
- hit every acceptance criterion

...and still move the system backwards.

Because what matters is not *"did we build it?"*

It is this:

> Did the system behave better under real conditions?

That feedback loop is slower, noisier, and harder to interpret than most <span class="blog-highlight blog-highlight--agile">Agile</span> frameworks assume.

## Closing Thoughts

If I strip all the language away, this is what <span class="blog-highlight blog-highlight--agile">Agile</span> means to me now:

> Build systems that can change safely.

Not quickly.

Safely.

Because in production <span class="blog-highlight blog-highlight--ml">ML</span>:

- you are always wrong in some dimension
- you are always learning
- every change has side effects

So the goal is not to move fast.

The goal is to move deliberately, with enough control to understand what changed and why.

Everything else, ceremonies, boards, sprint labels, is secondary.

If you are building <span class="blog-highlight blog-highlight--ml">ML</span> systems that actually run, you will hit these constraints sooner or later.

Better to design for them early than to retrofit discipline once things start breaking.
