from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostApi20261001ResourcesDocumentsFoldersBody")


@_attrs_define
class PostApi20261001ResourcesDocumentsFoldersBody:
    company_id: str
    """ Company ID """
    name: str
    """ Folder name """
    space: str
    """ The space of the folder is related to the type of documents that will be stored in it. You should always use
    "employee_my_documents" """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company_id = self.company_id

        name = self.name

        space = self.space

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "company_id": company_id,
                "name": name,
                "space": space,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        company_id = d.pop("company_id")

        name = d.pop("name")

        space = d.pop("space")

        post_api_20261001_resources_documents_folders_body = cls(
            company_id=company_id,
            name=name,
            space=space,
        )

        post_api_20261001_resources_documents_folders_body.additional_properties = d
        return post_api_20261001_resources_documents_folders_body

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
