from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProcurementPoTemplate")


@_attrs_define
class ProcurementPoTemplate:
    id: str
    """ The id of the PO template """
    company_id: str
    """ Identifier of the company that owns this template """
    name: str
    """ Name of the PO template """
    created_at: str
    """ Time the PO template was created """
    updated_at: str
    """ Time the PO template was last updated """
    created_by_id: str | Unset = UNSET
    """ Employee ID who created this template (null for system templates) """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        company_id = self.company_id

        name = self.name

        created_at = self.created_at

        updated_at = self.updated_at

        created_by_id = self.created_by_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "company_id": company_id,
                "name": name,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        company_id = d.pop("company_id")

        name = d.pop("name")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        created_by_id = d.pop("created_by_id", UNSET)

        procurement_po_template = cls(
            id=id,
            company_id=company_id,
            name=name,
            created_at=created_at,
            updated_at=updated_at,
            created_by_id=created_by_id,
        )

        procurement_po_template.additional_properties = d
        return procurement_po_template

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
