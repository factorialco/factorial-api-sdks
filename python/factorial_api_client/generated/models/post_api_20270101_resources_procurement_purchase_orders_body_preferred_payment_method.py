from enum import Enum


class PostApi20270101ResourcesProcurementPurchaseOrdersBodyPreferredPaymentMethod(str, Enum):
    BANKTRANSFER = "banktransfer"
    CASH = "cash"
    VIRTUALCARD = "virtualcard"

    def __str__(self) -> str:
        return str(self.value)
