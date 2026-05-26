from enum import Enum


class PostApi20251001ResourcesFinanceJournalEntriesBodyStatus(str, Enum):
    PUBLISHED = "published"
    REVERSED = "reversed"

    def __str__(self) -> str:
        return str(self.value)
