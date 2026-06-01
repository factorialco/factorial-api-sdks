from enum import Enum


class FinanceContactPreferredPaymentMethod(str, Enum):
    BANKTRANSFER = "banktransfer"
    CARD = "card"

    def __str__(self) -> str:
        return str(self.value)
