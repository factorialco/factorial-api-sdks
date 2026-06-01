from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.put_api_20260401_resources_integrations_syncable_sync_runs_id_body_status import (
    PutApi20260401ResourcesIntegrationsSyncableSyncRunsIdBodyStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.put_api_20260401_resources_integrations_syncable_sync_runs_id_body_error_messages import (
        PutApi20260401ResourcesIntegrationsSyncableSyncRunsIdBodyErrorMessages,
    )


T = TypeVar("T", bound="PutApi20260401ResourcesIntegrationsSyncableSyncRunsIdBody")


@_attrs_define
class PutApi20260401ResourcesIntegrationsSyncableSyncRunsIdBody:
    id: int
    """ Identifier of the syncable sync run """
    status: PutApi20260401ResourcesIntegrationsSyncableSyncRunsIdBodyStatus
    """ Status of the syncable sync run """
    error_messages: (
        PutApi20260401ResourcesIntegrationsSyncableSyncRunsIdBodyErrorMessages | Unset
    ) = UNSET
    """ Error or validation messages of the syncable sync run """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        status = self.status.value

        error_messages: dict[str, Any] | Unset = UNSET
        if not isinstance(self.error_messages, Unset):
            error_messages = self.error_messages.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "status": status,
            }
        )
        if error_messages is not UNSET:
            field_dict["error_messages"] = error_messages

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.put_api_20260401_resources_integrations_syncable_sync_runs_id_body_error_messages import (
            PutApi20260401ResourcesIntegrationsSyncableSyncRunsIdBodyErrorMessages,
        )

        d = dict(src_dict)
        id = d.pop("id")

        status = PutApi20260401ResourcesIntegrationsSyncableSyncRunsIdBodyStatus(d.pop("status"))

        _error_messages = d.pop("error_messages", UNSET)
        error_messages: (
            PutApi20260401ResourcesIntegrationsSyncableSyncRunsIdBodyErrorMessages | Unset
        )
        if isinstance(_error_messages, Unset):
            error_messages = UNSET
        else:
            error_messages = (
                PutApi20260401ResourcesIntegrationsSyncableSyncRunsIdBodyErrorMessages.from_dict(
                    _error_messages
                )
            )

        put_api_20260401_resources_integrations_syncable_sync_runs_id_body = cls(
            id=id,
            status=status,
            error_messages=error_messages,
        )

        put_api_20260401_resources_integrations_syncable_sync_runs_id_body.additional_properties = d
        return put_api_20260401_resources_integrations_syncable_sync_runs_id_body

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
