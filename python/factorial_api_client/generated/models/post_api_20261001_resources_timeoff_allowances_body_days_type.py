from enum import Enum


class PostApi20261001ResourcesTimeoffAllowancesBodyDaysType(str, Enum):
    FRENCH_CALENDAR_DAYS = "french_calendar_days"
    FRENCH_OUVRES = "french_ouvres"
    NATURAL_DAYS = "natural_days"
    NATURAL_DAYS_ONLY_RANGE = "natural_days_only_range"
    WORKING_DAYS = "working_days"

    def __str__(self) -> str:
        return str(self.value)
