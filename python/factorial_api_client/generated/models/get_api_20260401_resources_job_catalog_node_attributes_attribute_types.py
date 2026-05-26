from enum import Enum


class GetApi20260401ResourcesJobCatalogNodeAttributesAttributeTypes(str, Enum):
    COMPETENCY = "competency"
    IT_MANAGEMENT = "it_management"
    SALARY_RANGE = "salary_range"
    WORKING_CONDITIONS = "working_conditions"

    def __str__(self) -> str:
        return str(self.value)
