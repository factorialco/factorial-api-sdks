from enum import Enum


class PostApi20261001ResourcesPayrollPolicyPeriodsChangeStatusBodyStatus(str, Enum):
    PAID = "paid"
    PAYMENT_PROCESSING = "payment_processing"
    PAYROLL_CALCULATION = "payroll_calculation"
    PREPARATION = "preparation"
    SUPPLEMENTS_DEFINITION = "supplements_definition"
    UNDER_REVIEW = "under_review"

    def __str__(self) -> str:
        return str(self.value)
