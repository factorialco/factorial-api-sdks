from enum import Enum


class GoalsGoalFrequency(str, Enum):
    HALF_YEARLY = "half_yearly"
    MONTHLY = "monthly"
    QUARTERLY = "quarterly"
    YEARLY = "yearly"

    def __str__(self) -> str:
        return str(self.value)
