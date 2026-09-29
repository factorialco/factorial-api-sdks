from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ProcurementPurchaseRequestCost")


@_attrs_define
class ProcurementPurchaseRequestCost:
    """Total cost of the purchase request

    Example:
        {'cents': 10000, 'currency': 'EUR'}

    """

    cents: int
    """ Total cost in cents (smallest currency unit) """
    currency: str
    """ Currency code in ISO 4217 format """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cents = self.cents

        currency = self.currency

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cents": cents,
                "currency": currency,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cents = d.pop("cents")

        currency = d.pop("currency")

        procurement_purchase_request_cost = cls(
            cents=cents,
            currency=currency,
        )

        procurement_purchase_request_cost.additional_properties = d
        return procurement_purchase_request_cost

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
