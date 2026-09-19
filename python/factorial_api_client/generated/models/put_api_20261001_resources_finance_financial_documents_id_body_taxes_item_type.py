from enum import Enum


class PutApi20261001ResourcesFinanceFinancialDocumentsIdBodyTaxesItemType(str, Enum):
    PERSONAL_INCOME = "personal_income"
    VAT = "vat"

    def __str__(self) -> str:
        return str(self.value)
