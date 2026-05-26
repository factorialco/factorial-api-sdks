from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FinanceTaxRate")


@_attrs_define
class FinanceTaxRate:
    id: int
    """ Factorial id """
    rate: float
    """ Specifies the numerical percentage for the tax rate between -1 and 1. """
    tax_type_id: int
    """ The identifier of the related TaxType record. """
    updated_at: str
    """ Last update date of the tax rate. """
    description: str | Unset = UNSET
    """ An optional text describing the tax rate's purpose or context. """
    external_id: str | Unset = UNSET
    """ The external id of the tax rate. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        rate = self.rate

        tax_type_id = self.tax_type_id

        updated_at = self.updated_at

        description = self.description

        external_id = self.external_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "rate": rate,
                "tax_type_id": tax_type_id,
                "updated_at": updated_at,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if external_id is not UNSET:
            field_dict["external_id"] = external_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        rate = d.pop("rate")

        tax_type_id = d.pop("tax_type_id")

        updated_at = d.pop("updated_at")

        description = d.pop("description", UNSET)

        external_id = d.pop("external_id", UNSET)

        finance_tax_rate = cls(
            id=id,
            rate=rate,
            tax_type_id=tax_type_id,
            updated_at=updated_at,
            description=description,
            external_id=external_id,
        )

        finance_tax_rate.additional_properties = d
        return finance_tax_rate

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
