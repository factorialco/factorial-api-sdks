from enum import Enum


class PutApi20261001ResourcesAttendanceEditTimesheetRequestsIdBodyLocationType(str, Enum):
    BUSINESS_TRIP = "business_trip"
    OFFICE = "office"
    WORK_FROM_HOME = "work_from_home"

    def __str__(self) -> str:
        return str(self.value)
