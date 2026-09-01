from enum import Enum


class GetApi20261001ResourcesFinanceCategoriesType(str, Enum):
    ALL = "all"
    EXPENSE = "expense"
    MILEAGE = "mileage"
    PERDIEM = "perdiem"

    def __str__(self) -> str:
        return str(self.value)
