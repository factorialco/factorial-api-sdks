from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.finance_tax_type_type import FinanceTaxTypeType
from ..types import UNSET, Unset

T = TypeVar("T", bound="FinanceTaxType")


@_attrs_define
class FinanceTaxType:
    id: str
    """ Factorial id """
    name: str
    """ The name assigned to the tax type. """
    type_: FinanceTaxTypeType
    """ The tax category used to distinguish different tax kinds. """
    updated_at: str
    """ Last update date of the tax type. """
    country_code: str | Unset = UNSET
    """ The country code where this tax type applies. """
    external_id: str | Unset = UNSET
    """ The external id of the tax type. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        type_ = self.type_.value

        updated_at = self.updated_at

        country_code = self.country_code

        external_id = self.external_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "type": type_,
                "updated_at": updated_at,
            }
        )
        if country_code is not UNSET:
            field_dict["country_code"] = country_code
        if external_id is not UNSET:
            field_dict["external_id"] = external_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        type_ = FinanceTaxTypeType(d.pop("type"))

        updated_at = d.pop("updated_at")

        country_code = d.pop("country_code", UNSET)

        external_id = d.pop("external_id", UNSET)

        finance_tax_type = cls(
            id=id,
            name=name,
            type_=type_,
            updated_at=updated_at,
            country_code=country_code,
            external_id=external_id,
        )

        finance_tax_type.additional_properties = d
        return finance_tax_type

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
