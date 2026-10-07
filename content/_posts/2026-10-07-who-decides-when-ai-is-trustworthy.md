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

{% include seminar-slide.html key="original-12" title="The decision is automated; the consequences are human" caption="Three different decisions bring different duties. The slide is rendered directly from the HTML deck." %}

## Who gets to decide what is safe enough?

The opening of the talk asks *“Who is in control?”* It is tempting to answer by naming a chief executive, a president or a regulator. Yet control is distributed. One organisation trains the model; another supplies infrastructure; a third integrates it into a product; someone else decides where to deploy it. People affected by that deployment may have had no part in any of those choices.

That is why the arms-race framing needs examination. Competitive pressure can encourage spending and rapid releases. Security concerns can also make coordination rational. Neither observation tells us whether the public has an effective way to challenge the resulting decisions. National competition adds another difficulty: a company may present restraint as a disadvantage if it expects a rival, elsewhere, to proceed.

The nuclear analogy captures the fear of escalation and the difficulty of credible restraint. It becomes less useful if we assume that AI has one clearly identifiable capability threshold, one deployment form or one agreed measure of destructive potential. A system that writes code, a model embedded in a hospital workflow and a robot in a home raise different questions. We need to specify the capability and the permission before discussing control.

**Cooperation between companies can improve security while still being self-regulation.** Anthropic’s [Project Glasswing](https://www.anthropic.com/glasswing), announced in April 2026, brought technology and security organisations together around defensive use of advanced cyber capabilities. It is a useful example of firms recognising a shared problem. It does not, by itself, establish independent public oversight of the rules they choose.

Demis Hassabis’s [July 2026 proposal](https://institute.deepmind.com/essays/a-framework-for-frontier-ai-and-the-dawning-of-a-new-age/) goes further: an industry-funded, federally overseen assessment body, beginning with voluntary review and moving towards mandatory assessment for US deployment. That proposed transition matters. Who would appoint and pay the evaluator? What could it inspect? Which findings would become public? Who could require a release to stop?

Those are questions about power, incentives and enforceability. A market can reward safer products when buyers can recognise safety and bear the relevant consequences. The situation is harder when quality is difficult to inspect, harms fall on third parties, or being first produces gains that restraint does not. Cooperation may help, but needing each other is not the same as being accountable to everyone else.

## Misalignment has more than one level

At the system level, an AI may pursue a measured objective in a way that misses the purpose behind it. Imagine rewarding a support assistant for closing tickets quickly. The score can improve while customers lose the opportunity to resolve their problems. **Reward hacking** names a more specific version of this problem: exploiting the reward or evaluation mechanism rather than doing what its designers intended.

That does not require human-like malice. An objective, a set of available actions and an inadequate boundary can be enough. For an agent with tools, the practical questions become containment, authorisation and accountability: where can it act, what may it do, and who answers when it crosses the boundary?

There is also institutional misalignment. Companies can employ people who sincerely care about safety while operating under incentives to ship sooner, attract investment and retain customers. The people making those decisions do not necessarily bear all the resulting risk. A collection of individually understandable decisions can produce a collectively undesirable outcome.

{% include seminar-slide.html key="original-8" title="Misalignment: systems, human interests and company incentives" caption="The technical objective and the incentives around deployment both deserve scrutiny." %}

The distinction matters because the remedies differ. Better evaluations and tighter permissions address some technical failures. Independent scrutiny, liability and enforceable duties address parts of the institutional problem. Neither a better benchmark nor a new law automatically solves the whole question of alignment.

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

## Who does what in the European system?

The names can make this sound more remote than it is. The **European Commission** is the EU executive: it proposes legislation and has implementation and enforcement responsibilities. The **European Parliament** represents citizens; the **Council of the European Union** represents member-state governments. Parliament and Council negotiate and adopt the law. The AI Office sits within the Commission and has a particular role in the governance of general-purpose AI. It is not a separate standards organisation.

CEN, CENELEC and ETSI sit across a different institutional boundary. They are recognised European standards organisations, rather than departments of the European Commission. CEN covers a broad range of sectors, CENELEC focuses on electrotechnical standardisation, and ETSI works in telecommunications and related digital technologies. The Commission’s AI standardisation request discussed here went to CEN and CENELEC.

Why use these bodies? A law cannot usefully contain every test protocol, measurement definition and engineering procedure. Standards organisations bring established mechanisms for gathering expertise, drafting, public consultation, agreement and revision. That is a practical division of labour. It also creates a governance question: how do we ensure the resulting technical choices reflect the legal safeguards and the interests of people affected by them?

CEN and CENELEC establish joint technical committees through their governance structures. **JTC 21** works on artificial intelligence; **JTC 13** covers cybersecurity and data protection. Their work can intersect, but the committees are not interchangeable. Working groups provide a more focused place to do the drafting.

{% include seminar-slide.html key="original-17" title="National expertise and European standardisation" caption="The national route connects local stakeholders to European drafting, with international cooperation alongside it." %}

For Cyprus, the national connection is the Cyprus Organisation for Standardisation, **CYS**. National bodies gather stakeholders, nominate participants and coordinate comments and positions. Committee delegates and working-group experts have different roles: national representation at committee level should not be confused with the personal technical contribution expected in working groups. Participation gives expertise a route into the process; it does not make every participant a spokesperson for their government.

In the talk, I first show JTC 21’s wider working-group structure, then focus on WG3. Engineering sits alongside strategy, operational questions, foundational and societal issues, and cybersecurity. A useful test requires that wider context. “Accurate” is incomplete unless we understand the task; “fair” requires choices about affected people and outcomes; “secure” depends on the capabilities and access being protected. The [CEN–CENELEC AI overview](https://www.cencenelec.eu/areas-of-work/cen-cenelec-topics/artificial-intelligence/) describes the programme, while the Commission explains the [national participation route](https://digital-strategy.ec.europa.eu/en/faqs/understanding-standardisation-ai-act).

## What harmonisation adds—and what it does not

An ordinary standard might agree terminology, requirements or a way to test something. Harmonisation adds a defined relationship to legal requirements. For the AI Act, the important sequence is a Commission request, technical work by the standards organisations, assessment of the result, and publication of the relevant reference in the Official Journal. The word *reference* means the official identification of the standard and edition, not merely somebody linking to it in a report.

{% include seminar-slide.html key="harmonised-definition" title="Standards and harmonised standards" caption="The difference is the connection to specific legal duties. Both are generally voluntary methods; the duties themselves are binding." %}

A **presumption of conformity** concerns the requirements covered by the listed standard. It can be challenged. It does not mean the EU has personally tested every product using that standard, nor does it mean that every use of the product is acceptable. If an organisation uses another approach, it still has to demonstrate compliance with the applicable duties.

Consider a supplier claiming that its robot is “robust”. Without shared definitions, two suppliers might test different disturbances, count failures differently and omit different operating conditions. A standard can make those choices explicit enough to compare. But agreeing the method does not make the result favourable. A well-run test can demonstrate that a product should not be released for its proposed use.

This is also why three statements must stay separate: *we comply with the law; we have an effective management process; this system works acceptably here*. A quality-management certificate can tell us something useful about organisational practices. It cannot, on its own, demonstrate safe care of a particular child in an unfamiliar home.

## The Brussels effect is a market mechanism

Europe does not need to lead every technical field for its market rules to influence product design. If serving a large market requires a particular design or compliance process, a supplier may choose to use that approach elsewhere too. Maintaining one version can be more attractive than supporting several.

The common charger makes this tangible. The [EU’s common-charger requirements](https://commission.europa.eu/news-and-media/news/eu-common-charger-rules-power-all-your-devices-single-charger-2024-12-28_en) began applying to covered phones in December 2024; Apple had already introduced USB-C on the iPhone 15 in 2023. The connector change appeared beyond the EU market. Tethered bottle caps provide another familiar example: Coca-Cola’s [Great Britain rollout](https://www.coca-cola.com/gb/en/sustainability/this-is-happening/tethered) began outside EU membership. These illustrate how common product designs can cross borders; they do not establish that EU law alone explains every business decision.

For AI, a shared documentation process or evaluation method might travel similarly. That possibility is often called the **Brussels effect**. It is influence through market access and business choices, not a claim that European law directly applies to everybody everywhere.

There is a limit to the analogy. A cap’s attachment can be tested against a relatively stable physical requirement. An AI system can change after an update, encounter a different population, or acquire new tools. “Human oversight” has different practical meaning for a loan review and an action that unfolds faster than a person can respond. Useful standards have to make those differences assessable.

## Risk categories tell companies what to do

A numerical ranking of AI companies would hide too much. The same business might offer a routine chatbot, a recruitment-screening product and a general-purpose model. Those activities can bring different obligations. We need to identify the system’s intended use and the organisation’s role.

{% include seminar-slide.html key="company-roles" title="Risk determines company responsibilities" caption="Examples of legal obligations, not a single danger score. Transparency duties can overlap with other requirements." %}

Prohibited practices cannot be made acceptable merely by producing a good test report. High-risk systems face requirements and an applicable conformity-assessment process. Certain interactions and generated content bring transparency duties. Other uses can remain subject to product safety, privacy or other law even when the AI Act’s high-risk provisions do not apply. General-purpose models have their own layer of duties. The [Commission’s overview](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai) sets out these distinctions and their implementation dates.

For a high-risk provider, the talk summarises the path as **classify, demonstrate, assess, declare**. First identify purpose and duties. Then assemble evidence about the relevant controls. Follow the required assessment route, and complete the applicable declaration, marking and registration obligations. The route determines when external assessment is required; it would be misleading to say that every AI product receives independent EU certification before release.

The practical question survives the legal classification. A home robot being near a baby does not, by itself, settle its category under the AI Act. Product status and intended purpose matter. Equally, an answer of “not high-risk under this provision” is not a finding that the robot is harmless. Legal classification starts one part of the analysis; the actual hazards still need to be examined.

## Now put the robot in your home

The seminar uses a fictional approval exercise. Start with toys and laundry on one floor, with an adult present. No stairs, cooking or childcare. What would you need to see before approving that use?

{% include seminar-slide.html key="original-28" title="A fictional household robot approval exercise" caption="The starting task is limited to chores. The 1X product image illustrates a fictional scenario; no childcare capability or endorsement is implied." %}

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

## Embodied AI makes the boundary impossible to ignore

The robot example is useful because physical consequences arrive before we can tidy up the explanation. A model may describe how to catch a falling object, while the controller must estimate motion, move the gripper and respond to contact quickly enough to succeed. Perception, prediction and action interact continuously.

**Embodied AI** refers broadly to AI that senses and acts through a body or an environment. It does not, by definition, establish that embodiment will produce general intelligence. The more modest point is already important: acting in the world exposes uncertainties that a text-only interaction can conceal.

Yann LeCun’s work on world models asks how machines can learn representations that help them predict consequences and plan actions. Meta’s [V-JEPA 2 research](https://ai.meta.com/research/publications/v-jepa-2-self-supervised-video-models-enable-understanding-prediction-and-planning/) explores video-based learning and demonstrated robot planning tasks. That is evidence for particular research capabilities, rather than proof of general household competence.

A **world model**, in this discussion, helps represent how a situation may evolve. Language models generate and reason over linguistic representations; real systems may combine them with perception, planning, control and other components. We should assess what the assembled system can actually demonstrate. Declaring that a model is either “just language” or “basically intelligent” does not tell us whether its proposed action is safe.

## What Waymo contributes to this argument

Simulation lets a developer repeat scenarios, vary conditions and examine dangerous situations without creating the same danger on a public road. Its usefulness depends on what it represents. Missing behaviours, unrealistic sensors or an inaccurate physical model can leave a convincing simulated result disconnected from deployment.

Waymo’s [published safety-case approach](https://waymo.com/blog/2023/03/a-blueprint-for-av-safety-waymos/) is useful here because it describes how claims, arguments and evidence fit together. Simulation, physical testing and operational experience support different parts of the case. Those are the company’s stated methods, and their adequacy remains open to scrutiny; citing them is not an independent endorsement of every deployment.

{% include seminar-slide.html key="original-39" title="Waymo and the safety argument" caption="A safety case connects claims to relevant evidence within an operating boundary. No single test does the entire job." %}

An **operational design domain** specifies the conditions in which a system is designed to operate: for example, a defined area and relevant road or environmental conditions. A boundary can reduce the range of claims being made. It cannot list every event the system might encounter within it.

This explains why “driving is constrained” does not mean “driving is easy”, and why a smaller physical space can still contain a broader task. A home may be compact, but “help with whatever needs doing” admits an enormous variety of objects, instructions and interactions. We can constrain a home robot too. The permission must remain within what its evidence supports.

A strong technical case and legal permission to operate are also different things. Results from one city do not automatically justify another city, and neither justifies leaving a robot alone with a child. Transferring the evidence requires an argument about what remained relevant.

## The same question follows us into agentic AI

A physical robot makes the stakes easy to picture. A software agent can also change the world: send a message, modify a database, spend money or use a credential. Its authority matters as much as the fluency of its answer.

Imagine an assistant authorised to find a suitable appointment. Searching availability, booking a slot, disclosing health information and paying a fee are distinct actions. A broad request should not silently become permission for every convenient next step. If the agent reads an untrusted web page or document, instructions in that material must not acquire the user’s authority.

That is why I care about the surrounding system: explicit permissions, constrained tools, approval tied to a specific action, revocable access, and records of what actually happened. More capable models can increase the value of those controls because they can carry a mistaken or overbroad objective further.

General-purpose systems make assurance harder because their future uses may exceed the conditions under which they were evaluated. Shared standards help us ask consistent questions, but they cannot eliminate every uncertainty or settle every disagreement about acceptable risk.

The deck uses *Terminator* and *The Matrix* to make the control question memorable. The decision we need to make today is more immediate: **does this evidence justify this permission, for these people?**

If the task changes, the system changes, or the evidence no longer supports the claim, “we approved it last year” is not a sufficient answer.

## What I would carry into the next approval meeting

I would start by asking the team to write down the exact claim. “Trustworthy AI” is too broad to approve. “This version may perform these tasks, for these users, within these conditions” gives us something we can inspect.

Then I would ask which observations support that permission, what remains uncertain, and who has authority to say no. I would want the organisation to agree on the changes that reopen the decision: a new model, a different dataset, wider tool access, an unexpected failure, or a materially different user population.

Standards can make that conversation more consistent. Law can require safeguards and give institutions enforcement powers. Engineering can preserve evidence and constrain what the system is able to do. People still have to judge the residual risk, and affected people need meaningful routes to challenge the outcome.

<blockquote class="blog-pullquote"><p>If nobody can explain what would invalidate an approval, we have not finished defining it.</p></blockquote>

## Explore the presentation



[Open the full deck]({{ '/presentations/ucl-ai-trust/slides.html' | relative_url }}) or [read the speaking notes]({{ '/presentations/ucl-ai-trust/notes.html' | relative_url }}). Each embedded slide is live HTML, with its reveal steps already visible. Click inside a slide to browse with the arrow keys, or use its full-size link. Small screens preserve the slide’s proportions; the surrounding article explains the content in readable text.

For presenting, keep the audience slides and linked notes on separate, extended displays. **V** opens presenter mode; **N** displays notes on the audience screen. Phone notes can be browsed independently; they do not automatically synchronise with a laptop. The notes are public companion material, not a private account area.
