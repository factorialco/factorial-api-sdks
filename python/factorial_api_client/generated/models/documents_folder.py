from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DocumentsFolder")


@_attrs_define
class DocumentsFolder:
    active: bool
    """ Whether the folder is active or not """
    id: int
    """ Folder ID """
    name: str
    """ Folder name """
    space: str
    """ The space of the folder is related to the place where the folder is displayed. """
    company_id: int | Unset = UNSET
    """ Company ID of the folder """
    parent_folder_id: int | Unset = UNSET
    """ Id of the parent folder """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active = self.active

        id = self.id

        name = self.name

        space = self.space

        company_id = self.company_id

        parent_folder_id = self.parent_folder_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "active": active,
                "id": id,
                "name": name,
                "space": space,
            }
        )
        if company_id is not UNSET:
            field_dict["company_id"] = company_id
        if parent_folder_id is not UNSET:
            field_dict["parent_folder_id"] = parent_folder_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        active = d.pop("active")

        id = d.pop("id")

        name = d.pop("name")

        space = d.pop("space")

        company_id = d.pop("company_id", UNSET)

        parent_folder_id = d.pop("parent_folder_id", UNSET)

        documents_folder = cls(
            active=active,
            id=id,
            name=name,
            space=space,
            company_id=company_id,
            parent_folder_id=parent_folder_id,
        )

        documents_folder.additional_properties = d
        return documents_folder

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
