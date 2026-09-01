from enum import Enum


class IntegrationsSyncableSyncRunStatus(str, Enum):
    FAILED = "failed"
    INVALID = "invalid"
    RUNNING = "running"
    SUCCESS = "success"

    def __str__(self) -> str:
        return str(self.value)
