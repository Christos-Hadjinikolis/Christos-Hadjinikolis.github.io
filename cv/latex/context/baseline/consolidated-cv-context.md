# Consolidated CV Context

Purpose: single working context file for CV tailoring, role-fit analysis, cover letters, recruiter notes, and interview preparation.

Last consolidated: 2026-06-10

## Source Files

- `cv/latex/cv.tex`: canonical two-page CV source.
- Former `cv/latex/context/vortexa.md`: raw career-impact notes, originally written around January 2024 and extended with later notes; consolidated here and removed.
- `content/pages/experience.md`: public narrative timeline for the website.
- Existing role variants under `cv/latex/variants/*/_role-context/`: prior fit assessments and positioning choices.

Use this document as orientation, not as a substitute for factual checking. Before adding a claim to the CV, confirm that it is supported by the source CV, the raw context note, or direct user confirmation.

## Current Positioning

Christos Hadjinikolis is a Staff-level ML Tech Lead / Pod Lead with 16 years of combined industry and academic experience across AI research, production ML systems, MLOps, distributed data infrastructure, and technical leadership.

The strongest market positioning is:

- Staff / Principal Machine Learning Engineer
- Staff / Principal ML Platform Engineer
- ML Systems / AI Infrastructure Lead
- Applied AI / Decisioning Platform Lead
- Head-of-ML or Director-track roles where the scope values technical leadership, platform maturity, and production ML delivery more than pure people-management scale
- LLM systems / applied AI engineering roles where the differentiator is building the harness around model behaviour rather than claiming frontier-model research depth

The current evidence is strongest for hands-on technical leadership, cross-functional delivery, production ML systems, and applied LLM systems engineering. It is weaker for formal manager-of-managers scope, large budget ownership, large org ownership, and direct frontier LLM alignment work unless the user supplies additional evidence.

## Core Narrative

The through-line is the shift from research and teaching into production AI systems, then into architecture, platform ownership, and team-level leverage.

Key message:

> I build and lead reliable ML systems that move advanced modelling work from experimentation into trusted production behaviour.

Supporting themes:

- Production is the center of the profile.
- Strong bridge between data science, ML engineering, data engineering, and backend services.
- Repeated work on model lifecycle, observability, rollout safety, streaming architecture, and decision support.
- Comfortable operating across ambiguous systems with legacy debt, operational constraints, and cross-team dependencies.
- Technical communication and mentoring are recurring strengths from teaching, doctoral work, consulting, and pod leadership.
- AI governance and standardisation are differentiators through ISO/JTC 21 and UCL research/teaching on practical AI standardisation, the AI Act, auditability, explainability, and safe adoption. Do not default this positioning to maritime analytics except in specialised maritime variants.
- The standards thesis should be explicit: advocate auditability, model/data versioning, prediction tracking, explainability, and standards that make safe AI adoption attractive to companies.

## Master CV Snapshot

Current headline:

- ML Tech Lead (Staff-Level) at Vortexa Ltd | Ph.D.
- Committee Expert Member at JTC'21

Current summary emphasis:

- 16 years of combined industry and academic experience designing and deploying large-scale AI systems.
- Recent focus on real-time inference pipelines, event-driven architectures, and scalable backend services for ML-driven products.
- Built and maintain systems that expose model APIs, stream predictions, and support continuous feedback loops.
- Comfortable across research and production.
- Track record in robust, observable, maintainable AI infrastructure.

Current visible technical stack:

- Languages: Java, Kotlin, Python, SQL, Cypher.
- Cloud: AWS, GCP.
- MLOps / orchestration: Airflow, MLflow, KubeVela.
- Data / streaming: Spark, Flink, Kafka, Elasticsearch, polars, pandas.
- ML: time series, graph analytics, forecasting, model evaluation.
- Engineering: CI/CD, Docker, FastAPI, model/data versioning, monitoring.

## Vortexa Context

Dates:

- Joined Vortexa in December 2020.
- Current role in CV: ML Tech Lead (Staff-Level) | Pod Lead.

Public/current CV framing:

- Leads design and delivery of real-time ML systems for maritime forecasting.
- Focus areas include destination-prediction services, streaming data infrastructure, and scalable deployment workflows.
- Helped standardise pipelines, improve observability, and reduce latency across services.

### Core Vortexa Domains

Use these domains when tailoring CVs or cover notes.

#### Real-Time ML and Inference Services

Evidence:

- Delivered backend APIs for model serving with versioning, switch-over logic, and logging.
- Designed services for resilience and auditability in a regulated environment.
- Introduced fallback mechanisms, health checks, and minimal-downtime release paths for continuously operating prediction services.
- Built out training/inference workflows with CI/CD and online evaluation tools.
- Delivered destination-model-as-a-service work through Ithaca.
- Supported waiting-time / ETA modelling through Chronos.

Useful phrasing:

- Production ML services with auditability, fallback paths, and versioned rollout.
- Real-time inference systems for customer-facing intelligence.
- Research-to-production ownership for model services.
- ML systems that degrade gracefully rather than failing silently.

Avoid unless confirmed:

- Claims of global-scale consumer traffic.
- Claims of formal SLO ownership or incident-command responsibility unless the user confirms.
- Claims of model-serving tools not present in evidence, such as Triton, Ray Serve, or KServe.

#### Streaming and Event-Driven Architecture

Evidence:

- Introduced/scaled Flink to move stream processing toward a framework-driven dataflow model, reducing code complexity, maintenance effort, and Kafka partition-coupled scaling limits.
- Designed Kafka/Flink pipelines supporting near real-time model updates and downstream triggers across 15+ ETL components.
- Led or helped lead adoption of Flink as a primary stream-processing framework.
- Worked with Kafka Streams / Java / Kotlin through Autobahn and voyage destination updates.
- Initiated mentorship / training around event-driven processing, Flink, and Kafka Streams.
- Current notes say he is leading the transition to an event-driven architecture, including strategy and cross-team collaboration.

Useful phrasing:

- Event-driven ML architecture.
- Near real-time enrichment and prediction pipelines.
- Stateful stream-processing strategy.
- Streaming foundations for low-latency ML decision support.

Avoid unless confirmed:

- Exact latency numbers.
- Claims of full company-wide ownership if the scope was team or cross-team influence.

#### Destination Intelligence

Systems and concepts referenced:

- Homework
- Ithaca
- Chronos
- Destination prediction
- Waiting-time / ETA prediction
- LNG prediction quality
- Sanctioned destination rules
- Pathfinder integration
- Fixture-aware predictions
- Hysteresis / prediction stability

Evidence:

- Took over a legacy destination-model repository with poor documentation and complex business logic.
- Delivered destination prediction as a service.
- Improved processing speed, latency, and throughput according to raw context.
- Addressed LNG prediction inaccuracy.
- Tackled spikes in waiting-time predictions through a new model.
- Implemented rules to control sanctioned destinations for regulatory/compliance alignment.

Useful phrasing:

- Led productionisation of model services for destination and arrival prediction.
- Improved prediction stability, operational reliability, and customer-facing intelligence.
- Balanced ML automation with compliance-sensitive business rules.

Avoid unless confirmed:

- Hard accuracy gains.
- Revenue/customer-retention claims.
- Regulatory ownership beyond implementing compliance-aligned logic.

#### Voyage Intelligence

Systems and concepts referenced:

- Bon Voyage
- Voyage generation
- Voyage publishing
- Voyage enrichment
- Voyage destination updates
- Autobahn

Evidence:

- Productionised voyage generation work into Bon Voyage.
- Identified and addressed I/O bottlenecks across Python and Airflow repositories.
- Delivered voyage destination updates in a Java/Kotlin Kafka Streams repository.
- Implemented monitoring in Bon Voyage and Autobahn.
- Resolved production bottlenecks and bugs.

Useful phrasing:

- Productionised voyage generation and publishing pipelines.
- Modernised data access and observability around voyage intelligence.
- Bridged Python ML workflows and JVM stream-processing systems.

#### AIS Data Quality and Signal Processing

Systems and concepts referenced:

- AIS signal processing.
- Kalman filtering.
- Contested-water signal quality.
- ML-based noise filtering.
- AIS source evaluation, including JDS, TOTO, Jade, and others.

Evidence:

- Public experience page states work on AIS denoising operators based on Kalman filtering.
- Raw notes say he pushed innovation around Kalman Filter work in R&D.
- Consolidated notes previously stated support/sponsorship of AIS source evaluations and signal-quality investigations; treat those as useful but verify before using externally.

Useful phrasing:

- Improved signal quality feeding downstream prediction systems.
- Supported data-quality initiatives for noisy real-world vessel telemetry.
- Applied filtering and quality-control thinking to streaming ML inputs.

Avoid unless confirmed:

- Claiming sole ownership of Kalman filter productionisation.
- Specific measured accuracy improvements.

#### DynamicIO and Python Ecosystem Modernisation

Evidence:

- Created DynamicIO, a Python library for abstracting I/O.
- DynamicIO became used across 15+ repositories according to raw context and public talk history.
- Used DynamicIO to decouple I/O from business logic, create seams for local tests based on characteristic sample data, define cross-team/domain-owner/system SLAs through schema and data validations, and shorten feedback loops without repeatedly exercising long-running DAGs in DEV; one 3-hour DAG path could be sufficiently tested locally in under 5 minutes.
- In high-level CV copy, DynamicIO does not always need to be named; the larger leadership signal is that the user advocated local E2E/integration tests and explicit seams that let engineers trust their changes without running long DAGs or relying on single-owner manual review.
- Replaced inefficient vendor-package practices with internal package publication.
- Helped introduce AWS CodeArtifact.
- Supported publication of internal Python packages such as vtx-runners and graph-structure.
- ODSC 2022 talk on DynamicIO.

Useful phrasing:

- Created reusable internal tooling adopted across 15+ repositories.
- Standardised Python I/O patterns, reduced duplicated data-access code, and made business logic easier to test locally.
- Modernised internal package publication and reuse.
- Improved development velocity, feedback-cycle time, and maintainability across Python teams.

This is one of the strongest evidence-backed platform stories.

#### MLOps and Platform Practices

Evidence:

- Cultivated MLOps practices at Vortexa, including model versioning, data-model dependencies, and model monitoring.
- When the user joined Vortexa, the team's MLOps maturity was low; the user taught research/prototyping discipline and how to build maintainable ML pipelines that can evolve.
- Introduced model/data versioning concepts, recommended the tools and practices to implement them, introduced MLflow, introduced model deployment as services, and introduced model-accuracy monitoring dashboards.
- Grew Vortexa's ML development lifecycle from research/prototype habits into production lifecycle practice.
- Improved unit-test coverage and local end-to-end tests using characteristic sample data.
- Enabled shift-left feedback loops.
- Improved code quality, development experience, and pipeline robustness.
- Built CI/CD and model lifecycle workflows.
- Local E2E/integration tests changed review dynamics: repos moved away from single-person ownership and careful manual refactor review toward evidence-backed PRs that could reach production in hours rather than days.

Useful phrasing:

- Raised ML engineering standards across experimentation, deployment, monitoring, and maintainability.
- Established Vortexa's ML development lifecycle from research to production: prototyping discipline, MLflow, model/data versioning, service-based model deployment, replay/evaluation interfaces, and live accuracy-monitoring dashboards.
- Turned research-grade model work into reproducible, observable production systems.
- Improved developer confidence through local test fixtures and end-to-end test paths.
- Reduced single-owner review bottlenecks and increased engineers' confidence in their own changes through local E2E/integration tests and tests-as-docs.

#### Architecture and Organisational Scaling

Evidence:

- Advocated for Architectural Decision Records.
- Instigated a weekly company architecture forum for presenting ideas, discussing trade-offs, shared learning, and feedback.
- Contributed input to team-topology and re-org initiatives, especially how pods should interact with analysts/SMEs, frontend teams, and product; frame as influence, not ownership.
- Drove Vortexa's Data Production Team from 4 people to 30+ and raised its operating maturity through hiring process design, system design culture, strategic platform choices, and cross-functional operating-model advocacy; do not reduce this to passive "helped scale" wording.
- Accuracy boundary for public claims: the user did not hold formal director authority over the full department, so frame this as strategic influence, mechanisms, and adoption rather than manager-of-managers ownership.
- Developed and applied hiring practices, including LeetCode-style and system design evaluations; contributed to senior/principal DS/DE hiring across levels.
- Advocated cross-functional team shapes combining engineers, Product, analysts, and SMEs, and pushed for adoption as a way to make product/engineering/domain interfaces more effective.
- Turns ambiguous product/model friction into scoped workstreams and product-ready interfaces, using proposal discipline and stakeholder workshops without requiring Vortexa-specific domain wording in public CV copy.
- Uses DORA metrics and Jira-based monitoring/alert workflows as delivery-health mechanisms for reaction speed, bottleneck visibility, toil/burnout reduction, and team trust.
- DORA screenshot supplied 2026-07-31 for the team's latest 12-month DX view: open-to-deploy 15.9 hours, merge-to-deploy 16.2 minutes, deploy frequency 14.65/week, change-fail percentage 0.52%, and time-to-recover 39.4 minutes. Use these as point-in-time supporting evidence, not timeless claims; in concise CV copy, prefer deploy frequency and change-failure percentage as the most recruiter-legible delivery/reliability signals.
- Contributed to Architecture Guild-style work.
- Built a data-flow graph/history of Vortexa's processing components through interviews and platform archaeology.
- Presented platform lineage and system evolution to the company.

Useful phrasing:

- Created mechanisms for architectural transparency and shared decision-making.
- Reduced knowledge silos through ADRs, architecture forums, and system lineage work.
- Drove engineering practice and operating-model maturity during startup-to-scale-up transition.

#### Side Panel Positioning

Use the side panel as a recruiter scan path, not a generic tools inventory. The strongest compact categories are:

- Avoid repeating every body metric in the side panel. It should act as a scan index, not a second miniature CV.
- Scale: estate ownership, org scale-up, client-facing ML, high-volume streaming.
- People: hiring, mentoring, retention, cross-functional delivery.
- Systems: MLOps, observability, explainability, streaming reliability.
- Practice: streaming platforms, DORA/Jira signals, architecture decisions, local E2E tests.
- Technical: production ML, signal cleaning, Java/Kotlin, Python, SQL, Kafka/Flink, Airflow, AWS/GCP.
- Public work: PyPI libraries dynamicio and skeleton-replay, Skeleton Replay on JetBrains Marketplace, and practical AI standards through JTC'21/UCL. Use this as a credibility signal for productised developer tooling, release discipline, documentation, and standards work, not as a generic hobby-project list.
- Keep MTTR under 30 minutes in the Vortexa body where monitoring/runbooks/rollback/on-call context explains it; do not foreground it in the side panel.

#### Team Leadership

Evidence:

- Pod Lead for Turingeries.
- Managed or led a fully remote team while delivering Ithaca; onboarded and mentored two new members during that period.
- Responsibilities in raw notes include technical supervision, people management, backlog refinement, prioritisation, stakeholder management, mentoring, and product-management-like work.
- Mentored engineers, data scientists, and analysts.
- Hiring context for Vortexa/DPT: hiring manager for 6 roles over the years; because of reorgs/restructures, do not imply all six remained under current supervision. Interviewed 31+ candidates as hiring manager and participated in 60+ interview loops overall across DPT staffing/onboarding. Current team has been fully retained and every member was recently promoted/progressed.
- Ran or initiated event-driven architecture mentorship sessions with seven participants, including two from a frontend/product engineering team.

Useful phrasing:

- Staff-level technical leadership with pod-level delivery accountability.
- Mentored engineers and data scientists across ML engineering and streaming systems.
- Combined architecture, delivery planning, stakeholder management, and hands-on implementation.

Avoid unless confirmed:

- Formal line-management headcount.
- Manager-of-managers claims.
- Director-level budget or org ownership.

#### AI Adoption and Developer Workflow

Evidence:

- Promoted practical AI adoption practices.
- Identified friction points in AI-assisted development.
- Public post: `content/_posts/2026-04-08-llm-clis-have-a-review-speed-problem.md`.
- Themes include verification, trust, risk awareness, review quality, smaller changes, and production confidence.

Useful phrasing:

- Advocates for AI-assisted engineering practices grounded in verification and production risk.
- Focuses on trust, evaluation, and operational boundaries around automation.
- Useful bridge for AI governance, agentic workflow, and developer-platform roles.

Avoid unless confirmed:

- Claims of shipping a production autonomous-agent platform.
- Claims of LLM fine-tuning, RLHF, or production multi-agent orchestration.

## Promet Context

Promet is the reference portfolio project for demonstrating applied LLM engineering. It is a local-first AI workbench focused on memory-aware, tool-using agents, with Ollama as the first supported runtime.

The strongest positioning is LLM systems engineering rather than prompt writing. Promet shows the ability to design the infrastructure around LLM adoption:

- Model runtime adapters.
- Orchestration boundaries.
- Prompt construction.
- Streaming behaviour.
- Tool execution.
- Permissions.
- Local-first configuration.
- Traceability.
- Deterministic verification loops.

### Current Strengths Demonstrated By Promet

- Designing local-first LLM applications with replaceable model-runtime boundaries.
- Building the harness around model behaviour: prompts, session state, streaming, tools, approvals, and failure handling.
- Treating tool safety, logging, and auditability as core product concerns.
- Structuring AI systems so memory, RAG, tools, and model runtimes can evolve as separate components.
- Creating developer feedback loops with tests, traces, UI checks, and architecture documentation.
- Translating ambiguous LLM product ideas into maintainable software architecture.

### Practical LLM Adoption Exposure

Promet reflects exposure to the practical challenges teams face when adopting LLMs:

- Controlling context.
- Managing latency.
- Avoiding brittle post-processing.
- Keeping vendor-specific details out of orchestration.
- Testing nondeterministic behaviour.
- Deciding what should belong to the model versus the application harness.

### Honest Boundaries

Promet is intentionally built to support future layers such as fine-tuning, production RAG, and long-term memory systems, but those should not yet be claimed as deep experience unless separately confirmed.

Current honest position:

- Strong foundation for custom LLM applications.
- Clear interfaces.
- Bounded retrieval design.
- Explicit memory-policy thinking.
- Tool governance.
- Local evaluation.
- Maintainable runtime architecture.

Avoid unless confirmed:

- Deep fine-tuning experience.
- Production RAG ownership.
- Long-term memory systems shipped in production.
- RLHF/RLAIF/DPO/PPO or model-alignment research.
- Claims that Promet is a commercial production product.

Job-role positioning:

> LLM systems engineer / applied AI engineer with strong software engineering discipline, focused on building reliable custom LLM products from the harness upward.

## DataReply Context

Dates:

- 04/2016-12/2020.
- Joined Data Reply's London spin-off as its first consultant.
- Progressed from Data Scientist to ML Engineer and Senior Consultant.
- Played a formative role in growing the team from 3 practitioners + 2 managers to 30+ consultants.
- User was asked to move toward an Associate Partner path before leaving; treat this as private context unless explicitly needed, not as a default CV claim.
- Leadership included client meetings, scoping goals, facilitating technical delivery, consultant placement, interviewing, mentoring, and guiding hires.
- Ran the London Flink Meetup for roughly five years from 2016 to mid-2020.
- Worked across UBS, Vodafone, CNHi, UniCredit, Mondadori, Gamesys, and opportunities around BT/HSBC; use named clients sparingly in the CV.
- Data Reply should now be framed as consulting plus project/client leadership, not as purely IC work. Still avoid overstating formal people-management authority across the full Data Reply organisation.

### Vodafone

Evidence:

- Worked on Vodafone's internal MLOps platform, Infinity Project, before it was completed.
- Infinity was built on GCP using Kubeflow; keep Kubeflow as project context, not as a current sidebar skill claim.
- Supported versioning, deployment, telemetry, experiment workflows / resource-governed notebooks.
- Implemented CI/CD pipelines, unified feature stores, and monitoring.
- Vodafone was an early point where the user was put in charge of technical delivery, people coordination, stakeholder interaction, and product-facing delivery across multiple workstreams.
- Red Agent was a mobile-network feature-engineering framework for profiling users from network data.

Best use:

- ML platform roles.
- MLOps roles.
- Platform engineering roles.
- Research-to-production stories.

### CNHi

Evidence:

- Built time-series forecasting models for agricultural vehicles.
- Supported alerting and automated deployment.
- Led prototyping and transitioned statistical models into scalable cloud-ready services.
- First substantial DS team-lead experience: led/guided a data-science team using PySpark over live vehicle sensor data to infer maintenance/repair needs.
- Operated with Scrum Master/product-facing backlog discipline.

Best use:

- Forecasting, industrial ML, applied ML, IoT/telemetry, model operationalisation.

### UBS

Evidence:

- Designed real-time pipelines using graph analytics and process mining.
- Produced organisational insights and decision automation.
- Built observability tools with Kafka, Elasticsearch, and Python.
- Developed software-engineering and ML-engineering discipline at UBS through exposure to Extreme Programming, pairing, productionisation, and enterprise delivery constraints.
- Eventually became the sole embedded Data Reply consultant on the UBS account.

Best use:

- Graph analytics.
- Decision intelligence.
- Real-time analytics.
- Enterprise data infrastructure.

## Research, Education, and Standards

### Ph.D.

Evidence:

- Ph.D. in Computer Science, King's College London, 2010-2014.
- Thesis: Persuasion Dialogues and Opponent Modelling.
- Developed logical inference methods for large knowledge graphs.
- Combined symbolic reasoning, graph analytics, and Bayesian techniques including MCMC.
- Best Poster Award at IJCAI 2013 out of 413 submissions.
- EPSRC PhD Scholarship.
- Outstanding TA Award.
- Graduate Certificate in Academic Practice.

Best use:

- Research-adjacent ML roles.
- Knowledge graphs / reasoning / semantics.
- AI governance and decisioning roles.
- Principal roles needing credibility across research and engineering.

### Undergraduate

Evidence:

- Diploma / BEng in Computer Engineering, University of Thessaly, 2004-2010.
- Five-year polytechnic degree.
- Strong mathematics focus.
- Majored in Artificial Intelligence.

### Standards and Affiliations

Evidence:

- ISO / JTC 21 committee expert member since January 2021.
- Working Group 3, developing AI standards aligned with EU policies and international norms.
- UCL Department of Information Studies Associate Researcher since October 2024; helps expose students to practical AI applications and lectures on AI standardisation, the AI Act, auditability, versioning, explainability, and safe adoption.
- Supports AI application, standardisation, and ethics initiatives.

Best use:

- AI governance.
- Responsible AI.
- Trust and safety.
- Regulated-domain roles.
- Platform roles where auditability, reliability, and standards matter.

## Public Work

Talks and interviews:

- 2023: Agile in Action podcast interview on agile data science and the Vortexa journey.
- 2022: ODSC talk on DynamicIO and abstracting I/O for ML systems.
- 2020: iunera interview on agile data science.
- 2020: Big Data Warsaw talk on graph analytics over communication and trade events.
- 2018: Connected Data London panel on graph AI.
- 2018: Minds Mastering Machines talk on doing data science the agile way.

Useful positioning:

- External credibility.
- Ability to explain complex systems.
- Thought leadership in ML engineering, graph analytics, and production data science.

## Role-Fit Patterns

### Strong Fits

Roles are strongest when they value:

- Production ML systems.
- ML platform engineering.
- Event-driven architecture.
- Real-time inference.
- MLOps maturity.
- Data/model versioning, monitoring, CI/CD, and observability.
- Staff-level technical leadership.
- Cross-functional delivery across ML, DS, DE, product, and infrastructure.
- AI governance, auditability, and trustworthy automation.
- Applied LLM systems engineering, especially tool use, local runtimes, orchestration, permissions, traceability, and deterministic verification loops.

Examples:

- Staff ML Platform Engineer.
- Principal ML Systems Engineer.
- Staff Applied AI Engineer.
- LLM Systems Engineer.
- Applied AI Platform Engineer.
- ML Infrastructure Lead.
- Content / decisioning platform roles where the emphasis is systems, quality, and governance rather than media-specialist modelling.

### Credible Stretch Fits

Roles are plausible but need careful positioning when they ask for:

- Foundation model infrastructure.
- LLM platform work.
- Generative AI systems.
- Custom LLM products built from model-runtime, orchestration, tool-use, memory/RAG, and evaluation foundations.
- Principal-level AI product ownership.
- Trust and safety / policy decisioning.
- Multimodal systems.
- Director-track platform leadership.

Position as:

- Strong production ML systems and platform leader.
- Credible applied LLM systems engineer through Promet.
- Credible research-to-production bridge.
- Strong on evaluation, reliability, observability, and governance.
- Expanding into LLM/generative AI systems where supported by current work.

### Weak or High-Risk Fits Without More Evidence

Roles become weak if screening requires:

- Hands-on RLHF/RLAIF/DPO/PPO.
- LoRA/QLoRA/full LLM fine-tuning.
- LLM pre-training or continued pre-training.
- Swift production development.
- Ray, Triton, Iceberg, or specialist model-serving stack as hard requirements.
- Direct audio/video/image ML production systems.
- Deep production RAG or long-term memory ownership.
- Formal Director-of-Engineering scope with multiple EMs.
- Large budget ownership.
- Large SRE org ownership.
- GPU cluster scheduling or foundation-model training infrastructure at very large scale.
- Biotech/life-science domain expertise.

Handle these as gaps. Do not fabricate.

## Evidence Bank For CV Tailoring

Use these as candidate bullets, then tighten to fit the role and verify exact details.

### ML Platform / Infrastructure

- Led production ML services for destination and arrival prediction, with versioned serving, fallback mechanisms, health checks, and observable rollout paths.
- Built and maintained real-time ML pipelines that connect streaming data, model inference, and downstream decision support.
- Worked on Vodafone's internal MLOps platform on GCP/Kubeflow, supporting model versioning, deployment, telemetry, and resource-governed notebooks; do not imply completion ownership.
- Standardised ML engineering practices around model versioning, data-model dependencies, monitoring, CI/CD, and local end-to-end testing.

### Streaming / Data Engineering

- Designed Kafka/Flink pipelines for near real-time enrichment, model updates, and downstream triggers across 15+ ETL components.
- Established Apache Flink as a strategic stream-processing direction, with the value in dataflow modelling, framework-driven development, lower cognitive load, lower maintenance effort, richer operational visibility, and compute scaling decoupled from Kafka partitioning.
- Bridged Python ML workflows with JVM stream-processing components in Java/Kotlin/Kafka Streams.
- Built distributed workflows over geospatial, textual, and graph-structured data; avoid framing Flink adoption as primarily a throughput improvement.

### Architecture / Staff Leadership

- Instigated a weekly company architecture forum and promoted ADR practices to reduce knowledge silos, improve architectural decision-making, and create useful feedback loops.
- Promoted Flink and Airflow Python repository archetypes to reduce cognitive load, speed up repeated delivery patterns, and reduce maintenance man-hours.
- Advocated for docs close to code, ADRs as durable historical records, championed/adopted Backstage for the team, supported wider Backstage adoption, championed dev containers, and pushed developer-platform style standardisation.
- Supports OpenMetadata adoption to improve data lineage, auditability of processing trails, and understanding of system interfaces.
- Built a cross-system lineage view of Vortexa's production data flow by interviewing engineers and mapping component history.
- Led pod-level delivery across technical direction, prioritisation, backlog refinement, stakeholder management, mentoring, and hiring.
- Shaped cross-functional delivery topology around engineers, Product, analysts, and SMEs, using advice, feedback, and sustained advocacy rather than formal department-level authority.
- Mentored engineers and data scientists in ML engineering, event-driven architecture, Kafka, Flink, testing, and production discipline.

### Product / Business Impact

- Delivered destination-model-as-a-service work that improved latency, throughput, and operational maintainability.
- Addressed LNG prediction quality and waiting-time prediction spikes through model and service improvements.
- Implemented sanctioned-destination control logic to align prediction systems with compliance needs.
- Improved analyst and customer trust by increasing prediction stability and reducing operational support burden. Verify precise wording before external use.

### Governance / Trust / AI Adoption

- ISO/JTC 21 committee expert member working on AI standards aligned with EU and international norms, with emphasis on auditability, model/data versioning, prediction tracking, and explainability.
- UCL Associate Researcher connecting practical AI applications with AI standardisation, auditability, model/data versioning, explainability, and safe adoption.
- Advocates for AI-assisted engineering workflows grounded in verification, bounded risk, review quality, and production confidence.
- Designs ML systems with auditability, fallback paths, monitoring, and controlled rollout rather than treating model output as sufficient.

## Claims To Verify Before External Use

These may be true based on context, but require direct confirmation or careful wording before putting them in a CV or application:

- Exact team size led at Vortexa.
- Exact number of direct reports, if any.
- Whether performance reviews were formal line-management responsibility.
- Whether he managed budget or headcount planning.
- Exact latency, throughput, uptime, cost, or accuracy improvements unless backed by current evidence.
- Scope of Flink adoption: team-level, department-level, or company-level.
- Scope of Architecture Guild participation and authority.
- Exact ownership of Kalman filter productionisation.
- Exact operational incident/SRE responsibility.
- Any hands-on LLM fine-tuning, production RAG, or long-term memory delivery.
- Any claim that Promet is production/commercial rather than a reference portfolio project.

## Tailoring Rules

- Keep claims factual and evidence-backed.
- Prefer stronger, narrower claims over broad seniority claims that are hard to prove.
- For Staff/Principal roles, emphasise system ownership, architecture, mentoring, technical standards, and cross-team influence.
- For Director roles, only emphasise people/org leadership where scope is explicit; otherwise frame as Director-track or Staff-plus.
- For LLM roles, foreground production ML, evaluation, observability, data quality, governance, verification discipline, and Promet's harness-level LLM engineering; do not claim RLHF/fine-tuning/alignment unless confirmed.
- For trust/safety or governance roles, connect sanctioned-destination rules, auditability, fallback mechanisms, ISO standards, and verification-oriented AI adoption.
- For platform roles, foreground DynamicIO, CI/CD, model lifecycle, streaming architecture, and reusable internal tooling; mention Vodafone Kubeflow only as historical project context.
- For research-heavy roles, foreground Ph.D., graph reasoning, Bayesian methods, IJCAI award, and research-to-production bridge.

## One-Line Positioning Options

General:

- Staff-level ML systems leader with deep experience turning advanced modelling work into reliable, observable production systems.

Platform:

- ML platform and infrastructure lead specialising in model lifecycle, real-time inference, event-driven data systems, and production reliability.

Governance / Trust:

- Production ML leader focused on trustworthy automation, auditability, evaluation discipline, and AI systems that can be safely operated at scale.

Director-track:

- Staff-plus ML technology leader combining hands-on architecture, pod leadership, platform strategy, mentoring, and cross-functional delivery.

LLM / Generative AI stretch:

- Production ML systems engineer with strong evaluation and platform discipline, and growing focus on reliable generative AI systems.

Applied LLM systems:

- LLM systems engineer focused on the application harness around model behaviour: runtime abstraction, prompt/session orchestration, streaming, tool governance, traceability, and deterministic verification.
