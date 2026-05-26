from enum import Enum


class PutApi20251001ResourcesTrainingsSessionsIdBodySchedule(str, Enum):
    SCHEDULED = "scheduled"
    SELFPACED = "selfpaced"

    def __str__(self) -> str:
        return str(self.value)
