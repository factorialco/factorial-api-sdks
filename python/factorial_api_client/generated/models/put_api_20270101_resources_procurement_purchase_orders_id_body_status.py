from enum import Enum


class PutApi20270101ResourcesProcurementPurchaseOrdersIdBodyStatus(str, Enum):
    CLOSED = "closed"
    DRAFT = "draft"
    ORDERED = "ordered"
    PARTIAL = "partial"
    PENDING = "pending"
    RECEIVED = "received"

    def __str__(self) -> str:
        return str(self.value)
