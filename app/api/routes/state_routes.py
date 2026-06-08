from fastapi import APIRouter
from app.state.state_manager import StateManager

router = APIRouter()

state_manager = StateManager()

@router.get("/workflow/{workflow_id}")
def get_workflow(workflow_id: str):

    workflow = state_manager.get(workflow_id)

    if not workflow:
        return {
            "error": "Workflow not found"
        }

    return workflow