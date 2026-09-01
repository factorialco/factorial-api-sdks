from enum import Enum


class PostApi20261001ResourcesTrainingsSessionsBodyRemindersItemTimeframe(str, Enum):
    CUSTOM = "custom"
    ONEDAY = "oneday"
    ONEHOUR = "onehour"
    ONEWEEK = "oneweek"
    THREEDAYS = "threedays"
    TWODAYS = "twodays"

    def __str__(self) -> str:
        return str(self.value)
