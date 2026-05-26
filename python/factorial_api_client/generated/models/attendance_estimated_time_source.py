from enum import Enum


class AttendanceEstimatedTimeSource(str, Enum):
    CONTRACT_HOURS = "contract_hours"
    NONE = "none"
    SHIFT_MANAGEMENT = "shift_management"
    WORK_SCHEDULE = "work_schedule"

    def __str__(self) -> str:
        return str(self.value)
