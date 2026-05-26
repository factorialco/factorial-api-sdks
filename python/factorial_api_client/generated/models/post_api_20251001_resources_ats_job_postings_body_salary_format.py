from enum import Enum


class PostApi20251001ResourcesAtsJobPostingsBodySalaryFormat(str, Enum):
    FIXED_AMOUNT = "fixed_amount"
    RANGE = "range"

    def __str__(self) -> str:
        return str(self.value)
