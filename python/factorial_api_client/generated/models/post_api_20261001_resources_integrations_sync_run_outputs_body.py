from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import File

T = TypeVar("T", bound="PostApi20261001ResourcesIntegrationsSyncRunOutputsBody")


@_attrs_define
class PostApi20261001ResourcesIntegrationsSyncRunOutputsBody:
    sync_run_id: str
    """ Identifier of the sync run this output belongs to """
    file: File
    """ The CSV file to upload as the sync run output """
    file_name: str
    """ Optional custom name for the uploaded file. When omitted, a standardized name is generated. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sync_run_id = self.sync_run_id

        file = self.file.to_tuple()

        file_name = self.file_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sync_run_id": sync_run_id,
                "file": file,
                "file_name": file_name,
            }
        )

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("sync_run_id", (None, str(self.sync_run_id).encode(), "text/plain")))

        files.append(("file", self.file.to_tuple()))

        files.append(("file_name", (None, str(self.file_name).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sync_run_id = d.pop("sync_run_id")

        file = File(payload=BytesIO(d.pop("file")))

        file_name = d.pop("file_name")

        post_api_20261001_resources_integrations_sync_run_outputs_body = cls(
            sync_run_id=sync_run_id,
            file=file,
            file_name=file_name,
        )

        post_api_20261001_resources_integrations_sync_run_outputs_body.additional_properties = d
        return post_api_20261001_resources_integrations_sync_run_outputs_body

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
