# 🏦 Banking Workflow Orchestrator
An LLM-powered workflow orchestration engine for intelligent banking automation
A production-style AI-driven backend system built with FastAPI, Llama 3.1 (Ollama), and a modular execution architecture. This engine demonstrates how modern banking platforms can automate internal operations using LLM reasoning, workflow planning, policy enforcement, tool execution, audit logging, and human approval gates.
```
Natural language input → Structured banking workflows → Safe, step-by-step execution with full traceability.
```

## 📋 Table of Contents
```
1. How It Works
2. Core Capabilities
3. Supported Intents
4. Architecture Overview
5. Example Workflow
6. Tool System
7. Human Approval Flow
8. State & Audit System
9. API Reference
10. Project Structure
11. Setup Instructions
12. Design Principles
13. Future Enhancements
```

## 🧠 How It Works

The system follows a complete LLM-to-execution pipeline:
```
User Input
    ↓
Intent Detection (LLM)
    ↓
Policy Engine
    ↓
Workflow Planner (LLM)
    ↓
Tool Planner
    ↓
Tool Execution Engine
    ↓
State Management + Audit Logging
    ↓
Response or Human Approval
```
Every request passes through controlled stages ensuring safety, traceability, and deterministic execution—even when LLMs are involved.

## 🚀 Core Capabilities
Feature	Description:

- LLM-based intent detection using Llama 3.1
- Dynamic workflow generation based on intent
- Policy-based decision making (ALLOW / DENY / REQUIRE APPROVAL)
- Tool execution engine for banking operations like:
  KYC verification, account creation, loan processing, and notifications
- Human approval system for sensitive workflows like loans
- Persistent workflow state tracking using SQLite
- Full audit logging of every system event
- Resume capability for paused workflows


## 🎯 Supported Intents

The system currently understands:

- ACCOUNT_OPENING
- LOAN_APPLICATION
- KYC_UPDATE

Each intent triggers a different workflow with dynamically generated steps.


## 🏛️ Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                        User Input                           │
└─────────────────────────┬───────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│                  Intent Agent (LLM)                         │
│            Classifies user request into intent              │
└─────────────────────────┬───────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│                    Policy Engine                            │
│         Checks permissions and approval requirements        │
└─────────────────────────┬───────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│               Workflow Planner (LLM)                        │
│           Generates ordered execution steps                 │
└─────────────────────────┬───────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│                    Tool Planner                             │
│            Maps steps to executable tools                   │
└─────────────────────────┬───────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│               Tool Execution Engine                         │
│         Runs banking operations with error handling         │
└─────────────────────────┬───────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│           State Manager + Audit Logger                      │
│        Persists state and logs all events                   │
└─────────────────────────┬───────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│            Final Response / Approval Flow                   │
└─────────────────────────────────────────────────────────────┘
```

## ⚙️ Example Workflow

When a user sends:
apply for loan

The system executes:

1	Intent Detection: LOAN_APPLICATION
2	Policy Check: Allowed / Requires Approval
3	Workflow Planning: kyc_check → loan_eligibility_check → create_loan_application
4	Tool Execution: Runs each banking operation sequentially
5	Approval Gate: Pauses for human approval (if required)
6	Resume: Continues after admin approval
7	Completion: Stores final state + logs all events

## 🔧 Tool System
The system uses a registry-based tool execution layer with banking operations such as:
- kyc_check
- create_account
- send_welcome_email
- loan_eligibility_check
- credit_check
- risk_assessment
- create_loan_application
- approve_loan
- update_kyc
- notify_customer
Each tool is executed safely in a controlled environment with error handling.

## 👤 Human Approval Flow
Sensitive operations (especially LOAN_APPLICATION) require manual approval:
```
Workflow Starts
      ↓
System Pauses at Approval Gate
      ↓
Admin Reviews via API
      ↓
POST /approve/{workflow_id}
      ↓
Execution Resumes
      ↓
Completion Logged
```

## 📊 State & Audit System
The system maintains full traceability using:

### State Management (SQLite)
Stores:
- workflow_id
- intent
- execution status
- completed steps

### Audit Logging
Tracks:
- WORKFLOW_STARTED
- INTENT_DETECTED
- POLICY_CHECK
- WORKFLOW_PLANNED
- TOOL_EXECUTION
- WORKFLOW_COMPLETED


## 🏗️ Project Structure
```
app/
├── agents/          # LLM-based intent detection
├── api/
│   └── routes/      # FastAPI endpoint definitions
├── audit/           # Event logging system
├── database/        # SQLite connection and models
├── execution/       # Tool execution engine
├── human/           # Approval flow management
├── policy/          # Policy enforcement logic
├── state/           # Workflow state management
├── workflow/        # Workflow planning and orchestration
└── models/          # Pydantic data models
main.py              # Application entry point
```

## ⚙️ Setup Instructions
Prerequisites:
Python 3.9+
Ollama
 with Llama 3.1 model installed
Installation
bash

# Clone the repository
git clone [github.com](https://github.com/YOUR_USERNAME/banking-workflow-orchestrator.git)
cd banking-workflow-orchestrator

# Create virtual environment
python -m venv venv
# Activate virtual environment
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
# Install dependencies
pip install -r requirements.txt
# Start the server
uvicorn app.main:app --reload
Access the API
Open your browser to:
[127.0.0.1](http://127.0.0.1:8000/docs)

## 🔐 Design Principles
LLM is used only for reasoning, not execution
Execution layer is deterministic and safe
Failures never crash workflows
Every action is traceable via audit logs
Human approval is enforced for critical operations

## 🔮 Future Enhancements
 Redis-based distributed state management
 Kafka event streaming architecture
 Role-based authentication system
 React-based enterprise dashboard
 Docker + Kubernetes deployment
 Prometheus + Grafana observability
 Multi-LLM support (GPT / Claude / Llama)

## 🤝 Contributing
Contributions are welcome! Please open an issue or submit a pull request.
