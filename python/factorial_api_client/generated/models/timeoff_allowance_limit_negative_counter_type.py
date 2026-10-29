from enum import Enum


class TimeoffAllowanceLimitNegativeCounterType(str, Enum):
    LIMIT_NEGATIVE_COUNTER = "limit_negative_counter"
    NO_LIMIT = "no_limit"

    def __str__(self) -> str:
        return str(self.value)
