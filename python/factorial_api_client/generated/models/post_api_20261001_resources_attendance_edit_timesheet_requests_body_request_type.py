from enum import Enum


class PostApi20261001ResourcesAttendanceEditTimesheetRequestsBodyRequestType(str, Enum):
    CREATE_SHIFT = "create_shift"
    DELETE_SHIFT = "delete_shift"
    UPDATE_SHIFT = "update_shift"

    def __str__(self) -> str:
        return str(self.value)
