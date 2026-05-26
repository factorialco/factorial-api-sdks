from enum import Enum


class ExpensesPerDiemPayment(str, Enum):
    NOT_REIMBURSABLE = "not_reimbursable"
    REIMBURSABLE = "reimbursable"

    def __str__(self) -> str:
        return str(self.value)
