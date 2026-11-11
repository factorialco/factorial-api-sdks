from enum import Enum


class GoalsGoalMeasureType(str, Enum):
    CURRENCY = "currency"
    NUMERIC = "numeric"
    PERCENTAGE = "percentage"
    QUALITATIVE = "qualitative"
    SUB_GOAL = "sub_goal"

    def __str__(self) -> str:
        return str(self.value)
