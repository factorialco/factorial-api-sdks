from enum import Enum


class PutApi20251001ResourcesTimeoffAllowancesIdBodyNegativeCounterType(str, Enum):
    NEGATIVE_COUNTER_DISABLED = "negative_counter_disabled"
    NEGATIVE_COUNTER_ENABLED = "negative_counter_enabled"

    def __str__(self) -> str:
        return str(self.value)
