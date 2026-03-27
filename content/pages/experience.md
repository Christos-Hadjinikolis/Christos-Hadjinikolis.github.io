---
title: Professional Experience
subtitle: How the scope evolved
layout: "page"
icon: fa-briefcase
order: 3
permalink: /experience.html
---
<div class="page-shell experience-page">
  <section class="page-hero">
    <div class="page-panel page-panel--tinted">
      <div class="page-kicker">🧭 Professional Arc</div>
      <h3>From research and teaching to full ownership of real-time ML systems</h3>
      <p class="page-summary">
        This page is intentionally not a second CV. It is the story of how my scope changed over time: from explaining ideas,
        to building models, to owning the systems, trade-offs, and teams needed to make those models useful in production.
      </p>
      <ul class="page-pills">
        <li class="page-pill">🎓 Research roots</li>
        <li class="page-pill">🏗️ Production systems</li>
        <li class="page-pill">⚙️ Streaming architecture</li>
        <li class="page-pill">👥 Team leadership</li>
        <li class="page-pill">🏛️ Standards work</li>
      </ul>
      <div class="page-actions">
        <a href="{{ '/assets/pdfs/cv.pdf' | relative_url }}" class="button scrolly">View Latest CV</a>
        <a href="{{ '/my-cv.html' | relative_url }}" class="button scrolly">Back to CV Snapshot</a>
      </div>
    </div>

    <div class="page-panel">
      <h3>✨ What Changed Along The Way</h3>
      <ul class="page-rule-list">
        <li>
          <strong>Early years: explaining and teaching</strong>
          I learned to break complex ideas down clearly and help others build confidence in technical subjects.
        </li>
        <li>
          <strong>Consulting years: delivery under ambiguity</strong>
          I learned how messy systems, unclear requirements, and real stakeholder pressure reshape “correct” engineering.
        </li>
        <li>
          <strong>Current years: systems and leverage</strong>
          I now focus on architecture, operational quality, and building teams that can ship dependable ML systems repeatedly.
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
            <h4>🏗️ Consulting became the bridge from data science to ML engineering</h4>
            <div class="experience-role">Data Reply · London, UK</div>
          </div>
          <div class="experience-badge">Data Scientist → ML Engineer</div>
        </div>
        <p class="experience-hook">
          This was the period where “interesting model work” stopped being enough. I had to deal with enterprise constraints,
          legacy systems, production expectations, and the uncomfortable gap between experimentation and deployment.
        </p>
        <div class="experience-columns">
          <div class="experience-mini-panel">
            <h5>Representative client work</h5>
            <ul class="page-list">
              <li><strong>🏦 UBS:</strong> graph analytics, process mining, and real-time insight pipelines with Kafka, Elasticsearch, and Python.</li>
              <li><strong>🚜 CNHi:</strong> time-series forecasting for agricultural vehicles with alerting and deployment paths.</li>
              <li><strong>📱 Vodafone:</strong> internal MLOps platform work on GCP and Kubeflow, with CI/CD, telemetry, and reproducibility.</li>
            </ul>
          </div>
          <div class="experience-mini-panel">
            <h5>What this phase taught me</h5>
            <ul class="page-list">
              <li>Most ML failures are systems failures, not modelling failures.</li>
              <li>Ambiguous environments are where architecture matters most.</li>
              <li>Bridging DS and engineering is a delivery problem as much as a technical one.</li>
            </ul>
          </div>
        </div>
      </article>
    </div>

    <div class="experience-step">
      <div class="experience-era">
        <span class="period">Since 12/2020</span>
        <span class="label">Leadership<br>real-time systems at scale</span>
      </div>
      <article class="experience-card">
        <div class="experience-card-head">
          <div>
            <h4>🚢 Vortexa: owning streaming-first ML systems end to end</h4>
            <div class="experience-role">ML Tech Lead (Staff-Level) · Pod Lead</div>
            <div class="experience-location">London, UK</div>
          </div>
          <div class="experience-badge">Architecture · Delivery · People</div>
        </div>
        <p class="experience-hook">
          At Vortexa, the center of gravity shifted again: from delivering components to owning systems, quality bars, and the teams responsible for keeping them reliable over time.
        </p>
        <div class="experience-columns">
          <div class="experience-mini-panel">
            <h5>What I built</h5>
            <ul class="page-list">
              <li>Destination and ETA systems using transformer-based sequence models with automated refresh and longitudinal evaluation.</li>
              <li>Real-time Kafka/Flink pipelines over global AIS feeds, powering prediction, anomaly triggers, and downstream decision support.</li>
              <li>AIS denoising operators based on Kalman filtering to improve signal quality and downstream model accuracy.</li>
              <li>MLOps foundations around rollout strategy, observability, model versioning, and operational discipline.</li>
            </ul>
          </div>
          <div class="experience-mini-panel">
            <h5>What I own now</h5>
            <ul class="page-list">
              <li>Cross-functional delivery across ML, DS, and DE.</li>
              <li>Hiring, mentoring, roadmap alignment, and execution quality.</li>
              <li>Architecture decisions that account for latency, replayability, and failure modes.</li>
              <li>Raising the bar from “the model works” to “the system can be trusted.”</li>
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
        <li><strong>Since 01/2021 · ISO JTC 21 WG3</strong><br>Committee Expert Member working on AI standards aligned with international and EU policy directions.</li>
        <li><strong>Since 10/2024 · UCL Department of Information Studies</strong><br>Associate Researcher supporting AI application, standardisation, and ethics initiatives.</li>
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
        <li><strong>If it cannot be measured, it is not done.</strong></li>
        <li><strong>Deterministic systems beat clever hacks.</strong></li>
        <li><strong>Models must degrade gracefully.</strong></li>
        <li><strong>System quality should scale through people and process, not heroics.</strong></li>
      </ul>
      <p class="page-note">Guiding principle: “Make it work. Make it right. Make it fast.”</p>
    </div>
  </section>
</div>
