from enum import Enum


class GetApi20261001ResourcesCompensationsPayrollRunEmployeesCompensationsResultType(str, Enum):
    COMPENSATION = "compensation"
    PAYROLL_RESULT = "payroll_result"

    def __str__(self) -> str:
        return str(self.value)
