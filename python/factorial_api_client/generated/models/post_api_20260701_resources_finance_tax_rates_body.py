from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20260701ResourcesFinanceTaxRatesBody")


@_attrs_define
class PostApi20260701ResourcesFinanceTaxRatesBody:
    description: str | Unset = UNSET
    """ An optional text describing the tax rate's purpose or context. """
    rate: float | Unset = UNSET
    """ Specifies the numerical percentage for the tax rate between -1 and 1. """
    tax_type_id: str | Unset = UNSET
    """ The identifier of the related TaxType record. """
    external_id: str | Unset = UNSET
    """ The external id of the tax rate. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        rate = self.rate

        tax_type_id = self.tax_type_id

        external_id = self.external_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if rate is not UNSET:
            field_dict["rate"] = rate
        if tax_type_id is not UNSET:
            field_dict["tax_type_id"] = tax_type_id
        if external_id is not UNSET:
            field_dict["external_id"] = external_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        rate = d.pop("rate", UNSET)

        tax_type_id = d.pop("tax_type_id", UNSET)

        external_id = d.pop("external_id", UNSET)

        post_api_20260701_resources_finance_tax_rates_body = cls(
            description=description,
            rate=rate,
            tax_type_id=tax_type_id,
            external_id=external_id,
        )

        post_api_20260701_resources_finance_tax_rates_body.additional_properties = d
        return post_api_20260701_resources_finance_tax_rates_body

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
