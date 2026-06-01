from enum import Enum


class ContractsCompensationTimeCondition(str, Enum):
    CUSTOM = "custom"
    FULL_DAY = "full_day"
    HALF_DAY = "half_day"

    def __str__(self) -> str:
        return str(self.value)
