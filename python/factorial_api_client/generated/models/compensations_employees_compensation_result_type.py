from enum import Enum


class CompensationsEmployeesCompensationResultType(str, Enum):
    COMPENSATION = "compensation"
    PAYROLL_RESULT = "payroll_result"

    def __str__(self) -> str:
        return str(self.value)
