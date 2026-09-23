from enum import Enum


class PostApi20261001ResourcesIntegrationsSyncableSyncRunsBulkUpsertBodyItemsItemStatus(str, Enum):
    FAILED = "failed"
    INVALID = "invalid"
    RUNNING = "running"
    SUCCESS = "success"

    def __str__(self) -> str:
        return str(self.value)
