from enum import Enum


class PutApi20261001ResourcesCompensationsAdditionalCompensationsIdBodyAmountStrategyType(
    str, Enum
):
    CONTRACTS_FIXED_AMOUNT_STRATEGY = "contracts_fixed_amount_strategy"
    CONTRACTS_PER_WORKED_DAY_AMOUNT_STRATEGY = "contracts_per_worked_day_amount_strategy"
    CONTRACTS_VARIABLE_AMOUNT_STRATEGY = "contracts_variable_amount_strategy"

    def __str__(self) -> str:
        return str(self.value)
