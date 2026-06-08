from enum import Enum

class WorkflowType(str, Enum):
    """
    Supported workflow types in the system
    """

    ACCOUNT_OPENING = "ACCOUNT_OPENING"
    LOAN_PROCESSING = "LOAN_PROCESSING"
    KYC_UPDATE = "KYC_UPDATE"


class PolicyDecision(str, Enum):
    """
    Possible outcomes from policy engine
    """

    ALLOW = "ALLOW"
    DENY = "DENY"
    REQUIRE_APPROVAL = "REQUIRE_APPROVAL"
    DEFER = "DEFER"


class ExecutionStatus(str, Enum):
    """
    Tool execution status
    """

    SUCCESS = "SUCCESS"
    FAILED = "FAILED"
    RETRYING = "RETRYING"