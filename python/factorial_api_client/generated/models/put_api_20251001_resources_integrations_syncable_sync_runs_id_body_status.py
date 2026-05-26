from enum import Enum


class PutApi20251001ResourcesIntegrationsSyncableSyncRunsIdBodyStatus(str, Enum):
    FAILED = "failed"
    INVALID = "invalid"
    SUCCESS = "success"

    def __str__(self) -> str:
        return str(self.value)
