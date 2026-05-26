from enum import Enum


class BankingTransactionType(str, Enum):
    CARD_PAYMENT = "card_payment"
    CARD_REFUND = "card_refund"
    DISPUTE = "dispute"
    FEES = "fees"
    INCOMING = "incoming"
    INCOMING_TRANSFER = "incoming_transfer"
    OUTGOING = "outgoing"
    OUTGOING_TRANSFER = "outgoing_transfer"
    PAYMENT = "payment"
    PAYROLL = "payroll"
    TOPUP = "topup"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
