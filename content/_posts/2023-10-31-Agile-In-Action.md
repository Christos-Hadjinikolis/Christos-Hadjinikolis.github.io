---
title: "Agile In Action: Bridging Data Science and Engineering"
title_html: "<span class='blog-title-accent blog-title-accent--agile'>Agile</span> In Action: Bridging Data Science and Engineering"
author: Christos Hadjinikolis
layout: post
og_image: assets/images/posts/2023/agile-in-action/2023-10-31-Turner.png
description: "What Agile looked like to me in 2023 at Vortexa: helping data scientists and engineers learn together, communicate clearly, and ship ML systems that can survive production."
seo_keywords: ["agile machine learning", "data science and engineering", "ML teams", "productionizing models", "experimentation", "Vortexa"]
tldr_why_read: "Read this if your <span class=\"blog-highlight blog-highlight--ml\">ML</span> work keeps getting stuck between promising notebooks and production systems that nobody fully owns."
tldr_persona: "Especially useful for data scientists, software engineers, and <span class=\"blog-highlight blog-highlight--ml\">ML</span> leads trying to make cross-functional teams work without hiding behind process."
tldr_learn: "Why <span class=\"blog-highlight blog-highlight--agile\">Agile</span> mattered to me less as ritual and more as a way to synchronise experimentation, communication, and engineering discipline."
tldr_takeaways: ["<span class=\"blog-highlight blog-highlight--agile\">Agile</span> is useful when it makes experiments explicit", "The real gap sits between a notebook and a production system", "Communication is part of the system, not an afterthought"]
---

<div class="image center">
  <img src="{{ 'assets/images/posts/2023/agile-in-action/2023-10-31-Turner.png' | relative_url }}" alt="Joseph Mallord William Turner | Dutch Boats in a Gale ('The Bridgewater Sea Piece') | National Gallery, London" />
  <p class="image-credit">Picture taken from <a href="https://www.nationalgallery.org.uk/paintings/joseph-mallord-william-turner-dutch-boats-in-a-gale-the-bridgewater-sea-piece" target="_blank" rel="noopener noreferrer">National Gallery, London</a></p>
</div>

A few weeks ago, Bill Raymond invited me onto his <a href="https://agileinaction.com/agile-in-action-podcast/2023/10/31/bridging-ai-data-science-and-engineering-a-personal-journey.html" target="_blank" rel="noopener noreferrer">Agile in Action podcast</a> after reading an older post of mine on <a href="{% post_url 2020-08-11-agile-data-science %}">doing data science the Agile way</a>.

I said yes because this topic has followed me through most of my career.

I started as a data scientist. Then I spent years watching perfectly respectable prototypes fail to become products. By the time I reached Vortexa, I was leading a team of data scientists and engineers and living right in the middle of the tension I had been talking about for years.

That is the version of <span class="blog-highlight blog-highlight--agile">Agile</span> I wanted to discuss in the episode. Not the clean whiteboard version. The one that appears when a model has to leave a <span class="blog-highlight blog-highlight--python">Python</span> notebook, survive production, and still make sense to the people who have to operate it.

> The real gap in <span class="blog-highlight blog-highlight--ml">ML</span> teams is rarely enthusiasm. It is the distance between a model that works once and a system that can be trusted repeatedly.

## Why This Topic Stayed With Me

Part of the reason this topic matters so much to me is that I learned it the frustrating way.

At Data Reply, I worked on one prototype after another. We would explore a problem, build something promising, show strong results, and then hit the same wall: the client liked the idea, but the system never really made it into production. Sometimes the missing piece was infrastructure. Sometimes it was culture. Sometimes it was simply that nobody owned the hard part after the demo.

That started to change for me at UBS.

For the first time, I heard the sentence I had wanted to hear for years: *"Great. Now how do we put this into production?"*

I was paired with an experienced engineer, and that changed the direction of my career. I stopped seeing engineering as the final packaging step after the interesting work was done. I started seeing it as part of the thinking itself.

That shift is still with me today.

## The Real Gap Between Data Science And Engineering

When people talk about cross-functional <span class="blog-highlight blog-highlight--ml">ML</span> teams, they often make the collaboration sound natural. In practice, it is not.

Data scientists are usually optimising for learning:

- trying ideas quickly
- testing hypotheses
- moving fast through a messy search space

Engineers are usually optimising for control:

- reproducibility
- determinism
- maintainability
- safe change over time

Both instincts are valid.

The problem is that they are protecting the system from different failure modes.

> The issue is not that data scientists are messy and engineers are rigid. The issue is that both are right about different kinds of breakage.

Take a simple pricing model. A data scientist can build a strong prototype in a notebook, engineer the features, train the model, and prove the concept. But once that model becomes part of a product, somebody has to make sure the production path transforms the raw input in exactly the same way. If the training pipeline and the prediction pipeline drift apart, the system lies even when the model itself is good.

That is why the gap matters so much.

It is not about user interfaces or wrapping code nicely. It is about making sure the system that predicts tomorrow behaves like the system that was validated yesterday.

## What <span class="blog-highlight blog-highlight--agile">Agile</span> Actually Helped With

When I say <span class="blog-highlight blog-highlight--agile">Agile</span> helped here, I do not mean that Scrum ceremonies somehow solved the problem.

What helped was having a way to make uncertainty legible.

For me, that meant three things.

### 1. Making experiments explicit

In <span class="blog-highlight blog-highlight--ml">ML</span> work, *"we are exploring"* is too vague.

An experiment becomes useful when the team can answer:

- what assumption are we testing?
- what would count as useful evidence?
- what result would tell us to stop?

That sounds simple, but it changes the conversation completely. It stops research from turning into open-ended wandering and gives product and engineering a clearer way to understand what the team is actually learning.

### 2. Creating shared visibility

At Vortexa, one of the most useful habits we built was a regular data science catch-up where engineers and data scientists could present what they were doing, why they were doing it, and where the risks were.

This was not code review. It was not a status ritual either.

It was a way to keep everyone on the same mental map.

That mattered because a lot of problems in <span class="blog-highlight blog-highlight--ml">ML</span> systems do not come from one catastrophic mistake. They come from small drifts in understanding. A feature is computed one way in training, another way in production. An assumption about data quality goes unchallenged. A result sounds promising, but nobody else can reproduce it.

Communication is not a soft add-on here.

It is part of the control surface of the system.

### 3. Putting discipline around handoffs

The teams I trust most are not the ones with the nicest process diagrams. They are the ones that make handoffs visible and expensive enough that people try to remove them.

If the data scientist can disappear after training a model and the engineer is left to guess the rest, the system will eventually reflect that fracture.

If the engineer is never exposed to how experimental the work really is, they will overestimate how stable the solution already is.

<span class="blog-highlight blog-highlight--agile">Agile</span> helped when it forced us to confront those boundaries earlier.

## What <span class="blog-highlight blog-highlight--ml">ML</span> Teams Still Underestimate

One of the themes that came up in the podcast is that many teams still underestimate how much work starts after the model looks good.

You do not just need versioned code. You need versioned data and a credible way to tie the two together.

You do not just need a model in production. You need monitoring, drift detection, and a practical way to replace the model without breaking the product.

You do not just need experimentation. You need a path from experimentation to something deterministic enough to support.

This is why I often say that notebooks are wonderful research tools and terrible places to leave an idea if you want a system around it to survive.

## The Lesson I Was Trying To Communicate

When Bill asked what <span class="blog-highlight blog-highlight--agile">Agile</span> meant to me in this context, the answer I wanted to give was not especially fashionable.

It was this:

> In <span class="blog-highlight blog-highlight--ml">ML</span>, Agile is useful when it helps the team learn quickly without losing control of the system.

That is really the heart of it.

Not velocity in the abstract.

Not ceremony for its own sake.

Not pretending that uncertainty can be planned away.

Just a disciplined way to:

- test assumptions early
- expose the right risks
- keep engineers and data scientists in sync
- and make sure the thing you learned can actually survive contact with production

That was my view then, and I still think it was the right thing to say.

## The Podcast

If you prefer the conversation version, the episode is below.

<iframe width="560" height="315" src="https://www.youtube.com/embed/LdDasrMOJLs?si=dk-YcjCqW6YpBPWZ" title="Agile in Action podcast episode" frameborder="0" loading="lazy" referrerpolicy="strict-origin-when-cross-origin" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
