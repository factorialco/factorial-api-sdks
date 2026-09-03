from enum import Enum


class AttendanceWorkedTimeWorkedTimeBlocksItemTimeType(str, Enum):
    ANY_TIME = "any_time"
    OVERTIME = "overtime"
    REGULAR = "regular"

    def __str__(self) -> str:
        return str(self.value)
