from enum import Enum


class BankingCardPaymentStatus(str, Enum):
    CLOSED = "closed"
    PENDING = "pending"
    REJECTED = "rejected"
    REVERSED = "reversed"

    def __str__(self) -> str:
        return str(self.value)
