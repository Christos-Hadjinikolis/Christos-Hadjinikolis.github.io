---
title: "Kafka Streams vs Flink Is The Wrong Question"
title_html: "<span class='blog-title-accent blog-title-accent--kafka'>Kafka Streams</span> vs <span class='blog-title-accent blog-title-accent--flink'>Flink</span> Is The Wrong Question"
author: Christos Hadjinikolis
layout: post
og_image: assets/images/posts/2026/when-flink-earns-its-complexity-over-kafka-streams/application-vs-platform-crossroads.png
og_image_alt: "A hand-drawn ninja engineer at a crossroads between rewriting toward Flink and curating a Kafka Streams system into a more platform-aware architecture."
linkedin_post_url: https://www.linkedin.com/feed/update/urn:li:share:7445396058735579136/
linkedin_embed_url: https://www.linkedin.com/embed/feed/update/urn:li:share:7445396058735579136?collapsed=1
substack_post_url: "https://christoshadjinikolis.substack.com/p/kafka-streams-vs-flink-is-the-wrong"
description: "A production-minded comparison of Kafka Streams and Flink that focuses on state, recovery, rescaling, and platform boundaries."
seo_keywords: ["Kafka Streams", "Apache Flink", "stream processing", "stateful streaming", "event-driven architecture"]
tldr_why_read: 'Read this if you are tempted to replace <span class="blog-highlight blog-highlight--kafka">Kafka Streams</span> with <span class="blog-highlight blog-highlight--flink">Flink</span> mostly because <span class="blog-highlight blog-highlight--flink">Flink</span> feels cleaner, more modern, or more familiar.'
tldr_persona: 'Especially useful for streaming engineers and platform teams inheriting messy <span class="blog-highlight blog-highlight--kafka">Kafka</span>-native systems and deciding whether to rewrite or rehabilitate them.'
tldr_learn: 'Where <span class="blog-highlight blog-highlight--flink">Flink</span> genuinely pulls away, where <span class="blog-highlight blog-highlight--kafka">Kafka Streams</span> is stronger than its reputation, and why familiarity bias is a dangerous architecture strategy.'
tldr_takeaways: ['<span class="blog-highlight blog-highlight--flink">Flink</span> still wins on runtime flexibility and recovery', '<span class="blog-highlight blog-highlight--kafka">Kafka Streams</span> gets very far when the system is still application-shaped and Kafka-native', 'Rewriting because a framework feels old is often familiarity pretending to be engineering judgment']
---
I am not neutral about <span class="blog-highlight blog-highlight--flink">Flink</span>.

I have spent years advocating for it, using it anywhere I could, organizing London meetups around it before COVID, and talking to anyone who would listen about why the dataflow model is such a good way to think. I still love that model. I love how naturally event-driven systems can align to a domain: *a ship enters a port, this state changes, that downstream action happens next.* Both <span class="blog-highlight blog-highlight--flink">Flink</span> and <span class="blog-highlight blog-highlight--kafka">Kafka Streams</span> let you express stateful processes in a way that can stay close to business reality.

And that is exactly why this lesson was useful for me.

When I joined a later role, I found myself surrounded by repositories built with <span class="blog-highlight blog-highlight--kafka">Kafka Streams</span>. My first instinct was simple: replace them with <span class="blog-highlight blog-highlight--flink">Flink</span>. Some of those repos were chaotic, under-loved, and far away from the kind of streaming architecture I like to build. I felt outside my waters. I wanted to modernize, refactor, migrate, clean the slate.

But over time, after giving those systems the attention they deserved, I learned something more valuable than another framework argument:

<blockquote class="blog-pullquote">
  <p>The useful question is not whether <span class="blog-highlight blog-highlight--flink">Flink</span> is <em>"better"</em> than <span class="blog-highlight blog-highlight--kafka">Kafka Streams</span>.</p>
  <p>The useful question is when your streaming problem stops being an application concern and becomes a platform concern.</p>
</blockquote>

That is still the line I care about most. But now I care about it with much more respect for both sides.

<figure class="blog-figure blog-figure--wide">
  <img src="{{ 'assets/images/posts/2026/when-flink-earns-its-complexity-over-kafka-streams/application-vs-platform-crossroads.png' | relative_url }}" alt="A hand-drawn ninja engineer at a crossroads between rewriting toward Flink and curating a Kafka Streams system into a platform-aware architecture." />
  <figcaption class="blog-figure__caption">This is the real fork in the road: not which mascot wins, but whether the system is still application-shaped or is becoming a platform concern.</figcaption>
</figure>

## The Bias I Had To Correct

There is a recurring engineering mistake hiding in this topic: *you inherit a system that feels old, untidy, or unfashionable, and you start reaching for the framework you know better.*

I have had to relearn this lesson more than once in my career. It is almost embarrassing how often it comes back, which is probably proof of how important it is.

I originally wanted to replace those <span class="blog-highlight blog-highlight--kafka">Kafka Streams</span> solutions largely because I was more fluent in <span class="blog-highlight blog-highlight--flink">Flink</span>. That fluency gave me clarity in one framework and discomfort in the other, and I briefly mistook that feeling for architecture.

That is a dangerous mistake.

Once I slowed down, cleaned up the code, made the domain model clearer, and brought more disciplined engineering practices to those codebases, I ended up with a much less dramatic conclusion:

if you give an existing streaming system enough love, enough structure, and enough respect for the underlying model, you can get very far without rewriting it.

That does not make <span class="blog-highlight blog-highlight--flink">Flink</span> less good. It just makes engineering judgment less theatrical.

<figure class="blog-figure blog-figure--wide">
  <img src="{{ 'assets/images/posts/2026/when-flink-earns-its-complexity-over-kafka-streams/rewrite-or-repair.png' | relative_url }}" alt="A hand-drawn ninja engineer illustration showing the temptation to rewrite a messy Kafka Streams system while a cleaner architectural repair path is explained." />
  <figcaption class="blog-figure__caption">The urge to rewrite is strong. The better question is whether the system is structurally wrong or simply under-engineered.</figcaption>
</figure>

<div class="blog-insight">
  <span class="blog-insight__label">The Lesson</span>
  <p><strong>Framework preference is not architecture.</strong> My first instinct was to rewrite messy <span class="blog-highlight blog-highlight--kafka">Kafka Streams</span> systems into <span class="blog-highlight blog-highlight--flink">Flink</span>. The better answer was to clean the model first, then decide whether the runtime was actually the problem.</p>
</div>

## What I Still Love About Flink

Let me be clear: I am still a very strong <span class="blog-highlight blog-highlight--flink">Flink</span> advocate.

I still think the <span class="blog-highlight blog-highlight--flink">Flink</span> dataflow model is one of the cleanest ways to reason about stateful stream processing. Operator boundaries are explicit. State feels local to the operator that owns it. Checkpointing, recovery, repartitioning, and event-time semantics feel like first-class runtime concepts instead of side effects of a library attached to a broker.

That is a big deal to me, because I care a lot about how easily a streaming system can be explained.

When a framework makes the flow of state and events easy to communicate, it usually also makes the system easier to maintain.

But none of that comes for free.

<span class="blog-highlight blog-highlight--flink">Flink</span> asks you to pay an upfront complexity tax in operations, onboarding, debugging, and platform maturity. Misconfigured jobs are not charming. They are expensive. The model feels cleaner once you have paid that tax, not before.

This is why I still reach for <span class="blog-highlight blog-highlight--flink">Flink</span> eagerly when the runtime itself needs to be a serious part of the design.

## Where Kafka Streams Grew On Me

What changed for me was not that I stopped liking <span class="blog-highlight blog-highlight--flink">Flink</span>. What changed is that I learned to appreciate where <span class="blog-highlight blog-highlight--kafka">Kafka Streams</span> is more enabling than I first allowed.

### 1. The State Model Is Different, Not Just Worse

One of the things that threw me off at first was the ergonomics of state in <span class="blog-highlight blog-highlight--kafka">Kafka Streams</span>.

<span class="blog-highlight blog-highlight--kafka">Kafka Streams</span> gives you state stores, changelog-backed recovery, and table-oriented patterns that can feel more globally available than <span class="blog-highlight blog-highlight--flink">Flink</span>'s cleaner operator-local state style. The processor API is very explicit that processors interact with attached state stores, and those stores are fault-tolerant by default. In practice, the default persistent path is a local <span class="blog-highlight blog-highlight--kafka">RocksDB</span> store backed by a compacted changelog topic. On top of that, table abstractions and `GlobalKTable`-style patterns can make shared reference data or queryable state feel very convenient in the application model.

* [Kafka Streams architecture](https://kafka.apache.org/40/streams/architecture/)
* [Kafka Streams processor API and state stores](https://kafka.apache.org/42/streams/developer-guide/processor-api/)

That convenience comes with real trade-offs:

* local <span class="blog-highlight blog-highlight--kafka">RocksDB</span> state is fast and useful, but fault tolerance still depends on changelogs
* restore times can still become painful at scale, especially when local state is lost and the store must rebuild from the changelog
* the relationship between topology code and materialized state can become messy in under-disciplined repos
* the convenience of reachable state can encourage poor habits if the model is not kept clear

But convenience is still convenience. There are use cases where having easier access to shared or queryable state is genuinely useful, and it would be dishonest to pretend otherwise.

My instinct, because of my <span class="blog-highlight blog-highlight--flink">Flink</span> background, was to push <span class="blog-highlight blog-highlight--kafka">Kafka Streams</span> code toward a more operator-local way of thinking anyway: make state ownership clearer, keep logic close to the transform that really owns it, and avoid turning the topology into a stateful soup. That discipline improved those codebases a lot.

But that is exactly the point: bringing some <span class="blog-highlight blog-highlight--flink">Flink</span>-style discipline into <span class="blog-highlight blog-highlight--kafka">Kafka Streams</span> made the code better. It did not prove that the whole system needed to become <span class="blog-highlight blog-highlight--flink">Flink</span>.

### 2. Kafka-Native Integration Is A Real Strength

I am not even talking here about the obvious ecosystem point in a lazy way. Yes, <span class="blog-highlight blog-highlight--kafka">Kafka Streams</span> lives naturally inside the <span class="blog-highlight blog-highlight--kafka">Kafka</span> ecosystem. Yes, it works comfortably with keyed messages, schemas, topics, and the usual surrounding tooling. Yes, schema-registry-oriented flows often feel more straightforward there.

That matters. Not because <span class="blog-highlight blog-highlight--flink">Flink</span> cannot do these things. It can. But because being native to the ecosystem reduces friction when the whole world around the application is already shaped like <span class="blog-highlight blog-highlight--kafka">Kafka</span>.

You should not dismiss that as a minor detail. It is part of the operating model.

## Where Flink Still Pulls Away

This is where my original instincts still hold up.

### 1. Scaling Stops At The Broker Boundary Much Earlier In Kafka Streams

The scaling constraint in <span class="blog-highlight blog-highlight--kafka">Kafka Streams</span> is tightly tied to partitions, tasks, and instances. That is not a bug. It is the design. It is also why the system stays so close to <span class="blog-highlight blog-highlight--kafka">Kafka</span> itself.

But it has consequences.

There comes a point where adding more application instances does not really solve the problem because the partitioning boundary is already telling you how far you can go cleanly. You can absolutely scale <span class="blog-highlight blog-highlight--kafka">Kafka Streams</span>, but the broker topology keeps exerting a much stronger influence on the application topology.

At that point, scaling stops being primarily demand-driven and starts becoming topology-constrained.

<span class="blog-highlight blog-highlight--flink">Flink</span>, by contrast, is still constrained at the source when consuming from <span class="blog-highlight blog-highlight--kafka">Kafka</span>, but once records are inside the runtime it has far more freedom to repartition, redistribute work, and run operators at a different parallelism from the source. I would not call that infinite scaling. I would call it a materially more flexible runtime.

* [Stateful stream processing](https://nightlies.apache.org/flink/flink-docs-stable/docs/concepts/stateful-stream-processing/)
* [Flink concepts overview](https://nightlies.apache.org/flink/flink-docs-stable/docs/concepts/overview/)

That difference becomes major once traffic spikes, repartition pressure, or uneven workloads start shaping your architecture.

### 2. Checkpointing And Recovery Are In A Different League

This is still one of the clearest differentiators for me.

<span class="blog-highlight blog-highlight--flink">Flink</span>'s checkpointing model is part of the platform. Recovery is an explicit runtime capability, not just the consequence of rebuilding local state from changelogs. The barrier-based snapshotting model, savepoints, and state redistribution semantics are exactly the kind of thing that make <span class="blog-highlight blog-highlight--flink">Flink</span> feel like an engine rather than a library.

In <span class="blog-highlight blog-highlight--kafka">Kafka Streams</span>, the picture is a little more nuanced than *"it always has to read the whole changelog again."* If the local state store still exists, the runtime can replay from the previously checkpointed offset and catch up from there. If local state is gone, it has to rebuild from the changelog from the beginning of the retained data. That is meaningfully better than a naive full replay every time, and it is one of the reasons the <span class="blog-highlight blog-highlight--kafka">RocksDB</span> path works as well as it does in practice.

But the deeper point still holds: fault tolerance and task migration are still anchored in changelog restoration, and on large stateful applications that can become one of the dominant operational pain points. Retention choices matter. Restore time matters. Recovery becomes less predictable under failure. Operational patience starts turning into architecture.

* [Running Streams applications and state restoration](https://kafka.apache.org/41/streams/developer-guide/running-app/)

That is the point where <span class="blog-highlight blog-highlight--flink">Flink</span> stops being a nice architectural preference and starts becoming a serious operational advantage.

## The Real Trade-Off

So, here is the trade in one sentence:

<span class="blog-highlight blog-highlight--kafka">Kafka Streams</span> is a very good way to build <span class="blog-highlight blog-highlight--kafka">Kafka</span>-native streaming applications.

<span class="blog-highlight blog-highlight--flink">Flink</span> is a very good way to operate stateful dataflows as a platform concern.

Those are not the same problem, even if the diagrams sometimes look similar.

And this is why I do not buy generic advice like *"use <span class="blog-highlight blog-highlight--flink">Flink</span> if you need scale"* or *"use <span class="blog-highlight blog-highlight--kafka">Kafka Streams</span> if you want simplicity."*

Both statements are misleading. They sound practical, but they hide the real failure modes, encourage cargo-cult architecture, and make comfort-driven rewrites sound more principled than they are.

The better rule is this:

<blockquote class="blog-pullquote blog-pullquote--compact">
  <p>If your system is still primarily an application that processes <span class="blog-highlight blog-highlight--kafka">Kafka</span> topics, <span class="blog-highlight blog-highlight--kafka">Kafka Streams</span> is often the right engineering choice.</p>
  <p>If your system is becoming a stateful processing layer that needs explicit control over time, state, replay, recovery, and heterogeneous I/O, <span class="blog-highlight blog-highlight--flink">Flink</span> starts to justify its existence very quickly.</p>
</blockquote>

## The Harder Lesson

This is the part I most wanted to say personally.

I am still a huge <span class="blog-highlight blog-highlight--flink">Flink</span> proponent. That has not changed.

What has changed is that I now trust myself less when my first reaction is *"we should rewrite this in the framework I prefer."*

That reaction is often just comfort seeking.

Sometimes you really should migrate. Sometimes the runtime boundary is wrong, recovery is too painful, scaling is too constrained, and <span class="blog-highlight blog-highlight--flink">Flink</span> is the more honest architecture.

But sometimes the better engineering decision is to love the existing system properly: clarify the model, clean the state boundaries, improve the abstractions, respect the domain flow, and stop assuming that old means wrong.

That was the lesson here for me.

If I had followed my first instinct blindly, I would have replaced some systems for the wrong reason.

## What I Would Actually Do

If I were starting with a <span class="blog-highlight blog-highlight--kafka">Kafka</span>-centric JVM team, modest operational requirements, and clean <span class="blog-highlight blog-highlight--kafka">Kafka</span>-in/<span class="blog-highlight blog-highlight--kafka">Kafka</span>-out topologies, I would still be very happy with <span class="blog-highlight blog-highlight--kafka">Kafka Streams</span>.

I would move toward <span class="blog-highlight blog-highlight--flink">Flink</span> once one or more of these became persistently true:

* stateful jobs became expensive to recover or rescale
* I needed a broader processing platform rather than a library
* event-time and replay behaviour started driving design choices
* the system stopped being comfortably <span class="blog-highlight blog-highlight--kafka">Kafka</span>-shaped
* operability and runtime visibility became a daily concern rather than an occasional debugging aid

That is the moment <span class="blog-highlight blog-highlight--flink">Flink</span> stops being overkill and starts being the more honest architecture.

And that brings me back to where I started.

I still love <span class="blog-highlight blog-highlight--flink">Flink</span>. I still think its model is easier to reason about once runtime concerns become serious. I still think it is the stronger platform when state, recovery, and rescaling dominate the design.

Many rewrites begin as comfort and only later get dressed up as architecture.

That is the part I understand better now, and it is probably the most useful thing this comparison taught me.
