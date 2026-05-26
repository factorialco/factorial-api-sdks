from enum import Enum


class GetApi20260401ResourcesExpensesExpensablesStatus(str, Enum):
    APPROVED = "approved"
    CHANGES_REQUESTED = "changes_requested"
    DRAFT = "draft"
    IN_PAYROLL = "in_payroll"
    PAID = "paid"
    PENDING = "pending"
    REJECTED = "rejected"
    REVERSED = "reversed"
    SENT_TO_PAY = "sent_to_pay"

    def __str__(self) -> str:
        return str(self.value)
