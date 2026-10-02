from enum import Enum


class TimeoffAllowanceTenurePeriodsItemPeriodType(str, Enum):
    MONTHS = "months"
    YEARS = "years"

    def __str__(self) -> str:
        return str(self.value)
