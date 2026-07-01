from enum import Enum


class PostApi20260701ResourcesTimeoffAllowancesBodyFrequency(str, Enum):
    LIFETIME = "lifetime"
    MONTHLY_FLEXIBLE = "monthly_flexible"
    YEARLY = "yearly"

    def __str__(self) -> str:
        return str(self.value)
