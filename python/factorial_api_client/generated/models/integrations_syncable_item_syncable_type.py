from enum import Enum


class IntegrationsSyncableItemSyncableType(str, Enum):
    COMPENSATIONSCOMPENSATION = "compensations/compensation"
    EMPLOYEE_UPDATESLEAVE = "employee_updates/leave"
    EXPENSESEXPENSE = "expenses/expense"
    FINANCEVENDOR = "finance/vendor"

    def __str__(self) -> str:
        return str(self.value)
