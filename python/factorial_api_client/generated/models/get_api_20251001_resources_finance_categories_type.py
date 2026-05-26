from enum import Enum


class GetApi20251001ResourcesFinanceCategoriesType(str, Enum):
    ALL = "all"
    EXPENSE = "expense"
    MILEAGE = "mileage"
    PERDIEM = "perdiem"

    def __str__(self) -> str:
        return str(self.value)
