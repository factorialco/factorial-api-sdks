from enum import Enum


class PutApi20260401ResourcesTimeoffAllowancesIdBodyRounding(str, Enum):
    DECIMALS = "decimals"
    HALF_DAY = "half_day"
    QUARTERS = "quarters"
    ROUND_UP = "round_up"

    def __str__(self) -> str:
        return str(self.value)
