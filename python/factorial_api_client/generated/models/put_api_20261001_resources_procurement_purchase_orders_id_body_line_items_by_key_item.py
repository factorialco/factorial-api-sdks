from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.put_api_20261001_resources_procurement_purchase_orders_id_body_line_items_by_key_item_fields_item import (
        PutApi20261001ResourcesProcurementPurchaseOrdersIdBodyLineItemsByKeyItemFieldsItem,
    )


T = TypeVar("T", bound="PutApi20261001ResourcesProcurementPurchaseOrdersIdBodyLineItemsByKeyItem")


@_attrs_define
class PutApi20261001ResourcesProcurementPurchaseOrdersIdBodyLineItemsByKeyItem:
    position: int
    fields: list[PutApi20261001ResourcesProcurementPurchaseOrdersIdBodyLineItemsByKeyItemFieldsItem]
    id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        position = self.position

        fields = []
        for fields_item_data in self.fields:
            fields_item = fields_item_data.to_dict()
            fields.append(fields_item)

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "position": position,
                "fields": fields,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.put_api_20261001_resources_procurement_purchase_orders_id_body_line_items_by_key_item_fields_item import (
            PutApi20261001ResourcesProcurementPurchaseOrdersIdBodyLineItemsByKeyItemFieldsItem,
        )

        d = dict(src_dict)
        position = d.pop("position")

        fields = []
        _fields = d.pop("fields")
        for fields_item_data in _fields:
            fields_item = PutApi20261001ResourcesProcurementPurchaseOrdersIdBodyLineItemsByKeyItemFieldsItem.from_dict(
                fields_item_data
            )

            fields.append(fields_item)

        id = d.pop("id", UNSET)

        put_api_20261001_resources_procurement_purchase_orders_id_body_line_items_by_key_item = cls(
            position=position,
            fields=fields,
            id=id,
        )

        put_api_20261001_resources_procurement_purchase_orders_id_body_line_items_by_key_item.additional_properties = d
        return put_api_20261001_resources_procurement_purchase_orders_id_body_line_items_by_key_item

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
