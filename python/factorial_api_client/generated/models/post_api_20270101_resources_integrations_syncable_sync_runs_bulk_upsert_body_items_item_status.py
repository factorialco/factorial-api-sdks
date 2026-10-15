from enum import Enum


class PostApi20270101ResourcesIntegrationsSyncableSyncRunsBulkUpsertBodyItemsItemStatus(str, Enum):
    FAILED = "failed"
    INVALID = "invalid"
    RUNNING = "running"
    SUCCESS = "success"

    def __str__(self) -> str:
        return str(self.value)
