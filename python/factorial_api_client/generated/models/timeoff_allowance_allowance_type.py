from enum import Enum


class TimeoffAllowanceAllowanceType(str, Enum):
    DAYS = "days"
    HOURS = "hours"

    def __str__(self) -> str:
        return str(self.value)
