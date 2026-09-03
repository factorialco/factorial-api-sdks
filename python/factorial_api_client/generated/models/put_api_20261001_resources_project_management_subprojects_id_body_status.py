from enum import Enum


class PutApi20261001ResourcesProjectManagementSubprojectsIdBodyStatus(str, Enum):
    ACTIVE = "active"
    CLOSED = "closed"
    DRAFT = "draft"
    PROCESSING = "processing"

    def __str__(self) -> str:
        return str(self.value)
