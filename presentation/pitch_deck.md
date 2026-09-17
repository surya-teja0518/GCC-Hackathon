# 🏆 PNC GCC Hackathon — Presentation Deck & Pitch Script

**Product**: `dbpulse` (PULSE-AI — Proactive Database Reliability Agent)  
**Owners**: Surya Teja Vajjhala (CGI) + Teammate  
**Theme Fit**: *Business Impact & Risk* (Primary) / *Engineering Velocity* (Secondary)  
**Demo Target**: 90-second live loop (`Detect → Diagnose → Raise Incident`)

---

## Slide 1: Title Slide & Executive Summary

### Visual Layout
- Dark technical theme (`#14171C`), soft teal glowing logo: **`dbpulse`**.
- Subtitle: *Proactive Database Reliability Powered by Azure AI*.
- Presenter Names: Surya Teja Vajjhala (CGI) & Teammate.

### Speaker Script (30 seconds)
> *"Good morning judges. We are excited to present **dbpulse** — a proactive AI database reliability agent designed to catch, diagnose, and resolve database incidents before customers ever feel the impact.*  
> *In modern enterprise banking, database outages don't start with a crash — they start silently: an uncommitted row lock, connection pool leakage, or an unindexed query scan. By the time a monitoring alert fires and a DBA logs in, customers are already experiencing slow checkouts and app timeouts. **dbpulse** solves this by turning passive monitoring into an autonomous AI agent."*

---

## Slide 2: The Problem — Passive Monitoring vs. Business Risk

### Visual Layout
- **Left Column (Current State)**: Traditional Dashboards & Monitoring (Grafana/Datadog)
  - ❌ Alerts fire *after* thresholds are breached.
  - ❌ DBAs spend 15–30 minutes manually querying `pg_stat_activity` & `pg_locks` to trace root causes.
  - ❌ Customer impact: High MTTR (Mean Time to Resolution), transaction failures, revenue risk.
- **Right Column (Target State)**: Proactive AI Agent
  - ✅ Continuous metric telemetry polling across database fleet.
  - ✅ RAG-grounded instant diagnosis in plain English.
  - ✅ Automated incident ticket drafting with copyable SQL remediation attached.

### Speaker Script (30 seconds)
> *"Traditional monitoring dashboards are passive — they tell you that something is broken, but they leave the investigation to a human under pressure. A DBA has to sift through thousands of session rows, identify blocking PIDs, and formulate remediation queries manually.*  
> *This creates an average incident resolution window of 15 to 30 minutes. In financial services, 15 minutes of database lock contention can mean thousands of failed transactions and significant enterprise risk."*

---

## Slide 3: The Solution — `dbpulse` (Detect → Diagnose → Act)

### Visual Layout
- Workflow Diagram:
```
[PostgreSQL Telemetry] ──> [Anomaly Detection] ──> [RAG Knowledge Engine] ──> [Azure AI Foundry] ──> [Incident Ticket + Copyable SQL]
```
- **Key Safety Guardrail**:  
  > 🛡 *"generates SQL for a human to run — nothing executes automatically."*

### Speaker Script (45 seconds)
> *"Enter **dbpulse**. **dbpulse** is not another dashboard. It is an agentic AI reliability assistant that continuously watches PostgreSQL fleet telemetry.*  
> *When an anomaly occurs, it retrieves exact domain troubleshooting guidance via RAG, invokes Claude Sonnet 5 on Azure AI Foundry to diagnose the root cause in plain English, and drafts an actionable incident ticket complete with exact remediation SQL.*  
> *Crucially, we follow a strict enterprise safety principle: **dbpulse generates SQL for a human DBA to execute — nothing mutates production databases automatically.**"*

---

## Slide 4: Live Demo — The 90-Second Money Moment

### Visual Demo Flow (Live Screen Capture / Demonstration)

| Step | Time | What the Panel Sees | Presenter Narrative |
| :--- | :--- | :--- | :--- |
| **1. Baseline** | `00:00` | Single-page dark console (`#14171C`). Fleet strip shows `PNCPRD01`, `RECON_DB`, `MBL_STG` healthy. | *"Here is our live dbpulse console watching our PostgreSQL fleet. Everything is currently operating normally."* |
| **2. Anomaly** | `00:15` | Trigger **Row Lock Contention** scenario. `PNCPRD01` status turns coral (`RISK 88/100`), blocked sessions jump to 4, banner alerts PID 48219 tuple lock. | *"Now, a bulk update batch acquires an exclusive lock on public.orders and hangs without committing. Immediately, dbpulse flags the anomaly in real time."* |
| **3. Diagnosis** | `00:40` | Agent panel populates with teal glow (`#3FA9A0`), plain-English root cause, source citations (`source: pg_stat_activity, pg_locks`), and step-by-step SQL (`pg_cancel_backend(48219)`). | *"Within seconds, the agent panel populates. It explains that PID 48219 holds an uncommitted lock on public.orders blocking 4 sessions, and provides the exact safe cancellation SQL."* |
| **4. Incident** | `00:70` | Click **"Raise Incident Ticket"** → Ticket `INC-00458` card appears, assigned to DBA on-call; timeline footer updates. | *"With one click, the agent raises incident INC-00458 for the on-call DBA with diagnostic queries pre-attached. Total time elapsed: under 90 seconds."* |

---

## Slide 5: Technical Architecture & Azure Stack

### Visual Layout
- **Backend Layer**: Flask single-process backend serving REST APIs & static assets.
- **Database Layer**: Azure Database for PostgreSQL (Flexible Server), monitoring `pg_stat_activity`, `pg_locks`, `pg_stat_database`.
- **AI & RAG Layer**: Azure AI Foundry (Claude Sonnet 5 / `gpt-5.4-mini`) + RAG knowledge retriever.
- **Frontend Layer**: React console with custom "Terminal Glow" design system (`IBM Plex` typography).
- **Resilience Guarantee**: Built-in synthetic database simulator & cached diagnosis fallback for 100% demo uptime.

### Speaker Script (30 seconds)
> *"Behind the scenes, **dbpulse** runs on a lean, high-velocity stack. The backend is built with Python Flask, querying Azure Database for PostgreSQL system views. The AI engine leverages Azure AI Foundry running Claude Sonnet 5, grounded by our wait-event RAG knowledge base. The frontend is a dark technical console designed specifically for high-stress incident management."*

---

## Slide 6: Product Depth & Enterprise Vision

### Visual Layout
- **Mockup Highlights (Vision Slides)**:
  - Fleet Heatmap & Multi-Database Drilldowns.
  - Feedback Loop & Threshold Tuning (DBAs can upvote/downvote agent recommendations to refine RAG grounding).
  - Zero PNC Proprietary Code: 100% fresh, independently-authored open-source code targeting synthetic Postgres datasets (`testdb`).

### Speaker Script (30 seconds)
> *"While today's demo focuses on a single-page incident console, our full vision includes fleet-wide heatmaps, automated post-mortem summary generation, and a DBA feedback loop where engineers can refine RAG parameters.*  
> *All code presented today is 100% fresh, original code built during this hackathon using synthetic banking datasets."*

---

## Slide 7: Business Impact & Enterprise Value

### Visual Layout
- ⚡ **MTTR Reduction**: 15–30 minutes → **Under 90 seconds** (10x faster incident resolution).
- 🛡 **Risk Mitigation**: Eliminates cascading lock contentions before customer transaction failure.
- 🚀 **Engineering Velocity**: Automates repetitive DBA triage so senior engineers focus on architecture.

### Speaker Script (30 seconds)
> *"The business impact of **dbpulse** is immediate:  
> First, it reduces Mean Time to Resolution from 15 minutes down to 90 seconds.  
> Second, it directly protects customer experience by catching row locks and connection leaks before users hit app timeouts.  
> And third, it dramatically boosts engineering velocity by delivering root causes and fixes directly to on-call DBAs."*

---

## Slide 8: Conclusion & Q&A

### Visual Layout
- **Summary Points**:
  - `Detect → Diagnose → Raise Incident` in under 90 seconds.
  - Azure AI Foundry + Azure PostgreSQL powered.
  - Safety-first: SQL generation with human-in-the-loop approval.
- **Repository Link**: `github.com/surya-teja0518/GCC-Hackathon`
- Presenter Contact & Thank You.

### Speaker Script (15 seconds)
> *"Thank you judges! **dbpulse** bridges the gap between AI innovation and mission-critical database reliability. We welcome your questions."*

---

## ❓ Anticipated Panel Questions & Recommended Answers

### Q1: *"How do you prevent the AI agent from executing dangerous SQL commands?"*
- **Answer**: *"Great question. Security and safety are central to our design. **dbpulse** operates strictly on a human-in-the-loop model: it generates diagnostic and remediation SQL for a human DBA to inspect and run — nothing executes automatically against production databases."*

### Q2: *"What happens if the LLM API hangs or network connectivity drops during an incident?"*
- **Answer**: *"We built **dbpulse** with enterprise resilience in mind. If the LLM API call fails or times out, our fallback engine instantly generates deterministic, RAG-grounded root causes and remediation scripts so the DBA is never left without guidance."*

### Q3: *"Can this scale to hundreds of databases across multiple cloud regions?"*
- **Answer**: *"Yes. Because PostgreSQL system views like `pg_stat_activity` and `pg_stat_database` are lightweight cluster-wide views, a single monitoring connection can observe multiple database instances simultaneously with minimal overhead."*
