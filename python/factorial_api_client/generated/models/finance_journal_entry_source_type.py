from enum import Enum


class FinanceJournalEntrySourceType(str, Enum):
    ACCOUNT = "account"
    BANK_TRANSACTION = "bank_transaction"
    EXPENSE = "expense"
    FINANCE_RECONCILIATION = "finance_reconciliation"
    INVOICE = "invoice"
    JOURNAL_ENTRY = "journal_entry"
    PAYROLL_RESULT = "payroll_result"
    RECONCILIATION = "reconciliation"

    def __str__(self) -> str:
        return str(self.value)
