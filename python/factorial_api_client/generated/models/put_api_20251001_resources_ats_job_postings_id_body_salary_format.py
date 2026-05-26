from enum import Enum


class PutApi20251001ResourcesAtsJobPostingsIdBodySalaryFormat(str, Enum):
    FIXED_AMOUNT = "fixed_amount"
    RANGE = "range"

    def __str__(self) -> str:
        return str(self.value)
