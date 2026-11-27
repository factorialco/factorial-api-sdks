from enum import Enum


class PostApi20270101ResourcesTimeoffAllowancesBodyTenurePeriodsItemPeriodType(str, Enum):
    MONTHS = "months"
    YEARS = "years"

    def __str__(self) -> str:
        return str(self.value)
