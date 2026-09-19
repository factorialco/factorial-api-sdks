from enum import Enum


class TimeoffFrenchLeaveDayCountUnit(str, Enum):
    DAYS = "days"
    HOURS = "hours"

    def __str__(self) -> str:
        return str(self.value)
