from enum import Enum


class TrainingsSessionSchedule(str, Enum):
    SCHEDULED = "scheduled"
    SELFPACED = "selfpaced"

    def __str__(self) -> str:
        return str(self.value)
