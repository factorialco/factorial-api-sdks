from enum import Enum


class PostApi20260701ResourcesTimeoffAllowanceIncidencesBodyTargetBalance(str, Enum):
    ACCRUED = "accrued"
    AVAILABLE = "available"

    def __str__(self) -> str:
        return str(self.value)
