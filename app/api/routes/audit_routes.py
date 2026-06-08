from fastapi import APIRouter, Query
from app.audit.audit_store import audit_store

router = APIRouter()

@router.get("/audit-logs")
def get_audit_logs(workflow_id: str = None):

    if workflow_id:
        return audit_store.get_by_workflow(workflow_id)

    return audit_store.get_all()