from enum import Enum


class PostApi20260401ResourcesFinanceLedgerAccountResourcesUpsertBodyBalanceType(str, Enum):
    CREDIT = "credit"
    DEBIT = "debit"

    def __str__(self) -> str:
        return str(self.value)
