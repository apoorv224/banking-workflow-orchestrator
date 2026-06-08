from fastapi import APIRouter
from app.core.singleton import orchestrator

router = APIRouter()


@router.get("/audit-logs")
def get_audit_logs():
    return orchestrator.audit_logger.get_logs()