from enum import Enum


class PostApi20261001ResourcesFinanceAccountsBodyType(str, Enum):
    BANK = "bank"
    CURRENT_ASSET = "current_asset"
    CURRENT_LIABILITY = "current_liability"
    EQUITY = "equity"
    EXPENSE = "expense"
    INCOME = "income"
    NON_CURRENT_ASSET = "non_current_asset"
    NON_CURRENT_LIABILITY = "non_current_liability"

    def __str__(self) -> str:
        return str(self.value)
