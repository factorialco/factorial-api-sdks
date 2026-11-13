from enum import Enum


class PutApi20270101ResourcesProcurementPurchaseOrdersIdBodyPreferredPaymentMethod(str, Enum):
    BANKTRANSFER = "banktransfer"
    CASH = "cash"
    VIRTUALCARD = "virtualcard"

    def __str__(self) -> str:
        return str(self.value)
