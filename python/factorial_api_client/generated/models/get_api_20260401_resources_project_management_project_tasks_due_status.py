from enum import Enum


class GetApi20260401ResourcesProjectManagementProjectTasksDueStatus(str, Enum):
    DUE_IN_FUTURE = "due_in_future"
    DUE_TODAY = "due_today"
    NO_DUE = "no_due"
    OVER_DUE = "over_due"

    def __str__(self) -> str:
        return str(self.value)
