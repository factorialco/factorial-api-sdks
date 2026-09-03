from enum import Enum


class PostApi20261001ResourcesShiftManagementShiftsBulkCreateBodyShiftsItemState(str, Enum):
    BACKUP = "backup"
    DRAFT = "draft"
    PUBLISHED = "published"

    def __str__(self) -> str:
        return str(self.value)
