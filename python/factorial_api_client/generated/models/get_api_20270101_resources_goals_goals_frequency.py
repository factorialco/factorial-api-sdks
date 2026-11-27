from enum import Enum


class GetApi20270101ResourcesGoalsGoalsFrequency(str, Enum):
    HALF_YEARLY = "half_yearly"
    MONTHLY = "monthly"
    QUARTERLY = "quarterly"
    YEARLY = "yearly"

    def __str__(self) -> str:
        return str(self.value)
