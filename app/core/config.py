from pydantic import BaseModel

class Settings(BaseModel):
    """
    Central configuration for Banking Workflow Orchestrator
    """
    APP_NAME: str = "banking-workflow-orchestrator"
    VERSION: str = "0.1.0"

    DEBUG: bool = True

    # future placeholders (DO NOT USE YET)
    POLICY_ENGINE_ENABLED: bool = True
    WORKFLOW_ENGINE_ENABLED: bool = True
    AUDIT_ENABLED: bool = True


settings = Settings()