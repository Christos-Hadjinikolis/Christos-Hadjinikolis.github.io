---
title: My CV
subtitle: Engineering Manager Snapshot
intro_theme: cv
intro_kicker: "Curated Overview"
intro_summary: "A fast-read view of how I create leverage: managing ML/data teams, live streaming systems, production reliability, developer standards, and standards-facing AI work."
intro_card_title: "In One Frame"
intro_points:
  - "Engineering management"
  - "Streaming-first ML systems"
  - "Standards, reliability, and delivery"
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
      <h3>Engineering Manager for production ML and real-time data systems</h3>
      <p class="page-summary">
        I manage a mixed MLE/DS/DE team and remain close enough to architecture to lead hard technical calls. My work spans live data processing, streaming infrastructure, model evaluation/replay, observability, and the operating discipline needed to turn noisy model behaviour into trustworthy product intelligence.
      </p>
      <ul class="page-pills">
        <li class="page-pill">👥 Team leadership</li>
        <li class="page-pill">⚙️ Kafka + Flink</li>
        <li class="page-pill">🧠 ML operations</li>
        <li class="page-pill">🛰️ Maritime intelligence</li>
        <li class="page-pill">📈 Delivery health</li>
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
          <strong>Manage technical ML/data teams</strong>
          Hiring, 1:1s, mentoring, reviews, progression, onboarding, and delivery governance.
        </li>
        <li>
          <strong>Lead live-processing strategy</strong>
          Post-ingestion streaming systems, Flink/Kafka trade-offs, replayability, monitoring, and failure handling.
        </li>
        <li>
          <strong>Bridge ML and real-world constraints</strong>
          Aligning model output with analyst feedback, product decisions, operational rules, and prediction trust.
        </li>
        <li>
          <strong>Scale delivery systems</strong>
          Standardisation, docs close to code, tests-as-docs, ADRs, DORA/Jira signals, and healthier feedback loops.
        </li>
      </ul>
    </div>
  </section>

  <section class="page-grid">
    <div class="page-panel">
      <h3>🚢 Selected Work</h3>
      <ul class="page-list">
        <li>Real-time vessel destination and ETA prediction systems downstream of 10+ AIS providers.</li>
        <li>Post-ingestion streaming pipelines spanning normalisation, signal quality, ML inference, monitoring, and product enrichment.</li>
        <li>AIS denoising and signal-quality improvement using stateful filtering approaches.</li>
        <li>Event-driven ML architectures with replay/evaluation interfaces, observability, fallback paths, and production rollout discipline.</li>
        <li>Developer-standardisation work that reduced cognitive load and made ML/data delivery patterns repeatable across repositories.</li>
      </ul>
    </div>

    <div class="page-panel">
      <h3>📐 Core Principles</h3>
      <ul class="page-list">
        <li><strong>Production is the only truth.</strong></li>
        <li><strong>If it cannot be measured, it is not done.</strong></li>
        <li><strong>Deterministic systems beat clever hacks.</strong></li>
        <li><strong>Models must degrade gracefully.</strong></li>
        <li><strong>System quality should come through people and process, not heroics.</strong></li>
      </ul>
    </div>

    <div class="page-panel">
      <h3>📚 Career Snapshot</h3>
      <ul class="page-timeline">
        <li><strong>Since 12/2020 · Vortexa, London</strong><br>Engineering Manager / ML Tech Lead managing a five-person MLE/DS/DE pod and live-processing strategy for streaming-first maritime intelligence systems.</li>
        <li><strong>2016–2020 · Data Reply, London</strong><br>Mostly hands-on consulting across Vodafone, CNHi, and UBS, with project-specific team/product leadership at CNHi and platform-shaping work at Vodafone.</li>
        <li><strong>2010–2016 · KCL, UCL, GSM, David Game College</strong><br>Teaching and academic roles across computing, AI, software, and data subjects.</li>
      </ul>
    </div>

    <div class="page-panel">
      <h3>🏛️ Standards & Research</h3>
      <ul class="page-list">
        <li><strong>Since 10/2024 · UCL</strong><br>Associate Researcher working at the intersection of AI and maritime analytics.</li>
        <li><strong>Since 01/2021 · ISO/CEN-CENELEC JTC 21 WG3</strong><br>Committee Expert Member advocating practical AI standards for auditability, model/data versioning, explainability, and safer adoption.</li>
      </ul>
    </div>

    <div class="page-panel">
      <h3>🎙️ Talks & Interviews</h3>
      <ul class="page-list">
        <li><strong>2023</strong> Agile in Action podcast interview on the Vortexa journey and agile data science.</li>
        <li><strong>2022</strong> ODSC talk on <em>dynamicio</em> and abstracting I/O in ML systems.</li>
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
