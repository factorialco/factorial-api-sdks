from enum import Enum


class GetApi20261001ResourcesFinanceJournalLinesReconciliationStatus(str, Enum):
    PENDING = "pending"
    RECONCILED = "reconciled"
    SNOOZED = "snoozed"

    def __str__(self) -> str:
        return str(self.value)
