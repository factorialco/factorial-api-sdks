from enum import Enum


class PostApi20251001ResourcesTrainingsSessionsBodySchedule(str, Enum):
    SCHEDULED = "scheduled"
    SELFPACED = "selfpaced"

    def __str__(self) -> str:
        return str(self.value)
