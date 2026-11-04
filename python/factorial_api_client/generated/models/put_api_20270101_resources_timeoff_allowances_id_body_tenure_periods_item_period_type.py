from enum import Enum


class PutApi20270101ResourcesTimeoffAllowancesIdBodyTenurePeriodsItemPeriodType(str, Enum):
    MONTHS = "months"
    YEARS = "years"

    def __str__(self) -> str:
        return str(self.value)
