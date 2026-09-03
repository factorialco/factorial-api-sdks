from enum import Enum


class PutApi20261001ResourcesFinanceFinancialDocumentsIdBodyStatus(str, Enum):
    PAID = "paid"
    PROCESSING = "processing"
    REVIEW = "review"
    SENT_TO_PAY = "sent_to_pay"

    def __str__(self) -> str:
        return str(self.value)
