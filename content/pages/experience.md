---
title: Professional Experience
subtitle: How the scope evolved
intro_theme: experience
intro_kicker: "Narrative Timeline"
intro_summary: "Not a second CV. This page shows how the work widened over time: from teaching and research, into consulting under constraints, and then into engineering management for production ML and live data systems."
intro_card_title: "What This Page Tracks"
intro_points:
  - "How the scope changed"
  - "What each phase taught me"
  - "Why production became the center"
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
        This page is intentionally not a second CV. It is the story of how my scope changed over time: from explaining ideas,
        to building models, to managing the people, systems, trade-offs, and stakeholder interfaces needed to make those models useful in production.
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
          I learned how messy systems, unclear requirements, product pressure, and client constraints reshape “correct” engineering.
        </li>
        <li>
          <strong>Current years: management and leverage</strong>
          I now focus on architecture, operational quality, team growth, stakeholder alignment, and repeatable delivery systems.
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
        <span class="period">2016–2020</span>
        <span class="label">Consulting<br>shipping under constraints</span>
      </div>
      <article class="experience-card">
        <div class="experience-card-head">
          <div>
            <h4>🏗️ Consulting became the bridge from data science to technical leadership</h4>
            <div class="experience-role">Data Reply</div>
            <div class="experience-location">London, UK</div>
          </div>
          <div class="experience-badge">Data Scientist → ML Engineer</div>
        </div>
        <p class="experience-hook">
          This was the period where “interesting model work” stopped being enough. I had to deal with enterprise constraints,
          legacy systems, production expectations, product backlogs, and the uncomfortable gap between experimentation and deployment.
        </p>
        <div class="experience-columns">
          <div class="experience-mini-panel">
            <h5>Representative client work</h5>
            <ul class="page-list">
              <li><strong>🏦 UBS:</strong> graph analytics, process mining, and real-time insight pipelines with Kafka, Elasticsearch, and Python; later the sole embedded Data Reply consultant.</li>
              <li><strong>🚜 CNHi:</strong> lead data scientist / Scrum Master for a DS team processing live vehicle sensory data with PySpark to infer maintenance needs.</li>
              <li><strong>📱 Vodafone:</strong> worked on Infinity, a GCP/Kubeflow data-science platform, and built Red Agent, a mobile-network feature-engineering framework.</li>
            </ul>
          </div>
          <div class="experience-mini-panel">
            <h5>What this phase taught me</h5>
            <ul class="page-list">
              <li>Most ML failures are systems failures, not modelling failures.</li>
              <li>Ambiguous environments are where architecture and product discipline matter most.</li>
              <li>Bridging DS, engineering, and product is a delivery problem as much as a technical one.</li>
              <li>Good managers create feedback loops that help specialists do their best work.</li>
            </ul>
          </div>
        </div>
      </article>
    </div>

    <div class="experience-step">
      <div class="experience-era">
        <span class="period">Since 12/2020</span>
        <span class="label">Management<br>teams, systems, reliability</span>
      </div>
      <article class="experience-card">
        <div class="experience-card-head">
          <div>
            <h4>🚢 Vortexa: managing teams and live ML/data systems at scale</h4>
            <div class="experience-role">Engineering Manager / ML Tech Lead · Pod Lead</div>
            <div class="experience-location">London, UK</div>
          </div>
          <div class="experience-badge">Architecture · Delivery · People</div>
        </div>
        <p class="experience-hook">
          At Vortexa, the center of gravity shifted again: from delivering components to owning the live streaming intelligence estate, a major client-facing part of the company's backend platform, setting operating standards, and leading a 10-person cross-functional team around it.
        </p>
        <div class="experience-columns">
          <div class="experience-mini-panel">
            <h5>What I lead</h5>
            <ul class="page-list">
              <li>A 10-person cross-functional team: 6 MLE/DE/DS, 2 Product, and 2 SMEs.</li>
              <li>Direct management of the MLE/DE/DS core, with indirect leadership across product and domain partners.</li>
              <li>1:1s, reviews, promotion input, hiring, retention, onboarding, sprint reviews, retrospectives, mentoring, and code pairing.</li>
              <li>Hiring and interview loops: developed hiring practices and system design evaluations; 5 senior DS/DE hires, 31 candidate evaluations, graduate mentoring, and intern management.</li>
              <li>Team practices that reduce single-person ownership: clearer ownership, pairing, docs close to code, tests-as-docs, and new joiners raising PRs within a week.</li>
            </ul>
          </div>
          <div class="experience-mini-panel">
            <h5>What the estate requires</h5>
            <ul class="page-list">
              <li>A client-facing live streaming intelligence estate processing roughly 6M filtered vessel-position records/hour, focused on 13.5K monitored vessels.</li>
              <li>Two-year Kafka Streams-to-Flink transformation strategy, establishing Flink as a future-proofed platform direction aligned with company growth and using its dataflow model, independent state/checkpointing, and operational UI to reduce cognitive load and partition-coupled scaling.</li>
              <li>Monitoring, runbooks, rollback/fallback paths, and Jira alert workflows keeping MTTR under 30 minutes.</li>
              <li>DORA metrics, architecture forums, ADRs, dev containers, Backstage adoption, and DynamicIO data contracts/SLAs to make delivery healthier, faster, and safer.</li>
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
        <li><strong>2022 · ODSC</strong><br>Industry talk on <em>dynamicio</em> and abstracting I/O for ML systems.</li>
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
      <p class="page-note">Guiding principle: “Make it work. Make it right. Make it fast.”</p>
    </div>
  </section>
</div>
