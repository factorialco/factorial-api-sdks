from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PutApi20251001ResourcesDocumentsFoldersIdBody")


@_attrs_define
class PutApi20251001ResourcesDocumentsFoldersIdBody:
    company_id: int
    """ Company ID """
    id: int
    """ Folder id """
    name: str
    """ Folder name """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company_id = self.company_id

        id = self.id

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "company_id": company_id,
                "id": id,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        company_id = d.pop("company_id")

        id = d.pop("id")

        name = d.pop("name")

        put_api_20251001_resources_documents_folders_id_body = cls(
            company_id=company_id,
            id=id,
            name=name,
        )

        put_api_20251001_resources_documents_folders_id_body.additional_properties = d
        return put_api_20251001_resources_documents_folders_id_body

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
