from enum import Enum


class GetApi20261001ResourcesFinanceJournalLinesJournalEntryTypes(str, Enum):
    BANK = "bank"
    BILL = "bill"
    CREDIT_NOTE = "credit_note"
    EXTERNAL = "external"
    INVOICE = "invoice"
    MERGED_LEDGER_ACCOUNT = "merged_ledger_account"
    PAYROLL_RESULT = "payroll_result"
    RECEIPT = "receipt"
    RECONCILIATION = "reconciliation"
    TAX = "tax"

    def __str__(self) -> str:
        return str(self.value)
