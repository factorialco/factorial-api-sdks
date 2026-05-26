from enum import Enum


class PayrollSupplementUnit(str, Enum):
    MONEY = "money"
    TIME = "time"
    UNITS = "units"

    def __str__(self) -> str:
        return str(self.value)
