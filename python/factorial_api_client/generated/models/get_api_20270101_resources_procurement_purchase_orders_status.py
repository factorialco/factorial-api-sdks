from enum import Enum


class GetApi20270101ResourcesProcurementPurchaseOrdersStatus(str, Enum):
    CLOSED = "closed"
    DRAFT = "draft"
    ORDERED = "ordered"
    PARTIAL = "partial"
    PENDING = "pending"
    PROCESSING = "processing"
    RECEIVED = "received"

    def __str__(self) -> str:
        return str(self.value)
