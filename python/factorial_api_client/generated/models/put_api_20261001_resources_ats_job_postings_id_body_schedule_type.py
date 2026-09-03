from enum import Enum


class PutApi20261001ResourcesAtsJobPostingsIdBodyScheduleType(str, Enum):
    FULL_TIME = "full_time"
    PART_TIME = "part_time"

    def __str__(self) -> str:
        return str(self.value)
