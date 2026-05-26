from enum import Enum


class GetApi20251001ResourcesAttendanceOvertimeRequestsStatus(str, Enum):
    APPROVED = "approved"
    NONE = "none"
    PENDING = "pending"
    REJECTED = "rejected"

    def __str__(self) -> str:
        return str(self.value)
