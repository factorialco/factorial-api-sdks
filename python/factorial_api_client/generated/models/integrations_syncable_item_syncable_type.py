from enum import Enum


class IntegrationsSyncableItemSyncableType(str, Enum):
    COMPENSATIONSCOMPENSATION = "compensations/compensation"
    EMPLOYEE_UPDATESLEAVE = "employee_updates/leave"
    EMPLOYEE_UPDATESWORKED_TIME = "employee_updates/worked_time"
    EXPENSESEXPENSE = "expenses/expense"
    FINANCEVENDOR = "finance/vendor"

    def __str__(self) -> str:
        return str(self.value)
