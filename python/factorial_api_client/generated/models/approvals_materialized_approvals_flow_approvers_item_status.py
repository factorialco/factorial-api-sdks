from enum import Enum


class ApprovalsMaterializedApprovalsFlowApproversItemStatus(str, Enum):
    APPROVED = "approved"
    CHANGES_REQUESTED = "changes_requested"
    IGNORED = "ignored"
    PENDING = "pending"
    REJECTED = "rejected"
    REQUESTEDINFORMATION = "requestedinformation"
    STOPPED = "stopped"
    WAITING_CHANGES = "waiting_changes"

    def __str__(self) -> str:
        return str(self.value)
