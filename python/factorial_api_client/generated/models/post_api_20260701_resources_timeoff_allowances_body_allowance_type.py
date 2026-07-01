from enum import Enum


class PostApi20260701ResourcesTimeoffAllowancesBodyAllowanceType(str, Enum):
    DAYS = "days"
    HOURS = "hours"

    def __str__(self) -> str:
        return str(self.value)
