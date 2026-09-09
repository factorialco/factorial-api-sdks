from enum import Enum


class ContractsMaterializedTemplateTemplateItemDependenciesItemType(str, Enum):
    DYNAMIC_OPTIONS = "dynamic_options"
    VISIBILITY_TOGGLE = "visibility_toggle"

    def __str__(self) -> str:
        return str(self.value)
