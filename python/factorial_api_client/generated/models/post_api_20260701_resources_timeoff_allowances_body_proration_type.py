from enum import Enum


class PostApi20260701ResourcesTimeoffAllowancesBodyProrationType(str, Enum):
    PRORATION_DISABLED = "proration_disabled"
    PRORATION_ENABLED = "proration_enabled"

    def __str__(self) -> str:
        return str(self.value)
