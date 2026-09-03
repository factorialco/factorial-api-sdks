from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.post_api_20261001_resources_integrations_syncable_sync_runs_bulk_upsert_body_items_item import (
        PostApi20261001ResourcesIntegrationsSyncableSyncRunsBulkUpsertBodyItemsItem,
    )


T = TypeVar("T", bound="PostApi20261001ResourcesIntegrationsSyncableSyncRunsBulkUpsertBody")


@_attrs_define
class PostApi20261001ResourcesIntegrationsSyncableSyncRunsBulkUpsertBody:
    sync_run_id: str
    """ Identifier of the sync run the reported items belong to """
    items: list[PostApi20261001ResourcesIntegrationsSyncableSyncRunsBulkUpsertBodyItemsItem]
    """ Outcome of each item the external system discovered/processed for this run. Rows are matched by
    (sync_run_id, external_identifier, syncable_type). """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sync_run_id = self.sync_run_id

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sync_run_id": sync_run_id,
                "items": items,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_api_20261001_resources_integrations_syncable_sync_runs_bulk_upsert_body_items_item import (
            PostApi20261001ResourcesIntegrationsSyncableSyncRunsBulkUpsertBodyItemsItem,
        )

        d = dict(src_dict)
        sync_run_id = d.pop("sync_run_id")

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = PostApi20261001ResourcesIntegrationsSyncableSyncRunsBulkUpsertBodyItemsItem.from_dict(
                items_item_data
            )

            items.append(items_item)

        post_api_20261001_resources_integrations_syncable_sync_runs_bulk_upsert_body = cls(
            sync_run_id=sync_run_id,
            items=items,
        )

        post_api_20261001_resources_integrations_syncable_sync_runs_bulk_upsert_body.additional_properties = d
        return post_api_20261001_resources_integrations_syncable_sync_runs_bulk_upsert_body

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
