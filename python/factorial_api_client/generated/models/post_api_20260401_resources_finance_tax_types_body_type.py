from enum import Enum


class PostApi20260401ResourcesFinanceTaxTypesBodyType(str, Enum):
    PERSONAL_INCOME = "personal_income"
    VAT = "vat"

    def __str__(self) -> str:
        return str(self.value)
