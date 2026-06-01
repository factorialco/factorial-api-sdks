from enum import Enum


class PostApi20260401ResourcesTrainingsSessionsBodySchedule(str, Enum):
    SCHEDULED = "scheduled"
    SELFPACED = "selfpaced"

    def __str__(self) -> str:
        return str(self.value)
