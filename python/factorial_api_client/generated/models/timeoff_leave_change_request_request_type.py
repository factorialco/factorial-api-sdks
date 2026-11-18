from enum import Enum


class TimeoffLeaveChangeRequestRequestType(str, Enum):
    CANCEL_LEAVE = "cancel_leave"
    UPDATE_LEAVE = "update_leave"

    def __str__(self) -> str:
        return str(self.value)
