from enum import Enum


class PutApi20261001ResourcesCompensationsEmployeesCompensationsIdBodyStrategyType(str, Enum):
    COMPENSATIONS_FIXED_AMOUNT_STRATEGY = "compensations_fixed_amount_strategy"
    COMPENSATIONS_PER_WORKED_DAY_AMOUNT_STRATEGY = "compensations_per_worked_day_amount_strategy"
    COMPENSATIONS_VARIABLE_AMOUNT_STRATEGY = "compensations_variable_amount_strategy"

    def __str__(self) -> str:
        return str(self.value)
