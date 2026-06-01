from enum import Enum


class PostApi20260401ResourcesTimeoffAllowancesBodyTenurePeriodTransition(str, Enum):
    AFTER_MILESTONE = "after_milestone"
    BEGINNING_OF_CYCLE = "beginning_of_cycle"
    END_OF_CYCLE = "end_of_cycle"

    def __str__(self) -> str:
        return str(self.value)
