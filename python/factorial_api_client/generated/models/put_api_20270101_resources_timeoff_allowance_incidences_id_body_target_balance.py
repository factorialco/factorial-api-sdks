from enum import Enum


class PutApi20270101ResourcesTimeoffAllowanceIncidencesIdBodyTargetBalance(str, Enum):
    ACCRUED = "accrued"
    AVAILABLE = "available"

    def __str__(self) -> str:
        return str(self.value)
