# PNC GCC Hackathon — DB Reliability Agent (`dbpulse`)

> **Proactive Postgres DB Reliability Agent**: Watches PostgreSQL KPIs, detects anomalies, performs RAG-grounded root-cause diagnosis in plain English, and drafts/raises incident tickets for DBA remediation — before customers notice impact.

![Theme Fit](https://img.shields.io/badge/Theme-Business%20Impact%20%26%20Risk-blue)
![Secondary Fit](https://img.shields.io/badge/Theme-Engineering%20Velocity-green)
![Tech Stack](https://img.shields.io/badge/Stack-Flask%20%7C%20React%20%7C%20Postgres%20%7C%20RAG-orange)

---

## 🚀 Key Features

1. **Proactive Anomaly Detection**: Monitors PostgreSQL system views (`pg_stat_activity`, `pg_locks`, `pg_stat_database`) in real time across the database fleet (`PNCPRD01`, `RECON_DB`, `MBL_STG`).
2. **RAG-Grounded Root Cause Diagnosis**: Grounds LLM reasoning (Claude Sonnet 5 / OpenAI / Foundry) with a specialized PostgreSQL wait-event knowledge base to explain root causes in plain English with source citations (`source: pg_stat_activity, pg_locks`).
3. **Safety-First Action Drafting**: Generates copyable, step-by-step SQL remediation scripts (e.g. `pg_cancel_backend`, index recommendations). Follows strict safety principles (*"generates SQL for a human to run — nothing executes automatically"*).
4. **90-Second Demo Loop**: Complete end-to-end flow: `Detect Anomaly → Diagnose Root Cause → Raise Incident (INC-00458)`.
5. **Zero-Risk Fallback Engine**: Built-in synthetic database engine and cached diagnosis fallback ensure the application runs 100% out-of-the-box even without an active Postgres instance or external LLM API key.

---

## 🎨 Visual Design System ("Terminal Glow")

Dark technical console designed specifically for DBAs under incident pressure:
- **Background**: `#14171C`
- **Agent Presence**: `#3FA9A0` (Teal glow & accents reserved strictly for AI presence)
- **Risk Indicator**: `#D9643A` (Coral accent for anomaly signals)
- **Healthy Fleet**: `#5B8C6E` (Sage accent for healthy nodes)
- **Typography**: `IBM Plex Sans` + `IBM Plex Mono`

---

## 🛠 Project Structure

```
├── backend/
│   ├── app.py              # Flask server & REST API endpoints
│   ├── db_monitor.py       # PostgreSQL queries & synthetic DB engine
│   ├── rag_engine.py       # PostgreSQL wait event RAG knowledge base
│   ├── agent.py            # AI diagnosis reasoning engine & fallback
│   ├── test_backend.py     # Unit test suite for backend APIs
│   └── requirements.txt    # Python dependencies
├── src/
│   ├── components/         # Modular React components
│   │   ├── Header.tsx
│   │   ├── FleetStrip.tsx
│   │   ├── KpiRow.tsx
│   │   ├── AnomalyBanner.tsx
│   │   ├── AgentPanel.tsx
│   │   ├── IncidentCard.tsx
│   │   ├── DemoControls.tsx
│   │   └── TimelineFooter.tsx
│   ├── App.tsx             # Main single-page console layout
│   └── index.css           # Global design tokens & terminal glow styles
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

# Run Flask backend server
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

Run python unit tests:
```bash
python backend/test_backend.py
```

---

## 👥 Authors
- **Surya Teja Vajjhala (CGI)**
- Built for the **PNC GCC Hackathon**
