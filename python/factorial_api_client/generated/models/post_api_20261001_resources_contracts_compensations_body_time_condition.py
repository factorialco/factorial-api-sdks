from enum import Enum


class PostApi20261001ResourcesContractsCompensationsBodyTimeCondition(str, Enum):
    CUSTOM = "custom"
    FULL_DAY = "full_day"
    HALF_DAY = "half_day"

    def __str__(self) -> str:
        return str(self.value)
