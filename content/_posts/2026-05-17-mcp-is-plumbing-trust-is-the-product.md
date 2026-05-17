---
title: "MCP Finally Clicked: It Is Plumbing. Trust Is The Product."
title_html: "<span class='blog-title-accent blog-title-accent--signal'>MCP</span> Finally Clicked: It Is Plumbing. Trust Is The Product."
author: Christos Hadjinikolis
layout: post
date: 2026-05-17
description: "A practical mental model for the Model Context Protocol, why it appeared, and why local AI systems still need their own routing, approval, evidence, and trust boundaries."
seo_keywords: ["Model Context Protocol", "MCP", "AI agents", "tool calling", "MCP server", "MCP Manager", "Docker MCP Toolkit", "local-first AI", "tool safety", "agentic AI"]
nav_tags: ["MCP", "Agents", "Trust"]
og_image: "assets/images/posts/2026/mcp-is-plumbing/ninja avatar-minion-at-a-cluttered-local-AI-workbench.png"
og_image_alt: "Hand-drawn ninja avatar-minion wiring Gmail, Calendar, and Wikipedia into a local AI assistant through labelled MCP cables."
tldr_why_read: "Read this if <span class=\"blog-highlight blog-highlight--agent\">MCP</span> sounds useful but the words around it still feel slightly slippery: server, client, host, manager, tool, function, gateway, catalog."
tldr_persona: "Especially useful for engineers building local or private <span class=\"blog-highlight blog-highlight--agent\">AI</span> assistants who need external tools without turning every integration into a custom connector or a trust problem."
tldr_learn: "Why <span class=\"blog-highlight blog-highlight--agent\">MCP</span> arrived when agents needed real tools, what it standardizes, what it absolutely does not solve, and why serious agents need staged intent narrowing before exact tool calls."
tldr_takeaways: ["MCP is valuable exactly where it is boring: it standardizes connector plumbing", "Available is not the same as routed, and routed is not the same as approved", "The useful architecture separates intent identification, tool exposure, tool execution, and safety/orchestration"]
---
I am joining the <span class="blog-highlight blog-highlight--agent">MCP</span> party a little late.

Not because I ignored it completely, but because the first pass did not feel as obvious to me as the enthusiasm around it suggested. There was a lot of jargon. The setup path had more moving pieces than I wanted. The whole business of piping messages through local processes, gateways, containers, profiles, and JSON schemas felt slightly tedious before it felt useful.

That is usually a sign that I do not understand something existentially yet.

I do not just want to know *what command to run*. I want to understand why the thing had to exist in the first place. What problem was the ecosystem trying to solve? What else was happening around the same time? Which part is genuinely new, and which part is just an old integration problem with a better name?

So this post is mostly written for the version of me that needed the explanation to be digestible.

Hopefully it helps someone else too.

My conclusion after working through it is simple:

<blockquote class="blog-pullquote">
  <p><span class="blog-highlight blog-highlight--agent">MCP</span> is valuable exactly where it is boring.</p>
  <p>It standardizes connector plumbing. It does not absolve the host application from trust, routing, approval, or evidence discipline.</p>
</blockquote>

<figure class="blog-figure blog-figure--wide">
  <img src="{{ 'assets/images/posts/2026/mcp-is-plumbing/ninja avatar-minion-at-a-cluttered-local-AI-workbench.png' | relative_url }}" alt="Hand-drawn ninja avatar-minion wiring Gmail, Calendar, and Wikipedia into a local AI assistant through labelled MCP cables such as STDIO, JSON-RPC, OAuth, Docker profile, and tool schema." loading="lazy" />
  <figcaption class="blog-figure__caption">This was the part I needed to demystify first: the assistant can look calm while the connector plumbing underneath still feels messy.</figcaption>
</figure>

## Why MCP Had To Happen

LLMs started as text systems.

You sent text in. You got text out. That was already useful, but it had an obvious ceiling. A model could explain how to search email, but it could not search your email. It could suggest a calendar event, but it could not inspect your calendar. It could tell you which shell command might help, but it could not safely inspect the repository unless the surrounding application gave it a controlled way to do so.

Then AI applications started adding tools.

The pattern itself was sensible. The model should not directly touch the outside world. It should ask for help, and the host application should mediate the action.

<div class="blog-insight">
  <span class="blog-insight__label">The Tool Loop</span>
  <div class="blog-flow">
    <div class="blog-flow__step">Model sees a gap</div>
    <div class="blog-flow__arrow" aria-hidden="true">&rarr;</div>
    <div class="blog-flow__step">Host validates request</div>
    <div class="blog-flow__arrow" aria-hidden="true">&rarr;</div>
    <div class="blog-flow__step">Host executes action</div>
    <div class="blog-flow__arrow" aria-hidden="true">&rarr;</div>
    <div class="blog-flow__step">Evidence returns</div>
    <div class="blog-flow__arrow" aria-hidden="true">&rarr;</div>
    <div class="blog-flow__step">Model writes answer</div>
  </div>
  <p>The important detail is ownership: the model proposes, but the host validates, executes, records, and shapes the evidence before the final answer is written.</p>
</div>

The problem was not the loop. The problem was **glue code**.

Every serious AI application began needing connectors: Gmail, Slack, GitHub, files, calendars, databases, browsers, search, internal systems. Each connector needed provider-specific setup, credentials, scopes, pagination, rate-limit handling, argument schemas, error normalization, result shaping, and model-facing descriptions.

That **glue code** has an unpleasant habit: it looks small when you write one connector and becomes architectural weight when every host application repeats it differently.

Gmail needs one shape of OAuth, search, labels, snippets, and attachment handling. Slack needs another shape of channels, threads, users, bot permissions, and message posting. GitHub, calendars, browsers, databases, and files all bring their own little integration worlds. Then each AI host still has to translate those worlds into something a model can discover and call.

That is how you end up with a connector zoo, and then with glue code proliferating around the zoo.

The timing matters too. Around the same period, the conversation moved from chatbots toward agents, coding assistants, desktop assistants, local runtimes, and tools that could act on real systems. Models were getting better, but they were still isolated from the places where useful work actually happens. A coding assistant needs the repository. A personal assistant needs calendar and email. A business assistant needs internal documents, tickets, dashboards, and databases.

That world cannot scale on every app hand-rolling every connector and every connector contract.

Anthropic introduced the Model Context Protocol on November 25, 2024 as an open standard for connecting AI assistants to systems where data lives. The official MCP docs use the USB-C analogy: one standard connection shape instead of a different cable for every device. That analogy is imperfect, but useful enough.

The deeper point is this:

<blockquote class="blog-pullquote blog-pullquote--compact">
  <p><span class="blog-highlight blog-highlight--agent">MCP</span> exists because every AI app should not have to reinvent the same connector protocol differently.</p>
</blockquote>

Before <span class="blog-highlight blog-highlight--agent">MCP</span>, connecting an assistant to external systems usually meant each host application had to invent its own integration language. <span class="blog-highlight blog-highlight--agent">MCP</span> gives those integrations a common shape, so the glue code can move behind a more standard boundary instead of leaking into every product in a slightly different form.

## The Simplest Mental Model

Here is the version that finally made it click for me.

An <span class="blog-highlight blog-highlight--agent">MCP server</span> is just a program that exposes capabilities through the MCP protocol.

It might wrap Gmail. It might wrap Slack. It might wrap a filesystem. It might wrap Wikipedia. It might expose a database, a browser, a local command, or some internal company system.

The server usually does not do magic. It wraps something more ordinary:

- a Gmail MCP server wraps the Gmail API
- a Slack MCP server wraps the Slack API
- a filesystem MCP server wraps local files
- a Wikipedia MCP server wraps Wikipedia data

The AI application is the MCP host. It creates MCP clients to maintain connections to MCP servers, asks what functions are available, receives schemas, calls one of those functions, and gets structured results back.

That means <span class="blog-highlight blog-highlight--agent">MCP</span> gives the host and server a repeatable handshake:

<div class="blog-insight">
  <span class="blog-insight__label">The MCP Handshake</span>
  <ul>
    <li><strong>Discovery:</strong> the host asks which functions the server exposes.</li>
    <li><strong>Description:</strong> the server returns names, descriptions, and argument schemas.</li>
    <li><strong>Execution:</strong> the host calls one function with validated arguments.</li>
    <li><strong>Result:</strong> the server returns structured data for the host to shape into evidence.</li>
  </ul>
</div>

That is the useful part.

But notice what is missing from that list.

MCP does not decide whether the function is safe. It does not decide whether the user approved it. It does not decide whether a Gmail result should be summarized, redacted, logged, cached, or shown back to the model. It does not decide whether `send_email` should be available just because `search_messages` is available.

Those are product and harness decisions.

## The Jargon That Tripped Me

The words are part of the problem.

In MCP language, a callable operation is often called a *tool*. In product language, that can be confusing. A normal user does not think "Gmail has 17 tools." They think "Gmail is a tool, and it can do several things."

I now prefer this vocabulary:

- **Model runtime or provider:** where inference happens, such as LM Studio, Ollama, Claude, or another hosted model API.
- **MCP server:** the process that exposes external functions through MCP.
- **MCP host:** the AI application that coordinates one or more MCP server connections.
- **MCP client:** the per-server connection component the host uses to talk to an MCP server.
- **MCP Manager:** software that helps install, run, group, configure, or authorize MCP servers.
- **Product tool:** a user-recognizable capability such as Gmail, Calendar, Wikipedia, Search, or Slack.
- **Function:** one executable operation inside that product tool, such as `search_messages`, `list_events`, or `get_summary`.

That distinction sounds pedantic until you build the UI.

If a Docker MCP profile shows Gmail, Slack, and Wikipedia, that is not the same thing as telling the model it can call every function from every server. It only means those servers are visible or available through the manager.

Visibility is not execution.

## The Context Window Is The Real Tool Problem

Once the vocabulary became clearer, the harder question was not *"can MCP expose tools?"*

It was this:

<blockquote class="blog-pullquote">
  <p>How does an <span class="blog-highlight blog-highlight--agent">LLM</span> choose tools without overloading its context window with the full tooling universe?</p>
</blockquote>

This is one of the most important practical agent-engineering problems.

The model cannot make a structured tool decision if it knows nothing about available capabilities. But it also does not need full API docs, full MCP schemas, every server capability, every argument definition, every OAuth flow, and every connector detail.

That would be a bad trade. Context windows are finite. Large manifests create noise. Token cost grows. Reasoning quality degrades. Tool selection gets worse because the model is searching through too much irrelevant surface area.

The useful abstraction is lighter:

<div class="blog-insight">
  <span class="blog-insight__label">Expose Intentions First</span>
  <ul>
    <li><strong>search_emails:</strong> find relevant email messages.</li>
    <li><strong>search_web:</strong> fetch current or external public information.</li>
    <li><strong>inspect_local_files:</strong> read or search local project context.</li>
    <li><strong>query_calendar:</strong> inspect schedule and availability.</li>
    <li><strong>search_slack:</strong> find relevant team conversation history.</li>
  </ul>
</div>

The <span class="blog-highlight blog-highlight--agent">LLM</span> chooses an intention first. It reads the user request, the relevant conversation history, and the lightweight capabilities currently exposed by the harness. The harness then expands that intention into the small subset of tools that matter.

That is the key architectural optimization.

The structured response should also be machine-readable. The model should not say, *"I think I should probably search emails now."* That forces the harness into brittle prose parsing, regex routing, and unsafe ambiguity.

It should emit something narrow, such as `{"intent": "search_emails"}`. After the harness exposes the relevant tool subset, the model can then emit the exact tool call, such as `{"tool": "gmail_search_messages", "arguments": {"query": "from:recruiter newer_than:7d"}}`.

The nuance matters: the harness should not infer broad intent from raw prose. That would either require another model call or a brittle NLP router. The conversational <span class="blog-highlight blog-highlight--agent">LLM</span> owns intention identification; the harness owns what happens after a structured intention is declared.

That gives us a staged narrowing process:

<div class="blog-insight">
  <span class="blog-insight__label">Staged Tool Narrowing</span>
  <div class="blog-stage-flow">
    <div class="blog-stage-flow__step">
      <span class="blog-stage-flow__index">1</span>
      <div class="blog-stage-flow__body"><strong>User message</strong>The user asks for something that may require external capability.</div>
    </div>
    <div class="blog-stage-flow__step">
      <span class="blog-stage-flow__index">2</span>
      <div class="blog-stage-flow__body"><strong>Harness exposes lightweight intentions</strong>The model sees a small capability menu, not every MCP schema in the universe.</div>
    </div>
    <div class="blog-stage-flow__step">
      <span class="blog-stage-flow__index">3</span>
      <div class="blog-stage-flow__body"><strong>LLM emits structured intent</strong>The output is machine-readable, such as <code>{"intent": "search_emails"}</code>.</div>
    </div>
    <div class="blog-stage-flow__step">
      <span class="blog-stage-flow__index">4</span>
      <div class="blog-stage-flow__body"><strong>Harness maps intent to tool subset</strong>Email intent can expose Gmail search/list functions without exposing Slack, filesystem, or calendar schemas.</div>
    </div>
    <div class="blog-stage-flow__step">
      <span class="blog-stage-flow__index">5</span>
      <div class="blog-stage-flow__body"><strong>LLM emits exact tool call</strong>The model now sees the relevant function names and argument schemas, then chooses one.</div>
    </div>
    <div class="blog-stage-flow__step">
      <span class="blog-stage-flow__index">6</span>
      <div class="blog-stage-flow__body"><strong>Harness validates and executes</strong>The harness checks policy, approvals, scopes, and arguments before calling through MCP.</div>
    </div>
    <div class="blog-stage-flow__step">
      <span class="blog-stage-flow__index">7</span>
      <div class="blog-stage-flow__body"><strong>Evidence returns</strong>Results are bounded, shaped, logged, and then passed back to the model for the final answer.</div>
    </div>
  </div>
</div>

<figure class="blog-figure blog-figure--wide">
  <img src="{{ 'assets/images/posts/2026/mcp-is-plumbing/staged-tool-narrowing-context-window.png' | relative_url }}" alt="Ninja avatar-minion guiding many available tools through intention, relevant tools, and exact call gates while a context-window meter moves from overloaded to readable." loading="lazy" />
  <figcaption class="blog-figure__caption">The trick is not to show the model every tool. Narrow the search space first, then ask for the exact structured call.</figcaption>
</figure>

This is where the boundary between the model and the harness matters.

<div class="blog-layer-grid">
  <div class="blog-layer-card">
    <h4>Main LLM</h4>
    <p>Understands the user request, reasons about intent, emits structured intent or tool-call decisions, and writes the final answer from supplied evidence.</p>
    <p>It should not own raw API execution, auth, validation, approval, or audit.</p>
  </div>
  <div class="blog-layer-card">
    <h4>Harness</h4>
    <p>Maintains thread state, exposes lightweight intentions, maps intentions to tool subsets, validates calls, manages approval, executes tools, logs activity, and shapes evidence.</p>
    <p>This is the real agent control layer.</p>
  </div>
  <div class="blog-layer-card">
    <h4>MCP Layer</h4>
    <p>Standardizes discovery, function schemas, and calls to external capability providers.</p>
    <p>It is not reasoning, planning, memory, safety, or orchestration.</p>
  </div>
</div>

Some systems expose all tools directly to the model. For a small demo or a tiny tool ecosystem, that is reasonable. It is simpler, has fewer orchestration steps, and avoids another round trip.

But as the tool ecosystem grows, that simplicity stops being free.

If the model sees hundreds of tools and thousands of schema fields, the context window becomes a dumping ground. The practical answer is hierarchical exposure: choose intention from a small set, expose only the relevant tool subset, then generate the exact structured call.

## Docker MCP Toolkit Is A Manager, Not The Trust Model

This is where my own work made the lesson concrete.

I have been working on a local AI-first solution, and one of the practical questions was how external tools should appear without making the user paste transport commands into a form like a punishment.

The first time the boundary became obvious, the UI could see more than the runtime was willing to use. A manager profile could show external capabilities. A tools page could display them. But that did not mean the model should immediately receive every function behind that profile.

That felt annoying at first, because it made the product look less "connected" than the setup technically was. But the annoyance was useful. It forced the distinction I had been missing.

Docker Desktop's MCP Toolkit is useful here because it gives a manager-like UI around catalogs, profiles, containers, gateway behavior, and credential support. Docker's own docs describe the catalog as a curated collection of MCP servers and the gateway as a proxy that handles server lifecycle, routing, and authentication across profiles.

That is useful plumbing.

But it is still plumbing.

The local assistant harness still has to decide what enters the model-visible manifest.

For example, a Docker MCP profile may make Wikipedia, Gmail, and Slack visible. The local harness may still choose a much narrower runtime posture:

<div class="blog-insight">
  <span class="blog-insight__label">Available Versus Routed</span>
  <ul>
    <li><strong>Wikipedia:</strong> available and routed, because the enabled functions are read-only.</li>
    <li><strong>Gmail:</strong> available, but not routed until account authorization, scopes, and read-only policy are clear.</li>
    <li><strong>Slack:</strong> available, but write-capable functions stay blocked until approval flows exist.</li>
  </ul>
</div>

This is the distinction I care about most:

<blockquote class="blog-pullquote">
  <p>Available is not the same as routed.</p>
  <p>Routed is not the same as approved.</p>
</blockquote>

Once that clicked, MCP stopped looking like a magical agent feature and started looking like a sensible extension boundary.

<figure class="blog-figure blog-figure--wide">
  <img src="{{ 'assets/images/posts/2026/mcp-is-plumbing/docker-mcp-manager.png' | relative_url }}" alt="Hand-drawn ninja avatar-minion connecting selected Docker MCP Manager tools into a model-visible manifest, shown beside Docker Desktop MCP Toolkit catalog and profile screenshots." loading="lazy" />
  <figcaption class="blog-figure__caption">Docker MCP Toolkit can make tools visible, but the local harness still decides which functions are routed into the model-visible manifest.</figcaption>
</figure>

If you want the terminal version of creating a Docker MCP profile, assigning catalog servers, and registering the gateway with a client, I moved that into a small companion reference: [Docker MCP Toolkit profile setup]({{ '/references/docker-mcp-manager-profile-setup/' | relative_url }}).

The product point remains the same: a profile registers servers with Docker MCP. It does not make every advertised function safe to route into the model.

## The Connector Zoo MCP Avoids

Suppose I ignored MCP and connected everything directly.

The architecture would begin simply enough: direct adapters for Gmail, Slack, GitHub, Calendar, the local filesystem, and whatever database or browser integration came next.

That can work for one or two integrations. Then the same questions return:

- how do we discover operations and describe them to the model?
- how do we validate arguments and normalize errors?
- how do we keep credentials out of prompts and logs?
- how do we separate read actions from write actions?
- how do we return useful evidence without flooding the model?
- how do we package local dependencies on a real user's machine?

MCP gives a standard answer to the discovery, schema, and call shape. It lets tool builders package capability once and lets different AI hosts consume it without inventing a new connector contract every time.

That is valuable. It still leaves the host with the trust boundary.

## One Request Makes The Boundary Obvious

Take a simple personal-assistant request:

<blockquote class="blog-pullquote blog-pullquote--compact">
  <p>Summarize my unread email from this morning.</p>
</blockquote>

If Gmail access exists somewhere in the system, it is tempting to think the problem is solved. It is not.

The useful execution path has several boundaries:

<div class="blog-insight">
  <span class="blog-insight__label">Read-Only Gmail Path</span>
  <div class="blog-flow">
    <div class="blog-flow__step">User asks</div>
    <div class="blog-flow__arrow" aria-hidden="true">&rarr;</div>
    <div class="blog-flow__step">Model selects email intent</div>
    <div class="blog-flow__arrow" aria-hidden="true">&rarr;</div>
    <div class="blog-flow__step">Harness exposes Gmail tools</div>
    <div class="blog-flow__arrow" aria-hidden="true">&rarr;</div>
    <div class="blog-flow__step">Model chooses search</div>
    <div class="blog-flow__arrow" aria-hidden="true">&rarr;</div>
    <div class="blog-flow__step">Harness checks policy</div>
    <div class="blog-flow__arrow" aria-hidden="true">&rarr;</div>
    <div class="blog-flow__step">MCP server reads</div>
    <div class="blog-flow__arrow" aria-hidden="true">&rarr;</div>
    <div class="blog-flow__step">Evidence is bounded</div>
    <div class="blog-flow__arrow" aria-hidden="true">&rarr;</div>
    <div class="blog-flow__step">Answer is written</div>
  </div>
  <p>The audit record belongs to the harness path as well. It should say which connector ran, which function was called, and what kind of evidence returned.</p>
</div>

Each arrow is doing different work.

The MCP server knows how to talk to Gmail. The model knows how to identify the email-search intention and summarize the returned evidence. The local harness decides which Gmail functions become visible, whether the final function call is allowed, what evidence is allowed back, and what gets recorded.

Now change the request:

<blockquote class="blog-pullquote blog-pullquote--compact">
  <p>Reply to Alex and say I will be ten minutes late.</p>
</blockquote>

That is no longer the same class of action. The system should compose a draft, show the recipient and exact text, wait for approval, and only then send. If the same path treats search and send as merely two advertised functions, the architecture has already lost an important distinction.

That is why the host cannot outsource judgment to MCP.

## Read-Only Is Not A Vibe

One of the fastest ways to make an assistant feel impressive is to let it touch personal tools.

One of the fastest ways to make it untrustworthy is to blur read and write behavior.

I would start with read-only actions:

<div class="blog-insight">
  <span class="blog-insight__label">Read-Only First</span>
  <ul>
    <li><strong>Gmail:</strong> search messages, list labels, fetch snippets.</li>
    <li><strong>Calendar:</strong> list events, check free/busy, show calendar names.</li>
    <li><strong>Wikipedia:</strong> search, get summaries, fetch article metadata.</li>
  </ul>
</div>

I would hold back actions that change the world:

<div class="blog-insight">
  <span class="blog-insight__label">Approval Required</span>
  <ul>
    <li><strong>Gmail:</strong> send email, delete email, forward attachment.</li>
    <li><strong>Calendar:</strong> create events, update events, invite attendees, cancel meetings.</li>
    <li><strong>Slack:</strong> post messages, react, invite users.</li>
  </ul>
</div>

Those actions need previews, approvals, audit records, and revocation. They should not become available merely because a server advertises them.

The same applies to evidence.

If a Wikipedia connector returns a title and URL, that can be cited as Wikipedia evidence. If a Gmail connector returns a message subject, the system should not invent a public source URL because some generic normalizer once did that for Wikipedia. Helpful fallbacks become false provenance when they are applied globally.

This is where the boring engineering matters.

Fail closed when a function is ambiguous. Keep credentials out of prompts. Do not route write actions before the approval path exists. Do not turn private snippets into fake citations. Keep the audit trail local and explicit.

This is not fear. It is interface discipline.

<figure class="blog-figure blog-figure--wide">
  <img src="{{ 'assets/images/posts/2026/mcp-is-plumbing/read-only-product-policy.png' | relative_url }}" alt="Ninja avatar-minions separating read-only access from write actions, with approval controls, Gmail snippets, calendar events, and policy-before-permission notes." loading="lazy" />
  <figcaption class="blog-figure__caption">Read-only is a product policy, not a hopeful interpretation of a function name. Visibility does not imply permission.</figcaption>
</figure>

## Local-First Does Not Mean Offline-Only

This point also confused me at first.

If I am building a local AI-first system, does using Gmail through MCP violate the local-first idea?

Not necessarily.

Local-first does not mean the system can never call an external API. Gmail is external. Slack is external. Calendar is external. Search is external. The useful local-first boundary is about ownership and control:

- the model runtime can be local
- user configuration can be local
- tool preferences can be local
- approval state can be local
- audit records can be local
- credentials should stay out of prompts and logs
- the harness decides what evidence reaches the model

A local Gmail MCP server may still call Google APIs after the user authorizes it. That is fine. The important part is that the model is not handed OAuth tokens and told to improvise.

The local harness mediates.

That is the architecture I trust.

## The Stack I Wish Someone Had Drawn For Me

By this point, the stack is simple enough to state once:

<div class="blog-insight">
  <span class="blog-insight__label">The Stack</span>
  <ul>
    <li><strong>User:</strong> asks for help from the local assistant.</li>
    <li><strong>Local assistant app / harness:</strong> owns routing, validation, approvals, audit, and evidence shaping.</li>
    <li><strong>Model runtime or provider:</strong> handles inference for reasoning and answer generation.</li>
    <li><strong>MCP Manager:</strong> discovers, groups, launches, or authorizes MCP servers.</li>
    <li><strong>MCP server:</strong> exposes one provider or capability domain.</li>
    <li><strong>Provider API or local resource:</strong> performs the underlying real-world read or action.</li>
  </ul>
</div>

The useful part of the diagram is not the arrows. It is ownership.

When these responsibilities collapse, the trust model moves to the wrong place. The model layer can end up executing actions the assistant app cannot audit. The MCP Manager can accidentally turn catalog visibility into permission. The MCP server can decide how much private data returns to the model.

So the architecture lesson is simple:

<blockquote class="blog-pullquote blog-pullquote--compact">
  <p><span class="blog-highlight blog-highlight--agent">MCP</span> standardizes connection.</p>
  <p>It does not standardize judgment.</p>
</blockquote>

## Where I Would Start

For a practical local assistant, I would not start by connecting every personal tool and hoping policy catches up.

I would start narrower:

1. connect one public, read-only server such as Wikipedia
2. show the discovered functions grouped under one user-facing tool
3. route only functions with explicit read-only metadata
4. record tool calls and compact evidence
5. add Gmail or Calendar read-only after authorization and scope display are clear
6. add write actions only after preview, approval, audit, and disable paths are real

That order is slower than a demo.

It is also much closer to something I would trust.

The uncomfortable part is that responsible MCP adoption can look unimpressive at first. A profile may show ten exciting tools, while the assistant only routes one public read-only connector. That looks cautious because it is cautious.

But the alternative is worse: a system that confuses discovery with permission, then discovers the trust model only after private data or side effects are already in the path.

<figure class="blog-figure blog-figure--wide">
  <img src="{{ 'assets/images/posts/2026/mcp-is-plumbing/gmail-mcp-server-setup-path.png' | relative_url }}" alt="Hand-drawn implementation path for MCP adoption with ninja avatar-minions carrying Wikipedia read-only, Gmail auth state, Calendar scopes, approval preview, and audit trail blocks beside a Gmail MCP tools configuration panel." loading="lazy" />
  <figcaption class="blog-figure__caption">This is the staged path I trust more than a flashy demo: read-only first, then identity, scopes, approval previews, and audit before write-capable functions become routine.</figcaption>
</figure>

## Closing Thoughts

MCP makes much more sense to me when I stop treating it as an agent feature and start treating it as an integration standard.

It is not the assistant. It is not the model runtime or provider. It is not the safety model. It is not the product UI. It is not the approval system.

It is the protocol that lets an AI host discover and call external capabilities in a more standard way.

That is already enough.

The real product work starts after discovery: deciding what should be visible, what should be routed, what should require approval, what evidence should return, and what must never enter the prompt in the first place.

That is why I now find MCP interesting.

Not because it removes the hard parts, but because it gives the hard parts a cleaner place to live.

## Useful References

- [Docker MCP Toolkit profile setup]({{ '/references/docker-mcp-manager-profile-setup/' | relative_url }})
- [Anthropic: Introducing the Model Context Protocol](https://www.anthropic.com/news/model-context-protocol)
- [Model Context Protocol: What is MCP?](https://modelcontextprotocol.io/docs/getting-started/intro)
- [Docker MCP Catalog](https://docs.docker.com/ai/mcp-catalog-and-toolkit/catalog/)
- [Docker MCP Gateway](https://docs.docker.com/ai/mcp-catalog-and-toolkit/mcp-gateway/)
