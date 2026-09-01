from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AtsApplicationCv")


@_attrs_define
class AtsApplicationCv:
    """CV file attachment of the application (includes filename, url, byte_size, content_type, created_at)"""

    filename: str
    url: str
    byte_size: int
    content_type: str
    created_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        filename = self.filename

        url = self.url

        byte_size = self.byte_size

        content_type = self.content_type

        created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "filename": filename,
                "url": url,
                "byte_size": byte_size,
                "content_type": content_type,
            }
        )
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        filename = d.pop("filename")

        url = d.pop("url")

        byte_size = d.pop("byte_size")

        content_type = d.pop("content_type")

        created_at = d.pop("created_at", UNSET)

        ats_application_cv = cls(
            filename=filename,
            url=url,
            byte_size=byte_size,
            content_type=content_type,
            created_at=created_at,
        )

        ats_application_cv.additional_properties = d
        return ats_application_cv

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
