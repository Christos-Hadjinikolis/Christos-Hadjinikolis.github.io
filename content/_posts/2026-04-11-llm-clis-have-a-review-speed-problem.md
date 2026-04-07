---
title: "Coding Got Cheap. Verification Did Not."
title_html: "Coding Got Cheap. <span class='blog-title-accent blog-title-accent--verification'>Verification</span> Did Not."
author: Christos Hadjinikolis
layout: post
og_image: assets/images/posts/2026/llm-clis-have-a-new-friction-point/write-throughput-vs-verification-bottleneck.png
description: "Why AI coding tools increase code supply faster than teams can verify it, and why smaller PRs, merge queues, property-based tests, static analysis, and explicit guarantees matter more than hype."
seo_keywords: ["LLM coding agents", "code review", "merge queues", "property-based testing", "static analysis", "engineering productivity", "agentic coding"]
tldr_why_read: 'Read this if your team is using <span class="blog-highlight blog-highlight--ml">LLM</span> coding tools and is discovering that faster code generation does not automatically reduce <span class="blog-highlight blog-highlight--review">review friction</span> or speed up delivery.'
tldr_persona: 'Especially useful for tech leads, staff engineers, and platform teams trying to scale delivery while <span class="blog-highlight blog-highlight--review">review</span>, integration, and trust remain stubbornly human bottlenecks.'
tldr_learn: 'Why the real constraint is now <span class="blog-highlight blog-highlight--verification">verification</span>, why <span class="blog-highlight blog-highlight--agent">agents</span> still do not carry risk ownership or real <span class="blog-highlight blog-highlight--agent">agency</span>, and why smaller PRs, merge queues, and stronger guarantees matter more than raw output.'
tldr_takeaways: ['Write throughput is rising faster than <span class=\"blog-highlight blog-highlight--verification\">verification</span> throughput', '<span class=\"blog-highlight blog-highlight--agent\">Agents</span> can generate code, but they do not own production risk', 'The practical answer is smaller PRs, better guarantees, stronger automated checks, and disciplined integration']
---
Right now, the loudest claim around <span class="blog-highlight blog-highlight--ml">LLM</span> coding tools is that coding is becoming a commodity.

I think that is directionally right.

What I do not think follows automatically is the part people usually jump to next: that software delivery will therefore speed up by the same factor.

The more I use these tools, the less convinced I am by that leap.

Yes, they can write routine code quickly; they can refactor at a pace that would have felt absurd not long ago.

But one friction point keeps getting sharper every time:

<blockquote class="blog-pullquote">
  <p>We have increased <span class="blog-highlight blog-highlight--signal">write throughput</span>.</p>
  <p>We have not increased <span class="blog-highlight blog-highlight--verification">verification throughput</span> at the same rate.</p>
</blockquote>

That is the part I think many teams are about to feel much more acutely: <span class="blog-highlight blog-highlight--review">review friction</span>.

At least, that was obvious in my own team within a week of all of us adopting <span class="blog-highlight blog-highlight--ml">LLM</span> CLIs more seriously in our workflow. Code was appearing faster. Refactors were cheaper. Experiments were easier to try. But the moment those changes started piling up, the real constraint showed itself again: someone still had to understand them, <span class="blog-highlight blog-highlight--review">review</span> them, and decide whether they were safe to merge.

And while this is easiest to see with <span class="blog-highlight blog-highlight--ml">LLM</span> CLIs and all the current code-vibing enthusiasm, I do think the point extends to <span class="blog-highlight blog-highlight--agent">agents</span> too.

<blockquote class="blog-pullquote">
  <p><span class="blog-highlight blog-highlight--agent">Agents</span> do not have the <span class="blog-highlight blog-highlight--agent">agency</span> they would need to make software delivery scale in a production environment.</p>
</blockquote>

They can generate code. They can propose plans. They can widen the search space. But they do not own production risk. They do not carry pager duty. They do not defend the change in front of a customer. They do not absorb the cost of being wrong.

That responsibility is still human.

And because that responsibility is still human, the bottleneck has moved.

<div class="image center">
  <img src="{{ 'assets/images/posts/2026/llm-clis-have-a-new-friction-point/write-throughput-vs-verification-bottleneck.png' | relative_url }}" alt="Ninja engineers generating pull requests faster than a slower verification station can review, verify, and merge them." />
  <p class="image-credit">The new imbalance is simple: code generation is accelerating faster than <span class="blog-highlight blog-highlight--review">review</span> and <span class="blog-highlight blog-highlight--verification">verification</span>.</p>
</div>

## From Writing To Verification

For a while, most of the conversation around coding <span class="blog-highlight blog-highlight--agent">agents</span> was about output:

- how many files they can touch
- how quickly they can scaffold
- how much code they can produce in one go
- whether coding itself is becoming a commodity

That is no longer enough as a way of thinking.

If code generation gets ten times faster while <span class="blog-highlight blog-highlight--review">review</span>, integration, and <span class="blog-highlight blog-highlight--verification">verification</span> stay roughly flat, the system does not become ten times faster.

It becomes unstable.

What used to be scarce was code production.

What is scarce now is trust.

And trust is slower.

It lives inside:

- <span class="blog-highlight blog-highlight--review">review</span> bandwidth
- change understanding
- test quality
- integration sequencing
- rollback confidence
- the ability to explain why a change is safe

That is why I do not find *"these tools make engineers faster"* a very useful claim on its own.

Faster at producing diffs is not the same thing as faster at delivering software.

Worse, if you leave the system unchanged, the imbalance compounds:

- more code appears
- reviewers get overloaded
- <span class="blog-highlight blog-highlight--review">review</span> quality drops
- defects move downstream
- rollback frequency rises
- trust in generated changes starts to erode

So no, the bottleneck did not disappear.

It moved from writing code to trusting code.

## The Wrong Fix: More Agents

I think many teams are still responding to this with the wrong instinct.

If generation is cheap, they assume the answer is to introduce even more <span class="blog-highlight blog-highlight--agent">agents</span>, even more automatic change, even more output.

But more <span class="blog-highlight blog-highlight--agent">agents</span> do not solve a trust bottleneck.

They amplify it.

Without strong engineering constraints, cheap generation gives you:

- bigger pull requests because exploration is cheap
- noisier pull requests because changing code is cheap
- more speculative diffs because rewriting is cheap
- slower <span class="blog-highlight blog-highlight--review">reviews</span> because understanding still costs the same

That is not scale.

That is faster chaos.

If teams do not build a stronger trust system around these tools, they will not really scale AI-assisted development. They will just generate more change than they can responsibly absorb.

## The Better Framing: Verification Systems Design

This is why I think the right framing is not *"how do we optimise the PR process?"*

It is:

<blockquote class="blog-pullquote">
  <p>How do we design a <span class="blog-highlight blog-highlight--verification">verification</span> system that can keep up with generated change?</p>
</blockquote>

Smaller PRs matter. Merge queues matter. I believe that strongly. But they are not enough on their own.

They improve the shape of change.

They do not automatically make change trustworthy.

If you want AI-assisted development to scale, you need a system that turns fast code generation into verifiable, reviewable, bounded progress.

That means moving from <em>reviewing code</em> to <em>reviewing guarantees</em>.

A <span class="blog-highlight blog-highlight--verification">verification</span> system is not just a pile of checks. It is a structured way of turning change into bounded, testable, explainable units of risk.

## Review Guarantees, Not Just Diffs

Right now, too many AI-assisted workflows still look like this:

`tool writes code -> human reviews diff -> human approves -> hope nothing subtle broke`

That does not scale.

It just shifts cognitive load onto the reviewer.

The better pattern is to require every serious change to state clearly:

- what changed
- what must remain true
- how we know it works
- what failure modes were considered

If that information is missing, the reviewer is being asked to reconstruct intent from the diff, infer risk from context, and simulate behaviour in their head.

That is expensive.

And that is exactly the kind of <span class="blog-highlight blog-highlight--review">review friction</span> we should be trying to remove.

The important part is to make those guarantees tangible. For example:

- this transformation preserves ordering invariants
- this refactor is behaviorally equivalent under property tests
- this change cannot affect downstream state transitions because the boundary remains unchanged

Once a reviewer sees that kind of claim backed by evidence, the whole exercise changes. They stop scanning raw volume and start checking bounded risk.

<div class="image center">
  <img src="{{ 'assets/images/posts/2026/llm-clis-have-a-new-friction-point/review-guarantees-not-just-diffs.png' | relative_url }}" alt="Ninja engineers reviewing guarantees, invariants, tests, and failure modes instead of just scanning raw diffs." />
  <p class="image-credit">A better <span class="blog-highlight blog-highlight--review">review</span> model is not “read more diff.” It is “check stronger guarantees.”</p>
</div>

## Back To Fundamentals

This is the part I find slightly amusing. Once you follow the argument through, the answer starts sounding strangely old-fashioned.

If <span class="blog-highlight blog-highlight--review">review friction</span> is the bottleneck, then we do not get out of it with more theatrical tooling.

We get out of it by returning to fundamentals:

- smaller PRs
- clearer intent
- narrower scope
- better tests
- merge queues
- easier rollback

That is not because these are fashionable process ideas.

It is because they reduce the cost of <span class="blog-highlight blog-highlight--review">review</span> and <span class="blog-highlight blog-highlight--verification">verification</span>.

Large PRs force reviewers into archaeology. They have to reverse-engineer intent, infer boundaries, and simulate outcomes in their head.

Small PRs let them ask a much narrower question:

> Is this one change understandable, bounded, and safe to merge?

That is a real throughput advantage.

In an <span class="blog-highlight blog-highlight--agent">agent</span>-assisted workflow, this matters even more. The natural temptation is to let the tool range widely and submit one impressive diff. That is exactly the wrong shape of change if trust is the bottleneck.

So yes, I still want smaller PRs, stacked changes, narrow intent, and one decision per <span class="blog-highlight blog-highlight--review">review</span> unit. I just no longer think of that as simple hygiene. It is part of the <span class="blog-highlight blog-highlight--verification">verification</span> system.

This is also where a simple **test-driven** instinct helps a lot.

If someone wants to do a refactor, one very clean pattern is:

1. first PR: add tests and increase coverage
2. second PR: do the refactor

The separation matters.

In the first PR, the intent is obvious: we are improving confidence.

In the second PR, the tests stay fixed, which makes the claim much narrower: behaviour should stay the same.

That lowers cognitive load immediately.

The same principle generalises. If a change is behavioural, keep the scope small. If a feature is large, deliver it in steps. The hardest work is usually restructuring, and that is exactly where thinking hard about incremental delivery matters most.

If you want something practical to adapt for your own team, I put together a reusable reference here:

* [**PR template for higher-trust AI-assisted delivery**]({{ '/references/pr-template-for-ai-assisted-delivery/' | relative_url }})

## Force Decomposition At Generation Time

This is where I would push the workflow harder.

Do not wait until <span class="blog-highlight blog-highlight--review">review</span> time to discover that the diff is too large.

Force decomposition earlier.

The correct shape is:

`task -> plan -> substeps -> PR sequence`

Not:

`task -> giant AI diff -> panic review`

This is one of the most useful things these tools can do, by the way. They should not just write code. They should help propose the incremental delivery plan by which the code can be introduced safely.

That is a much better use of an <span class="blog-highlight blog-highlight--agent">agent</span> than simply asking it for more implementation.

<div class="image center">
  <img src="{{ 'assets/images/posts/2026/llm-clis-have-a-new-friction-point/small-prs-and-merge-queue.png' | relative_url }}" alt="Ninja engineers breaking a large feature into small pull requests that move through CI, checks, review, and merge in an orderly queue." />
  <p class="image-credit">Small PRs are not tidiness theatre. They are one of the cleanest ways to lower <span class="blog-highlight blog-highlight--review">review friction</span>.</p>
</div>

## Shift Validation Left Into Machines

If humans remain the primary validators of AI-generated code, I do not think the model scales very far.

Humans should still own risk.

But they should not be forced to simulate execution in their head for every meaningful change.

That means stronger machine-side <span class="blog-highlight blog-highlight--verification">verification</span>.

### 1. Property-based testing

I think **property-based testing** is one of the most underused tools here.

Why?

Because many AI-generated bugs are not obvious syntax bugs. They are edge-case bugs. Boundary bugs. *"This looked correct for three examples and broke on the fourth"* bugs.

Property-based testing helps because it checks invariants across many generated inputs instead of blessing one or two happy-path examples.

A few practical cases:

- a parser should round-trip valid inputs without losing structure
- a serialization layer should preserve data after encode/decode
- a ranking function should preserve ordering invariants you care about
- a pricing or allocation function should never produce negative totals or violate conservation constraints
- a stream transformation should preserve event counts when it is not supposed to drop or duplicate events
- an aggregate that should only grow as more events arrive should remain monotonic
- a pipeline that depends on arrival order should preserve event ordering where that contract is supposed to hold

That matters because it turns *"I read the diff and it seemed fine"* into *"the core property stayed true under many cases."*

That is a better <span class="blog-highlight blog-highlight--verification">verification</span> signal.

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

The more routine structural mistakes a machine can reject automatically, the less human energy gets wasted on basic hygiene.

That leaves humans freer to <span class="blog-highlight blog-highlight--review">review</span> the part that actually matters: design, guarantees, and risk.

### 3. Runtime assertions

I am much less enthusiastic about **runtime assertions** than about tests, validation, or stronger system boundaries.

Most of the time, if you need an assertion, it is worth asking whether the system should have prevented that state earlier through better design, clearer contracts, or stricter validation.

In other words, I would not treat assertions as a primary <span class="blog-highlight blog-highlight--verification">verification</span> strategy.

They still have a narrow place, though, around internal invariants that should be impossible if the rest of the system is behaving correctly. For example:

- a state machine reaches an illegal transition
- two mutually exclusive internal flags are both true
- an event-ordering assumption inside one component is suddenly broken
- an internal contract is violated in a way that risks silent corruption

That is where a loud failure can be better than quietly propagating bad state.

So yes, assertions can help, but only as a last line of defence. I would much rather prevent bad states than merely notice them at runtime.

## Add Risk Awareness To Review

Another thing I think teams need is a more explicit notion of **change risk**.

Not every AI-generated change should go through the same <span class="blog-highlight blog-highlight--review">review</span> path.

There is a difference between:

- a local refactor
- a business-logic change
- a concurrency change
- a stateful systems change
- a distributed recovery or integration change

Those should not all be treated as the same kind of review object.

What I would want is some form of confidence or risk scoring:

- 🟢 low-risk cosmetic or local changes get a lighter path
- 🟠 medium-risk logic changes get stronger automated evidence
- 🔴 high-risk stateful or distributed changes get narrower scope and deeper human scrutiny

Right now, most teams still treat this too uniformly:

open PR, assign reviewer, hope for the best.

That is not mature enough for the level of change velocity these tools can produce.

## The Self-Driving Analogy

The analogy that feels closest to me is not really *"there is no driver."*

<blockquote class="blog-pullquote">
  <p>The problem with self-driving was never just whether people would emotionally accept the absence of a driver.</p>
</blockquote>

The real issue was whether there was a **validation system** strong enough to make the absence of a driver trustworthy.

Simulation mattered.

Certification mattered.

Safety cases mattered.

<span class="blog-highlight blog-highlight--verification">Verification</span> pipelines mattered.

We did not start trusting self-driving because models improved. We trusted it only to the extent that validation systems became industrial.

That is the relevant parallel here.

We do not need <span class="blog-highlight blog-highlight--agent">agents</span> with mystical <span class="blog-highlight blog-highlight--agent">agency</span>.

We need systems that make their output trustworthy enough to integrate at speed.

If I were designing for this bottleneck deliberately, I would want something closer to this:

1. A task is decomposed into a sequence of narrow changes before major implementation begins.
2. Each change states intent, invariants, and how correctness will be validated.
3. Automated checks do the first line of trust work: tests, static analysis, diff classification, CI.
4. Reviewers focus mostly on boundary decisions, guarantees, and system fit.
5. Merge queues and rollback paths keep integration disciplined and stop trust from being wasted in merge thrash.

That is a much more serious model than *"AI writes, human skims, merge and pray."*

The practical takeaway is not to resist <span class="blog-highlight blog-highlight--agent">agents</span>.

It is to build an engineering system where <span class="blog-highlight blog-highlight--review">review</span> and <span class="blog-highlight blog-highlight--verification">verification</span> can keep up with them.

The real unit of speed is not how quickly code appears in a branch.

It is how quickly a team can move a change from idea to trusted production without losing control of the system.

That is the metric that matters.

And once you define speed that way, the answer stops sounding futuristic.

It becomes strangely familiar:

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

If <span class="blog-highlight blog-highlight--ml">LLM</span> tooling keeps improving, the teams that win will not be the ones that generate the most code.

They will be the ones that turn trust into a system.

<blockquote class="blog-pullquote">
  <p>If coding is becoming a commodity, <span class="blog-highlight blog-highlight--verification">verification</span> is not.</p>
  <p>And if <span class="blog-highlight blog-highlight--agent">agents</span> do not have <span class="blog-highlight blog-highlight--agent">agency</span>, the burden of trust still sits with us.</p>
</blockquote>

Many teams are about to discover that the next productivity battle is not about writing code at all.

It is about whether their engineering system can metabolise AI-generated change without losing control.

The best prompt in the world will not save a team that cannot review, verify, and integrate change with discipline.

That is a much less theatrical advantage.

It is also the real one.
