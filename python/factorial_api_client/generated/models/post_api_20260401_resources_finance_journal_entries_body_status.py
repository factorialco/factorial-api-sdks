from enum import Enum


class PostApi20260401ResourcesFinanceJournalEntriesBodyStatus(str, Enum):
    PUBLISHED = "published"
    REVERSED = "reversed"

    def __str__(self) -> str:
        return str(self.value)
