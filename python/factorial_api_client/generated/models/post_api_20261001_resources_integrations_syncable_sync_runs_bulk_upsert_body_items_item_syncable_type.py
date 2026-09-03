from enum import Enum


class PostApi20261001ResourcesIntegrationsSyncableSyncRunsBulkUpsertBodyItemsItemSyncableType(
    str, Enum
):
    COMPENSATIONSCOMPENSATION = "compensationscompensation"
    EMPLOYEEUPDATESLEAVE = "employeeupdatesleave"
    EMPLOYEEUPDATESWORKEDTIME = "employeeupdatesworkedtime"
    EXPENSESEXPENSABLE = "expensesexpensable"
    FINANCECONTACT = "financecontact"

    def __str__(self) -> str:
        return str(self.value)
