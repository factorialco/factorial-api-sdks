from enum import Enum


class GetApi20261001ResourcesFinanceCategoriesStatuses(str, Enum):
    DELETED = "deleted"
    DISABLED = "disabled"
    ENABLED = "enabled"

    def __str__(self) -> str:
        return str(self.value)
