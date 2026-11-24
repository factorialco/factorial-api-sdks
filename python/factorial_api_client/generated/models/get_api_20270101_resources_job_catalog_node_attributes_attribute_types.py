from enum import Enum


class GetApi20270101ResourcesJobCatalogNodeAttributesAttributeTypes(str, Enum):
    ADDITIONAL_COMPENSATION = "additional_compensation"
    COMPETENCY = "competency"
    IT_MANAGEMENT = "it_management"
    SALARY_RANGE = "salary_range"
    WORKING_CONDITIONS = "working_conditions"

    def __str__(self) -> str:
        return str(self.value)
