from enum import Enum


class ContractsContractActivityPeriodType(str, Enum):
    ACTIVITY = "activity"
    INACTIVITY = "inactivity"

    def __str__(self) -> str:
        return str(self.value)
