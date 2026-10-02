from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.integrations_syncable_sync_run_status import IntegrationsSyncableSyncRunStatus

if TYPE_CHECKING:
    from ..models.integrations_syncable_sync_run_error_messages_item import (
        IntegrationsSyncableSyncRunErrorMessagesItem,
    )


T = TypeVar("T", bound="IntegrationsSyncableSyncRun")


@_attrs_define
class IntegrationsSyncableSyncRun:
    id: str
    """ Identifier of the syncable sync run """
    status: IntegrationsSyncableSyncRunStatus
    """ Status of the syncable sync run """
    error_messages: list[IntegrationsSyncableSyncRunErrorMessagesItem]
    """ Error or validation messages of the syncable sync run """
    sync_run_id: str
    """ Identifier of the sync run """
    syncable_state_id: str
    """ Identifier of the syncable state this run item is linked to. Refers to the integrations/syncable_state
    resource """
    company_id: str
    """ Identifier of the company """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        status = self.status.value

        error_messages = []
        for error_messages_item_data in self.error_messages:
            error_messages_item = error_messages_item_data.to_dict()
            error_messages.append(error_messages_item)

        sync_run_id = self.sync_run_id

        syncable_state_id = self.syncable_state_id

        company_id = self.company_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "status": status,
                "error_messages": error_messages,
                "sync_run_id": sync_run_id,
                "syncable_state_id": syncable_state_id,
                "company_id": company_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.integrations_syncable_sync_run_error_messages_item import (
            IntegrationsSyncableSyncRunErrorMessagesItem,
        )

        d = dict(src_dict)
        id = d.pop("id")

        status = IntegrationsSyncableSyncRunStatus(d.pop("status"))

        error_messages = []
        _error_messages = d.pop("error_messages")
        for error_messages_item_data in _error_messages:
            error_messages_item = IntegrationsSyncableSyncRunErrorMessagesItem.from_dict(
                error_messages_item_data
            )

            error_messages.append(error_messages_item)

        sync_run_id = d.pop("sync_run_id")

        syncable_state_id = d.pop("syncable_state_id")

        company_id = d.pop("company_id")

        integrations_syncable_sync_run = cls(
            id=id,
            status=status,
            error_messages=error_messages,
            sync_run_id=sync_run_id,
            syncable_state_id=syncable_state_id,
            company_id=company_id,
        )

        integrations_syncable_sync_run.additional_properties = d
        return integrations_syncable_sync_run

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
