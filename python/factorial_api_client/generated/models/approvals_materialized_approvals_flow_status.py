from enum import Enum


class ApprovalsMaterializedApprovalsFlowStatus(str, Enum):
    APPROVED = "approved"
    CHANGES_REQUESTED = "changes_requested"
    REJECTED = "rejected"
    REQUESTEDINFORMATION = "requestedinformation"
    RUNNING = "running"
    STOPPED = "stopped"

    def __str__(self) -> str:
        return str(self.value)
