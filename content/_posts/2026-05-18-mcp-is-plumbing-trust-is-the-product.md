---
title: "MCP Finally Clicked: It Is Plumbing. Trust Is The Product."
title_html: "<span class='blog-title-accent blog-title-accent--signal'>MCP</span> Finally Clicked: It Is Plumbing. Trust Is The Product."
author: Christos Hadjinikolis
layout: post
date: 2026-05-18
description: "A practical mental model for the Model Context Protocol, how APIs become model-readable tools, and why local AI systems still need routing, approval, evidence, and trust boundaries."
seo_keywords: ["Model Context Protocol", "MCP", "AI agents", "tool calling", "MCP server", "MCP Manager", "Docker MCP Toolkit", "REST API", "API wrapper", "local-first AI", "tool safety", "agentic AI"]
nav_tags: ["MCP", "Agents", "Trust"]
og_image: "assets/images/posts/2026/mcp-is-plumbing/ninja avatar-minion-at-a-cluttered-local-AI-workbench.png"
og_image_alt: "Hand-drawn ninja avatar-minion wiring Gmail, Calendar, and Wikipedia into a local AI assistant through labelled MCP cables."
linkedin_post_url: "https://www.linkedin.com/feed/update/urn:li:activity:7462244482751578113/"
linkedin_embed_url: "https://www.linkedin.com/embed/feed/update/urn:li:activity:7462244482751578113?collapsed=1"
tldr_why_read: "Read this if <span class=\"blog-highlight blog-highlight--agent\">MCP</span> sounds useful but the words around it still feel slightly slippery: API, tool, function, <span class=\"blog-highlight blog-highlight--mcp-server\">MCP server</span>, <span class=\"blog-highlight blog-highlight--mcp-client\">MCP client</span>, host, manager, gateway, catalog."
tldr_persona: "Especially useful for engineers building local or private <span class=\"blog-highlight blog-highlight--agent\">AI</span> assistants who need external tools without turning every integration into custom <span class=\"blog-highlight blog-highlight--connector\">connectors</span> or a trust problem."
tldr_learn: "Why <span class=\"blog-highlight blog-highlight--agent\">MCP</span> arrived when <span class=\"blog-highlight blog-highlight--agent\">agents</span> needed real tools, how an API call becomes a model-readable tool, what MCP standardizes, and why serious agents still need staged intent narrowing."
tldr_takeaways: ["An MCP tool is often an ordinary API call wrapped in a model-readable contract", "MCP is valuable exactly where it is boring: it standardizes <span class=\"blog-highlight blog-highlight--connector\">connector</span> plumbing", "Available is not the same as routed, and routed is not the same as approved", "The useful architecture separates intent identification, tool exposure, tool execution, and safety/orchestration"]
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
  <p>It standardizes <span class="blog-highlight blog-highlight--connector">connector</span> plumbing. It does not absolve the host application from trust, routing, approval, or evidence discipline.</p>
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

The problem was not the loop. The problem was <span class="blog-highlight blog-highlight--glue">glue code</span>.

Every serious AI application began needing <span class="blog-highlight blog-highlight--connector">connectors</span>: Gmail, Slack, GitHub, files, calendars, databases, browsers, search, internal systems. Each <strong>connector</strong> needed provider-specific setup, credentials, scopes, pagination, rate-limit handling, argument schemas, error normalization, result shaping, and model-facing descriptions.

That <span class="blog-highlight blog-highlight--glue">glue code</span> has an unpleasant habit: it looks small when you write one <strong>connector</strong> and becomes architectural weight when every host application repeats it differently.

Gmail needs one shape of OAuth, search, labels, snippets, and attachment handling. Slack needs another shape of channels, threads, users, bot permissions, and message posting. GitHub, calendars, browsers, databases, and files all bring their own little integration worlds. Then each AI host still has to translate those worlds into something a model can discover and call.

That is how you end up with a <span class="blog-highlight blog-highlight--connector">connector zoo</span>, and then with <span class="blog-highlight blog-highlight--glue">glue code</span> proliferating around the zoo.

The timing matters too. Around the same period, the conversation moved from <span class="blog-highlight blog-highlight--chatbot">chatbots</span> toward <span class="blog-highlight blog-highlight--agent">agents</span>, coding assistants, desktop assistants, local runtimes, and tools that could act on real systems. Models were getting better, but they were still isolated from the places where useful work actually happens. A coding assistant needs the repository. A personal assistant needs calendar and email. A business assistant needs internal documents, tickets, dashboards, and databases.

That world cannot scale on every app hand-rolling every connector and every connector contract.

Anthropic introduced the Model Context Protocol on November 25, 2024 as an open standard for connecting AI assistants to systems where data lives. The official MCP docs use the USB-C analogy: one standard connection shape instead of a different cable for every device. That analogy is imperfect, but useful enough.

The deeper point is this:

<blockquote class="blog-pullquote blog-pullquote--compact">
  <p><span class="blog-highlight blog-highlight--agent">MCP</span> exists because every AI app should not have to reinvent the same connector protocol differently.</p>
</blockquote>

Before <span class="blog-highlight blog-highlight--agent">MCP</span>, connecting an assistant to external systems usually meant each host application had to invent its own integration language. <span class="blog-highlight blog-highlight--agent">MCP</span> gives those integrations a common shape, so the <span class="blog-highlight blog-highlight--glue">glue code</span> can move behind a more standard boundary instead of leaking into every product in a slightly different form.

## The Jargon That Tripped Me

The words are part of the problem, so it is worth clearing them before drawing the system.

In MCP language, a callable operation is often called a *tool*. In product language, that can be confusing. A normal user does not think "Gmail has 17 tools." They think "Gmail is a tool, and it can do several things."

I now prefer this vocabulary:

- **AI application / MCP host:** the product boundary that owns the assistant experience and coordinates one or more <span class="blog-highlight blog-highlight--mcp-server">MCP server</span> connections.
- **<span class="blog-highlight blog-highlight--harness">Harness</span> / agent control layer:** the host-side component that owns routing, validation, approvals, audit, and evidence shaping.
- **Model runtime or provider:** where inference happens, such as LM Studio, Ollama, Claude, or another hosted model API.
- **<span class="blog-highlight blog-highlight--mcp-client">MCP client</span>:** the per-server connection component the host uses to talk to an <span class="blog-highlight blog-highlight--mcp-server">MCP server</span>.
- **<span class="blog-highlight blog-highlight--mcp-server">MCP server</span>:** the process across the protocol boundary that exposes external functions through MCP.
- **MCP Manager:** software that helps install, run, group, configure, or authorize <span class="blog-highlight blog-highlight--mcp-server">MCP servers</span>.
- **Product tool:** a user-recognizable capability such as Gmail, Calendar, Wikipedia, Search, or Slack.
- **Function:** one executable operation inside that product tool, such as `search_messages`, `list_events`, or `get_summary`. In many cases, the function eventually becomes an ordinary API call.

That distinction sounds pedantic until you build the UI.

If an MCP Manager profile shows Gmail, Slack, and Wikipedia, that is not the same thing as telling the model it can call every function from every server. It only means those servers are visible or available through the manager.

Visibility is not execution.

Once that vocabulary is less slippery, the mental model becomes much easier.

## A Tool Is Usually An API Call

This is the missing layer in many MCP explanations.

Before <span class="blog-highlight blog-highlight--agent">MCP</span>, there were already APIs.

An API is a contract that lets one software system ask another software system to do something. In a REST API, that contract usually looks like HTTP endpoints, methods, parameters, authentication, and JSON responses. A human developer reads the documentation, understands the authentication model, writes client code, handles errors, and decides how the result should be used.

For example, a simple weather integration might eventually call an HTTP endpoint shaped roughly like this:

```http
GET /weather/current?city=London&units=metric
Authorization: Bearer ...
```

That is not an AI concept. It is normal application integration.

The API exposes an endpoint. The application code owns the orchestration.

What MCP changes is the consumer of that contract. Instead of only giving a human developer an endpoint to wire manually, the MCP server exposes a capability in a form that an AI host can discover, describe to a model, validate, and invoke.

The same weather capability might become a model-readable tool description:

```json
{
  "name": "get_current_weather",
  "description": "Get the current weather for a city.",
  "inputSchema": {
    "type": "object",
    "properties": {
      "city": {
        "type": "string",
        "description": "City name"
      },
      "units": {
        "type": "string",
        "enum": ["metric", "imperial"]
      }
    },
    "required": ["city"]
  }
}
```

Then, when the user asks *"what is the weather in London?"*, the model does not call the weather provider directly. The host gives the model a constrained tool contract. The model proposes a structured call:

```json
{
  "tool": "get_current_weather",
  "arguments": {
    "city": "London",
    "units": "metric"
  }
}
```

The host-side <span class="blog-highlight blog-highlight--harness">harness</span> validates that request. The <span class="blog-highlight blog-highlight--mcp-client">MCP client</span> sends it to the weather <span class="blog-highlight blog-highlight--mcp-server">MCP server</span>. The server translates the tool call into the provider-specific API request, handles the provider response, and returns structured data back across the MCP boundary.

That is the concrete shape of the idea.

<div class="blog-insight">
  <span class="blog-insight__label">API To Tool</span>
  <div class="blog-flow">
    <div class="blog-flow__step">Provider API endpoint</div>
    <div class="blog-flow__arrow" aria-hidden="true">&rarr;</div>
    <div class="blog-flow__step"><span class="blog-highlight blog-highlight--mcp-server">MCP server</span> wraps it</div>
    <div class="blog-flow__arrow" aria-hidden="true">&rarr;</div>
    <div class="blog-flow__step">Tool name and schema</div>
    <div class="blog-flow__arrow" aria-hidden="true">&rarr;</div>
    <div class="blog-flow__step">Host exposes tool</div>
    <div class="blog-flow__arrow" aria-hidden="true">&rarr;</div>
    <div class="blog-flow__step">Model proposes call</div>
  </div>
  <p>The model sees the constrained, structured tool contract. The server still deals with the ordinary provider API behind the boundary.</p>
</div>

<blockquote class="blog-pullquote blog-pullquote--compact">
  <p>A tool is not magic agent intelligence.</p>
  <p>It is usually an API capability wrapped in a model-readable contract.</p>
</blockquote>

This is also why MCP can feel underwhelming when inspected closely.

Under the hood, many <span class="blog-highlight blog-highlight--mcp-server">MCP servers</span> are wrappers around ordinary APIs. A GitHub server may call the GitHub API. A Slack server may call the Slack API. A Gmail server may call the Gmail API. The novelty is not that APIs suddenly exist. The novelty is that the assistant ecosystem gets a standard way to discover capabilities, see their schemas, call them with structured arguments, and receive structured results.

In other words:

<div class="blog-insight">
  <span class="blog-insight__label">API Versus MCP</span>
  <ul>
    <li><strong>REST API:</strong> "Here are endpoints. Developer, wire the integration and orchestration yourself."</li>
    <li><strong>MCP:</strong> "Here are capabilities in a form an AI host can expose to a model and invoke through a standard protocol."</li>
  </ul>
</div>

That distinction matters because it prevents two bad interpretations.

The first is over-selling MCP as if it replaces APIs. It does not. It often sits on top of them.

The second is under-selling MCP as *just an API wrapper*. It is often a wrapper, but the wrapper is doing something specific: turning provider-specific operations into a common, discoverable, schema-backed tool interface for an LLM runtime.

## The Simplest Mental Model

Here is the version that finally made it click for me.

An <span class="blog-highlight blog-highlight--mcp-server">MCP server</span> is the adapter that exposes those capabilities through the MCP protocol.

It is called a <em>server</em> because, from the assistant's point of view, it serves capabilities over a protocol boundary. That does not mean it has to be a public web server running somewhere on the internet. It can be a local process, a Docker container, or a small service launched by the host. *External* here means outside the host boundary, not necessarily remote.

The practical pattern is usually one <span class="blog-highlight blog-highlight--mcp-server">MCP server</span> per capability provider.

A Gmail <span class="blog-highlight blog-highlight--mcp-server">MCP server</span> is the Gmail-side adapter. It can expose many callable functions:

- `search_messages`
- `list_labels`
- `get_thread`
- `create_draft`
- `send_message`

A Slack <span class="blog-highlight blog-highlight--mcp-server">MCP server</span> is the Slack-side adapter. A filesystem <span class="blog-highlight blog-highlight--mcp-server">MCP server</span> is the local-files adapter. The server is the boundary around the provider; the functions inside it are the individual operations.

Most of the time, the server still wraps something ordinary:

- a Gmail <span class="blog-highlight blog-highlight--mcp-server">MCP server</span> wraps the Gmail API
- a Slack <span class="blog-highlight blog-highlight--mcp-server">MCP server</span> wraps the Slack API
- a filesystem <span class="blog-highlight blog-highlight--mcp-server">MCP server</span> wraps local files
- a Wikipedia <span class="blog-highlight blog-highlight--mcp-server">MCP server</span> wraps Wikipedia data

In MCP terms, the AI application is the MCP host.

For this post, think of the host as the product boundary: the assistant UI, conversation state, model interface, <span class="blog-highlight blog-highlight--harness">harness</span>, and <span class="blog-highlight blog-highlight--mcp-client">MCP clients</span> all live on the host side. The actual model may be local or hosted; the host is the application that calls it. The <strong>harness</strong> is not a separate MCP role. It is the part of the host I care about because it owns routing, validation, approvals, audit, and evidence shaping.

An <span class="blog-highlight blog-highlight--mcp-client">MCP client</span> is the host-side protocol connection to one <span class="blog-highlight blog-highlight--mcp-server">MCP server</span>. If the host talks to Gmail, Slack, and the filesystem, it may maintain separate <span class="blog-highlight blog-highlight--mcp-client">MCP client</span> connections for each server. Across that protocol boundary sit the <span class="blog-highlight blog-highlight--mcp-server">MCP servers</span>.

<div class="blog-component-map" role="group" aria-label="MCP host, client, server, and provider relationship">
  <div class="blog-component-map__column blog-component-map__column--host">
    <span class="blog-component-map__label">AI application / MCP host</span>
    <div class="blog-component-map__node">Assistant UI + conversation state</div>
    <div class="blog-component-map__node blog-component-map__node--harness">Harness / agent control layer<br><small>routing, policy, approvals, audit, evidence</small></div>
    <div class="blog-component-map__node">Model interface<br><small>calls local runtime or hosted model API</small></div>
    <div class="blog-component-map__node blog-component-map__node--client"><span class="blog-highlight blog-highlight--mcp-client">MCP clients</span><br><small>host-side connections to servers</small></div>
  </div>
  <div class="blog-component-map__boundary">MCP protocol boundary</div>
  <div class="blog-component-map__column">
    <span class="blog-component-map__label"><span class="blog-highlight blog-highlight--mcp-server">MCP servers</span></span>
    <div class="blog-component-map__node blog-component-map__node--server">Gmail <span class="blog-highlight blog-highlight--mcp-server">MCP server</span><br><small>search, labels, threads, drafts, send</small></div>
    <div class="blog-component-map__node blog-component-map__node--server">Slack <span class="blog-highlight blog-highlight--mcp-server">MCP server</span><br><small>channels, threads, messages</small></div>
    <div class="blog-component-map__node blog-component-map__node--server">Filesystem <span class="blog-highlight blog-highlight--mcp-server">MCP server</span><br><small>read, search, metadata</small></div>
  </div>
  <div class="blog-component-map__boundary">Provider boundary</div>
  <div class="blog-component-map__column">
    <span class="blog-component-map__label">Provider / resource</span>
    <div class="blog-component-map__node blog-component-map__node--provider">Gmail API</div>
    <div class="blog-component-map__node blog-component-map__node--provider">Slack API</div>
    <div class="blog-component-map__node blog-component-map__node--provider">Local files</div>
  </div>
</div>

That means <span class="blog-highlight blog-highlight--agent">MCP</span> gives the host and server a repeatable handshake around capabilities that may ultimately be API calls:

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

Those are product and <span class="blog-highlight blog-highlight--harness">harness</span> decisions.

## The Context Window Is The Real Tool Problem

Once the vocabulary became clearer, the harder question was not *"can MCP expose tools?"*

It was this:

<blockquote class="blog-pullquote">
  <p>How does an <span class="blog-highlight blog-highlight--agent">LLM</span> choose tools without overloading its context window with the full tooling universe?</p>
</blockquote>

This is one of the most important practical agent-engineering problems.

The lazy version of a chatbot application, especially before a clean server boundary exists, is to start every thread with a huge prompt:

```text
You can search Gmail, list Gmail labels, fetch Gmail threads,
create drafts, search Slack, post to Slack, inspect files,
query calendars, search tickets, browse the web...
```

That is not an architecture. It is a context-window landfill.

MCP gives the host a standard way to discover tool schemas, but the host still has to decide which of those schemas should reach the model at this moment. Dumping every discovered server, function, argument definition, OAuth caveat, and <span class="blog-highlight blog-highlight--connector">connector</span> detail into every conversation recreates the old problem in a new place.

The lighter abstraction is to expose intentions first:

```json
{
  "available_intents": [
    { "intent": "search_emails", "policy": "read_only" },
    { "intent": "query_calendar", "policy": "read_only" },
    { "intent": "inspect_local_files", "policy": "read_only" },
    { "intent": "search_slack", "policy": "read_only" }
  ]
}
```

Now the <span class="blog-highlight blog-highlight--agent">LLM</span> can answer the first routing question without seeing the full Gmail, Slack, Calendar, and filesystem manifests. For a user request like *"show me the latest three emails"*, the model can emit a narrow structured intention:

```json
{
  "intent": "search_emails"
}
```

The host-side <span class="blog-highlight blog-highlight--harness">harness</span> then maps that intention to the relevant <span class="blog-highlight blog-highlight--mcp-server">MCP server</span> and exposes only the small tool subset needed for the next model decision:

```json
{
  "available_tools": [
    {
      "name": "gmail_list_messages",
      "arguments": {
        "max_results": "number",
        "query": "string"
      }
    },
    {
      "name": "gmail_get_thread",
      "arguments": {
        "thread_id": "string"
      }
    }
  ]
}
```

Only then does the model choose the exact callable function:

```json
{
  "tool": "gmail_list_messages",
  "arguments": {
    "max_results": 3,
    "query": "newer_than:1d"
  }
}
```

That is the staged narrowing process. The <span class="blog-highlight blog-highlight--agent">LLM</span> owns intention identification. The <span class="blog-highlight blog-highlight--harness">harness</span> owns mapping, policy, approval, execution, audit, and evidence shaping. The <span class="blog-highlight blog-highlight--mcp-server">MCP server</span> owns the provider-specific call shape.

<div class="blog-sequence" role="group" aria-label="Staged tool narrowing sequence from user request to MCP result">
  <div class="blog-sequence__actors" aria-hidden="true">
    <span>User</span>
    <span>Chat UI</span>
    <span>Harness</span>
    <span>Model</span>
    <span>Gmail <span class="blog-highlight blog-highlight--mcp-server">MCP server</span></span>
    <span>Gmail API</span>
  </div>
  <div class="blog-sequence__step">
    <div class="blog-sequence__message" style="--from: 1; --to: 3;"><strong>User request</strong><span>"Show me the latest three emails."</span></div>
  </div>
  <div class="blog-sequence__step">
    <div class="blog-sequence__message" style="--from: 2; --to: 4;"><strong>User turn</strong><span>Conversation state reaches the harness.</span></div>
  </div>
  <div class="blog-sequence__step">
    <div class="blog-sequence__message blog-sequence__message--harness" style="--from: 3; --to: 5;"><strong>Expose intentions</strong><span>Prompt includes small intent menu, not every schema.</span></div>
  </div>
  <div class="blog-sequence__step">
    <div class="blog-sequence__message blog-sequence__message--model blog-sequence__message--return" style="--from: 3; --to: 5;"><strong>Structured intent</strong><code>{"intent":"search_emails"}</code></div>
  </div>
  <div class="blog-sequence__step">
    <div class="blog-sequence__message blog-sequence__message--harness" style="--from: 3; --to: 5;"><strong>Expose Gmail tools</strong><span>Only the Gmail read subset is made visible.</span></div>
  </div>
  <div class="blog-sequence__step">
    <div class="blog-sequence__message blog-sequence__message--model blog-sequence__message--return" style="--from: 3; --to: 5;"><strong>Exact tool call</strong><code>gmail_list_messages({max_results:3})</code></div>
  </div>
  <div class="blog-sequence__step">
    <div class="blog-sequence__message blog-sequence__message--harness" style="--from: 3; --to: 5;"><strong>Validate policy</strong><span>Schema, scopes, read-only posture, approval rules.</span></div>
  </div>
  <div class="blog-sequence__step">
    <div class="blog-sequence__message blog-sequence__message--server" style="--from: 5; --to: 7;"><strong>Provider request</strong><span>The Gmail MCP server calls the Gmail API.</span></div>
  </div>
  <div class="blog-sequence__step">
    <div class="blog-sequence__message blog-sequence__message--server blog-sequence__message--return" style="--from: 3; --to: 7;"><strong>MCP result</strong><span>Metadata returns to the harness as evidence.</span></div>
  </div>
  <div class="blog-sequence__step">
    <div class="blog-sequence__message blog-sequence__message--harness" style="--from: 3; --to: 5;"><strong>Shape evidence</strong><span>Redact, audit, compact, then send evidence to the model.</span></div>
  </div>
  <div class="blog-sequence__step">
    <div class="blog-sequence__message blog-sequence__message--model blog-sequence__message--return" style="--from: 2; --to: 5;"><strong>Answer</strong><span>The model writes the human-readable response.</span></div>
  </div>
</div>

If a write action appears in the middle of that flow, the harness should pause for preview and approval before execution. The point is not to make the model timid. The point is to keep the model's search space small while keeping side effects under product control.

<figure class="blog-figure blog-figure--wide">
  <img src="{{ 'assets/images/posts/2026/mcp-is-plumbing/staged-tool-narrowing-context-window.png' | relative_url }}" alt="Ninja avatar-minion guiding many available tools through intention, relevant tools, and exact call gates while a context-window meter moves from overloaded to readable." loading="lazy" />
  <figcaption class="blog-figure__caption">The trick is not to show the model every tool. Narrow the search space first, then ask for the exact structured call.</figcaption>
</figure>

Some systems expose all tools directly to the model. For a small demo or a tiny tool ecosystem, that is reasonable. It is simpler, has fewer orchestration steps, and avoids another round trip.

But as the tool ecosystem grows, that simplicity stops being free.

If the model sees hundreds of tools and thousands of schema fields, the context window becomes a dumping ground. The practical answer is hierarchical exposure: choose intention from a small set, expose only the relevant tool subset, then generate the exact structured call.

## Docker MCP Toolkit Is A Manager, Not The Trust Model

This is where my own work made the lesson concrete.

I have been working on a local AI-first solution, and one of the practical questions was how external tools should appear without making the user paste transport commands into a form like a punishment.

The first time the boundary became obvious, the UI could see more than the runtime was willing to use. A manager profile could show external capabilities. A tools page could display them. But that did not mean the model should immediately receive every function behind that profile.

That felt annoying at first, because it made the product look less "connected" than the setup technically was. But the annoyance was useful. It forced the distinction I had been missing.

Docker Desktop's MCP Toolkit is useful here because it gives a manager-like UI around catalogs, profiles, containers, gateway behavior, and credential support. Docker's own docs describe the catalog as a curated collection of <span class="blog-highlight blog-highlight--mcp-server">MCP servers</span> and the gateway as a proxy that handles server lifecycle, routing, and authentication across profiles.

That is useful plumbing.

But it is still plumbing.

The host-side <span class="blog-highlight blog-highlight--harness">harness</span> still has to decide what enters the model-visible manifest.

For example, a Docker MCP profile may make Wikipedia, Gmail, and Slack visible. The host-side <strong>harness</strong> may still choose a much narrower runtime posture:

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

<blockquote class="blog-pullquote blog-pullquote--compact">
  <p><span class="blog-highlight blog-highlight--agent">MCP</span> standardizes connection.</p>
  <p>It does not standardize judgment.</p>
</blockquote>

<figure class="blog-figure blog-figure--wide">
  <img src="{{ 'assets/images/posts/2026/mcp-is-plumbing/docker-mcp-manager.png' | relative_url }}" alt="Hand-drawn ninja avatar-minion connecting selected Docker MCP Manager tools into a model-visible manifest, shown beside Docker Desktop MCP Toolkit catalog and profile screenshots." loading="lazy" />
  <figcaption class="blog-figure__caption">Docker MCP Toolkit can make tools visible, but the host-side harness still decides which functions are routed into the model-visible manifest.</figcaption>
</figure>

If you want the terminal version of creating a Docker MCP profile, assigning catalog servers, and registering the gateway with a client, I moved that into a small companion reference: [Docker MCP Toolkit profile setup]({{ '/references/docker-mcp-manager-profile-setup/' | relative_url }}).

The product point remains the same: a profile registers servers with Docker MCP. It does not make every advertised function safe to route into the model.

## Read-Only Is Not A Vibe

One of the fastest ways to make an assistant feel impressive is to let it touch personal tools.

One of the fastest ways to make it untrustworthy is to blur read and write behavior.

The same Gmail server can make the distinction obvious. *"Summarize my unread email from this morning"* is a read path. The <span class="blog-highlight blog-highlight--mcp-server">MCP server</span> knows how to talk to Gmail, but the host-side <span class="blog-highlight blog-highlight--harness">harness</span> still decides whether the Gmail functions are visible, which result fields come back, and what gets recorded.

*"Reply to Alex and say I will be ten minutes late"* is a different class of action. The system should compose a draft, show the recipient and exact text, wait for approval, and only then send. If the same path treats search and send as merely two advertised functions, the architecture has already lost the important distinction.

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

This is also how I think about local AI-first systems. Local-first does not have to mean offline-only. Gmail, Slack, Calendar, and Search may still be external APIs. The important part is that credentials stay out of prompts and logs, approval state and audit records remain under the user's control, and the host-side <span class="blog-highlight blog-highlight--harness">harness</span> decides what evidence reaches the model.

<figure class="blog-figure blog-figure--wide">
  <img src="{{ 'assets/images/posts/2026/mcp-is-plumbing/read-only-product-policy.png' | relative_url }}" alt="Ninja avatar-minions separating read-only access from write actions, with approval controls, Gmail snippets, calendar events, and policy-before-permission notes." loading="lazy" />
  <figcaption class="blog-figure__caption">Read-only is a product policy, not a hopeful interpretation of a function name. Visibility does not imply permission.</figcaption>
</figure>

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
