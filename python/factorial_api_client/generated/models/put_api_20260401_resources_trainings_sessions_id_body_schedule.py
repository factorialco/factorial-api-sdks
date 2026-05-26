from enum import Enum


class PutApi20260401ResourcesTrainingsSessionsIdBodySchedule(str, Enum):
    SCHEDULED = "scheduled"
    SELFPACED = "selfpaced"

    def __str__(self) -> str:
        return str(self.value)
