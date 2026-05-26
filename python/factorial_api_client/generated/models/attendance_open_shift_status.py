from enum import Enum


class AttendanceOpenShiftStatus(str, Enum):
    CLOSED = "closed"
    CREATED = "created"
    OPENED = "opened"

    def __str__(self) -> str:
        return str(self.value)
