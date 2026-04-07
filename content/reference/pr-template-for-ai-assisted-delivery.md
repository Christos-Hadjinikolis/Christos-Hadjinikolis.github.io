---
title: Pull Request Template For AI-Assisted Delivery
subtitle: A markdown template for smaller, more reviewable, higher-trust change
layout: page
hide: true
permalink: /references/pr-template-for-ai-assisted-delivery/
intro_theme: experience
intro_kicker: "Reference"
intro_summary: "A reusable PR template shaped around the ideas in the verification post: narrow scope, explicit guarantees, evidence, and reviewability."
intro_card_title: "What This Template Optimizes For"
intro_points:
  - "Lower cognitive load during review"
  - "Clear intent and bounded change scope"
  - "Explicit guarantees, evidence, and rollback thinking"
robots: noindex, nofollow, noarchive
canonical: false
---

<div class="page-shell">
  <section class="page-grid">
    <div class="page-panel">
      <h3>Why This Exists</h3>
      <p class="page-summary">
        When code generation gets cheaper, the real bottleneck becomes review, verification, and integration. This template is deliberately biased toward smaller, clearer pull requests that are easy to understand and safe to merge.
      </p>
    </div>

    <div class="page-panel">
      <h3>How To Use It</h3>
      <ul class="page-list">
        <li>Keep the PR scope narrow enough that one reviewer can understand it quickly.</li>
        <li>Prefer separate PRs for coverage, refactor, and behavior change when possible.</li>
        <li>Make guarantees explicit instead of forcing the reviewer to infer them from the diff.</li>
        <li>Do not treat every section as mandatory theatre; use judgment, but keep intent obvious.</li>
      </ul>
    </div>

    <div class="page-panel page-panel--wide">
      <h3>Markdown Template</h3>
      <pre><code>## Summary

Short description of the change in 2 to 4 sentences.

## Change Type

- [ ] Tests / coverage only
- [ ] Pure refactor
- [ ] Small behavior change
- [ ] New feature increment
- [ ] High-risk stateful / distributed change

## Risk Level

- 🟢 Low: cosmetic or local change
- 🟠 Medium: logic or behavior change with bounded impact
- 🔴 High: stateful, distributed, concurrency, recovery, or integration-sensitive change

Selected risk level: ...

## Why This PR Exists

- What pain or need does this PR address?
- Why is this the right incremental step now?

## What Changed

- ...
- ...
- ...

## What Must Remain True

- ...
- ...
- ...

Examples:
- ordering is preserved
- behavior is unchanged outside the named boundary
- no event loss / duplication is introduced
- public API contract remains the same

## Evidence

- Tests added / updated:
  - ...
- Static analysis / checks:
  - ...
- Property-based tests / invariants:
  - ...
- Manual verification:
  - ...

## Review Guidance

- Review this first:
  - ...
- Reviewers should focus on:
  - ...
- Reviewers do not need to re-check:
  - ...

## Deployment / Rollback

- Rollout notes:
  - ...
- Rollback path:
  - ...

## Follow-Up PRs

- ...
- ...
</code></pre>
    </div>

    <div class="page-panel">
      <h3>Two Useful Patterns</h3>
      <ul class="page-list">
        <li><strong>Tests first, refactor second</strong>: one PR increases coverage, the next changes structure while tests stay fixed.</li>
        <li><strong>Feature in steps</strong>: land boundaries, flags, and compatibility scaffolding before the behavioral change itself.</li>
      </ul>
    </div>

    <div class="page-panel">
      <h3>Why This Helps</h3>
      <p class="page-summary">
        The template is not trying to make PRs look polished. It is trying to make them faster to review, easier to trust, and cheaper to roll back when necessary.
      </p>
    </div>
  </section>
</div>
