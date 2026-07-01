from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="IntegrationsSyncRunOutput")


@_attrs_define
class IntegrationsSyncRunOutput:
    id: str
    """ Identifier of the sync run output """
    sync_run_id: str
    """ Identifier of the sync run this output belongs to """
    file_name: str
    """ Name of the uploaded file """
    created_at: str
    """ Timestamp when the sync run output was created """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        sync_run_id = self.sync_run_id

        file_name = self.file_name

        created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "sync_run_id": sync_run_id,
                "file_name": file_name,
                "created_at": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        sync_run_id = d.pop("sync_run_id")

        file_name = d.pop("file_name")

        created_at = d.pop("created_at")

        integrations_sync_run_output = cls(
            id=id,
            sync_run_id=sync_run_id,
            file_name=file_name,
            created_at=created_at,
        )

        integrations_sync_run_output.additional_properties = d
        return integrations_sync_run_output

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
