from enum import Enum


class TimeoffAllowanceTenurePeriodsItemBalanceType(str, Enum):
    FIXED_BALANCE = "fixed_balance"
    TIME_WORKED_BASED = "time_worked_based"

    def __str__(self) -> str:
        return str(self.value)
