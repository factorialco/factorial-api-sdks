from enum import Enum


class PostApi20260401ResourcesTimeoffAllowancesBodyRangeType(str, Enum):
    EXACT_RANGE = "exact_range"
    EXTRA_NON_WORKING_DAYS_AT_END = "extra_non_working_days_at_end"

    def __str__(self) -> str:
        return str(self.value)
