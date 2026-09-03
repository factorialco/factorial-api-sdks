from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExpensesMileageFilesItem")


@_attrs_define
class ExpensesMileageFilesItem:
    id: str
    filename: str
    byte_size: int
    url: str | Unset = UNSET
    download_url: str | Unset = UNSET
    content_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        filename = self.filename

        byte_size = self.byte_size

        url = self.url

        download_url = self.download_url

        content_type = self.content_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "filename": filename,
                "byte_size": byte_size,
            }
        )
        if url is not UNSET:
            field_dict["url"] = url
        if download_url is not UNSET:
            field_dict["download_url"] = download_url
        if content_type is not UNSET:
            field_dict["content_type"] = content_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        filename = d.pop("filename")

        byte_size = d.pop("byte_size")

        url = d.pop("url", UNSET)

        download_url = d.pop("download_url", UNSET)

        content_type = d.pop("content_type", UNSET)

        expenses_mileage_files_item = cls(
            id=id,
            filename=filename,
            byte_size=byte_size,
            url=url,
            download_url=download_url,
            content_type=content_type,
        )

        expenses_mileage_files_item.additional_properties = d
        return expenses_mileage_files_item

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
