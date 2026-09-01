from enum import Enum


class PutApi20261001ResourcesTimeoffAllowanceIncidencesIdBodyTargetBalance(str, Enum):
    ACCRUED = "accrued"
    AVAILABLE = "available"

    def __str__(self) -> str:
        return str(self.value)
