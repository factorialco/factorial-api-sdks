from enum import Enum


class GoalsGoalTracking(str, Enum):
    MANUAL = "manual"
    SUB_GOALS = "sub_goals"

    def __str__(self) -> str:
        return str(self.value)
