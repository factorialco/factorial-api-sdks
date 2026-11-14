from enum import Enum


class PostApi20270101ResourcesAtsJobPostingsBodySalaryPeriod(str, Enum):
    ANNUAL = "annual"
    DAILY = "daily"
    MONTHLY = "monthly"

    def __str__(self) -> str:
        return str(self.value)
