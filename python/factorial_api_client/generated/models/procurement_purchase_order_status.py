from enum import Enum


class ProcurementPurchaseOrderStatus(str, Enum):
    CLOSED = "closed"
    DRAFT = "draft"
    ORDERED = "ordered"
    PARTIAL = "partial"
    PENDING = "pending"
    PROCESSING = "processing"
    RECEIVED = "received"

    def __str__(self) -> str:
        return str(self.value)
