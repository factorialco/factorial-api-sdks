from enum import Enum


class GetApi20261001ResourcesBankingCardPaymentsStatus(str, Enum):
    CLOSED = "closed"
    PENDING = "pending"
    REJECTED = "rejected"
    REVERSED = "reversed"

    def __str__(self) -> str:
        return str(self.value)
