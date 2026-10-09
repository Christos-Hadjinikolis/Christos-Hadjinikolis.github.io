---
title: My CV
subtitle: Engineering Manager Snapshot
intro_theme: cv
intro_kicker: "Curated Overview"
intro_summary: "Engineering Manager for production ML and data platforms: people development, technical direction and delivery, with explicit career progression and supported outcomes."
intro_card_title: "What To Remember"
intro_points:
  - "Six direct reports and a ten-person cross-functional team"
  - "Engineering Manager since February 2022; industry experience since 2016"
  - "Team development, faster delivery feedback and reliable production ML"
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
      <h3>Engineering Manager for production ML and data platforms</h3>
      <p class="page-summary">
        I manage six direct reports and lead a ten-person cross-functional team at Vortexa, with responsibility for people development, technical direction and delivery. I became Engineering Manager in February 2022 after joining as a Senior ML Engineer in December 2020. My teams turn research and complex data into reliable products.
      </p>
      <ul class="page-pills">
        <li class="page-pill">👥 Team leadership</li>
        <li class="page-pill">🧠 Applied ML systems</li>
        <li class="page-pill">🌱 People development</li>
        <li class="page-pill">🧭 Technical direction</li>
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
          Manage six direct reports, coach colleagues, run performance and career reviews, and set delivery priorities with a ten-person cross-functional team.
        </li>
        <li>
          <strong>Move ML work from research towards production</strong>
          Led delivery of destination and arrival-time models, with versioning, deployment, evaluation and monitoring so the team can improve production predictions.
        </li>
        <li>
          <strong>Agree priorities across disciplines</strong>
          Bring engineers, Product and domain experts together to resolve competing definitions of model quality and turn them into measurable objectives and prioritised work.
        </li>
        <li>
          <strong>Help teams deliver with confidence</strong>
          Make changes easier to test and review, share architecture decisions, and reduce dependence on individual experts.
        </li>
      </ul>
    </div>
  </section>

  <section class="page-grid">
    <div class="page-panel">
      <h3>📌 Evidence Behind The CV</h3>
      <ul class="page-list">
        <li><strong>People:</strong> manage six direct reports and lead a ten-person cross-functional team. Retained the full team and supported every member’s promotion or progression in the July 2026 team snapshot.</li>
        <li><strong>Hiring and growth:</strong> hiring manager for six roles over time; shaped hiring, system-design interviews, onboarding and mentoring as Data Production grew from four to more than thirty people.</li>
        <li><strong>Delivery:</strong> cut a three-hour pipeline development feedback loop to under five minutes through local end-to-end tests and reusable data-access patterns.</li>
        <li><strong>Estate:</strong> own engineering strategy and delivery for a live ML/data estate turning roughly 6M vessel-position records/hour into production intelligence for 13.5K monitored vessels.</li>
        <li><strong>ML delivery:</strong> led 0-to-1 research-to-production delivery for destination and arrival-time sequence/transformer models in PyTorch.</li>
        <li><strong>Evaluation:</strong> established batch/online model-evaluation and replay loops, analysed failure modes with domain experts and Product, and converted findings into model, data, and interface improvements.</li>
        <li><strong>Platform direction:</strong> led the Kafka Streams-to-Flink migration, enabling compute scaling independent of Kafka partitioning and improving operational visibility and maintainability; established shared on-call, runbooks and rollback/fallback practices.</li>
      </ul>
    </div>

    <div class="page-panel">
      <h3>🧪 Applied AI & Tooling</h3>
      <ul class="page-list">
        <li><strong><a href="{{ '/2026/08/01/skeleton-replay-runtime-architecture-evidence.html' | relative_url }}">Promet</a>:</strong> personal project exploring local AI assistant runtimes, voice, tool execution, approval boundaries, durable state and trace/replay workflows.</li>
        <li><strong><a href="https://pypi.org/project/skeleton-replay/">skeleton-replay</a>:</strong> public Python tooling that turns script/pytest runs into traces, architecture snapshots, workflow evidence, and replayable reports for review, debugging, onboarding, and LLM-assisted code understanding.</li>
        <li><strong><a href="https://plugins.jetbrains.com/plugin/32807-skeleton-replay">Skeleton Replay plugin</a>:</strong> PyCharm/IntelliJ workflow that brings runtime evidence and source navigation into the IDE.</li>
        <li><strong><a href="https://pypi.org/project/dynamicio/">dynamicio</a>:</strong> Python library for explicit data-access boundaries and schema validation, used across 15+ repositories to support local testing and reusable ML/data workflows.</li>
      </ul>
    </div>

    <div class="page-panel">
      <h3>📚 Career Snapshot</h3>
      <ul class="page-timeline">
        <li><strong>02/2022–present · Vortexa, London</strong><br>Engineering Manager / ML Systems Lead: six direct reports, a ten-person cross-functional team, and responsibility for people development, technical direction and delivery.</li>
        <li><strong>12/2020–02/2022 · Vortexa, London</strong><br>Senior ML Engineer, before progressing into engineering management.</li>
        <li><strong>04/2016–12/2020 · Data Reply, London</strong><br>Senior Consultant and first London spin-off consultant; grew from data scientist into ML engineer while supporting team growth, client delivery, mentoring, and project leadership across Vodafone, CNHi, and UBS.</li>
        <li><strong>2010–2016 · KCL, UCL, GSM, David Game College</strong><br>Teaching and academic roles across computing, AI, software, and data subjects.</li>
      </ul>
    </div>

    <div class="page-panel">
      <h3>🏛️ Standards & Research</h3>
      <ul class="page-list">
        <li><strong>Since 10/2024 · UCL</strong><br>Associate Researcher helping students connect AI standards, the AI Act, auditability, explainability, and practical AI adoption.</li>
        <li><strong>Since 2021 · ISO/CEN-CENELEC JTC 21 WG3</strong><br>Committee Expert Member contributing to AI standards aligned with EU policy and international norms, with emphasis on auditability, model/data versioning, explainability, and safer adoption.</li>
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
        <li><strong>Selected historical credentials</strong><br>AWS Machine Learning Specialty (2020), Google Professional Data Engineer (2017), Apache Spark Developer (2016).</li>
      </ul>
    </div>
  </section>
</div>
