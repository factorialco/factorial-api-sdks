from enum import Enum


class GetApi20261001ResourcesFinanceFinancialDocumentsDocumentTypes(str, Enum):
    CREDIT_NOTE = "credit_note"
    INVOICE = "invoice"
    RECEIPT = "receipt"

    def __str__(self) -> str:
        return str(self.value)
