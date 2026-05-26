from enum import Enum


class AttendanceWorkedTimeTimeUnit(str, Enum):
    HALF_DAY = "half_day"
    MINUTE = "minute"
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)
