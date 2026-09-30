from enum import Enum


class PostApi20261001ResourcesAtsJobPostingsBodySalaryPeriod(str, Enum):
    ANNUAL = "annual"
    DAILY = "daily"
    MONTHLY = "monthly"

    def __str__(self) -> str:
        return str(self.value)
