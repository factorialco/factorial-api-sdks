from enum import Enum


class GetApi20261001ResourcesShiftManagementShiftsOnlyStates(str, Enum):
    BACKUP = "backup"
    DRAFT = "draft"
    PUBLISHED = "published"

    def __str__(self) -> str:
        return str(self.value)
