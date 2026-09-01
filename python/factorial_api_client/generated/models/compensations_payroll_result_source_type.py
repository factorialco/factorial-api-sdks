from enum import Enum


class CompensationsPayrollResultSourceType(str, Enum):
    ATTENDANCE_REVIEW = "attendance_review"
    BENEFITS_COMPENSATION = "benefits_compensation"
    COMPENSATIONS_COMPENSATIONPOLICY = "compensations_compensationpolicy"
    EXPENSES_EXPENSABLE = "expenses_expensable"
    EXPENSES_EXPENSE = "expenses_expense"
    EXPENSES_MILEAGE = "expenses_mileage"
    INCENTIVES_COMPENSATIONPLANREQUEST = "incentives_compensationplanrequest"
    SALARY_ADVANCE_REQUEST = "salary_advance_request"
    TIMESETTINGS_CUSTOMTIMERANGECATEGORY = "timesettings_customtimerangecategory"

    def __str__(self) -> str:
        return str(self.value)
