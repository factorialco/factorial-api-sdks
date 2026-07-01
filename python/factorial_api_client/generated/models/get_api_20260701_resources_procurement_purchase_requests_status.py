from enum import Enum


class GetApi20260701ResourcesProcurementPurchaseRequestsStatus(str, Enum):
    APPROVED = "approved"
    CHANGES_REQUESTED = "changes_requested"
    DRAFT = "draft"
    PENDING = "pending"
    REJECTED = "rejected"

    def __str__(self) -> str:
        return str(self.value)
