from enum import Enum


class FinanceJournalEntryStatus(str, Enum):
    PUBLISHED = "published"
    REVERSED = "reversed"

    def __str__(self) -> str:
        return str(self.value)
