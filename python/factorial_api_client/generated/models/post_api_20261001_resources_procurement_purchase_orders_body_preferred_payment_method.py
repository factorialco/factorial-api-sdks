from enum import Enum


class PostApi20261001ResourcesProcurementPurchaseOrdersBodyPreferredPaymentMethod(str, Enum):
    BANKTRANSFER = "banktransfer"
    CASH = "cash"
    VIRTUALCARD = "virtualcard"

    def __str__(self) -> str:
        return str(self.value)
