from enum import Enum


class PostApi20261001ResourcesTimeoffAllowancesBodySourceUnits(str, Enum):
    BASE_UNITS = "base_units"
    BY_WORKED_TIME = "by_worked_time"
    OVERTIME_UNITS = "overtime_units"

    def __str__(self) -> str:
        return str(self.value)
