from enum import Enum


class ProjectManagementBudgetStrategyBudgetType(str, Enum):
    PROJECT_FIXED_COST = "project_fixed_cost"
    TOTAL_BUDGET = "total_budget"
    WITHOUT_BUDGET = "without_budget"

    def __str__(self) -> str:
        return str(self.value)
