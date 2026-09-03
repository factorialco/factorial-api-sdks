from enum import Enum


class PutApi20261001ResourcesTimeoffAllowancesIdBodyTenurePeriodsItemPeriodType(str, Enum):
    MONTHS = "months"
    YEARS = "years"

    def __str__(self) -> str:
        return str(self.value)
