from fastapi import FastAPI
from app.api.routes.state_routes import router as state_router
from app.api.routes.workflow_routes import router as workflow_router
from app.api.routes.admin_routes import router as admin_router
from app.api.routes.audit_routes import router as audit_router
from app.api.routes.approval_routes import router as approval_router
from app.database.init_db import init_db
from app.api.routes.history_routes import router as history_router
from app.api.routes.dashboard_routes import router as dashboard_router
from app.api.routes.core_routes import router as core_router

init_db()
app = FastAPI(title="Banking Workflow Orchestrator")
app.include_router(core_router)
app.include_router(workflow_router)
app.include_router(audit_router)
app.include_router(admin_router)
app.include_router(state_router)
app.include_router(approval_router)
app.include_router(history_router)
app.include_router(dashboard_router)

@app.get("/health")
def health():
    return {"status": "ok"}