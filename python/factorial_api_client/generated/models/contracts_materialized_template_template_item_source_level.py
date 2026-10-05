from enum import Enum


class ContractsMaterializedTemplateTemplateItemSourceLevel(str, Enum):
    COMPANY = "company"
    COUNTRY = "country"
    LEGAL_ENTITY = "legal_entity"

    def __str__(self) -> str:
        return str(self.value)
