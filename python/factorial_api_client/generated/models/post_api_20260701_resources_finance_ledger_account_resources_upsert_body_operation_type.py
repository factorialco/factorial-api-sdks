from enum import Enum


class PostApi20260701ResourcesFinanceLedgerAccountResourcesUpsertBodyOperationType(str, Enum):
    PURCHASE = "purchase"
    SALE = "sale"

    def __str__(self) -> str:
        return str(self.value)
