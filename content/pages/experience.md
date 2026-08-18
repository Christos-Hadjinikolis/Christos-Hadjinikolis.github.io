---
title: Professional Experience
subtitle: How the scope evolved
intro_theme: experience
intro_kicker: "Narrative Timeline"
intro_summary: "Not a second CV. This page shows how the scope widened over time: from teaching and research, into consulting under constraints, and then into engineering management for applied ML systems, model evaluation, reliability, and live data products."
intro_card_title: "What This Page Tracks"
intro_points:
  - "How the scope changed"
  - "What each phase taught me"
  - "Why reliable production systems became the centre"
layout: "page"
icon: fa-briefcase
icon_image: assets/images/site/icons/experience.svg
order: 3
permalink: /experience.html
---
<div class="page-shell experience-page">
  <section class="page-hero">
    <div class="page-panel page-panel--tinted">
      <div class="page-kicker">🧭 Professional Arc</div>
      <h3>From research and teaching to Engineering Management for applied ML systems</h3>
      <p class="page-summary">
        This page is intentionally not a second CV. It is the story of how the same pattern kept widening: make complex work understandable,
        turn ambiguity into structure, and build the teams, interfaces, evaluation loops, and operating models needed to make ML useful in production.
      </p>
      <ul class="page-pills">
        <li class="page-pill">🎓 Research roots</li>
        <li class="page-pill">🏗️ Production ML</li>
        <li class="page-pill">📐 Model eval/replay</li>
        <li class="page-pill">⚙️ Streaming architecture</li>
        <li class="page-pill">👥 Engineering management</li>
        <li class="page-pill">🏛️ Standards work</li>
      </ul>
      <div class="page-actions">
        <a href="{{ '/assets/pdfs/cv.pdf' | relative_url }}" class="button scrolly">View Latest CV</a>
        <a href="{{ '/my-cv.html' | relative_url }}" class="button scrolly">Back to CV Snapshot</a>
      </div>
    </div>

    <div class="page-panel">
      <figure class="page-panel-image page-panel-image--portrait">
        <img src="{{ 'assets/images/pages/experience/big-data-london-2018-experience.jpeg' | relative_url }}" alt="Christos Hadjinikolis speaking at Big Data London in 2018" loading="lazy" />
      </figure>
      <h3>✨ What Changed Along The Way</h3>
      <ul class="page-rule-list">
        <li>
          <strong>Early years: explaining and teaching</strong>
          I learned to break complex ideas down clearly and help others build confidence in technical subjects.
        </li>
        <li>
          <strong>Consulting years: delivery under ambiguity</strong>
          I learned how messy systems, unclear requirements, product pressure, and client constraints reshape "correct" engineering.
        </li>
        <li>
          <strong>Current years: management and leverage</strong>
          I now focus on people leadership, research-to-production ML delivery, evaluation loops, operational quality, stakeholder alignment, and repeatable delivery systems.
        </li>
      </ul>
    </div>
  </section>

  <section class="experience-story">
    <div class="experience-step">
      <div class="experience-era">
        <span class="period">2010–2016</span>
        <span class="label">Foundations<br>teaching, research, communication</span>
      </div>
      <article class="experience-card">
        <div class="experience-card-head">
          <div>
            <h4>🎓 Teaching, doctoral work, and the habit of clarity</h4>
            <div class="experience-role">KCL · UCL · GSM · David Game College</div>
          </div>
          <div class="experience-badge">Associate Lecturer · Coding Teacher · TA</div>
        </div>
        <p class="experience-hook">
          Before I was responsible for production systems, I spent years teaching and researching, which is where I developed
          the habit of explaining difficult ideas simply and structuring technical work carefully.
        </p>
        <div class="experience-columns">
          <div class="experience-mini-panel">
            <h5>What I was doing</h5>
            <ul class="page-list">
              <li>Teaching Java, Python, MATLAB, HTML, CSS, SQL, AI, systems, and data structures.</li>
              <li>Completing doctoral research in persuasion dialogues, opponent modelling, and large knowledge graphs.</li>
              <li>Working close to formal methods, graph reasoning, and research-driven problem solving.</li>
            </ul>
          </div>
          <div class="experience-mini-panel">
            <h5>What stayed with me</h5>
            <ul class="page-list">
              <li>Technical communication is a force multiplier.</li>
              <li>Good systems thinking starts with clean abstractions.</li>
              <li>Explaining something clearly is often the best test of understanding it.</li>
            </ul>
          </div>
        </div>
        <figure class="experience-artifact">
          <a class="experience-artifact-media" href="{{ '/assets/pdfs/ijcai-2013-opponent-modelling-poster.pdf' | relative_url }}">
            <img src="{{ 'assets/images/pages/experience/ijcai-2013-opponent-modelling-poster.png' | relative_url }}" alt="IJCAI 2013 poster for opponent modelling research by Christos Hadjinikolis" loading="lazy" />
          </a>
          <figcaption>
            <strong>IJCAI 2013 Best Poster Award</strong>
            <span>Ph.D. poster on opponent modelling and persuasion dialogues. <a href="{{ '/assets/pdfs/ijcai-2013-opponent-modelling-poster.pdf' | relative_url }}">Open the full poster PDF</a>.</span>
          </figcaption>
        </figure>
      </article>
    </div>

    <div class="experience-step">
      <div class="experience-era">
        <span class="period">04/2016–12/2020</span>
        <span class="label">Consulting<br>shipping under constraints</span>
      </div>
      <article class="experience-card">
        <div class="experience-card-head">
          <div>
            <h4>🏗️ Consulting became the bridge from data science to technical leadership</h4>
            <div class="experience-role">Data Reply</div>
            <div class="experience-location">London, UK</div>
          </div>
          <div class="experience-badge">Data Scientist → ML Engineer → Senior Consultant</div>
        </div>
        <p class="experience-hook">
          This was the period where model work became inseparable from delivery discipline. I joined the London spin-off as its first consultant,
          grew into a Senior Consultant, helped the team scale, and learned to turn enterprise constraints, client goals, and production
          expectations into deliverable ML/data systems.
        </p>
        <div class="experience-columns">
          <div class="experience-mini-panel">
            <h5>Representative client work</h5>
            <ul class="page-list">
              <li><strong>Client delivery:</strong> led client meetings, scoped goals, facilitated technical delivery, placed consultants, interviewed, mentored, and contributed to Data Reply's growth from a small founding team to 30+ consultants.</li>
              <li><strong>🏦 UBS:</strong> graph analytics, process mining, and real-time insight pipelines with Kafka, Elasticsearch, and Python; learned XP/pairing practices and later became the sole embedded Data Reply consultant.</li>
              <li><strong>🚜 CNHi:</strong> lead data scientist / Scrum Master for predictive maintenance on Azure/Databricks, translating stakeholder needs into a DS/DE backlog and guiding a PySpark team over live telemetry.</li>
              <li><strong>📱 Vodafone:</strong> led technical delivery across multiple workstreams, worked on Infinity, a GCP data-science platform based on Kubeflow, and built Red Agent, a mobile-network feature-engineering framework.</li>
            </ul>
          </div>
          <div class="experience-mini-panel">
            <h5>What this phase taught me</h5>
            <ul class="page-list">
              <li>Most ML failures are systems failures, not modelling failures.</li>
              <li>Ambiguous environments are where architecture and product discipline matter most.</li>
              <li>Bridging DS, engineering, and product is a delivery problem as much as a technical one.</li>
              <li>Good managers create feedback loops that make specialists faster, safer, and less dependent on individual memory.</li>
            </ul>
          </div>
        </div>
      </article>
    </div>

    <div class="experience-step">
      <div class="experience-era">
        <span class="period">12/2020–present</span>
        <span class="label">Management<br>teams, systems, reliability</span>
      </div>
      <article class="experience-card">
        <div class="experience-card-head">
          <div>
            <h4>🚢 Vortexa: managing teams and live ML/data systems at scale</h4>
            <div class="experience-role">Engineering Manager / ML Systems Lead</div>
            <div class="experience-location">London, UK</div>
          </div>
          <div class="experience-badge">Architecture · Delivery · People</div>
        </div>
        <p class="experience-hook">
          At Vortexa, the centre of gravity shifted again: from delivering components to owning engineering strategy and delivery for a live ML/data estate, setting operating standards, managing 6 direct reports, and leading a 10-person cross-functional team around model quality, reliability, stakeholder alignment, and delivery maturity.
        </p>
        <div class="experience-columns">
          <div class="experience-mini-panel">
            <h5>What I lead</h5>
            <ul class="page-list">
              <li>6 direct reports across Product, SME analysis, Data Science, and Data Engineering, plus leadership of a 10-person cross-functional team.</li>
              <li>Performance and career development, hiring for 6 roles, delivery accountability, sprint reviews, retrospectives, mentoring, and code pairing.</li>
              <li>Workshops across Product, SMEs, analysts, and engineers to turn model-quality disputes into shared definitions, measurable objectives, interface/SLA proposals, and OKR-linked workstreams.</li>
              <li>Team practices that reduce single-person ownership: clearer ownership, pairing, docs close to code, tests-as-docs, and onboarding that makes new joiners productive in production code quickly.</li>
            </ul>
          </div>
          <div class="experience-mini-panel">
            <h5>What the estate requires</h5>
            <ul class="page-list">
              <li>A live ML/data estate processing roughly 6M vessel-position records/hour into production intelligence for 13.5K monitored vessels.</li>
              <li>0-to-1 research-to-production delivery for destination and arrival-time sequence/transformer models in PyTorch.</li>
              <li>MLflow, model/data versioning, automated evaluation gates, replay, monitoring, and model-serving workflows.</li>
              <li>Batch/online model-evaluation and replay loops; failure-mode analysis with domain experts and Product to drive model, data, and interface improvements.</li>
              <li>Kafka Streams-to-Flink as a strategic platform move, with signal-quality controls, rollback/fallback paths, shared on-call, and MTTR under 30 minutes.</li>
              <li>Data contracts, repo archetypes, AWS CodeArtifact publishing, ADRs, dev containers, and local E2E tests to reduce ambiguity and improve delivery feedback loops.</li>
            </ul>
          </div>
        </div>
      </article>
    </div>
  </section>

  <section class="experience-bottom">
    <div class="page-panel">
      <div class="page-kicker">🏛️ Beyond The Core Role</div>
      <h3>Standards and research</h3>
      <ul class="page-list">
        <li><strong>Since 01/2021 · ISO/CEN-CENELEC JTC 21 WG3</strong><br>Committee Expert Member contributing to AI standards aligned with EU policy and international norms, including auditability, model/data versioning, explainability, and safer adoption.</li>
        <li><strong>Since 10/2024 · UCL Department of Information Studies</strong><br>Associate Researcher helping expose students to practical AI applications and lecturing on AI standardisation, the AI Act, auditability, versioning, explainability, and safe adoption.</li>
      </ul>
    </div>

    <div class="page-panel">
      <div class="page-kicker">🎙️ Public Work</div>
      <h3>Talks and interviews</h3>
      <ul class="page-list">
        <li><strong>2026 · Skeleton runtime evidence</strong><br>Published <a href="{{ '/2026/08/01/skeleton-replay-runtime-architecture-evidence.html' | relative_url }}">a public article on Promet, Skeleton, runtime evidence, and the harness around applied GenAI systems</a>.</li>
        <li><strong>2026 · skeleton-replay</strong><br>Published <a href="https://pypi.org/project/skeleton-replay/"><em>skeleton-replay</em></a> and a JetBrains plugin for turning Python runs into traces, architecture snapshots, workflow evidence, and replayable reports.</li>
        <li><strong>2023 · Agile in Action</strong><br>Podcast interview on agile data science and the Vortexa journey.</li>
        <li><strong>2022 · ODSC</strong><br>Industry talk on <a href="https://pypi.org/project/dynamicio/"><em>dynamicio</em></a>, a published PyPI library for abstracting I/O in ML systems.</li>
        <li><strong>2020 · iunera & Big Data Warsaw</strong><br>Interview and conference talk on agile data science and graph-driven analytics.</li>
        <li><strong>2018 · Connected Data London & Minds Mastering Machines</strong><br>Panel and talk appearances on graph AI and doing data science the agile way.</li>
      </ul>
    </div>

    <div class="page-panel">
      <div class="page-kicker">📐 Through-Line</div>
      <h3>What has remained constant</h3>
      <ul class="page-list">
        <li><strong>Production is the only truth.</strong></li>
        <li><strong>Models need evaluation, replay, monitoring, and graceful failure paths.</strong></li>
        <li><strong>Responsible AI is partly engineering work: auditability, explainability, ownership, and human accountability.</strong></li>
        <li><strong>Standards set teams free when they remove avoidable ambiguity.</strong></li>
        <li><strong>System quality should scale through clear ownership, evidence, and repeatable practice.</strong></li>
      </ul>
    </div>
  </section>
</div>
