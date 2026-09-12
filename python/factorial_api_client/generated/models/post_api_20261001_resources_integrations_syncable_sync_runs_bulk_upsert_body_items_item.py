from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_api_20261001_resources_integrations_syncable_sync_runs_bulk_upsert_body_items_item_status import (
    PostApi20261001ResourcesIntegrationsSyncableSyncRunsBulkUpsertBodyItemsItemStatus,
)
from ..models.post_api_20261001_resources_integrations_syncable_sync_runs_bulk_upsert_body_items_item_syncable_type import (
    PostApi20261001ResourcesIntegrationsSyncableSyncRunsBulkUpsertBodyItemsItemSyncableType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_api_20261001_resources_integrations_syncable_sync_runs_bulk_upsert_body_items_item_error_messages import (
        PostApi20261001ResourcesIntegrationsSyncableSyncRunsBulkUpsertBodyItemsItemErrorMessages,
    )


T = TypeVar(
    "T", bound="PostApi20261001ResourcesIntegrationsSyncableSyncRunsBulkUpsertBodyItemsItem"
)


@_attrs_define
class PostApi20261001ResourcesIntegrationsSyncableSyncRunsBulkUpsertBodyItemsItem:
    external_identifier: str
    """ Identifier of the item in the external system """
    syncable_type: (
        PostApi20261001ResourcesIntegrationsSyncableSyncRunsBulkUpsertBodyItemsItemSyncableType
    )
    """ The Factorial resource type this item maps to """
    status: PostApi20261001ResourcesIntegrationsSyncableSyncRunsBulkUpsertBodyItemsItemStatus
    """ Outcome of processing the item """
    syncable_id: str | Unset = UNSET
    """ The Factorial record this item resolved to (link). Only fills a missing link; re-linking to a different
    record is rejected. """
    error_messages: (
        PostApi20261001ResourcesIntegrationsSyncableSyncRunsBulkUpsertBodyItemsItemErrorMessages
        | Unset
    ) = UNSET
    """ Error or validation messages for failed rows """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        external_identifier = self.external_identifier

        syncable_type = self.syncable_type.value

        status = self.status.value

        syncable_id = self.syncable_id

        error_messages: dict[str, Any] | Unset = UNSET
        if not isinstance(self.error_messages, Unset):
            error_messages = self.error_messages.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "external_identifier": external_identifier,
                "syncable_type": syncable_type,
                "status": status,
            }
        )
        if syncable_id is not UNSET:
            field_dict["syncable_id"] = syncable_id
        if error_messages is not UNSET:
            field_dict["error_messages"] = error_messages

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_api_20261001_resources_integrations_syncable_sync_runs_bulk_upsert_body_items_item_error_messages import (
            PostApi20261001ResourcesIntegrationsSyncableSyncRunsBulkUpsertBodyItemsItemErrorMessages,
        )

        d = dict(src_dict)
        external_identifier = d.pop("external_identifier")

        syncable_type = (
            PostApi20261001ResourcesIntegrationsSyncableSyncRunsBulkUpsertBodyItemsItemSyncableType(
                d.pop("syncable_type")
            )
        )

        status = PostApi20261001ResourcesIntegrationsSyncableSyncRunsBulkUpsertBodyItemsItemStatus(
            d.pop("status")
        )

        syncable_id = d.pop("syncable_id", UNSET)

        _error_messages = d.pop("error_messages", UNSET)
        error_messages: (
            PostApi20261001ResourcesIntegrationsSyncableSyncRunsBulkUpsertBodyItemsItemErrorMessages
            | Unset
        )
        if isinstance(_error_messages, Unset):
            error_messages = UNSET
        else:
            error_messages = PostApi20261001ResourcesIntegrationsSyncableSyncRunsBulkUpsertBodyItemsItemErrorMessages.from_dict(
                _error_messages
            )

        post_api_20261001_resources_integrations_syncable_sync_runs_bulk_upsert_body_items_item = (
            cls(
                external_identifier=external_identifier,
                syncable_type=syncable_type,
                status=status,
                syncable_id=syncable_id,
                error_messages=error_messages,
            )
        )

        post_api_20261001_resources_integrations_syncable_sync_runs_bulk_upsert_body_items_item.additional_properties = d
        return (
            post_api_20261001_resources_integrations_syncable_sync_runs_bulk_upsert_body_items_item
        )

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
