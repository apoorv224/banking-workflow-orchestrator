class BaseAppException(Exception):
    """
    Root exception for Banking Workflow Orchestrator
    """

    def __init__(self, message: str, code: str = "BASE_ERROR"):
        self.message = message
        self.code = code
        super().__init__(self.message)


class ConfigurationError(BaseAppException):
    """
    Raised when system configuration is invalid
    """
    pass


class WorkflowError(BaseAppException):
    """
    Raised when workflow execution fails
    """
    pass


class PolicyError(BaseAppException):
    """
    Raised when policy evaluation fails
    """
    pass


class ExecutionError(BaseAppException):
    """
    Raised when tool execution fails
    """
    pass