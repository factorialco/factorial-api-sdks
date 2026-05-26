from enum import Enum


class CompensationsConceptUnitType(str, Enum):
    DISTANCE = "distance"
    MONEY = "money"
    TIME = "time"
    UNIT = "unit"

    def __str__(self) -> str:
        return str(self.value)
