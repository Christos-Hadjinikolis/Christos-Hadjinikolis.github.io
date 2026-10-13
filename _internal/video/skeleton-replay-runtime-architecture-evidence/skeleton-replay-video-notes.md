# Skeleton Replay Video Notes

Working title: **Skeleton: What Actually Ran?**

Target length: 3:15 to 4:00.

Use the HTML deck as supporting material, not as the whole video. The slides
should carry the story visually: code grows, the mental model gets stale, one
real run creates evidence, and that evidence can be replayed by a human, an IDE,
and an LLM.

The live proof should be recorded separately and stitched in the editor. The
deck no longer embeds report screenshots because the report is more convincing
when you show it moving for real.

## Style

Keep slide text sparse. Say the detail out loud.

The deck should feel like a motion storyboard:

- draw paths in the direction runtime evidence flows
- reveal nodes only when the narration names their role
- use artifacts as objects, not paragraphs
- keep persistent branding minimal; do not bake in avatars, subscribe graphics,
  watermarks, or clickable-looking badges
- leave the closing slide clean enough for YouTube end-screen overlays
- cut to real tools when the viewer needs proof

No separate Excalidraw storyboard for this version. The concept slides already
use sketch-like motion where it helps, and a separate whiteboard asset would add
production overhead without improving the first video.

Reusable deck rules now live in `.codex/skills/youtube-slide-deck/SKILL.md`.

## Core Story

Main thesis:

> AI can help us create Python systems faster than we can keep their architecture
> in our heads. Skeleton turns one real execution into replayable runtime
> evidence.

Important positioning:

- Skeleton is a developer-understanding tool, not a profiler.
- The PyPI package is `skeleton-replay`.
- The CLI command is `skeleton`.
- The PyCharm plugin is a frontend over the generated artifacts.
- `session.json` is the integration contract for IDEs and automation.

The strongest phrase to repeat:

> Source shows what could happen. Skeleton shows what did happen in this run.

## Demo App

Use the checked-in fixture:

```text
../skeleton/tests/fixtures/sample_io_boundaries/
|-- app.py
|-- order_domain.py
|-- order_service.py
|-- order_repository.py
|-- notification_adapter.py
`-- .skeleton/
    |-- trace.jsonl
    |-- snapshot.json
    |-- workflow.md
    |-- architecture_quality.md
    |-- quality.json
    |-- session.json
    `-- report.html
```

Runtime story:

- `app.py` composes the scenario.
- `OrderService` coordinates the use case.
- `SqliteOrderRepository` owns filesystem and SQLite work.
- `ConsoleNotifier` owns stdout.
- `Order` stays a small domain object.

That is enough for a useful video. Do not over-explain the fixture. The point is
the difference between inferred architecture and observed runtime evidence.

## Edit Plan

Suggested sequence:

1. Slide 1 to Slide 4: concept setup and sample app shape.
2. Source or CLI cutaway: show the fixture and the `skeleton run` command.
3. Slide 5 and Slide 6: explain non-invasive capture and artifact output.
4. Report walkthrough placeholder: record the real report moving.
5. Slide 7: return to the review question around I/O ownership.
6. Slide 8: explain the plugin contract.
7. Plugin cutaway: show PyCharm reading `session.json` and following the report.
8. Slide 9 and Slide 10: close with human plus LLM evidence.

The slides are the story spine. The cutaways are proof.

## Videos To Record

### Clip A: Source And CLI

Length: 15 to 25 seconds.

Record after Slide 4 or before Slide 5.

Show:

- `../skeleton/tests/fixtures/sample_io_boundaries/app.py`
- `order_service.py`, `order_repository.py`, and `notification_adapter.py`
- the command, either live or already visible in a terminal

Suggested command:

```bash
cd ../skeleton
uv run python -m skeleton_replay run tests/fixtures/sample_io_boundaries/app.py --out-dir tests/fixtures/sample_io_boundaries/.skeleton --no-open
```

Narration:

> This is a normal Python scenario. I am not decorating the functions or turning
> the app into a framework demo. Skeleton wraps the run and observes the
> project-local public calls and resource boundaries.

### Clip B: Report Walkthrough Placeholder

Length: 35 to 50 seconds.

Record after Slide 6.

Placeholder in the edit:

```text
[INSERT LIVE REPORT WALKTHROUGH HERE]
```

Open:

```text
../skeleton/tests/fixtures/sample_io_boundaries/.skeleton/report.html
```

Show:

- start at the entrypoint event
- play or scrub through the service call
- pause on repository database work
- pause on notifier stdout work
- switch views if useful, but keep the pace quick
- select a trace window and export JSON if the UI is clean on camera

Narration:

> This is the shift from architecture opinion to runtime evidence. The report is
> not a diagram I drew after reading the code. It is a replay of the run. As I
> move through the timeline, the active calls and resource boundaries change.

Avoid:

- reading every sidebar detail
- explaining every button
- making the report clip longer than the concept it supports

### Clip C: PyCharm Plugin

Length: 30 to 45 seconds.

Record after Slide 8.

Open the Skeleton Replay tool window in PyCharm and load:

```text
../skeleton/tests/fixtures/sample_io_boundaries/.skeleton/session.json
```

Show:

- Report tab with the generated `report.html`
- Workflow or Quality tab as secondary evidence
- Follow in IDE enabled
- click a report event and show the source highlight
- export trace-window JSON if the installed plugin build supports the local save flow

Narration:

> The plugin does not trace Python itself. It uses the configured interpreter to
> run Skeleton, then reads `session.json` to find the report and artifacts. That
> keeps the IDE integration thin and gives PyCharm the same evidence as the
> browser report.

### Clip D: Optional Scale View

Length: 10 to 15 seconds.

Use only if the main edit needs one more proof point.

Open:

```text
../skeleton/tests/fixtures/sample_large_graph/.skeleton/app/latest/report.html
```

Show:

- package or module view first
- one drilldown into detail view
- the replay controls still working

Narration:

> When the graph gets larger, the answer is not a single fixed diagram. It is
> the same trace, viewed at the level of abstraction that helps the review.

## Slide-By-Slide

### 1. What Actually Ran?

Time: 0:00 to 0:14.

On screen: title, short subtitle, three chips, evidence-loop visual.

Animation: title enters, the run loop assembles, no persistent avatar or
watermark.

Say:

> The hard part of AI-assisted coding is no longer just getting code. It is
> knowing whether the system that ran still matches the system in your head.

### 2. Fast Code. Stale Map.

Time: 0:14 to 0:34.

On screen: two short phrases only.

Animation: file tokens rush in; the mental-model graph pulses with uncertainty.

Say:

> LLMs can add files, adapters, tests, and refactors very quickly. That is useful,
> but it creates a second job: rebuilding the mental model of ownership,
> boundaries, and runtime flow.

### 3. Could Happen Is Not Did Happen.

Time: 0:34 to 0:55.

On screen: source side versus runtime side.

Animation: source stays busy; runtime path draws downward one step at a time.

Say:

> Reading code still matters, but source is a possibility space. It does not prove
> which object was instantiated, which adapter was crossed, or which branch ran
> in the scenario you care about.

### 4. One Order, A Few Owners.

Time: 0:55 to 1:16.

On screen: compact ownership graph.

Animation: nodes appear, edges draw, order packet moves through the app.

Say:

> The example is deliberately small. `app.py` composes the objects. The service
> coordinates the use case. The repository owns persistence. The notifier owns
> stdout. The domain object stays quiet.

Cut to Clip A after this slide if you want to ground the viewer in the actual
files before showing the runner.

### 5. Wrap The Run.

Time: 1:16 to 1:36.

On screen: runner boundary, two terminal lines, three chips.

Animation: capture ring expands around the app; terminal commands type in.

Say:

> Skeleton starts at the runner boundary. You run an existing script or pytest
> target. You do not put decorators through the application. The app remains a
> Python app.

### 6. A Run Becomes Evidence.

Time: 1:36 to 2:00.

On screen: one run in the center; artifact files around it.

Animation: evidence lines draw outward; artifact cards fan in.

Say:

> The artifacts are the product. `trace.jsonl` keeps the ordered events.
> `snapshot.json` builds the graph. `workflow.md` gives a compact narrative.
> `quality.json` gives review anchors. `report.html` is the browser replay, and
> `session.json` is the IDE and automation handoff.

Cut to Clip B here.

### 7. I/O Needs Owners.

Time: 2:45 to 3:02 if Clip B is used.

On screen: service, repository, notifier, domain, and I/O chips.

Animation: ownership nodes appear first, then I/O chips.

Say:

> The quality signal is not a verdict. It is a review anchor. In this fixture the
> repository should be busy because it owns persistence. The useful question is
> whether that responsibility stays intentional as the code changes.

### 8. Start At Session.json.

Time: 3:02 to 3:20.

On screen: session, report, source.

Animation: packet moves from manifest to report to source highlight.

Say:

> The plugin closes the loop inside PyCharm. It does not reimplement tracing. It
> reads `session.json`, loads the generated report and workflow, and follows
> report selections back into source.

Cut to Clip C here.

### 9. Same Evidence. Two Readers.

Time: 3:45 to 3:58 if Clip C is used.

On screen: Human and LLM.

Animation: vertical evidence stream draws between both readers.

Say:

> Humans need a visual workflow. LLMs need structured events, nodes, edges, and
> safe summaries. Skeleton is trying to make the same run useful to both.

Insert Clip D before this slide only if the video needs a quick scale proof.

### 10. Run It. Replay It. Ask From Evidence.

Time: final 10 to 14 seconds.

On screen: final phrase only, with the right side intentionally clean.

Animation: closing line locks into scenario, trace, review.

Say:

> That is the review loop: run the scenario, replay the workflow, then ask the
> architecture question from evidence. Does the system that ran match the system
> we thought we had?

## Recording Controls

Open the deck directly in a browser:

```text
_internal/video/skeleton-replay-runtime-architecture-evidence/skeleton-replay-video-slides.html?record=1
```

Controls:

- right arrow, space, or PageDown: next slide
- left arrow, Backspace, or PageUp: previous slide
- `R`: restart the current slide animation
- `C`: toggle clean recording mode
- `Home` and `End`: jump to first or last slide

Recommended recording setup:

- record 16:9 at 1920x1080 or 2560x1440
- record each slide as its own take if timing matters
- press `R` before a retake rather than refreshing the browser
- leave one second of stillness before and after every cutaway
- keep report and plugin clips short enough that the story still belongs to the video

## Files

- `skeleton-replay-video-slides.html`: animated concept deck for recording.
- `skeleton-replay-video-notes.md`: this narration and edit guide.
- No generated report screenshots are required in this folder. Use live report
  and plugin recordings for proof shots.
