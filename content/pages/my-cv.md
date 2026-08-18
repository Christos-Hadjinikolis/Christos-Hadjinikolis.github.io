---
title: My CV
subtitle: Engineering Manager Snapshot
intro_theme: cv
intro_kicker: "Curated Overview"
intro_summary: "A fast-read view of the same story as the PDF: applied ML systems leadership, research-to-production delivery, model evaluation, reliability, and practical AI standards."
intro_card_title: "What To Remember"
intro_points:
  - "Applied ML teams that turn research-grade models into product systems"
  - "Evaluation, replay, monitoring, and reliability around live ML"
  - "Responsible AI as engineering practice, not slogan"
layout: "page"
icon: fa-id-card
icon_image: assets/images/site/icons/cv.svg
order: 2
permalink: /my-cv.html
---
<div class="page-shell cv-page">
  <section class="page-hero">
    <div class="page-panel page-panel--tinted">
      <div class="page-kicker">🧠 Positioning</div>
      <h3>ML Engineering Manager for applied ML systems and real-time data products</h3>
      <p class="page-summary">
        I lead cross-functional teams that translate research-grade models, noisy data, and ambiguous product requirements into reliable production systems. At Vortexa, that means managing 6 direct reports, leading a 10-person team, and keeping model quality, evaluation, reliability, and stakeholder alignment close to the engineering work.
      </p>
      <ul class="page-pills">
        <li class="page-pill">👥 Team leadership</li>
        <li class="page-pill">🧠 Applied ML systems</li>
        <li class="page-pill">📐 Model eval/replay</li>
        <li class="page-pill">⚙️ Model serving</li>
        <li class="page-pill">🛡️ Client-facing reliability</li>
        <li class="page-pill">🏛️ AI standards</li>
      </ul>
      <div class="page-actions">
        <a href="{{ '/assets/pdfs/cv.pdf' | relative_url }}" class="button scrolly">Download PDF CV</a>
        <a href="{{ '/experience.html' | relative_url }}" class="button scrolly">Open Experience Timeline</a>
      </div>
    </div>

    <div class="page-panel">
      <figure class="page-panel-image page-panel-image--wide">
        <img src="{{ 'assets/images/pages/cv/big-data-london-2018-cv.jpeg' | relative_url }}" alt="Christos Hadjinikolis presenting at Big Data London in 2018" loading="lazy" />
      </figure>
      <h3>🧭 What I Actually Do</h3>
      <ul class="page-rule-list">
        <li>
          <strong>Build and manage technical teams</strong>
          Direct management, hiring, mentoring, reviews, progression, onboarding, delivery accountability, and cross-functional operating rhythm.
        </li>
        <li>
          <strong>Move ML work from research towards production</strong>
          PyTorch sequence/transformer models, model-serving workflows, MLflow, model/data versioning, evaluation gates, replay, and monitoring.
        </li>
        <li>
          <strong>Turn ML ambiguity into operating discipline</strong>
          Batch/online evaluation loops, failure-mode analysis, domain-expert feedback, product semantics, and prediction trust.
        </li>
        <li>
          <strong>Make applied AI systems inspectable</strong>
          Tool boundaries, schema validation, approval gates, durable state, traces, and runtime evidence for humans and LLM-assisted workflows.
        </li>
      </ul>
    </div>
  </section>

  <section class="page-grid">
    <div class="page-panel">
      <h3>📌 Evidence Behind The CV</h3>
      <ul class="page-list">
        <li><strong>People:</strong> manage 6 direct reports across Product, SME analysis, Data Science, and Data Engineering; lead a 10-person cross-functional team accountable for model quality, stakeholder alignment, reliability, and delivery maturity.</li>
        <li><strong>Estate:</strong> own engineering strategy and delivery for a live ML/data estate turning roughly 6M vessel-position records/hour into production intelligence for 13.5K monitored vessels.</li>
        <li><strong>ML delivery:</strong> led 0-to-1 research-to-production delivery for destination and arrival-time sequence/transformer models in PyTorch.</li>
        <li><strong>Evaluation:</strong> established batch/online model-evaluation and replay loops, analysed failure modes with domain experts and Product, and converted findings into model, data, and interface improvements.</li>
        <li><strong>Reliability:</strong> protect production trust through Kafka Streams-to-Flink migration, monitoring, fallback/rollback paths, shared on-call, and MTTR kept under 30 minutes.</li>
      </ul>
    </div>

    <div class="page-panel">
      <h3>🧪 Applied AI & Tooling</h3>
      <ul class="page-list">
        <li><strong><a href="{{ '/2026/08/01/skeleton-replay-runtime-architecture-evidence.html' | relative_url }}">Promet</a>:</strong> private applied GenAI project shaping hands-on work around voice, memory, tool use, streaming interaction, local runtimes, Hugging Face-backed speech assets, schema validation, approval gates, durable state, traces, and replay/evaluation.</li>
        <li><strong><a href="https://pypi.org/project/skeleton-replay/">skeleton-replay</a>:</strong> public Python tooling that turns script/pytest runs into traces, architecture snapshots, workflow evidence, and replayable reports for review, debugging, onboarding, and LLM-assisted code understanding.</li>
        <li><strong><a href="https://plugins.jetbrains.com/plugin/32807-skeleton-replay">Skeleton Replay plugin</a>:</strong> PyCharm/IntelliJ workflow that brings runtime evidence and source navigation into the IDE.</li>
        <li><strong><a href="https://pypi.org/project/dynamicio/">dynamicio</a>:</strong> published PyPI library for making I/O seams and local/dev/prod dataset switching explicit in ML/data workflows.</li>
      </ul>
    </div>

    <div class="page-panel">
      <h3>📚 Career Snapshot</h3>
      <ul class="page-timeline">
        <li><strong>12/2020–present · Vortexa, London</strong><br>Engineering Manager / ML Systems Lead owning engineering strategy and delivery for a live ML/data estate, managing 6 direct reports, and leading a 10-person cross-functional team around model quality, reliability, stakeholder alignment, and delivery maturity.</li>
        <li><strong>04/2016–12/2020 · Data Reply, London</strong><br>Senior Consultant and first London spin-off consultant; grew from data scientist into ML engineer while supporting team growth, client delivery, mentoring, and project leadership across Vodafone, CNHi, and UBS.</li>
        <li><strong>2010–2016 · KCL, UCL, GSM, David Game College</strong><br>Teaching and academic roles across computing, AI, software, and data subjects.</li>
      </ul>
    </div>

    <div class="page-panel">
      <h3>🏛️ Standards & Research</h3>
      <ul class="page-list">
        <li><strong>Since 10/2024 · UCL</strong><br>Associate Researcher helping students connect AI standards, the AI Act, auditability, explainability, and practical AI adoption.</li>
        <li><strong>Since 01/2021 · ISO/CEN-CENELEC JTC 21 WG3</strong><br>Committee Expert Member contributing to AI standards aligned with EU policy and international norms, with emphasis on auditability, model/data versioning, explainability, and safer adoption.</li>
      </ul>
    </div>

    <div class="page-panel">
      <h3>📐 Core Principles</h3>
      <ul class="page-list">
        <li><strong>Production is the only truth.</strong></li>
        <li><strong>Models need evaluation, replay, monitoring, and graceful failure paths.</strong></li>
        <li><strong>Responsible AI is partly an engineering discipline: evidence, auditability, ownership, and human accountability.</strong></li>
        <li><strong>System quality should come through clear ownership, measurable interfaces, and repeatable practice.</strong></li>
      </ul>
    </div>

    <div class="page-panel">
      <h3>🎙️ Talks & Interviews</h3>
      <ul class="page-list">
        <li><strong>2023</strong> Agile in Action podcast interview on the Vortexa journey and agile data science.</li>
        <li><strong>2022</strong> ODSC talk on <a href="https://pypi.org/project/dynamicio/"><em>dynamicio</em></a>, a published PyPI library for abstracting I/O in ML systems.</li>
        <li><strong>2020</strong> iunera interview blog on the agile approach in data science.</li>
        <li><strong>2020</strong> Big Data Warsaw talk on monitoring communication and trade events as graphs.</li>
        <li><strong>2018</strong> Connected Data London panel and Minds Mastering Machines talk.</li>
      </ul>
    </div>

    <div class="page-panel">
      <h3>🎓 Education & Credentials</h3>
      <ul class="page-list">
        <li><strong>Ph.D. in Computer Science · King’s College London</strong><br>Persuasion dialogues, opponent modelling, knowledge graphs, Bayesian techniques, and formal semantics.</li>
        <li><strong>Diploma (BEng) in Computer Engineering · University of Thessaly</strong><br>Polytechnic training with a strong focus on mathematics and artificial intelligence.</li>
        <li><strong>Selected certifications</strong><br>AWS ML Specialty, Google Data Engineer, Process Mining, Graph Analytics for Big Data, Neo4j, and Elasticsearch.</li>
      </ul>
    </div>
  </section>
</div>
