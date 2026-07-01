from enum import Enum


class PutApi20260701ResourcesTimeoffAllowancesIdBodyRangeType(str, Enum):
    EXACT_RANGE = "exact_range"
    EXTRA_NON_WORKING_DAYS_AT_END = "extra_non_working_days_at_end"

    def __str__(self) -> str:
        return str(self.value)
