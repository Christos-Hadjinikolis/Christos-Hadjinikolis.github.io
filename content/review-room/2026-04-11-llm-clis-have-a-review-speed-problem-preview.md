---
title: "LLM CLIs Have A Review-Speed Problem"
title_html: "<span class='blog-title-accent blog-title-accent--ml'>LLM</span> CLIs Have A Review-Speed Problem"
author: Christos Hadjinikolis
layout: post
hide: true
date: 2026-04-11
permalink: /review-room/post-4/
robots: noindex, nofollow, noarchive
canonical: false
og_image: assets/images/posts/2026/llm-clis-have-a-new-friction-point/write-throughput-vs-verification-bottleneck.png
description: "Why AI coding tools increase code supply faster than teams can verify it, and why smaller PRs, merge queues, property-based tests, static analysis, and explicit guarantees matter more than hype."
seo_keywords: ["LLM coding agents", "code review", "merge queues", "property-based testing", "static analysis", "engineering productivity", "agentic coding"]
tldr_why_read: 'Read this if your team is using <span class="blog-highlight blog-highlight--ml">LLM</span> coding tools and is starting to realise that generating code faster is not the same thing as delivering software faster.'
tldr_persona: 'Especially useful for tech leads, staff engineers, and platform teams trying to scale delivery while review, integration, and trust remain stubbornly human bottlenecks.'
tldr_learn: 'Why the real bottleneck is now <strong>verification throughput</strong>, why <span class="blog-highlight blog-highlight--ml">agents</span> still do not carry risk ownership, and what a higher-trust AI-assisted engineering workflow should actually look like.'
tldr_takeaways: ['Write throughput is rising faster than verification throughput', '<span class="blog-highlight blog-highlight--ml">LLM</span> tools do not remove trust; they force teams to systematise it', 'Smaller PRs help, but the real answer is decomposition, guarantees, automated checks, and better integration discipline']
---
*Preview copy shared privately for feedback before publication.*

The more I use <span class="blog-highlight blog-highlight--ml">LLM</span> coding tools, the less interested I am in the usual productivity claim.

Yes, they can write code quickly.

Yes, they can refactor faster than most humans want to.

Yes, routine implementation work is becoming cheaper.

But that does not automatically mean software delivery is getting faster.

The reason is simple:

<blockquote class="blog-pullquote">
  <p>We have increased <strong>write throughput</strong>.</p>
  <p>We have not increased <strong>verification throughput</strong> at the same rate.</p>
</blockquote>

That mismatch is now the real friction point.

I still like the phrase *"agents do not have agency,"* even if it sounds a little too clever at first. It points at something real. These tools can produce diffs. They can suggest plans. They can accelerate exploration. But they do not own production risk. They do not carry pager duty. They do not sign off on architectural consequences. They do not absorb the cost of being wrong.

That responsibility is still human.

And because that responsibility is still human, the bottleneck has moved.

<div class="image center">
  <img src="{{ 'assets/images/posts/2026/llm-clis-have-a-new-friction-point/write-throughput-vs-verification-bottleneck.png' | relative_url }}" alt="Ninja engineers generating pull requests faster than a slower verification station can review, verify, and merge them." />
  <p class="image-credit">Write throughput is scaling faster than verification throughput. That is the new friction point.</p>
</div>

## The Real Bottleneck Has Moved

For a while, most of the conversation around coding agents was about output:

- how many files they can touch
- how quickly they can scaffold
- how much code they can write in one go
- whether coding itself is becoming a commodity

That conversation is no longer enough.

If code generation gets ten times faster while review, validation, and integration stay roughly flat, then the system does not become ten times faster.

It becomes imbalanced.

What used to be scarce was code production.

What is scarce now is trust.

And trust is slower.

It lives inside:

- review bandwidth
- change understanding
- test quality
- integration sequencing
- rollback confidence
- the ability to explain why a change is safe

That is why I do not find *"these tools make engineers faster"* a very useful claim anymore.

Faster at producing diffs is not the same as faster at delivering software.

## The Throughput Mismatch

This is the sharper version of the problem:

- code generation is now cheap, fast, and abundant
- code understanding is still expensive, slow, and human-bound
- risk ownership still sits with people

That is the mismatch.

If you do nothing, the natural outcome is predictable:

- more code appears
- PRs get larger or more numerous
- reviewers get overloaded
- shallow reviews start passing
- review quality degrades
- defects move downstream
- rollback frequency rises
- trust in changes starts to erode

So no, the bottleneck did not disappear.

It moved from writing code to trusting code.

That is not just a mismatch. It is a structural imbalance, and it compounds over time.

## The Wrong Fix: More Agents

I think many teams are still responding to this with the wrong instinct.

If generation is cheap, they assume the answer is to introduce even more generation.

But more agents do not solve a trust bottleneck.

They amplify it.

Without strong engineering constraints, you get:

- bigger pull requests because exploration is cheap
- noisier pull requests because changing code is cheap
- more speculative diffs because rewriting is cheap
- slower reviews because understanding still costs the same

That is not scale.

That is chaos with better tooling.

Without a stronger trust system, most teams will not scale AI-assisted development at all. They will generate more code, review less of it properly, and gradually lose control of system behaviour.

## The Better Framing: Verification Systems Design

The part I think matters most is this:

we need to stop treating this as a `PR process` problem and start treating it as a **verification systems design** problem.

Smaller PRs matter a lot. Merge queues matter a lot. I still believe that. But they are not enough on their own.

They improve the shape of change.

They do not automatically make change trustworthy.

If you want AI-assisted development to scale, you need a system that turns fast code generation into verifiable, reviewable, bounded progress.

That means moving from *reviewing code* to *reviewing guarantees*.

A verification system is not just a collection of checks. It is a structured way of turning change into bounded, testable, explainable units of risk.

## Review Guarantees, Not Just Diffs

Right now, too many AI-assisted workflows still look like this:

`tool writes code -> human reviews diff -> human approves -> hope nothing subtle broke`

That does not scale.

It just shifts cognitive load onto reviewers.

The better pattern is to require every serious change to state clearly:

- what changed
- what must remain true
- how we know it works
- what failure modes were considered

If that information is missing, the reviewer is being asked to reconstruct intent from the diff.

That is expensive.

And that is exactly the bottleneck we should be trying to remove.

The important part is to make those guarantees tangible. For example:

- this transformation preserves ordering invariants
- this refactor is behaviorally equivalent under property tests
- this change cannot affect downstream state transitions because the boundary remains unchanged

Once a reviewer sees that kind of claim backed by evidence, they stop reviewing raw volume and start reviewing bounded risk.

<div class="image center">
  <img src="{{ 'assets/images/posts/2026/llm-clis-have-a-new-friction-point/review-guarantees-not-just-diffs.png' | relative_url }}" alt="Ninja engineers reviewing guarantees, invariants, tests, and failure modes instead of just scanning raw diffs." />
  <p class="image-credit">The higher-trust review model is not "read more diff." It is "review stronger guarantees."</p>
</div>

## Smaller PRs Still Matter, But For A More Serious Reason

I still think **smaller incremental PRs** are essential.

Not because they are aesthetically cleaner.

Because they reduce verification cost.

Large PRs force reviewers into archaeology. They have to reverse-engineer intent, infer boundaries, and simulate outcomes in their head.

Small PRs let them ask a narrower question:

> Is this one change understandable, bounded, and safe to merge?

That is a throughput advantage.

In an agent-assisted workflow, this matters even more. The natural temptation is to let the tool range widely and submit one impressive diff. That is precisely the wrong shape of change if trust is the bottleneck.

So yes, I still want smaller PRs, stacked changes, narrow intent, and one decision per review unit. I just no longer think of that as simple review hygiene. It is part of the verification system.

## Force Decomposition At Generation Time

This is where I would push the workflow harder.

Do not wait until review time to discover that the diff is too large.

Force decomposition earlier.

The correct shape is:

`task -> plan -> substeps -> PR sequence`

Not:

`task -> giant AI diff -> panic review`

This is one of the most practical uses of these tools, by the way. They should not only help write code. They should help propose the **incremental delivery plan** by which the code can be introduced safely.

That is a much more interesting use of an agent than just asking it to generate more implementation.

<div class="image center">
  <img src="{{ 'assets/images/posts/2026/llm-clis-have-a-new-friction-point/small-prs-and-merge-queue.png' | relative_url }}" alt="Ninja engineers breaking a large feature into small pull requests that move through CI, checks, review, and merge in an orderly queue." />
  <p class="image-credit">Small PRs are not tidiness theatre. They are how teams lower verification cost and keep integration moving.</p>
</div>

## Shift Validation Left Into Machines

If humans remain the primary validators of AI-generated code, I do not think the model scales very far.

Humans should still own risk.

But they should not be forced to simulate execution in their head for every meaningful change.

That means stronger machine-side validation.

### 1. Property-based testing

I think **property-based testing** is one of the most underused tools here.

Why?

Because many AI-generated bugs are not obvious syntax bugs. They are edge-case bugs. Boundary bugs. *This looked correct for three examples and broke on the fourth* bugs.

Property-based testing helps because it checks invariants across many generated inputs instead of blessing one or two happy-path examples.

A few practical cases:

- a parser should round-trip valid inputs without losing structure
- a serialization layer should preserve data after encode/decode
- a ranking function should preserve ordering invariants you care about
- a pricing or allocation function should never produce negative totals or violate conservation constraints
- a stream transformation should preserve event counts or monotonic properties where those are supposed to hold

That matters because it turns *"I read the diff and it seemed fine"* into *"the core property stayed true under many cases."*

That is a better trust signal.

### 2. Static analysis gates

**Static analysis** is another place where teams should be more aggressive.

Not static analysis theatre. Not one more badge in CI.

Real gates.

Practical examples:

- type errors should fail fast
- nullability violations should fail fast
- unsafe imports or forbidden dependencies should fail fast
- obvious dead code or unhandled branches should fail fast
- insecure patterns or dangerous API usage should fail fast

The more routine structural mistakes a machine can reject automatically, the less reviewer energy gets wasted on basic hygiene.

That leaves humans freer to review the part that actually matters: design, guarantees, and risk.

### 3. Runtime assertions

I would be a bit more careful with **runtime assertions**.

They are useful, but they are not a universal answer.

In the right places, they are powerful:

- assert that a state transition is legal
- assert that a value range remains sane
- assert that an event timestamp or ordering assumption still holds
- assert that an internal contract was not silently violated

These are especially valuable in systems where silent corruption is worse than loud failure.

But they are not free either.

Too many assertions in the wrong places can create noise, brittleness, or production overhead that teams stop respecting. So I would use them deliberately, especially around critical invariants, stateful boundaries, and data contracts, not as a blanket substitute for thinking.

## Add Risk Awareness To Review

Another thing I think teams need is a more explicit notion of **change risk**.

Not every AI-generated change should go through the same review path.

There is a difference between:

- a local refactor
- a business-logic change
- a concurrency change
- a stateful systems change
- a distributed recovery or integration change

Those should not all be treated as the same kind of review object.

What I would want is some form of confidence or risk scoring:

- low-risk cosmetic or local changes get a lighter path
- medium-risk logic changes get stronger automated evidence
- high-risk stateful or distributed changes get narrower scope and deeper human scrutiny

Right now, most teams still treat this too uniformly:

open PR, assign reviewer, hope for the best.

That is not mature enough for the level of change velocity these tools can produce.

## The Self-Driving Analogy, Properly Used

The analogy that feels closest to me is not really *"there is no driver."*

It is this:

the problem with self-driving was never just whether people would emotionally accept the absence of a driver.

The real issue was whether there was a **validation system** strong enough to make the absence of a driver trustworthy.

Simulation mattered.

Certification mattered.

Safety cases mattered.

Verification pipelines mattered.

We did not start trusting self-driving because models improved. We trusted it only to the extent that validation systems became industrial.

That is the relevant parallel here.

We do not need agents with mystical *agency*.

We need systems that make their output trustworthy enough to integrate at speed.

## Merge Queues Still Matter

This is also why I still think **merge queues** matter a lot.

If generation becomes easier, then integration discipline becomes more important.

Merge queues help because they:

- turn integration into an explicitly managed flow
- reduce branch collision noise
- make sequencing more predictable
- lower the chaos around concurrent change

They do not create trust on their own.

But they stop trust from being wasted in merge thrash and timing games.

## What A Higher-Trust Workflow Looks Like

If I were designing for this bottleneck deliberately, I would want something closer to this:

<div class="image center">
  <img src="{{ 'assets/images/posts/2026/llm-clis-have-a-new-friction-point/guarantees-driven-delivery-flow.png' | relative_url }}" alt="Ninja engineers moving small pull requests through a guarantees-focused workflow with static analysis, property tests, invariants, and explicit review criteria." />
  <p class="image-credit">The goal is not more code in flight. It is a calmer path from generated change to trusted production.</p>
</div>

1. A task is decomposed into a sequence of narrow changes before major implementation begins.
2. Each change states intent, invariants, and how correctness will be validated.
3. Automated checks do the first line of trust work: tests, static analysis, diff classification, CI.
4. Reviewers focus mostly on boundary decisions, guarantees, and system fit.
5. Merge queues and rollback paths keep integration disciplined.

That is a much more serious model than *"AI writes, human skims, merge and pray."*

## The Real Unit Of Speed

The real unit of speed is not how quickly code appears in a branch.

It is how quickly a team can move a change from idea to trusted production without losing control of the system.

That is the metric that matters.

And once you define speed that way, the answer stops being futuristic.

It becomes strangely old-fashioned:

- smaller PRs
- clearer intent
- stronger guarantees
- better tests
- static analysis gates
- selective runtime assertions
- merge queues
- low-friction rollback

These are not bureaucratic leftovers from a slower era.

They are what make faster tooling usable.

## The Harder Point

If <span class="blog-highlight blog-highlight--ml">LLM</span> tooling keeps improving, the teams that win will not be the ones that generate the most code.

They will be the ones that turn trust into a system.

Many teams are about to discover that the next productivity battle is not about writing code at all.

It is about whether their engineering system can metabolise AI-generated change without losing control.

That is a much less theatrical advantage.

It is also the real one.
