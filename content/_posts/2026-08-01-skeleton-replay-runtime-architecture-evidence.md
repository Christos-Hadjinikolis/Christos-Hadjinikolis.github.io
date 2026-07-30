---
title: "Skeleton: Runtime Evidence Beats Architecture Guesswork"
title_html: "<span class='blog-title-accent blog-title-accent--signal'>Skeleton</span>: Runtime Evidence Beats Architecture Guesswork"
author: Christos Hadjinikolis
layout: post
published: false
date: 2026-08-01
canonical: false
description: "Why vibe-coded Python projects need runtime evidence, how building a local AI assistant harness exposed the limits of code review alone, and how Skeleton turns one execution path into a human and LLM-readable architecture replay."
seo_keywords: ["Skeleton", "skeleton-replay", "vibe coding", "runtime tracing", "architecture replay", "Python architecture", "developer tools", "LLM-readable workflow", "AI coding", "software design", "architecture evidence", "PyCharm plugin"]
nav_tags: ["Architecture", "Python", "LLMs", "Developer Tools"]
tldr_why_read: "Read this if <span class=\"blog-highlight blog-highlight--agent\">AI</span> tools are helping you write code faster than you can understand, review, or explain the system that now exists."
tldr_persona: "Especially useful for <span class=\"blog-highlight blog-highlight--python\">Python</span> engineers, staff engineers, and vibe-coding teams who need a better way to inspect runtime behaviour than staring at thousands of lines of source."
tldr_learn: "Why <span class=\"blog-highlight blog-highlight--signal\">runtime evidence</span> matters for fast-growing codebases, how <span class=\"blog-highlight blog-highlight--python\">Python</span> can trace execution through standard runtime hooks, and how Skeleton turns one scenario into trace, snapshot, workflow, quality, and replay artifacts."
tldr_takeaways: ["The answer to a fast-growing AI-coded codebase cannot always be \"go read the code\"", "Runtime replay gives humans a visual workflow and gives <span class=\"blog-highlight blog-highlight--agent\">LLMs</span> structured evidence", "Skeleton is a developer-understanding tool, not a profiler", "One scenario is not the whole system, but it is far better evidence than architecture guesswork"]
---

{% comment %}
Draft TODO: keep unpublished until Promet screenshots, Skeleton replay screenshots, the PyCharm plugin video, and a post-specific social preview image are ready.
{% endcomment %}

The first real pain of AI-assisted coding is not getting code.

It is keeping up with the code after it exists.

At the beginning, this sounds like a ridiculous complaint. The model writes the boilerplate. It fills in the tests. It suggests a refactor. It wires a command. It does the boring part quickly, and suddenly the project moves faster than it used to.

Then the project becomes large enough that speed turns into a different problem.

You are not asking, "Can I generate this?"

You are asking, "Do I still understand what I generated?"

## The Chore Nobody Sells With Vibe Coding

Vibe coding is the trend everyone is fixated on right now.

And I get it. Being able to generate code quickly is beautiful. It changes the feel of programming. The friction of trying an idea drops dramatically. You can ask for a feature, a refactor, a test, a CLI command, a UI panel, a background worker, and the code starts appearing.

But there is a very unglamorous problem sitting right behind the excitement.

<blockquote class="blog-pullquote">
  <p>The faster the code appears, the faster your mental model goes stale.</p>
</blockquote>

When a project is small, the default answer is simple: go and read the code.

That answer stops being serious once the codebase grows. If the system is hundreds of thousands of lines, if the architecture boundaries were not designed correctly from the start, if loose functions and accidental modules have spread into the corners, if responsibility is scattered across places that do not obviously own it, then "just read the code" becomes a strangely optimistic suggestion.

It is not that reading code is useless. Of course it is useful. But source code tells you what could happen. It does not automatically show you what did happen in the workflow you care about.

And this matters more when an LLM helped create the code.

The model can create modules and classes. It can write tests. It can refactor. It can even explain what it thinks it built. But that does not mean the system's runtime behaviour is now obvious to you, or to the model.

That was the problem I ran into.

## Why I Started Building A Harness

For a while now I have been building a local AI assistant harness.

I am building it because I want to understand the hard parts properly. Not from a diagram. Not from a launch thread. Not from a shallow demo. I want to understand what it takes to build the thing that sits between a user and an LLM.

That means tool calling, tool registries, context management, context compaction, memory, short-term context, long-term memory, RAG, prompt enrichment, profile handling, voice interaction, approvals, traces, UI state, and all the awkward little details in between.

Call it the control layer. Call it the harness. Call it the product boundary around the model.

That boundary is where the interesting work happens.

<blockquote class="blog-pullquote">
  <p>I am building a <span class="blog-highlight blog-highlight--harness">harness</span> so that you do not have to learn the hard way how difficult a harness really is.</p>
</blockquote>

It has been revelational. I have learned a lot about what these models can do, where they are genuinely useful, and where they need much stronger boundaries than people like to admit.

But something became obvious very quickly: I could not follow the code anymore.

{% comment %}
Media TODO: add a Promet demo clip showing the local assistant UI, a voice interaction, and the assistant responding.
{% endcomment %}

## The Naive Assumption

When I started, I had a very naive assumption.

I thought: fine, the LLM can write code, but I will still review the pull requests. I will read the diffs. I will keep the architecture in my head. I will know what is happening.

After the tenth pull request, that belief started to look very fragile.

The issue was not only speed. It was style and ownership.

The way the LLM naturally wrote <span class="blog-highlight blog-highlight--python">Python</span> code was not always close to the object-oriented, actor-owned design I wanted. It had a tendency to create loose modules, loose functions, overloaded files, and little islands of behaviour that looked harmless locally but made the system harder to reason about globally.

One example stayed with me. I had multiple assistant profiles being instantiated up front, even though the whole product was thread-driven and only one assistant profile needed to be active for a given thread. That was not a subtle philosophical disagreement. It was redundant runtime behaviour. It reflected an ownership problem.

The uncomfortable part was this: I did not even know it was happening.

I did not know because I had not written all the code. I did not know because reading every changed file was too slow. I did not know because I had no good way to step through the system as an architectural workflow.

So at some point the problem became very clear:

<blockquote class="blog-pullquote">
  <p>I did not have a code generation problem.</p>
  <p>I had a code understanding problem.</p>
</blockquote>

## How Developers Understand Code

This forced me to think about something basic.

How do developers actually understand code?

Not how do we pretend to understand code. How do we really do it?

For me, code understanding is a mental model of flow. Something starts at an entry point. It moves through a module. It calls an object. That object owns some behaviour. A repository owns persistence. An adapter owns a boundary. A service coordinates a decision. Some value crosses from one place to another. Something returns.

That is why we care about abstraction. That is why we care about encapsulation. That is why object-oriented design, when done well, is not just ceremony. It gives us a way to group responsibility into actors we can think about.

We want to know who owns what.

That is also the rule I have been trying to force back into Promet: state, policy, lifecycle, I/O, validation, tracing, and orchestration should have visible owners. If a behaviour matters, it should not hide as a loose helper in a miscellaneous module.

So if ownership and data flow are the things I want to see, then a graph is the obvious shape.

Not a static graph of every possible import. Not a generic repository map. Not a confident AI summary that says "this appears to be a service layer" because it saw a filename called `service.py`.

I wanted the graph of what actually happened.

## The Late-Night Realisation

One late night, while trying to reason through these problems with an LLM, the obvious thing finally landed.

<span class="blog-highlight blog-highlight--python">Python</span> can trace itself.

That sounds slightly magical if you have not used the runtime hooks before, but it is very practical. Python exposes introspection and tracing APIs that let a program observe calls, returns, frames, file names, function names, local variables, and selected runtime events while another piece of Python code is executing.

The key hook for Skeleton is `sys.setprofile()`.

In simple terms, `sys.setprofile()` lets you install a callback function that Python calls when certain execution events happen. For Skeleton, the interesting events are function calls and returns. Skeleton runs the target script inside a controlled runner, observes project-local frames, and ignores local infrastructure like virtual environments, Git internals, and its own `.skeleton` output directories.

When a call happens, Python gives the callback a frame object. Skeleton reads a controlled slice of that frame: `frame.f_code` for the code object, file path, function name, and first line number; `frame.f_globals` for module context; and `frame.f_locals` for arguments and `self`.

That is enough metadata to say:

- this function was called
- it came from this file
- it belongs to this module
- it may be an instance method if `self` is present
- these are safe summaries of the arguments

When `self` is present, Skeleton can record the class name and a run-local object identity. That means a report can show that a method ran on a specific runtime instance without adding decorators to the target code. The object identity is not a permanent ID. It is meaningful for that one process and that one run.

On return, the hook receives the return value too, so it can record a safe summary of what came back. Values are summarized immediately, and the raw objects are discarded. When project-local code is already active on the trace stack, Skeleton can also record a small allow-list of resource boundary calls, like stdout, filesystem, SQLite, and basic socket calls.

The shape is roughly:

```python
import sys


def profiler(frame, event, arg):
    if event == "call":
        ...
    if event == "return":
        ...


sys.setprofile(profiler)
try:
    run_the_target_script()
finally:
    sys.setprofile(None)
```

That is not the full implementation, obviously, but it is the mental model.

There is also `sys.settrace()`, which is the lower-level tracing hook often used by debuggers. It can observe line-level events, but for Skeleton's first product shape, line-level debugging is not the point. The useful architectural signal is call and return flow: who called whom, in what order, with what safe value summaries, and where the important boundaries were.

Is this a Python-only idea?

No. The general idea of runtime tracing exists in many ecosystems. Java has profilers, agents, and JVM tooling. JavaScript has browser and Node profiling hooks. Native systems can use instrumentation, sampling profilers, eBPF-style approaches, and platform-specific tracing. Observability vendors do this sort of thing all the time at a different level.

What is special about <span class="blog-highlight blog-highlight--python">Python</span> is the cost of getting started. The standard runtime gives you a surprisingly direct path from ordinary user code to structured execution evidence. You do not need to rewrite the application. You do not need decorators everywhere. You do not need the target project to adopt a framework.

You can wrap an existing script or test, observe the runtime, and write artifacts.

That was enough for a first version.

## Then Skeleton Appeared

Once the tracing idea was clear, the next question was obvious: how do I make this useful?

A raw trace file is not enough. A dump of events is just another thing to stare at. I needed evidence that a developer could inspect quickly, and that an LLM could consume without guessing from source code alone.

So Skeleton became a pipeline:

<div class="blog-insight">
  <span class="blog-insight__label">Skeleton Pipeline</span>
  <div class="blog-flow">
    <div class="blog-flow__step">Run scenario</div>
    <div class="blog-flow__arrow" aria-hidden="true">&rarr;</div>
    <div class="blog-flow__step">Trace calls</div>
    <div class="blog-flow__arrow" aria-hidden="true">&rarr;</div>
    <div class="blog-flow__step">Build snapshot</div>
    <div class="blog-flow__arrow" aria-hidden="true">&rarr;</div>
    <div class="blog-flow__step">Write workflow</div>
    <div class="blog-flow__arrow" aria-hidden="true">&rarr;</div>
    <div class="blog-flow__step">Replay graph</div>
  </div>
  <p>The point is not to collect telemetry for its own sake. The point is to turn one execution path into architecture evidence.</p>
</div>

The first product decision was that Skeleton should be non-invasive.

You should be able to run:

```bash
skeleton run path/to/scenario.py
```

or:

```bash
python -m skeleton_replay run path/to/scenario.py
```

and get an artifact set beside the scenario.

No decorators. No application-code rewrite. No framework buy-in.

Skeleton records project-local public calls by default. It summarizes values rather than dumping object contents. It redacts likely secrets. It turns the observed run into a graph. And then it writes outputs that serve different audiences.

## What Skeleton Writes

The artifacts are the product.

- `trace.jsonl` is the raw ordered call and return evidence.
- `snapshot.json` is the derived graph: modules, functions, runtime instances, resources, edges, counts, roles, and architecture views.
- `workflow.md` is the compact written explanation for humans and LLMs.
- `quality.json` is machine-readable design signal.
- `architecture_quality.md` is a review surface with prompts, warnings, and anchors.
- `report.html` is the interactive replay for humans.
- `session.json` is the manifest that lets IDEs and automation find the artifact set.

That separation matters.

I do not want the HTML report to be the only useful object. I also do not want an LLM scraping a visual graph and pretending it understood it. The graph is for humans. The JSON and Markdown are for machines and humans who want a compact explanation.

{% comment %}
Media TODO: add a Skeleton artifact-grid screenshot showing trace.jsonl, snapshot.json, workflow.md, architecture_quality.md, report.html, and session.json together.
{% endcomment %}

## The Report Is A Workbench

The HTML report is where the idea becomes visible.

It uses a browser-based graph view, currently built around Cytoscape.js, with a replay timeline. As you move through events, the graph shows the runtime actors and relationships that have appeared so far. You can inspect a function call, see a safe summary of the arguments, see the return, and understand which actor was involved.

This is the part that matters for human understanding.

Developers do not think only in files. We think in flow. We think in paths. We think in responsibility moving from one actor to another.

The report gives that shape back to us.

{% comment %}
Media TODO: add a Skeleton replay demo clip stepping through a scenario from event 0 to the end, highlighting the selected runtime actor and call/return details.
{% endcomment %}

And then the PyCharm plugin closes the loop.

The plugin is deliberately a frontend over Skeleton. It does not trace Python itself. It invokes the configured Skeleton runner, reads `session.json`, embeds `report.html`, shows the workflow and quality outputs, and can follow selected report events back into the IDE.

That is where the loop starts to feel practical.

Run the scenario. Replay the graph. Click the event. Let the IDE take you back to the source context that produced it.

The point is not to make another report that lives beside the code. The point is to make runtime evidence usable while you are still thinking about the code.

{% comment %}
Media TODO: add a PyCharm plugin walkthrough showing the Skeleton tool window, startup report discovery, embedded replay, Workflow tab, Quality tab, and Follow in IDE behaviour.
{% endcomment %}

## Why This Helps The LLM Too

The human side is only half the story.

The other half is the LLM that is writing or modifying the code.

There is an easy trap here. Because the LLM created the modules and classes, we assume it understands how the code runs. But the model is still working from text, context windows, retrieved snippets, diffs, and whatever evidence we give it.

It can infer. It can summarize. It can sound confident.

But inference is not runtime evidence.

<blockquote class="blog-pullquote">
  <p>A model that wrote the code still benefits from being shown what the code actually did.</p>
</blockquote>

This is where Skeleton becomes more than a visualization.

A human can use the graph. The LLM can use `workflow.md`, `snapshot.json`, and selected trace-window exports. If I isolate a section of the workflow, I can hand the model a structured JSON packet that says: here are the events, here are the actors, here are the safe arguments, here are the returns, here is the call path.

That is a much better conversation.

Instead of asking the model to guess from source:

> "Please inspect this codebase and tell me how the email approval path works."

I can ask:

> "Here is the runtime evidence from the email approval scenario. Explain which actor owns the approval boundary and whether the call path matches the intended design."

Those are different tasks.

The first asks the model to infer the architecture.

The second asks it to reason from evidence.

## The Real Bridge

This is the part that excites me most.

Skeleton sits between the vibe coder, the reviewer, and the LLM.

The human needs visual understanding. We need to see the path. We need the workflow. We need to know which actors appeared at runtime and whether ownership looks sane.

The LLM needs structured evidence. It does not really benefit from a pretty graph in the same way we do. It benefits from stable IDs, JSON, Markdown, call records, safe summaries, and a compact explanation of what happened.

Skeleton gives both sides the version they can use.

<blockquote class="blog-pullquote">
  <p>The graph helps the human see the workflow.</p>
  <p>The structured artifacts help the LLM reason about it.</p>
</blockquote>

That is the bridge.

And it is a bridge I now think we need more and more as AI-assisted codebases grow quickly.

## What Skeleton Is Not

There is an honest limitation here.

One run is not the whole system.

If you trace one scenario, you have evidence for that scenario. You have not proven every possible path. You have not replaced tests. You have not solved architecture by drawing a graph. You have not built an observability vendor. You have not magically made messy code clean.

That distinction matters.

Skeleton is not a profiler. It is not primarily trying to answer "which function is slow?" It is not a debugger. It is not a replacement for code review, tests, design discipline, or explicit ownership.

It is a developer-understanding tool.

It helps you ask better questions:

- What actually ran?
- Which actor owned this behaviour?
- Which function called which function?
- Did a supposedly clean boundary get bypassed?
- Did we instantiate things we did not need?
- Did the path match the architecture we thought we had?
- What evidence can I give the next LLM or reviewer?

That is already enough.

## Why This Matters Now

The reason I care is not that I want another tool in the toolbox.

The reason I care is that AI-assisted development creates a new understanding gap.

We can generate code faster than we can review it. We can grow systems faster than we can update our mental models. We can ask LLMs to summarize repositories, but a plausible summary is not the same thing as observed behaviour.

So the answer cannot always be "go read the code."

Sometimes the answer has to be:

> Run the scenario. Generate the evidence. Replay the workflow. Then talk about the architecture.

That is what Skeleton is for.

It gives me a way to understand the local assistant harness I am building. It gives the LLM a way to corroborate its own understanding. It gives reviewers a way to discuss runtime behaviour without arguing from vibes.

That is the point: if AI helps us create software faster, our understanding tools have to become more concrete, more inspectable, and more evidence-driven.

{% comment %}
Publication TODO:
- Add one post-specific og_image PNG or JPEG.
- Add og_image_alt.
- Add screenshots or short clips for the Promet harness, Skeleton report, and PyCharm plugin workflow placeholders.
- Decide whether to include a generated opening visual contrasting static diagrams with runtime replay.
- Run the site audit before publishing.
- Prepare LinkedIn copy only after the final URL and preview image are ready.
{% endcomment %}
