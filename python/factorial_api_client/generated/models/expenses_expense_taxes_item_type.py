from enum import Enum


class ExpensesExpenseTaxesItemType(str, Enum):
    VAT = "vat"

    def __str__(self) -> str:
        return str(self.value)
