from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.post_api_20261001_resources_procurement_purchase_orders_body_line_items_item_fields_item import (
        PostApi20261001ResourcesProcurementPurchaseOrdersBodyLineItemsItemFieldsItem,
    )


T = TypeVar("T", bound="PostApi20261001ResourcesProcurementPurchaseOrdersBodyLineItemsItem")


@_attrs_define
class PostApi20261001ResourcesProcurementPurchaseOrdersBodyLineItemsItem:
    position: int
    """ Zero-based position of the line item. """
    fields: list[PostApi20261001ResourcesProcurementPurchaseOrdersBodyLineItemsItemFieldsItem]
    """ Line-item values as `{field_key, value}` pairs. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        position = self.position

        fields = []
        for fields_item_data in self.fields:
            fields_item = fields_item_data.to_dict()
            fields.append(fields_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "position": position,
                "fields": fields,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_api_20261001_resources_procurement_purchase_orders_body_line_items_item_fields_item import (
            PostApi20261001ResourcesProcurementPurchaseOrdersBodyLineItemsItemFieldsItem,
        )

        d = dict(src_dict)
        position = d.pop("position")

        fields = []
        _fields = d.pop("fields")
        for fields_item_data in _fields:
            fields_item = PostApi20261001ResourcesProcurementPurchaseOrdersBodyLineItemsItemFieldsItem.from_dict(
                fields_item_data
            )

            fields.append(fields_item)

        post_api_20261001_resources_procurement_purchase_orders_body_line_items_item = cls(
            position=position,
            fields=fields,
        )

        post_api_20261001_resources_procurement_purchase_orders_body_line_items_item.additional_properties = d
        return post_api_20261001_resources_procurement_purchase_orders_body_line_items_item

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
