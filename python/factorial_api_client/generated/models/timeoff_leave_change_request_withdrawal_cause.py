from enum import Enum


class TimeoffLeaveChangeRequestWithdrawalCause(str, Enum):
    AUTHOR = "author"
    LEAVE_DELETED = "leave_deleted"
    LEAVE_STARTED = "leave_started"
    LEAVE_UPDATED = "leave_updated"

    def __str__(self) -> str:
        return str(self.value)
