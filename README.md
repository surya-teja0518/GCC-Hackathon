# PNC GCC Hackathon — DB Reliability Agent (`dbpulse`)

> **Proactive Postgres DB Reliability Agent**: Watches PostgreSQL KPIs, detects anomalies, performs RAG-grounded root-cause diagnosis in plain English, provides interactive DBA triage tooling, and handles end-to-end incident dispatching — before customers notice impact.

![Theme Fit](https://img.shields.io/badge/Theme-Business%20Impact%20%26%20Risk-blue)
![Secondary Fit](https://img.shields.io/badge/Theme-Engineering%20Velocity-green)
![Tech Stack](https://img.shields.io/badge/Stack-Flask%20%7C%20React%20%7C%20Postgres%20%7C%20RAG-orange)

---

## 🚀 Key Features

### 1. 🔄 Dual Operational Modes (Agent vs. DBA)
Switch seamlessly via the top navigation bar between two operational paradigms:
- **🤖 Agent Mode (Autonomous)**: The agent continuously monitors fleet telemetry, auto-detects KPI anomalies, performs RAG-grounded root cause diagnosis, auto-generates copyable SQL remediation scripts, and pre-populates enterprise incident reports for one-click dispatch.
- **🛠️ DBA Mode (Manual Control & Workbench)**: Hands-on console for senior database administrators:
  - **3 Query Profiles**: One-click session filters (`Lock Contention / pg_locks`, `Idle Connections / ClientRead`, `Table Scans / DataFileRead`).
  - **Raw Session Table**: Detailed process inspector displaying PID, blocking chains, wait event, query duration, and query text.
  - **Interactive SQL Workbench**: Editable query buffer allowing DBAs to test and dry-run administrative SQL (`SELECT pg_cancel_backend(...)`).
  - **On-Demand AI Copilot**: **"🤖 Ask Agent for Suggestion"** button expands AI diagnostic recommendations and generated SQL without leaving manual mode.
  - **Manual Incident Creation**: Direct button to author and dispatch custom incidents manually.

### 2. 📋 Enterprise Incident Management (`#create-incident`)
- **Dedicated Incident Creation Flow**: Full-screen dispatch form accessible from both Agent and DBA modes.
- **Mode-Specific Badging**: Clearly marks incidents as either `AGENT AUTONOMOUS DISPATCH` (reported by `dbpulse AI Reliability Agent`) or `DBA MANUAL DISPATCH` (reported by `Human DBA Operations`).
- **Sequential Incident IDs**: Real-time ID generator (`GET /api/next-incident-id`) issuing sequential incident tracking numbers (`INC-00459`, `INC-00460`, ...).
- **Confirmation Receipts**: Instant receipt view with incident ID, priority badge, category, remediation action, and full audit timestamp.

### 3. 🧠 RAG-Grounded Root Cause Diagnosis
- Grounds LLM reasoning (Claude 3.5 Sonnet / GPT-4o / Azure AI Foundry) with a specialized PostgreSQL wait-event knowledge base.
- Explains root causes in plain English with source citations (`source: pg_stat_activity, pg_locks`).
- Strictly adheres to human-in-the-loop safety: **generates SQL for a human to review and execute — never executes destructive SQL autonomously**.

### 4. 🐘 Modern PostgreSQL 16+ Telemetry Engine
- Compatible with modern Postgres system catalogs: uses `cardinality(pg_blocking_pids(pid))` and `wait_event_type` (replaces deprecated `waiting` column) and groups cache hits by `datname`.
- Fleet-aware architecture: monitors primary production node (`PNCPRD01`) alongside fleet peers (`RECON_DB`, `MBL_STG`).
- Zero-risk fallback: built-in synthetic database engine and cached diagnosis fallback ensure the application runs 100% out-of-the-box even without a live database or cloud API key.

---

## 🎨 Visual Design System ("Terminal Glow")

Dark technical console designed specifically for database reliability engineers under incident pressure:
- **Background**: `#14171C` (Deep slate)
- **Agent Presence**: `#3FA9A0` (Teal glow & accents reserved strictly for AI presence)
- **DBA Workbench**: `#E5A93C` (Warm amber accent reserved for human DBA manual control)
- **Risk Indicator**: `#D9643A` (Coral accent for anomaly signals & blocking PIDs)
- **Healthy Fleet**: `#5B8C6E` (Sage accent for healthy nodes)
- **Typography**: `IBM Plex Sans` + `IBM Plex Mono`

---

## 🛠 Project Structure

```
├── backend/
│   ├── app.py              # Flask server, REST APIs (/api/next-incident-id, /api/raise-incident)
│   ├── db_monitor.py       # PostgreSQL 16+ queries & synthetic DB engine
│   ├── rag_engine.py       # PostgreSQL wait event RAG knowledge base
│   ├── agent.py            # AI diagnosis reasoning engine & fallback
│   ├── test_backend.py     # Unit test suite (fleet status, scenarios, incident generation)
│   └── requirements.txt    # Python dependencies
├── src/
│   ├── components/         # Modular React components
│   │   ├── Header.tsx             # Top bar with [🤖 Agent Mode] vs [🛠️ DBA Mode] pill switcher
│   │   ├── FleetStrip.tsx         # Fleet node status (PNCPRD01, RECON_DB, MBL_STG)
│   │   ├── KpiRow.tsx             # 4 live KPI cards (Lock Contention, Cache Hit, Idle, Commits)
│   │   ├── AnomalyBanner.tsx      # Anomaly alert banner
│   │   ├── AgentPanel.tsx         # Autonomous AI diagnosis, RAG grounding & remediation
│   │   ├── DbaConsolePanel.tsx    # Manual DBA triage console, session inspector & SQL buffer
│   │   ├── CreateIncidentPage.tsx # Dedicated incident creation page & success receipts
│   │   ├── IncidentCard.tsx       # Staged incident card & dispatch trigger
│   │   ├── DemoControls.tsx       # Anomaly scenario simulator (Lock Contention, Idle, Normal)
│   │   └── TimelineFooter.tsx     # Fleet event timeline and audit trail
│   ├── App.tsx             # Main dashboard layout & hash router (#create-incident)
│   └── index.css           # Global design tokens, amber/teal accents & terminal glow styles
├── mock_data/              # Enterprise banking test datasets (10,000+ records)
│   ├── generate_mock_data.py # Data generator for recon records, audit logs & accounts
│   ├── recon_records.csv   # Reconciliation transactions
│   ├── audit_logs.csv      # Security & administrative audit logs
│   └── account_balances.csv# Customer accounts & ledgers
├── design/
│   └── reference.html      # Interactive standalone reference design
└── package.json            # Node.js dependencies & scripts
```

---

## ⚡ Quickstart Guide

### Prerequisites
- Node.js 18+ & npm
- Python 3.11+

### 1. Backend Setup & Run

```bash
# Navigate to backend directory and install dependencies
cd backend
pip install -r requirements.txt

# (Optional) Set environment variables for live PostgreSQL & LLM API
export POSTGRES_URL="postgresql://user:password@localhost:5432/postgres"
export ANTHROPIC_API_KEY="your-key-here"

# Run Flask backend server (serves API on port 5000)
python app.py
```

### 2. Frontend Setup & Build

```bash
# Install Node dependencies
npm install

# Build production React bundle
npm run build

# Or run Vite dev server for hot reload
npm run dev
```

---

## 🧪 Testing

### Backend Unit Tests
Run the comprehensive backend test suite:
```bash
python backend/test_backend.py
```
*Validates 3-node fleet architecture, scenario injection, dynamic sequential incident IDs, and custom incident payloads.*

### Frontend Verification
Run TypeScript type-check and build:
```bash
npm run build
```

---

## 👥 Authors
- **Surya Teja Vajjhala (CGI)**
- Built for the **PNC GCC Hackathon**
