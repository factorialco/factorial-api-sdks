from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.put_api_20260401_resources_finance_tax_types_id_body_type import (
    PutApi20260401ResourcesFinanceTaxTypesIdBodyType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PutApi20260401ResourcesFinanceTaxTypesIdBody")


@_attrs_define
class PutApi20260401ResourcesFinanceTaxTypesIdBody:
    id: int
    """ The id of the tax type. """
    type_: PutApi20260401ResourcesFinanceTaxTypesIdBodyType
    """ The tax category used to distinguish different tax kinds. """
    name: str | Unset = UNSET
    """ The name assigned to the tax type. """
    country_code: str | Unset = UNSET
    """ The country code where this tax type applies. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_.value

        name = self.name

        country_code = self.country_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if country_code is not UNSET:
            field_dict["country_code"] = country_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        type_ = PutApi20260401ResourcesFinanceTaxTypesIdBodyType(d.pop("type"))

        name = d.pop("name", UNSET)

        country_code = d.pop("country_code", UNSET)

        put_api_20260401_resources_finance_tax_types_id_body = cls(
            id=id,
            type_=type_,
            name=name,
            country_code=country_code,
        )

        put_api_20260401_resources_finance_tax_types_id_body.additional_properties = d
        return put_api_20260401_resources_finance_tax_types_id_body

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
