from enum import Enum


class BankingCardPaymentRejectedReason(str, Enum):
    ACCOUNT_COMPLIANCE_DISABLED = "account_compliance_disabled"
    ACCOUNT_DISABLED = "account_disabled"
    ACCOUNT_INACTIVE = "account_inactive"
    AUTHENTICATION_FAILED = "authentication_failed"
    AUTHORIZATION_CONTROLS = "authorization_controls"
    CARDHOLDER_BLOCKED = "cardholder_blocked"
    CARDHOLDER_INACTIVE = "cardholder_inactive"
    CARDHOLDER_VERIFICATION_REQUIRED = "cardholder_verification_required"
    CARD_ACTIVE = "card_active"
    CARD_CANCELED = "card_canceled"
    CARD_EXPIRED = "card_expired"
    CARD_INACTIVE = "card_inactive"
    INCORRECT_CVC = "incorrect_cvc"
    INCORRECT_EXPIRY = "incorrect_expiry"
    INSECURE_AUTHORIZATION_METHOD = "insecure_authorization_method"
    INSUFFICIENT_FUNDS = "insufficient_funds"
    NOT_ALLOWED = "not_allowed"
    PIN_BLOCKED = "pin_blocked"
    SPENDING_CONTROLS = "spending_controls"
    SUSPECTED_FRAUD = "suspected_fraud"
    VERIFICATION_FAILED = "verification_failed"
    WEBHOOK_APPROVED = "webhook_approved"
    WEBHOOK_DECLINED = "webhook_declined"
    WEBHOOK_ERROR = "webhook_error"
    WEBHOOK_TIMEOUT = "webhook_timeout"

    def __str__(self) -> str:
        return str(self.value)
