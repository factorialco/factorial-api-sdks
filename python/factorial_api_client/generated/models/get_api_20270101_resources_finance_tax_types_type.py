from enum import Enum


class GetApi20270101ResourcesFinanceTaxTypesType(str, Enum):
    PERSONAL_INCOME = "personal_income"
    VAT = "vat"

    def __str__(self) -> str:
        return str(self.value)
