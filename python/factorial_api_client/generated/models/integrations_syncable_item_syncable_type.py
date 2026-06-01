from enum import Enum


class IntegrationsSyncableItemSyncableType(str, Enum):
    COMPENSATIONSCOMPENSATION = "compensations/compensation"
    EXPENSESEXPENSE = "expenses/expense"

    def __str__(self) -> str:
        return str(self.value)
