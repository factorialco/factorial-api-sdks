from enum import Enum


class PostApi20260401ResourcesTimeoffAllowancesBodyAvailableDays(str, Enum):
    ALL_DAYS = "all_days"
    BIMONTHLY_FIFTEENTH_AND_LAST = "bimonthly_fifteenth_and_last"
    BIMONTHLY_FIRST_AND_FIFTEENTH = "bimonthly_first_and_fifteenth"
    GENERATED_DAYS = "generated_days"
    GENERATED_DAYS_MONTHLY = "generated_days_monthly"
    GENERATED_DAYS_MONTHLY_FIRST_DAY = "generated_days_monthly_first_day"
    MENSIVERSARY = "mensiversary"
    MONTHLY_FIFTEENTH = "monthly_fifteenth"

    def __str__(self) -> str:
        return str(self.value)
