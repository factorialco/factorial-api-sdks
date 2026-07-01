from enum import Enum


class PutApi20260701ResourcesAtsJobPostingsIdBodySalaryFormat(str, Enum):
    FIXED_AMOUNT = "fixed_amount"
    RANGE = "range"

    def __str__(self) -> str:
        return str(self.value)
