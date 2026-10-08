from enum import Enum


class PostApi20270101ResourcesShiftManagementShiftsBulkCreateBodyShiftsItemCreationMode(str, Enum):
    AUTOMATIC = "automatic"
    MANUAL = "manual"

    def __str__(self) -> str:
        return str(self.value)
