from enum import Enum


class TimeSettingsSplitCustomTimeRangeCategoryCategoryType(str, Enum):
    EXTRA_HOUR = "extra_hour"
    SPECIAL_HOUR = "special_hour"

    def __str__(self) -> str:
        return str(self.value)
