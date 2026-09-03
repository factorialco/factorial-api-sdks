from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.integrations_syncable_state_status import IntegrationsSyncableStateStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.integrations_syncable_state_error_messages_item import (
        IntegrationsSyncableStateErrorMessagesItem,
    )


T = TypeVar("T", bound="IntegrationsSyncableState")


@_attrs_define
class IntegrationsSyncableState:
    id: str
    """ Identifier of the syncable state """
    resource_syncable_type: str
    """ The resource type of the linked record, in "namespace/resource" form """
    integration_uuid: str
    """ UUID of the marketplace integration """
    status: IntegrationsSyncableStateStatus
    """ Synchronization status of the record """
    error_messages: list[IntegrationsSyncableStateErrorMessagesItem]
    """ Error or validation messages of the syncable state """
    status_updated_at: str
    """ Timestamp of the last status change """
    syncable_id: str | Unset = UNSET
    """ Identifier of the Factorial record this state is linked to """
    external_identifier: str | Unset = UNSET
    """ Identifier of the record in the external system """
    syncable_deleted_at: str | Unset = UNSET
    """ Timestamp when the linked Factorial record was deleted, if any """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        resource_syncable_type = self.resource_syncable_type

        integration_uuid = self.integration_uuid

        status = self.status.value

        error_messages = []
        for error_messages_item_data in self.error_messages:
            error_messages_item = error_messages_item_data.to_dict()
            error_messages.append(error_messages_item)

        status_updated_at = self.status_updated_at

        syncable_id = self.syncable_id

        external_identifier = self.external_identifier

        syncable_deleted_at = self.syncable_deleted_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "resource_syncable_type": resource_syncable_type,
                "integration_uuid": integration_uuid,
                "status": status,
                "error_messages": error_messages,
                "status_updated_at": status_updated_at,
            }
        )
        if syncable_id is not UNSET:
            field_dict["syncable_id"] = syncable_id
        if external_identifier is not UNSET:
            field_dict["external_identifier"] = external_identifier
        if syncable_deleted_at is not UNSET:
            field_dict["syncable_deleted_at"] = syncable_deleted_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.integrations_syncable_state_error_messages_item import (
            IntegrationsSyncableStateErrorMessagesItem,
        )

        d = dict(src_dict)
        id = d.pop("id")

        resource_syncable_type = d.pop("resource_syncable_type")

        integration_uuid = d.pop("integration_uuid")

        status = IntegrationsSyncableStateStatus(d.pop("status"))

        error_messages = []
        _error_messages = d.pop("error_messages")
        for error_messages_item_data in _error_messages:
            error_messages_item = IntegrationsSyncableStateErrorMessagesItem.from_dict(
                error_messages_item_data
            )

            error_messages.append(error_messages_item)

        status_updated_at = d.pop("status_updated_at")

        syncable_id = d.pop("syncable_id", UNSET)

        external_identifier = d.pop("external_identifier", UNSET)

        syncable_deleted_at = d.pop("syncable_deleted_at", UNSET)

        integrations_syncable_state = cls(
            id=id,
            resource_syncable_type=resource_syncable_type,
            integration_uuid=integration_uuid,
            status=status,
            error_messages=error_messages,
            status_updated_at=status_updated_at,
            syncable_id=syncable_id,
            external_identifier=external_identifier,
            syncable_deleted_at=syncable_deleted_at,
        )

        integrations_syncable_state.additional_properties = d
        return integrations_syncable_state

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
