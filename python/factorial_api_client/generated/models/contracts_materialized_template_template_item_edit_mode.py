from enum import Enum


class ContractsMaterializedTemplateTemplateItemEditMode(str, Enum):
    ADD_ONLY = "add_only"
    FULL_EDITABLE = "full_editable"
    NOT_EDITABLE = "not_editable"

    def __str__(self) -> str:
        return str(self.value)
