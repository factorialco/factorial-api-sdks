from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.integrations_syncable_sync_run_status import IntegrationsSyncableSyncRunStatus

T = TypeVar("T", bound="IntegrationsSyncableSyncRun")


@_attrs_define
class IntegrationsSyncableSyncRun:
    id: int
    """ Identifier of the syncable sync run """
    status: IntegrationsSyncableSyncRunStatus
    """ Status of the syncable sync run """
    error_messages: list[Any]
    """ Error or validation messages of the syncable sync run """
    sync_run_id: int
    """ Identifier of the sync run """
    company_id: int
    """ Identifier of the company """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        status = self.status.value

        error_messages = self.error_messages

        sync_run_id = self.sync_run_id

        company_id = self.company_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "status": status,
                "error_messages": error_messages,
                "sync_run_id": sync_run_id,
                "company_id": company_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        status = IntegrationsSyncableSyncRunStatus(d.pop("status"))

        error_messages = cast(list[Any], d.pop("error_messages"))

        sync_run_id = d.pop("sync_run_id")

        company_id = d.pop("company_id")

        integrations_syncable_sync_run = cls(
            id=id,
            status=status,
            error_messages=error_messages,
            sync_run_id=sync_run_id,
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
