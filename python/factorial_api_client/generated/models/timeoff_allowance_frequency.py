from enum import Enum


class TimeoffAllowanceFrequency(str, Enum):
    LIFETIME = "lifetime"
    MONTHLY_FLEXIBLE = "monthly_flexible"
    YEARLY = "yearly"

    def __str__(self) -> str:
        return str(self.value)
