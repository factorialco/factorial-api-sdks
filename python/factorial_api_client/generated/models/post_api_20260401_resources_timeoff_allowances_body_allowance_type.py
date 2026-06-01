from enum import Enum


class PostApi20260401ResourcesTimeoffAllowancesBodyAllowanceType(str, Enum):
    DAYS = "days"
    HOURS = "hours"

    def __str__(self) -> str:
        return str(self.value)
