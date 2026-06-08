from fastapi import APIRouter
from app.execution.orchestrator import Orchestrator
from app.audit.audit_store import audit_store
from app.state.state_manager import StateManager

router = APIRouter()

orchestrator = Orchestrator()
state_manager = StateManager()


# ---------------- RUN WORKFLOW ----------------
@router.post("/api/workflow/run")
def run_workflow(request: dict):
    return orchestrator.run(request["user_input"])


# ---------------- GET WORKFLOW ----------------
@router.get("/api/workflow/{workflow_id}")
def get_workflow(workflow_id: str):
    return state_manager.get(workflow_id)


# ---------------- APPROVE ----------------
@router.post("/api/workflow/{workflow_id}/approve")
def approve(workflow_id: str):
    from app.human.approval_store import approval_store

    approval_store.approve(workflow_id)
    return orchestrator.resume(workflow_id)


# ---------------- AUDIT ----------------
@router.get("/api/audit")
def audit_logs():
    return audit_store.get_all()