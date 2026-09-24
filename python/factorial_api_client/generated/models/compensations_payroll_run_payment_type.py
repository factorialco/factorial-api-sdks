from enum import Enum


class CompensationsPayrollRunPaymentType(str, Enum):
    BONUS_BENEFIT = "bonus_benefit"
    DELAYED_PAYMENT = "delayed_payment"
    EXTRA_PAY = "extra_pay"
    RATE_DIFFERENCE = "rate_difference"
    REGULAR = "regular"
    SALARY_ADVANCE = "salary_advance"
    SEVERANCE = "severance"

    def __str__(self) -> str:
        return str(self.value)
