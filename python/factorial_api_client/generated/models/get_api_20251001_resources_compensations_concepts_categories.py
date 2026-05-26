from enum import Enum


class GetApi20251001ResourcesCompensationsConceptsCategories(str, Enum):
    COMPANY_CONTRIBUTION = "company_contribution"
    DEDUCTIONS = "deductions"
    EARNINGS_BENEFITS_IN_KIND = "earnings_benefits_in_kind"
    EARNINGS_FIXED_SALARY = "earnings_fixed_salary"
    EARNINGS_OTHERS = "earnings_others"
    EARNINGS_VARIABLE = "earnings_variable"
    SUMMARIZED_VALUES = "summarized_values"

    def __str__(self) -> str:
        return str(self.value)
