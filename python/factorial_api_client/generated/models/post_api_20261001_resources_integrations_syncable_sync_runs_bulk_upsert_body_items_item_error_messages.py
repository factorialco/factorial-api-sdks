from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar(
    "T",
    bound="PostApi20261001ResourcesIntegrationsSyncableSyncRunsBulkUpsertBodyItemsItemErrorMessages",
)


@_attrs_define
class PostApi20261001ResourcesIntegrationsSyncableSyncRunsBulkUpsertBodyItemsItemErrorMessages:
    """Error or validation messages for failed rows"""

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        post_api_20261001_resources_integrations_syncable_sync_runs_bulk_upsert_body_items_item_error_messages = cls()

        post_api_20261001_resources_integrations_syncable_sync_runs_bulk_upsert_body_items_item_error_messages.additional_properties = d
        return post_api_20261001_resources_integrations_syncable_sync_runs_bulk_upsert_body_items_item_error_messages

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
