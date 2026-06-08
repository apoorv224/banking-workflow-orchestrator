from fastapi import APIRouter
from app.execution.orchestrator import Orchestrator
from app.models.request_models import WorkflowRequest

router = APIRouter()

orchestrator = Orchestrator()

@router.post("/run-workflow")
async def run_workflow(request: WorkflowRequest):

    return orchestrator.run(request.user_input)