from enum import Enum


class FinanceLedgerAccountResourceResourceType(str, Enum):
    BANKACCOUNT = "bankaccount"
    CUSTOMCATEGORY = "customcategory"
    INVOICE = "invoice"
    PAYROLLCONCEPT = "payrollconcept"
    TAXTYPE = "taxtype"
    VENDOR = "vendor"

    def __str__(self) -> str:
        return str(self.value)
