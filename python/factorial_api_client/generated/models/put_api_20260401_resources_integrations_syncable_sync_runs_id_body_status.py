from enum import Enum


class PutApi20260401ResourcesIntegrationsSyncableSyncRunsIdBodyStatus(str, Enum):
    FAILED = "failed"
    INVALID = "invalid"
    SUCCESS = "success"

    def __str__(self) -> str:
        return str(self.value)
