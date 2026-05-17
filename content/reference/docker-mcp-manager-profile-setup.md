---
title: Docker MCP Toolkit Profile Setup
subtitle: A compact CLI reference for creating a Docker MCP profile and wiring it into a client
layout: page
hide: true
permalink: /references/docker-mcp-manager-profile-setup/
intro_theme: experience
intro_kicker: "Reference"
intro_summary: "A short companion page for the MCP article. It keeps Docker MCP profile commands available without turning the post itself into CLI documentation."
intro_card_title: "What This Covers"
intro_points:
  - "Create and inspect a Docker MCP profile"
  - "Add catalog servers to that profile"
  - "Run the Docker MCP Gateway from a client"
robots: noindex, nofollow, noarchive
canonical: false
---

<div class="page-shell">
  <section class="page-grid">
    <div class="page-panel">
      <h3>Why This Exists</h3>
      <p class="page-summary">
        The article argues that Docker MCP Toolkit is useful plumbing, but not the trust model. This page keeps the setup commands nearby for readers who want to try the plumbing without interrupting the main essay.
      </p>
      <p class="page-note">
        You still need Docker Desktop with MCP Toolkit enabled. OAuth-capable servers may also need account authorization in Docker Desktop after they are added to a profile.
      </p>
    </div>

    <div class="page-panel page-panel--wide">
      <h3>Create A Profile</h3>
      <pre><code># Check that the Docker MCP CLI is available.
docker mcp --help

# Create a profile that groups the MCP servers for one workspace.
docker mcp profile create --name promet

# Confirm the profile exists.
docker mcp profile list
docker mcp profile show promet
</code></pre>
    </div>

    <div class="page-panel page-panel--wide">
      <h3>Add Servers</h3>
      <pre><code># Browse the Docker MCP catalog and find the server IDs you want.
docker mcp catalog server ls mcp/docker-mcp-catalog

# Add one or more catalog servers to the profile.
# Replace &lt;server-id&gt; with the ID shown by Docker Desktop or the catalog command.
docker mcp profile server add promet \
  --server catalog://mcp/docker-mcp-catalog/&lt;server-id&gt;

# Check which servers are assigned to the profile.
docker mcp profile server ls --filter profile=promet
</code></pre>
      <p class="page-note">
        A profile groups server configuration. It does not mean every advertised function should be routed into an assistant's model-visible tool manifest.
      </p>
    </div>

    <div class="page-panel page-panel--wide">
      <h3>Run The Gateway</h3>
      <pre><code># Run the gateway for a client that connects over stdio.
docker mcp gateway run --profile promet
</code></pre>
      <p class="page-note">
        Omitting <code>--profile</code> uses Docker MCP's default profile. I prefer naming a profile explicitly when the setup belongs to a specific workspace or assistant.
      </p>
    </div>

    <div class="page-panel page-panel--wide">
      <h3>Manual Client Configuration</h3>
      <pre><code>{
  "servers": {
    "MCP_DOCKER": {
      "command": "docker",
      "args": ["mcp", "gateway", "run", "--profile", "promet"],
      "type": "stdio"
    }
  }
}
</code></pre>
    </div>

    <div class="page-panel page-panel--wide">
      <h3>Supported Named Clients</h3>
      <pre><code>docker mcp client connect &lt;client&gt; --profile promet
</code></pre>
      <p class="page-note">
        For example, Docker documents <code>docker mcp client connect vscode --profile my-project</code> for VS Code.
      </p>
    </div>

    <div class="page-panel">
      <h3>Product Boundary</h3>
      <ul class="page-list">
        <li>Docker MCP can make servers visible and runnable.</li>
        <li>The assistant harness should still decide what becomes model-visible.</li>
        <li>Read-only functions, write actions, approvals, audit, and evidence shaping remain product decisions.</li>
      </ul>
    </div>

    <div class="page-panel">
      <h3>Official References</h3>
      <ul class="page-list">
        <li><a href="https://docs.docker.com/ai/mcp-catalog-and-toolkit/cli/" target="_blank" rel="noopener noreferrer">Docker MCP Toolkit CLI</a></li>
        <li><a href="https://docs.docker.com/ai/mcp-catalog-and-toolkit/profiles/" target="_blank" rel="noopener noreferrer">Docker MCP Profiles</a></li>
      </ul>
    </div>
  </section>
</div>
