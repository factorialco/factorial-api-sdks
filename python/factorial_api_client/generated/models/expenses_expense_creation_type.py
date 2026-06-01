from enum import Enum


class ExpensesExpenseCreationType(str, Enum):
    AUTOMATIC = "automatic"
    MANUAL = "manual"
    TRAVELPERK = "travelperk"

    def __str__(self) -> str:
        return str(self.value)
