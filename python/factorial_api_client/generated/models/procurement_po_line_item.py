from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ProcurementPoLineItem")


@_attrs_define
class ProcurementPoLineItem:
    id: str
    """ The id of the line item """
    company_id: str
    """ Identifier of the company """
    purchase_order_id: str
    """ The purchase order this line item belongs to """
    position: int
    """ The display position of the line item """
    created_at: str
    """ When this line item was created """
    updated_at: str
    """ When this line item was last updated """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        company_id = self.company_id

        purchase_order_id = self.purchase_order_id

        position = self.position

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "company_id": company_id,
                "purchase_order_id": purchase_order_id,
                "position": position,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        company_id = d.pop("company_id")

        purchase_order_id = d.pop("purchase_order_id")

        position = d.pop("position")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        procurement_po_line_item = cls(
            id=id,
            company_id=company_id,
            purchase_order_id=purchase_order_id,
            position=position,
            created_at=created_at,
            updated_at=updated_at,
        )

        procurement_po_line_item.additional_properties = d
        return procurement_po_line_item

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
