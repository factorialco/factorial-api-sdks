from enum import Enum


class AttendanceOvertimeRequestStatus(str, Enum):
    APPROVED = "approved"
    NONE = "none"
    PENDING = "pending"
    REJECTED = "rejected"

    def __str__(self) -> str:
        return str(self.value)
