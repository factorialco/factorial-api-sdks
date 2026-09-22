from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20261001ResourcesFinanceFinancialDocumentsBodyLineItemsItem")


@_attrs_define
class PostApi20261001ResourcesFinanceFinancialDocumentsBodyLineItemsItem:
    description: str
    quantity: float
    unit_price_cents: int
    id: str | Unset = UNSET
    tax_rate_id: str | Unset = UNSET
    discount_percentage: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        quantity = self.quantity

        unit_price_cents = self.unit_price_cents

        id = self.id

        tax_rate_id = self.tax_rate_id

        discount_percentage = self.discount_percentage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "quantity": quantity,
                "unit_price_cents": unit_price_cents,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if tax_rate_id is not UNSET:
            field_dict["tax_rate_id"] = tax_rate_id
        if discount_percentage is not UNSET:
            field_dict["discount_percentage"] = discount_percentage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description")

        quantity = d.pop("quantity")

        unit_price_cents = d.pop("unit_price_cents")

        id = d.pop("id", UNSET)

        tax_rate_id = d.pop("tax_rate_id", UNSET)

        discount_percentage = d.pop("discount_percentage", UNSET)

        post_api_20261001_resources_finance_financial_documents_body_line_items_item = cls(
            description=description,
            quantity=quantity,
            unit_price_cents=unit_price_cents,
            id=id,
            tax_rate_id=tax_rate_id,
            discount_percentage=discount_percentage,
        )

        post_api_20261001_resources_finance_financial_documents_body_line_items_item.additional_properties = d
        return post_api_20261001_resources_finance_financial_documents_body_line_items_item

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
