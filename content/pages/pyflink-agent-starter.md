---
title: PyFlink Starter Archetype
subtitle: A minimal path from article to working scaffold
layout: page
hide: true
permalink: /pyflink-agent-starter.html
intro_theme: experience
intro_kicker: "Starter Page"
intro_summary: "A simple scaffold and agent prompt for readers who want to move from the PyFlink article into a small, Python-first streaming project without guessing the first few structural decisions."
intro_card_title: "What You Get"
intro_points:
  - "Official docs worth opening"
  - "Copy-paste local setup commands"
  - "A practical first agent prompt"
---

<div class="page-shell">
  <section class="page-grid">
    <div class="page-panel">
      <h3>Why This Exists</h3>
      <p class="page-summary">
        The hardest part of trying a new streaming stack is often not the API. It is deciding what the first non-chaotic project shape should look like. This starter is intentionally small and biased toward learning the runtime model early.
      </p>
    </div>

    <div class="page-panel">
      <h3>Open These First</h3>
      <ul class="page-list">
        <li><a href="https://nightlies.apache.org/flink/flink-docs-stable/docs/dev/python/installation/" target="_blank" rel="noopener noreferrer">PyFlink installation</a> for supported Python versions and package install.</li>
        <li><a href="https://nightlies.apache.org/flink/flink-docs-release-2.1/docs/dev/python/datastream/intro_to_datastream_api/" target="_blank" rel="noopener noreferrer">Python DataStream API intro</a> for the basic program shape.</li>
        <li><a href="https://nightlies.apache.org/flink/flink-docs-release-2.1/docs/dev/python/dependency_management/" target="_blank" rel="noopener noreferrer">Python dependency management</a> for shipping Python files, requirements, and archives.</li>
        <li><a href="https://nightlies.apache.org/flink/flink-docs-stable/docs/dev/python/debugging/" target="_blank" rel="noopener noreferrer">PyFlink debugging</a> for local and remote debug patterns.</li>
        <li><a href="https://hub.docker.com/_/flink" target="_blank" rel="noopener noreferrer">Official Flink Docker image</a> if you want a local cluster quickly.</li>
        <li><a href="https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/connectors/datastream/kafka/" target="_blank" rel="noopener noreferrer">Kafka connector docs</a> if your first real job is Kafka-shaped.</li>
      </ul>
    </div>

    <div class="page-panel">
      <h3>Suggested Structure</h3>
      <pre><code>pyflink-starter/
  README.md
  pyproject.toml
  flink_jobs/
    __init__.py
    job.py
    transforms.py
    model_logic.py
  tests/
    test_transforms.py
  docker/
    Dockerfile
  conf/
    local.env
</code></pre>
    </div>

    <div class="page-panel">
      <h3>Local Setup Commands</h3>
      <pre><code>python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install apache-flink==2.2.0

# optional: verify the install
python -c "import pyflink; print('pyflink ok')"
</code></pre>
      <p class="page-note">At the time of writing, the stable installation docs require Python 3.9, 3.10, 3.11, or 3.12.</p>
    </div>

    <div class="page-panel">
      <h3>Local Runtime Option</h3>
      <pre><code>docker network create flink-net

docker run -d --name jobmanager \
  --network flink-net \
  -p 8081:8081 \
  -e JOB_MANAGER_RPC_ADDRESS=jobmanager \
  flink:2.2 jobmanager

docker run -d --name taskmanager \
  --network flink-net \
  -e JOB_MANAGER_RPC_ADDRESS=jobmanager \
  flink:2.2 taskmanager
</code></pre>
      <p class="page-note">This is the quickest way to get a local Flink runtime without pretending the cluster side does not exist.</p>
    </div>

    <div class="page-panel">
      <h3>What To Build First</h3>
      <ul class="page-list">
        <li>Start with one small streaming job that reads a source, applies stateful logic, and emits a sink.</li>
        <li>Keep the model logic replaceable so you can compare native Python execution with a service boundary later.</li>
        <li>Prove local packaging, dependency shipping, and replay behavior before chasing throughput.</li>
      </ul>
    </div>

    <div class="page-panel">
      <h3>First Job Command</h3>
      <pre><code>python flink_jobs/job.py

# once you move to a real cluster, keep dependency shipping explicit
# and treat Python files / requirements / connector JARs as part of the job
</code></pre>
      <p class="page-note">The dependency-management docs matter early because PyFlink becomes operationally confusing exactly when teams treat packaging as an afterthought.</p>
    </div>

    <div class="page-panel">
      <h3>What The Archetype Should Prove</h3>
      <ul class="page-list">
        <li>A small DataStream job can run locally without magical hidden state.</li>
        <li>Python dependencies are explicit and can be shipped deliberately.</li>
        <li>Connector JARs are treated as runtime dependencies, not forgotten later.</li>
        <li>The model logic can stay native Python at first, but the boundary can still be changed later.</li>
      </ul>
    </div>

    <div class="page-panel">
      <h3>Agent Prompt</h3>
      <pre><code>Use the pyflink article as context and create a minimal PyFlink starter project.

Requirements:
- Python-first project layout
- one small DataStream job
- local runnable setup
- clear dependency management
- one testable transform module
- notes on where Java/JAR dependencies still enter the picture
- include a Docker-based local runtime option
- include a README with exact commands
- include one path for native Python model logic and one note on how to swap to a service boundary later

Do not optimize for scale yet.
Optimize for clarity, packaging sanity, and understanding the runtime boundary.
</code></pre>
    </div>

    <div class="page-panel">
      <h3>Useful Tooling</h3>
      <ul class="page-list">
        <li><strong>Python venv</strong> to keep the client-side environment isolated.</li>
        <li><strong>Docker</strong> to make the cluster side visible early instead of delaying it.</li>
        <li><strong>PyCharm / IntelliJ</strong> plus the official PyFlink debugging flow if you want local or remote Python UDF debugging.</li>
        <li><strong>Kafka</strong> only when your first example actually needs it; otherwise start with a smaller source/sink path and add connector JARs later.</li>
      </ul>
    </div>
  </section>
</div>
