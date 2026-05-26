from enum import Enum


class ExpensesExpensableReimbursementMethod(str, Enum):
    PAYROLL = "payroll"
    SEPA_TRANSFER = "sepa_transfer"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
