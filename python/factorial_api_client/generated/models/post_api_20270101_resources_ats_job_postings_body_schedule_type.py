from enum import Enum


class PostApi20270101ResourcesAtsJobPostingsBodyScheduleType(str, Enum):
    FULL_TIME = "full_time"
    PART_TIME = "part_time"

    def __str__(self) -> str:
        return str(self.value)
