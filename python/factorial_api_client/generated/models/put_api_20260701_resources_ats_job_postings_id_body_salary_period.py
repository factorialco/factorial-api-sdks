from enum import Enum


class PutApi20260701ResourcesAtsJobPostingsIdBodySalaryPeriod(str, Enum):
    ANNUAL = "annual"
    DAILY = "daily"
    MONTHLY = "monthly"

    def __str__(self) -> str:
        return str(self.value)
