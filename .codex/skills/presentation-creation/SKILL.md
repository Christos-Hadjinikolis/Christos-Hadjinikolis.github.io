---
name: presentation-creation
description: Create or revise live presentations and speaker notes in this repository, especially discussion-led HTML seminar decks. Use for slide narrative, presenter cues, mobile notes, or rehearsal revisions. For scripted YouTube narration use the separate youtube-slide-deck skill.
---

# Live presentations and speaker cues

## The presenter's preference

Christos wants to glance at notes, understand the points he must communicate, and then speak naturally and improvise. Notes must support that rhythm. They are neither a book to read aloud nor unexplained keywords.

- Before the bullets, write one short spoken lead-in that introduces what the slide is about and prepares the points. It should sound natural aloud, connect to the preceding thought, and not duplicate the title. Keep it separate from the bullet count.
- Give each slide a small, countable set of bullets. Each bullet is one meaningful speaking point.
- Start with a short **bold reminder phrase**, followed by one or two speakable sentences. Include enough context to remember what the point means and why it matters.
- Usually use three points on a content slide, one on a brief transition, and four or five only when the material needs them. These are guides, not quotas.
- Follow the thought: premise, example or explanation, then implication or question. Adapt this order to the slide rather than imposing a formula.
- Write in a direct, conversational voice. First-person phrasing is useful when appropriate. Leave space for the presenter to add his experience and respond to the audience.
- Keep transitions short and attach them to a substantive point where possible. Do not inflate the count with housekeeping or delivery instructions.
- Match CLICK labels to actual reveal order. Brief facilitation directions can sit inside a discussion bullet.
- Keep sources, detailed history and optional preparation in separate or collapsed background. Keep essential factual qualifications in the live cue; brevity must not change the claim.

Weak cue: “Standards — quality.”

Useful cue: “**Shared methods** — Two suppliers saying ‘robust’ may mean different things. Agreed tests let us compare the evidence.”

The glance test: can the presenter read the reminder phrase, recover the intended point from its short explanation, look up, and continue in his own words? If understanding requires reading a long paragraph, revise it or move preparation material to background.

## Slides and delivery

Each slide communicates one central idea with an eye-catching title, a little explanatory context and a clear reason to care. Use examples and visuals to make abstract ideas concrete. Follow the agreed theme; pop-culture imagery should support the point. Preserve the audience's space to think and discuss.

Show the speaking-point count on each notes card and make anchors visually distinct. Support readable phone cards and a separate presenter window when the existing deck provides them. Distinguish independent phone browsing from genuine synchronisation; do not promise cross-device control without implementing it.

## Repository workflow

1. Read repository guidance and inspect the existing deck before editing. Preserve unrelated work and the user's accepted narrative.
2. For the UCL seminar, edit `tmp/ucl-seminar/research/deck-content.json` as the source of truth. Keep its stable slide keys. The `intro` is the spoken lead-in before the bullets; `bullets` are live cues; `background` and `refs` are preparation.
3. Rebuild with `research/build-deck.py` and `research/build-notes.py` inside that seminar directory. The notes template is `research/notes-viewer.html`. Keep HTML notes, Markdown notes and the audience notes overlay consistent.
4. In an editorial rewrite, preserve audience content, timings, sources and factual meaning. If a substantive claim needs updating, verify it separately rather than silently changing it while shortening prose.
5. Check every slide has meaningful cues, anchors and the correct count. Review representative phone and desktop renderings; check navigation, reveal-linked cues and presenter synchronisation when those components change.
6. Keep private seminar output private. Do not publish or push unless requested. A notes-only edit does not require building the entire Jekyll site.

## Public UCL edition

The user authorised publishing the UCL deck and presenter notes on the website. After further slide edits, run `python3 scripts/export_ucl_seminar.py` to refresh `presentations/ucl-ai-trust/`. This exports only public fields and omits slides with `private_source`; never copy the entire preparation folder. The companion post is `content/_posts/2026-10-07-who-decides-when-ai-is-trustworthy.md`. Keep slide links and selected screenshots in step with numbering changes. Public presenter notes are accessible to everyone. Follow the publishing and Git skills before committing or pushing; an export alone does not deploy anything.
