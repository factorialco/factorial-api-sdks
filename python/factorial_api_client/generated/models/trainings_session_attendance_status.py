from enum import Enum


class TrainingsSessionAttendanceStatus(str, Enum):
    COMPLETED = "completed"
    INPROGRESS = "inprogress"
    MISSING = "missing"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
