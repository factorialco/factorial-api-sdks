from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20261001ResourcesProcurementPurchaseOrdersBodyHeaderFieldValuesItem")


@_attrs_define
class PostApi20261001ResourcesProcurementPurchaseOrdersBodyHeaderFieldValuesItem:
    field_key: str
    """ Stable field key of the template field. """
    value: str | Unset = UNSET
    """ Value for the field. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_key = self.field_key

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "field_key": field_key,
            }
        )
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_key = d.pop("field_key")

        value = d.pop("value", UNSET)

        post_api_20261001_resources_procurement_purchase_orders_body_header_field_values_item = cls(
            field_key=field_key,
            value=value,
        )

        post_api_20261001_resources_procurement_purchase_orders_body_header_field_values_item.additional_properties = d
        return post_api_20261001_resources_procurement_purchase_orders_body_header_field_values_item

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
