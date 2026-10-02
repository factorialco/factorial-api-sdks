from enum import Enum


class IntegrationsSyncableStateStatus(str, Enum):
    FAILED = "failed"
    INVALID = "invalid"
    OUTDATED = "outdated"
    SYNCED = "synced"
    SYNCING = "syncing"

    def __str__(self) -> str:
        return str(self.value)
