from enum import Enum


class GetApi20260701ResourcesFinanceJournalEntriesStatus(str, Enum):
    PUBLISHED = "published"
    REVERSED = "reversed"

    def __str__(self) -> str:
        return str(self.value)
