from enum import Enum


class PostApi20261001ResourcesTimeoffAllowancesBodyFrequency(str, Enum):
    LIFETIME = "lifetime"
    MONTHLY_FLEXIBLE = "monthly_flexible"
    YEARLY = "yearly"

    def __str__(self) -> str:
        return str(self.value)
