from enum import Enum


class AttendanceEstimatedTimeBreaksItemBreakType(str, Enum):
    FIXED = "fixed"
    FLEXIBLE = "flexible"
    SEMI_FLEXIBLE = "semi_flexible"

    def __str__(self) -> str:
        return str(self.value)
