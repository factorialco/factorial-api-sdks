from enum import Enum


class AttendanceWorkedTimeDayType(str, Enum):
    BANK_HOLIDAY = "bank_holiday"
    SATURDAY = "saturday"
    SUNDAY = "sunday"
    WORKDAY = "workday"

    def __str__(self) -> str:
        return str(self.value)
