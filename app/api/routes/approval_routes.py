from fastapi import APIRouter
from app.human.approval_store import approval_store
from app.execution.orchestrator import Orchestrator

router = APIRouter()

orchestrator = Orchestrator()

@router.post("/approve/{workflow_id}")
def approve(workflow_id: str):

    approval_store.approve(workflow_id)

    return orchestrator.resume(workflow_id)