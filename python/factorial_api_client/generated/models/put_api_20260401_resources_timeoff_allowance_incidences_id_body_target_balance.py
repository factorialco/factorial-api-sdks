from enum import Enum


class PutApi20260401ResourcesTimeoffAllowanceIncidencesIdBodyTargetBalance(str, Enum):
    ACCRUED = "accrued"
    AVAILABLE = "available"

    def __str__(self) -> str:
        return str(self.value)
