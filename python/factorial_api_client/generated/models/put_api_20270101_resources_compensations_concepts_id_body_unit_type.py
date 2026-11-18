from enum import Enum


class PutApi20270101ResourcesCompensationsConceptsIdBodyUnitType(str, Enum):
    DISTANCE = "distance"
    MONEY = "money"
    TIME = "time"
    UNIT = "unit"

    def __str__(self) -> str:
        return str(self.value)
