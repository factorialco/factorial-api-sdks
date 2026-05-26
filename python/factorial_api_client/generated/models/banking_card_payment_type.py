from enum import Enum


class BankingCardPaymentType(str, Enum):
    PAYMENT = "payment"
    REFUND = "refund"

    def __str__(self) -> str:
        return str(self.value)
