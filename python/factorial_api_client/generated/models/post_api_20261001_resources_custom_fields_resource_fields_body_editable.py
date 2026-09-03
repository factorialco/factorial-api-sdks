from enum import Enum


class PostApi20261001ResourcesCustomFieldsResourceFieldsBodyEditable(str, Enum):
    EVERYBODY = "everybody"
    LEGAL_ENTITY = "legal_entity"
    OWNED = "owned"
    REPORTEES = "reportees"
    TEAM_LEADER = "team_leader"

    def __str__(self) -> str:
        return str(self.value)
