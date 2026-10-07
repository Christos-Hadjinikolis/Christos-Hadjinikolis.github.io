---
title: "Who Decides When AI Is Trustworthy?"
title_html: "Who Decides When <span class='blog-title-accent blog-title-accent--signal'>AI Is Trustworthy</span>?"
author: Christos Hadjinikolis
layout: post
date: 2026-10-07 08:00:00 +0100
permalink: /blog/who-decides-when-ai-is-trustworthy/
description: "A home robot, a rejected loan and a difficult approval decision: how the EU AI Act, technical standards and inspectable evidence connect—and where assurance reaches its limits. Includes my UCL seminar slides and presenter notes."
seo_keywords: ["trustworthy AI", "EU AI Act", "CEN CENELEC JTC 21", "harmonised standards", "AI assurance", "human oversight", "embodied AI", "UCL seminar"]
og_image: /assets/images/posts/2026/who-decides-ai-trust/human-consequences.png
og_image_alt: "Seminar slide connecting refused loans, harmful recommendations and trading failures to rights, safety and accountability."
tldr_why_read: "A convincing demo can still leave you unable to justify letting an AI system act. The missing piece is a decision you can defend."
tldr_persona: "Engineers, product leaders and anyone asked to approve an AI-assisted decision or deployment. No background in EU regulation is assumed."
tldr_learn: "How law, standards and system-specific evidence connect, and why approval must be revisited when the task or system changes."
tldr_takeaways: ["Approve a defined use, not an adjective", "A standard helps structure evidence; it does not erase judgement", "A changed system may need a new approval"]
---

Would you let a robot tidy your house? Perhaps. Would you leave it alone with your baby?

That second question changes the conversation remarkably quickly. Suddenly, “the model is very capable” is an unsatisfying answer. I want to know what the robot is allowed to do, what it has been tested on, what happens when it fails, and who can intervene. I also want to know who takes responsibility for telling me that the evidence is enough.

This is the practical question behind my UCL seminar, **Who Decides When AI Is Trustworthy? The EU AI Act, Standards and the Limits of Assurance**. My perspective comes from production machine learning and participation in CEN–CENELEC JTC 21’s Working Group 3 on Engineering Aspects. I care about what happens between a reassuring claim and a system somebody actually has to operate.

If you build, buy or approve AI systems, that gap belongs to you too.

<div class="blog-insight">
  <span class="blog-insight__label">UCL seminar · 7 October 2026</span>
  <p><a href="{{ '/presentations/ucl-ai-trust/slides.html' | relative_url }}">Open the slides</a> · <a href="{{ '/presentations/ucl-ai-trust/notes.html' | relative_url }}">Open speaker notes / presenter view</a> · <a href="{{ '/presentations/ucl-ai-trust/sources.md' | relative_url }}">Sources and image credits</a></p>
  <p>The deck is a working edition and will continue to be refined. Use arrows or space to reveal points and advance. Press <strong>V</strong> in the slides for a linked presenter window; <strong>F</strong> for fullscreen.</p>
</div>

<figure class="blog-figure blog-figure--wide">
  <a href="{{ '/presentations/ucl-ai-trust/slides.html#15' | relative_url }}"><img src="{{ '/assets/images/posts/2026/who-decides-ai-trust/human-consequences.png' | relative_url }}" alt="Three illustrative decisions: a refused loan, an offensive recommendation and a trading system failure. Each raises different questions about rights, privacy, safety and accountability." width="1600" height="900" /></a>
  <figcaption class="blog-figure__caption">From the seminar: the decision may be automated, but the consequences are human.</figcaption>
</figure>

## “The AI said so” leaves too much unanswered

Take a rejected loan. Before debating whether the decision was acceptable, we need to identify the system that produced it. Which model version? Which inputs? Which training and evaluation records? What did the human reviewer see, and could they meaningfully overturn the recommendation?

An explanation can help someone understand a decision. Traceability helps reconstruct it. Accountability identifies who must answer for it. These are related requirements, but one cannot substitute for all the others. A fluent explanation does not establish that the underlying decision was fair.

The same applies to a trading system that amplifies losses, or a recommendation that exposes harmful profiling. Different situations bring different duties. The engineering question is whether we have preserved enough evidence to investigate, correct and challenge what happened.

<blockquote class="blog-pullquote"><p>An approval should attach to a defined use, a particular system and inspectable evidence.</p></blockquote>

## Law, standards and evidence do different jobs

The **EU AI Act** sets binding obligations intended to protect health, safety and fundamental rights while supporting the adoption of trustworthy AI. Its requirements depend on the use and the actors involved. A company supplying an AI system and an organisation deploying it can have different responsibilities. This is a risk-based legal framework, rather than a universal score for how dangerous a company is. The European Commission’s <a href="https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai">AI Act overview</a> explains the categories and implementation timetable.

Standards help turn broad requirements into shared technical methods: what to document, how to evaluate a claim, and how to make the result comparable. A **harmonised standard** is developed following a European Commission request to support particular EU legal requirements. Once its reference is published in the EU’s Official Journal, using it can provide a *presumption of conformity* for the requirements it covers. In plain language, that gives a recognised starting point for demonstrating compliance. It is not blanket approval of every capability or use. Standards are generally voluntary; the applicable legal duties remain binding. The Commission’s <a href="https://digital-strategy.ec.europa.eu/en/faqs/understanding-standardisation-ai-act">standardisation explainer</a> describes this relationship.

Then comes the evidence from the actual system. An agreed testing method is useful only if somebody applies it properly, records the conditions and understands what the result does—and does not—support.

CEN and CENELEC organise the European AI standards work through JTC 21. Experts enter this work through national standards bodies and other recognised participation routes. My group, WG3, brings the discussion back to what engineers can specify and test. For this talk, I describe that through three practical concerns: **data, behaviour and limits**. Is the information suitable for the task? What does the system demonstrate? What happens when it fails?

That translation takes work. Tests must be repeatable, affordable enough to use and relevant to people exposed to harm. Agreement also depends on whose expertise and interests are represented. A technically tidy process can still miss the person who bears the consequences.

## Now put the robot in your home

The seminar uses a fictional approval exercise. Start with toys and laundry on one floor, with an adult present. No stairs, cooking or childcare. What would you need to see before approving that use?

<figure class="blog-figure blog-figure--wide">
  <img src="https://cdn.sanity.io/images/qka6yvsc/production/fdda789a2e7c6caa9a798dd920b8a0acb254ea9d-1200x630.jpg?fit=max&amp;auto=format" alt="1X promotional photograph of its NEO home robot, also used in the seminar slides." loading="lazy" width="1200" height="630" />
  <figcaption class="blog-figure__caption">Image: <a href="https://www.1x.tech/neo">1X / NEO</a>, also used in the slides. The exercise is fictional; no childcare capability, failure or endorsement is attributed to the pictured product.</figcaption>
</figure>

Now the request changes: “Watch the baby while I go out.”

What does *watch* mean? Observe and send an alert? Approach the child? Pick them up? Who can respond, and how long would that take? Evidence for carrying laundry does not establish that any of those actions are acceptable.

Suppose the supplier offers a 99.9% success rate. I would ask what counted as success, how many trials were run, which conditions were represented and what the failures looked like. A rare failure can dominate the decision if its consequences are severe. The number alone leaves those questions open.

Then add remote access or a software update. We may now have a different permission boundary, different behaviour, or a different person able to act inside the home. The original approval needs another look.

For a real deployment, I would want a short approval record:

- **Allowed use:** the tasks, environment and actions covered by the decision.
- **Evidence:** the tests and observations supporting it, with their limitations.
- **Controls:** who can intervene, restrict access or stop operation.
- **Review triggers:** changes, incidents or new information that require reassessment.
- **Ownership:** who accepts the decision and who can challenge it.

This has a cost. Someone must maintain the records, rerun relevant evaluations and decide whether a change is material. A process that is too burdensome will be bypassed; one that records nothing will be difficult to defend when it matters. Good engineering makes the necessary evidence part of operating the system.

## The same question follows us into agentic AI

A physical robot makes the stakes easy to picture. A software agent can also change the world: send a message, modify a database, spend money or use a credential. Its authority matters as much as the fluency of its answer.

General-purpose systems make assurance harder because their future uses may exceed the conditions under which they were evaluated. Shared standards help us ask consistent questions, but they cannot eliminate every uncertainty or settle every disagreement about acceptable risk.

The deck uses *Terminator* and *The Matrix* to make the control question memorable. The decision we need to make today is more immediate: **does this evidence justify this permission, for these people?**

If the task changes, the system changes, or the evidence no longer supports the claim, “we approved it last year” is not a sufficient answer.

## Explore the presentation

<iframe src="{{ '/presentations/ucl-ai-trust/slides.html?preview=1#15' | relative_url }}" title="UCL seminar slides: Who Decides When AI Is Trustworthy?" loading="lazy" allow="fullscreen" allowfullscreen style="width:100%;aspect-ratio:16/9;border:1px solid #777;border-radius:8px;"></iframe>

[Open the full deck]({{ '/presentations/ucl-ai-trust/slides.html' | relative_url }}) or [read the speaking notes]({{ '/presentations/ucl-ai-trust/notes.html' | relative_url }}). The embedded view supports the arrow keys after you click it; the full deck gives more room to read.

For presenting, keep the audience slides and linked notes on separate, extended displays. **V** opens presenter mode; **N** displays notes on the audience screen. Phone notes can be browsed independently; they do not automatically synchronise with a laptop. The notes are public companion material, not a private account area.
