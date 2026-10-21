from enum import Enum


class GetApi20270101ResourcesShiftManagementShiftsOnlyStates(str, Enum):
    BACKUP = "backup"
    DRAFT = "draft"
    PUBLISHED = "published"

    def __str__(self) -> str:
        return str(self.value)
