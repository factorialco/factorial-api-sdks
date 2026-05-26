from enum import Enum


class PerformanceAgreementStatus(str, Enum):
    PENDING = "pending"
    SIGNED = "signed"

    def __str__(self) -> str:
        return str(self.value)
