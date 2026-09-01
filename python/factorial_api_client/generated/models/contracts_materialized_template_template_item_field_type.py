from enum import Enum


class ContractsMaterializedTemplateTemplateItemFieldType(str, Enum):
    BOOLEAN = "boolean"
    CENTS = "cents"
    INTEGER = "integer"
    OPTION = "option"
    STRING = "string"

    def __str__(self) -> str:
        return str(self.value)
