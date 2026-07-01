from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_api_20260701_resources_finance_tax_types_body_type import (
    PostApi20260701ResourcesFinanceTaxTypesBodyType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20260701ResourcesFinanceTaxTypesBody")


@_attrs_define
class PostApi20260701ResourcesFinanceTaxTypesBody:
    name: str
    """ The name assigned to the tax type. """
    type_: PostApi20260701ResourcesFinanceTaxTypesBodyType
    """ The tax category used to distinguish different tax kinds. """
    country_code: str | Unset = UNSET
    """ The country code where this tax type applies. """
    external_id: str | Unset = UNSET
    """ The external id of the tax type. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_.value

        country_code = self.country_code

        external_id = self.external_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "type": type_,
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
        name = d.pop("name")

        type_ = PostApi20260701ResourcesFinanceTaxTypesBodyType(d.pop("type"))

        country_code = d.pop("country_code", UNSET)

        external_id = d.pop("external_id", UNSET)

        post_api_20260701_resources_finance_tax_types_body = cls(
            name=name,
            type_=type_,
            country_code=country_code,
            external_id=external_id,
        )

        post_api_20260701_resources_finance_tax_types_body.additional_properties = d
        return post_api_20260701_resources_finance_tax_types_body

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
