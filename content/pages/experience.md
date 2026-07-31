---
title: Professional Experience
subtitle: How the scope evolved
intro_theme: experience
intro_kicker: "Narrative Timeline"
intro_summary: "Not a second CV. This page shows how the scope widened over time: from teaching and research, into consulting under constraints, and then into engineering management for production ML and live data systems."
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
      <h3>From research and teaching to Engineering Management for real-time ML systems</h3>
      <p class="page-summary">
        This page is intentionally not a second CV. It is the story of how the same pattern kept widening: make complex work understandable,
        turn ambiguity into structure, and build the teams, interfaces, and operating models needed to make ML useful in production.
      </p>
      <ul class="page-pills">
        <li class="page-pill">🎓 Research roots</li>
        <li class="page-pill">🏗️ Production ML</li>
        <li class="page-pill">⚙️ Streaming architecture</li>
        <li class="page-pill">👥 Engineering management</li>
        <li class="page-pill">📈 Delivery health</li>
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
          I now focus on team growth, architecture, operational quality, stakeholder alignment, and repeatable delivery systems.
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
              <li><strong>🚜 CNHi:</strong> lead data scientist / Scrum Master for a DS team processing live vehicle sensory data with PySpark to infer maintenance needs.</li>
              <li><strong>📱 Vodafone:</strong> led technical delivery across multiple workstreams, worked on Infinity, a GCP/Kubeflow data-science platform, and built Red Agent, a mobile-network feature-engineering framework.</li>
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
          At Vortexa, the centre of gravity shifted again: from delivering components to owning engineering strategy and delivery for a major client-facing live streaming backend estate, setting operating standards, and leading a 10-person cross-functional team around it.
        </p>
        <div class="experience-columns">
          <div class="experience-mini-panel">
            <h5>What I lead</h5>
            <ul class="page-list">
              <li>A 10-person cross-functional team: 6 MLE/DE/DS, 2 Product, and 2 SMEs.</li>
              <li>Direct management of the MLE/DE/DS core, with indirect leadership across product and domain partners.</li>
              <li>1:1s, reviews, promotion input, hiring, retention, onboarding, sprint reviews, retrospectives, mentoring, and code pairing.</li>
              <li>Hiring and interview loops: developed hiring practices and system design evaluations; hiring manager for 6 roles, 31+ candidates interviewed in that capacity, and 60+ interview loops overall across Data Production staffing; retained the current team fully, with every member recently promoted.</li>
              <li>Team practices that reduce single-person ownership: clearer ownership, pairing, docs close to code, tests-as-docs, and onboarding that makes new joiners productive in production code within their first week.</li>
            </ul>
          </div>
          <div class="experience-mini-panel">
            <h5>What the estate requires</h5>
            <ul class="page-list">
              <li>A client-facing live streaming intelligence estate processing roughly 6M filtered vessel-position records/hour, focused on 13.5K monitored vessels.</li>
              <li>Two-year Kafka Streams-to-Flink transformation strategy, establishing Flink as a future-proofed platform direction aligned with company growth and using its dataflow model, independent state/checkpointing, and operational UI to reduce cognitive load and partition-coupled scaling.</li>
              <li>Monitoring, runbooks, rollback/fallback paths, and Jira alert workflows keeping MTTR under 30 minutes.</li>
              <li>DORA/Jira delivery signals, architecture forums, ADRs, dev containers, Backstage adoption, and local E2E/integration tests to make delivery visible, healthier, faster, and safer; a recent 12-month view showed 14.65 deploys/week and 0.52% change failure.</li>
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
        <li><strong>Since 01/2021 · ISO/CEN-CENELEC JTC 21 WG3</strong><br>Committee Expert Member working on AI standards aligned with international and EU policy directions.</li>
        <li><strong>Since 10/2024 · UCL Department of Information Studies</strong><br>Associate Researcher helping expose students to practical AI applications and lecturing on AI standardisation, the AI Act, auditability, versioning, explainability, and safe adoption.</li>
      </ul>
    </div>

    <div class="page-panel">
      <div class="page-kicker">🎙️ Public Work</div>
      <h3>Talks and interviews</h3>
      <ul class="page-list">
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
        <li><strong>Standards set teams free when they remove avoidable ambiguity.</strong></li>
        <li><strong>Models need auditability, monitoring, and graceful failure paths.</strong></li>
        <li><strong>Healthy delivery needs visible signals, not hidden stress.</strong></li>
        <li><strong>System quality should scale through clear ownership, evidence, and repeatable practice.</strong></li>
      </ul>
    </div>
  </section>
</div>
