from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProcurementType")


@_attrs_define
class ProcurementType:
    company_id: str
    """ Identifier of the company that owns this type """
    created_at: str
    """ Time the procurement type was created """
    id: str
    """ The id of the type """
    name: str
    """ Name of the procurement type """
    updated_at: str
    """ Time the procurement type was last updated """
    author_id: str | Unset = UNSET
    """ Employee ID who created this type (null for system types) """
    description: str | Unset = UNSET
    """ Description of the procurement type """
    enabled: bool | Unset = UNSET
    """ Defines if a type is enabled """
    identifier: str | Unset = UNSET
    """ System identifier for default types """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company_id = self.company_id

        created_at = self.created_at

        id = self.id

        name = self.name

        updated_at = self.updated_at

        author_id = self.author_id

        description = self.description

        enabled = self.enabled

        identifier = self.identifier

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "company_id": company_id,
                "created_at": created_at,
                "id": id,
                "name": name,
                "updated_at": updated_at,
            }
        )
        if author_id is not UNSET:
            field_dict["author_id"] = author_id
        if description is not UNSET:
            field_dict["description"] = description
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if identifier is not UNSET:
            field_dict["identifier"] = identifier

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        company_id = d.pop("company_id")

        created_at = d.pop("created_at")

        id = d.pop("id")

        name = d.pop("name")

        updated_at = d.pop("updated_at")

        author_id = d.pop("author_id", UNSET)

        description = d.pop("description", UNSET)

        enabled = d.pop("enabled", UNSET)

        identifier = d.pop("identifier", UNSET)

        procurement_type = cls(
            company_id=company_id,
            created_at=created_at,
            id=id,
            name=name,
            updated_at=updated_at,
            author_id=author_id,
            description=description,
            enabled=enabled,
            identifier=identifier,
        )

        procurement_type.additional_properties = d
        return procurement_type

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
