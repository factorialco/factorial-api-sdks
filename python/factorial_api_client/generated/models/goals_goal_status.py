from enum import Enum


class GoalsGoalStatus(str, Enum):
    ACHIEVED = "achieved"
    MISSED = "missed"
    NOT_STARTED = "not_started"
    ON_TRACK = "on_track"

    def __str__(self) -> str:
        return str(self.value)
