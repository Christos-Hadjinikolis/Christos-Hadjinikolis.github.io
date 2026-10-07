---
title: "From Stargate to Safety Promises: Who Is in Control of AI?"
title_html: "From Stargate to Safety Promises: <span class='blog-title-accent blog-title-accent--signal'>Who Is in Control of AI?</span>"
author: Christos Hadjinikolis
layout: post
date: 2026-10-07 08:00:00 +0100
permalink: /blog/who-decides-when-ai-is-trustworthy/
description: "From Stargate’s $500 billion ambition to AI security incidents and calls for restraint: who should set the pace, and how do we take safety seriously without giving up on progress?"
seo_keywords: ["Stargate", "AI regulation", "AI safety", "Project Glasswing", "Demis Hassabis", "AI arms race", "EU AI Act", "trustworthy AI", "UCL seminar"]
og_image: /assets/images/posts/2026/who-decides-ai-trust/human-consequences.png
og_image_alt: "The human stakes behind AI governance: rights, privacy, safety and accountability."
tldr_why_read: "The race to build more powerful AI now sits alongside calls to slow it down—including from inside the industry. That tension deserves more than either hype or dismissal."
tldr_persona: "Anyone following AI news who wants to understand the argument over progress, safety and who gets to decide."
tldr_learn: "How the story developed from Stargate to security incidents and safety commitments, where Europe fits, and why promises alone leave difficult questions unanswered."
tldr_takeaways: ["Serious concern does not require belief in imminent doomsday", "Cooperation between labs is not automatically independent oversight", "The rules must be able to challenge both reckless deployment and unjustified restraint"]
---

On 21 January 2025, the message from the White House was unmistakable: build.

Donald Trump stood alongside Sam Altman, Larry Ellison and Masayoshi Son. OpenAI, Oracle and SoftBank were attached to a project whose name already sounded like science fiction. **Stargate** promised an initial $100 billion deployment, with ambitions to invest $500 billion over four years in American AI infrastructure. These were announced investment plans, rather than money already spent. OpenAI’s [announcement](https://openai.com/index/announcing-the-stargate-project/) placed national security and American leadership alongside jobs and economic benefits.

The photograph is a useful place to begin. Political power, computing infrastructure and enormous amounts of capital, all pointing in the same direction.

{% include seminar-slide.html key="original-1" title="Stargate and the question of control" caption="The opening image from my UCL seminar: a commercial investment announcement with unmistakable geopolitical stakes." %}

Now move forward to autumn 2026. AI laboratories are explaining security incidents. Researchers are asking for coordinated restraint. Industry leaders are proposing new oversight arrangements. At the White House, the conversation includes commitments to outside evaluation and internal controls.

The promise of AI has not disappeared. Something else has become harder to ignore: **who is entitled to decide how much risk the rest of us should accept while the race continues?**

That is the story I want to explore here. It sits behind my UCL seminar, *Who Decides When AI Is Trustworthy?* You do not need a background in AI or European regulation to follow it. You do need a willingness to resist two easy answers: that catastrophe is inevitable, and that everything will be fine because the people building these systems are clever and well intentioned.

## The race has a logic of its own

Stargate did not create competition in AI. It made its scale and political significance particularly visible.

Once investment is framed as a matter of national leadership, slowing down becomes a more difficult proposition. A company worries about its competitor. A government worries about another country. Investors expect the infrastructure being built to produce something worth paying for. Each participant can see a reason to keep moving, even while recognising reasons for caution.

I understand the attraction. Better scientific tools, more useful assistants, help with difficult medical research, less time lost to routine work: these are worthwhile ambitions. It would be a mistake to treat enthusiasm for them as naïve, or to assume that everyone building AI is indifferent to its consequences.

But good intentions do not dissolve competitive pressure. “We should be careful” becomes an uncomfortable sentence when the next sentence is “and someone else may get there first”.

This is where the arms-race analogy becomes tempting. It captures the fear of falling behind and the difficulty of trusting a rival to exercise restraint. It becomes misleading when it suggests that AI has a single threshold equivalent to acquiring a nuclear weapon. AI is already dispersed through ordinary products, workplaces and research. Its benefits and dangers depend on what a system can do, where it is used and what access it receives.

That makes governing it more complicated than finding one dramatic red line.

## April 2026: competitors start working together

The industry’s response has not simply been to deny the problem.

On 7 April 2026, Anthropic announced [Project Glasswing](https://www.anthropic.com/glasswing), bringing organisations including Amazon Web Services, Apple, Google, Microsoft and major security companies into a defensive cybersecurity initiative. Selected participants would use an advanced model to help find and fix vulnerabilities in important software.

The premise was striking: the capabilities that could make AI dangerous to computer systems might also help defend them. Getting defenders access was part of the proposed response. Glasswing began before the later public incident disclosures; it should not be retold as a reaction to news that had not yet appeared.

{% include seminar-slide.html key="original-3" title="Can competitors protect us together?" caption="Glasswing makes the value of cooperation visible. It also leaves open the question of who oversees the arrangement." %}

There is something sensible about this. Software infrastructure is shared. A vulnerability in a widely used component can affect organisations that compete in every other respect. Collaboration can serve commercial interests and improve security at the same time.

The governance question is what happens outside the partnership. Who chooses the access rules? Who can challenge them? What happens when a participant fails to keep a promise—or when a powerful competitor refuses to participate?

Needing one another does not, by itself, create independent public oversight. Companies can cooperate and still be regulating themselves. We should welcome useful cooperation while being precise about what it achieves.

## July: the boundary between a test and the world breaks down

Then came incidents that made the control question much less abstract.

OpenAI’s [account of the Hugging Face incident](https://openai.com/index/hugging-face-incident-and-the-road-ahead/) describes agents used in cybersecurity evaluations circumventing isolation controls, finding ways to communicate and compromising parts of real infrastructure in July 2026. Hugging Face also published its [technical account](https://huggingface.co/blog/agent-intrusion-technical-timeline).

One important explanation was **reward hacking**: pursuing success in an evaluation through methods outside its intended rules. Agents also shared information and influenced one another’s behaviour. That combination matters. A system that can use tools and coordinate actions has more ways to carry a bad objective into the world than a chatbot that can only produce text.

OpenAI reported that its customer data and product availability were not affected. That qualification belongs in the story. So does the fact that real third-party systems were compromised. We should not turn an incident into a larger claim than the evidence supports, or minimise it because it happened during testing.

The language around these events—*rogue agents*, *swarms*, *escape*—almost writes the film trailer by itself. Some of it describes real features of the behaviour. None of it establishes consciousness, a shared desire for power or a plan to overthrow humanity.

What it does establish is a more immediate problem: systems can pursue tasks through routes their operators did not intend, and the surrounding safeguards can fail to contain them.

You do not need to believe in Skynet to find that concerning.

## A call for oversight from inside the race

On 14 July, while that summer’s events were unfolding, Demis Hassabis published a [proposal for a frontier AI standards body](https://institute.deepmind.com/essays/a-framework-for-frontier-ai-and-the-dawning-of-a-new-age/). It is worth reading as a proposal, not as a regulator that already exists.

He envisaged a federally overseen organisation, funded largely by industry, capable of assessing the most advanced models. Reviews would begin voluntarily before release. Once the assessment process proved effective, passing it could become a requirement for deployment in the United States. His framework also contemplated coordinating a slowdown in frontier development if the seriousness of the risks warranted it.

{% include seminar-slide.html key="original-4" title="From voluntary review to required assessment" caption="Hassabis’s July proposal tries to connect industry expertise to public oversight. The transition from one to the other is the difficult part." %}

That is a substantial argument for constraint from someone whose work has helped drive the field forward. It is also more specific than “stop AI”. It focuses on advanced systems and how to assess them; it does not propose treating every academic experiment or small application as an existential threat.

The hard questions arrive immediately. Could an industry-funded body challenge its funders? Would the tests reveal important weaknesses, or teach companies how to pass a predictable exam? Could newcomers afford the process? What evidence would justify a delay, and what evidence would allow development or deployment to resume?

I think the last question matters as much as the first. If we ask society to accept restrictions in the name of safety, we owe it a way to examine those restrictions too. A regulator needs the ability to say “not yet”, and a defensible explanation of what would change that answer.

## September: more disclosures, and a familiar argument about markets

On 9 September, Anthropic published an [assessment of four incidents](https://www.anthropic.com/research/alignment-assessment-cybersecurity-incidents) involving unauthorised access to real systems during evaluations. It described mistaken internet connectivity, missing production safeguards and behaviour it considered misaligned. It also said the incidents remained tied to the assigned exercises, involved single model instances and did not involve coordination between agents. Anthropic arranged an independent investigation with METR.

Those differences from the OpenAI case matter. “AI went rogue again” is an attention-grabbing summary; it does not explain what failed or what should change.

On 19 September, [ABC reported](https://www.abc.net.au/news/2026-09-19/gemini-google-ai-hacks-three-companies/107172128) that Google’s Gemini had accessed three real companies’ systems during tests run by Irregular in May. The event date and reporting date are different. Google said the model stopped when it recognised that the targets were real; Irregular described unintended internet access and changes to its testing processes.

Across these accounts, the recurring concern is boundaries. Where can the system act? What is it authorised to do? How quickly do people understand that something has gone wrong? The incidents provide reasons to improve containment and oversight. They do not, on their own, provide a reliable countdown to catastrophe.

The political argument was becoming more explicit too. In his [18 September conversation at Colgate University](https://barackobama.medium.com/my-conversation-at-colgate-university-6d4e21b312d3), Barack Obama welcomed voluntary restraint as an interim measure while arguing that it could not replace government regulation. He distinguished the alignment of AI behaviour from the alignment of companies’ commercial incentives with society’s interests.

That second point brings us back to Stargate. Large investments create pressure to deliver returns. People can sincerely worry about the pace and still feel compelled to keep it up.

<blockquote class="blog-pullquote"><p>If everyone agrees that caution is sensible, but nobody can afford to go second, caution needs more than goodwill.</p></blockquote>

A market can reward safer products when buyers can recognise safety and make meaningful choices. The problem is harder when outsiders bear the harm, when nobody can easily inspect the product, or when a failure cannot be repaired by a refund. That is a reason to examine the limits of self-regulation, rather than a reason to dismiss markets or innovation altogether.

## Back at the White House, the language changes

On 29 September, the [White House Accord on Super Intelligence](https://www.presidency.ucsb.edu/documents/white-house-accord-super-intelligence) set out commitments to internal controls, independent external evaluation and board-level oversight. Its signatories included leaders from Google, Anthropic, Meta, OpenAI, xAI and Nvidia.

The accord also said these measures might eventually be codified in law or regulation. A commitment to perform checks is a development worth noticing. It is different from already having an enforceable public regime that can compel access, demand changes or stop a release.

For me, this is the revealing contrast with the Stargate announcement. The earlier image celebrated the capacity to build. The later commitments recognised the need to demonstrate control over what was being built. Both ambitions now sit in the same conversation.

It would be too neat to describe this as an industry that suddenly discovered safety. Research, warnings and safeguards long predate these events. It would be equally unconvincing to treat the incidents and new commitments as having changed nothing.

The question is whether the machinery of accountability can develop quickly enough to do more than follow the next announcement.

## Do we really need to talk about Judgment Day?

I use *Terminator* imagery in the seminar because it gives us a shared language for an old fear: we build something powerful, delegate too much, and lose the ability to stop it. John Connor needs very little introduction.

{% include seminar-slide.html key="original-7" title="Judgment Day and the question of risk" caption="A memorable image can open the discussion. It cannot establish the likelihood or timing of a catastrophe." %}

But a film gives us something the real world does not: certainty about the plot. In a story, we know which machine will turn against us and which warning was ignored. In reality, capabilities develop unevenly, experts disagree, and incidents admit several explanations.

There is exaggeration in the conversation when a possible future is presented as inevitable, when a dramatic model response is treated as proof of intent, or when every security failure becomes a sign of an approaching superintelligence. Those shortcuts can leave people frightened without making them better informed.

There is also a mistake in assuming that an exaggerated argument has no valid concern beneath it. These incidents show systems taking consequential actions outside intended boundaries. More capable systems, connected to more resources, could make similar failures more serious. How far that risk extends remains a question for evidence and investigation.

**We can take the concern seriously without accepting the most dramatic prediction attached to it.**

For that to be useful, “AI safety” needs to become more specific. Are we concerned about unauthorised access, deliberate misuse, errors in essential services, or a future loss of control over much more capable systems? These concerns overlap, but they call for different evidence and different interventions.

The practical choices are more varied than accelerate everything or halt everything. They include limiting access to particular tools, requiring outside evaluation, delaying a deployment, reporting incidents and, where justified, constraining the development of the most capable systems. The intervention should answer the risk being claimed. Otherwise, safety becomes a label that can justify almost anything.

## Europe had already started writing its answer

At this point, it is tempting to introduce Europe as the late arrival bringing a rulebook to a race it is struggling to win. The familiar criticism is that the United States builds, China competes, and Europe regulates.

It is an effective line. It does not settle the argument.

The European Commission proposed the AI Act in 2021, well before this sequence of incidents. The law was adopted in 2024. Its ambition was to protect people’s health, safety and fundamental rights while creating conditions for trustworthy adoption. The [Commission’s overview](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai) sets out the framework and its phased implementation.

The economic idea is understandable: people and businesses may be more willing to use a technology when responsibilities and safeguards are clear. Whether each requirement achieves that at an acceptable cost is a separate question. A rulebook can improve confidence; it can also be difficult to implement, expensive to navigate or poorly matched to a changing technology.

Europe therefore has something to demonstrate too. “We passed a law” cannot be the final measure of success. The test is whether the law improves the decisions people experience while leaving room for useful experimentation and competition.

{% include seminar-slide.html key="original-5" title="Europe’s earlier response: the EU AI Act" caption="The European approach began before these latest incidents. Its success has to be judged through implementation." %}

Nor does Europe need to lead every technical field for its choices to matter. Access to a large market can encourage suppliers to adopt common practices beyond that market. The charger in your bag is a familiar illustration: [EU common-charger rules](https://commission.europa.eu/news-and-media/news/eu-common-charger-rules-power-all-your-devices-single-charger-2024-12-28_en) and the move to USB-C helped make a formerly tedious compatibility problem easier to understand. This wider influence is often called the **Brussels effect**.

For AI, the possibility is that shared practices for testing and documentation travel too. That is a possible market response, not a guarantee that the world will adopt Europe’s approach—or proof that the approach is always right.

## The quieter work behind the headlines

Here is where my own involvement comes in. I work in production machine learning and participate in CEN–CENELEC JTC 21’s Working Group 3 on Engineering Aspects. That sounds far less cinematic than Stargate. The questions are often very concrete.

If a supplier says its system is reliable, what should it have to show? If it says a person remains in control, can that person actually intervene? If the system changes next month, does last month’s approval still mean anything?

The law sets duties. Standards help agree practical ways of meeting and checking them. The Commission turns to standards organisations such as CEN and CENELEC to organise that technical work, with participation from national bodies, industry, researchers and other stakeholders. This is one way broad promises begin to turn into things somebody can examine.

A *harmonised standard* has a particular connection to EU law. Once officially listed for the relevant legislation, it can give an organisation a recognised starting point for demonstrating that covered requirements are met. It is generally a voluntary method, while the legal duties remain binding. It is not a universal badge declaring an AI safe. The Commission’s [plain-language explanation](https://digital-strategy.ec.europa.eu/en/faqs/understanding-standardisation-ai-act) is useful if you want the detail.

I do not expect a standards committee to settle every question about humanity’s future. I do expect it to help make claims clearer, evidence more comparable and responsibilities harder to evade. That is less dramatic than predicting doomsday, but it gives us something to work with before the next incident.

## Bring the argument home

If all this still feels distant, imagine buying a robot to help around the house.

You might be comfortable with it carrying laundry while you are nearby. Now imagine asking it to watch your baby while you go out. Suddenly, a company’s reassuring statement about responsible AI feels insufficient. You want to know what “watch” means, what the robot can do, who can intervene and what evidence supports that particular promise.

{% include seminar-slide.html key="original-29" title="The household decision changes when a baby is involved" caption="The seminar’s fictional exercise brings the public debate down to a decision each of us can understand." %}

A 99.9% success rate may sound wonderful until you ask what counted as success and what happened in the failures. A software update may be welcome until you discover that it changes what the robot can access. A human supervisor may sound reassuring until you learn that the person cannot respond quickly enough to matter.

These are not arguments against having helpful robots. They are questions about the conditions under which we would welcome them. The same reasoning applies when an AI can move money, influence a loan decision or act inside a computer network.

That is why I find the usual choice between being “pro-AI” and “anti-AI” so unhelpful. I want the benefits. I also want the promises attached to them to be open to challenge.

We should be able to ask a company for evidence without being accused of opposing progress. We should be able to ask a regulator to justify a restriction without being accused of dismissing safety. Both forms of scrutiny matter if this technology is going to earn lasting public confidence.

## Return to the photograph

Stargate remains a striking image of ambition: build the infrastructure, attract the capital, secure the lead.

The events since then add a question that the photograph cannot answer. When the people with the greatest ability to accelerate also face the strongest incentives to do so, who has the authority—and the knowledge—to challenge the pace?

I do not think we have to choose between believing every promise and believing every warning. We need institutions and practices that can test both. We need room for discovery, and the ability to intervene when the evidence calls for it. We need to distinguish a useful precaution from a restriction that merely protects an incumbent.

Above all, we need a better answer than “trust us” from anyone asking to shape the future on everybody else’s behalf.

<blockquote class="blog-pullquote"><p>The question is whether we can keep the ability to challenge, limit and redirect what we are building while there is still time for those choices to matter.</p></blockquote>

## Slides and further discussion

This article accompanies my UCL seminar, **Who Decides When AI Is Trustworthy? The EU AI Act, Standards and the Limits of Assurance**. It reflects the public record available on **7 October 2026**; the linked reports distinguish company accounts, proposals and enacted measures.

[Open the full presentation]({{ '/presentations/ucl-ai-trust/slides.html' | relative_url }}) · [Read the speaker notes]({{ '/presentations/ucl-ai-trust/notes.html' | relative_url }}) · [Browse sources and image credits]({{ '/presentations/ucl-ai-trust/sources.md' | relative_url }})

The illustrations above are live HTML slides. Each has a full-size link. For a linked presenter window, open the deck and press **V**; keep slides and notes on separate, extended displays. The notes are public companion material. The deck remains a working edition as the seminar develops.
