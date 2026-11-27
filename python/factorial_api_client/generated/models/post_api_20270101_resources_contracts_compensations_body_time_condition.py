from enum import Enum


class PostApi20270101ResourcesContractsCompensationsBodyTimeCondition(str, Enum):
    CUSTOM = "custom"
    FULL_DAY = "full_day"
    HALF_DAY = "half_day"

    def __str__(self) -> str:
        return str(self.value)
