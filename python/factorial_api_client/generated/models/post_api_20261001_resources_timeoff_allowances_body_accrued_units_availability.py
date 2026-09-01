from enum import Enum


class PostApi20261001ResourcesTimeoffAllowancesBodyAccruedUnitsAvailability(str, Enum):
    CURRENT_CYCLE = "current_cycle"
    NEXT_CYCLE = "next_cycle"

    def __str__(self) -> str:
        return str(self.value)
