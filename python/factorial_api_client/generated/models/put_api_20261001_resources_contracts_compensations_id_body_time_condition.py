from enum import Enum


class PutApi20261001ResourcesContractsCompensationsIdBodyTimeCondition(str, Enum):
    CUSTOM = "custom"
    FULL_DAY = "full_day"
    HALF_DAY = "half_day"

    def __str__(self) -> str:
        return str(self.value)
