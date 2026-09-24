from enum import Enum


class GetApi20261001ResourcesContractsMaterializedTemplatesTemplateType(str, Enum):
    COMPANY = "company"
    CONTRACT_TYPE = "contract_type"
    COUNTRY = "country"
    LEGAL_ENTITY = "legal_entity"

    def __str__(self) -> str:
        return str(self.value)
