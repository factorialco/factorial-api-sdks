from enum import Enum


class ExpensesExpensableType(str, Enum):
    EXPENSE = "expense"
    MILEAGE = "mileage"
    PERDIEM = "perdiem"

    def __str__(self) -> str:
        return str(self.value)
