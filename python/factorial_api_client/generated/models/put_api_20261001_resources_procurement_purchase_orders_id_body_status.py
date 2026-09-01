from enum import Enum


class PutApi20261001ResourcesProcurementPurchaseOrdersIdBodyStatus(str, Enum):
    CLOSED = "closed"
    DRAFT = "draft"
    ORDERED = "ordered"
    PARTIAL = "partial"
    PENDING = "pending"
    RECEIVED = "received"

    def __str__(self) -> str:
        return str(self.value)
