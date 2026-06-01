from enum import Enum


class GetApi20260401ResourcesAttendanceOvertimeRequestsStatus(str, Enum):
    APPROVED = "approved"
    NONE = "none"
    PENDING = "pending"
    REJECTED = "rejected"

    def __str__(self) -> str:
        return str(self.value)
