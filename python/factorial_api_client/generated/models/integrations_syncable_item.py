from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.integrations_syncable_item_syncable_type import IntegrationsSyncableItemSyncableType

if TYPE_CHECKING:
    from ..models.integrations_syncable_item_sync_payload import IntegrationsSyncableItemSyncPayload


T = TypeVar("T", bound="IntegrationsSyncableItem")


@_attrs_define
class IntegrationsSyncableItem:
    syncable_sync_run_id: str
    """ identifier of a syncable item within the sync run. Refers to the integrations/syncable_sync_run resource """
    sync_payload: IntegrationsSyncableItemSyncPayload
    """ data of the item to be synced """
    syncable_type: IntegrationsSyncableItemSyncableType
    """ Type of the syncable item """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        syncable_sync_run_id = self.syncable_sync_run_id

        sync_payload = self.sync_payload.to_dict()

        syncable_type = self.syncable_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "syncable_sync_run_id": syncable_sync_run_id,
                "sync_payload": sync_payload,
                "syncable_type": syncable_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.integrations_syncable_item_sync_payload import (
            IntegrationsSyncableItemSyncPayload,
        )

        d = dict(src_dict)
        syncable_sync_run_id = d.pop("syncable_sync_run_id")

        sync_payload = IntegrationsSyncableItemSyncPayload.from_dict(d.pop("sync_payload"))

        syncable_type = IntegrationsSyncableItemSyncableType(d.pop("syncable_type"))

        integrations_syncable_item = cls(
            syncable_sync_run_id=syncable_sync_run_id,
            sync_payload=sync_payload,
            syncable_type=syncable_type,
        )

        integrations_syncable_item.additional_properties = d
        return integrations_syncable_item

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
