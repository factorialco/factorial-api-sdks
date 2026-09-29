from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProcurementPoFieldValue")


@_attrs_define
class ProcurementPoFieldValue:
    id: str
    """ The id of the field value """
    company_id: str
    """ Identifier of the company """
    purchase_order_id: str
    """ The purchase order this value belongs to """
    field_definition_id: str
    """ The field definition this value corresponds to """
    created_at: str
    """ When this field value was created """
    updated_at: str
    """ When this field value was last updated """
    line_item_id: str | Unset = UNSET
    """ The line item this value belongs to (null for header-level values) """
    value: str | Unset = UNSET
    """ The stored value as a string (type-cast based on field definition) """
    display_value: str | Unset = UNSET
    """ Human-readable display name for entity-type fields (resolved at read time) """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        company_id = self.company_id

        purchase_order_id = self.purchase_order_id

        field_definition_id = self.field_definition_id

        created_at = self.created_at

        updated_at = self.updated_at

        line_item_id = self.line_item_id

        value = self.value

        display_value = self.display_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "company_id": company_id,
                "purchase_order_id": purchase_order_id,
                "field_definition_id": field_definition_id,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if line_item_id is not UNSET:
            field_dict["line_item_id"] = line_item_id
        if value is not UNSET:
            field_dict["value"] = value
        if display_value is not UNSET:
            field_dict["display_value"] = display_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        company_id = d.pop("company_id")

        purchase_order_id = d.pop("purchase_order_id")

        field_definition_id = d.pop("field_definition_id")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        line_item_id = d.pop("line_item_id", UNSET)

        value = d.pop("value", UNSET)

        display_value = d.pop("display_value", UNSET)

        procurement_po_field_value = cls(
            id=id,
            company_id=company_id,
            purchase_order_id=purchase_order_id,
            field_definition_id=field_definition_id,
            created_at=created_at,
            updated_at=updated_at,
            line_item_id=line_item_id,
            value=value,
            display_value=display_value,
        )

        procurement_po_field_value.additional_properties = d
        return procurement_po_field_value

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
