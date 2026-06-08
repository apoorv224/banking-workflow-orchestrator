from pydantic import BaseModel

class WorkflowRequest(BaseModel):
    user_input: str