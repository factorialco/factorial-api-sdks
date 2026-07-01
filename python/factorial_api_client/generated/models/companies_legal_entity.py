from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CompaniesLegalEntity")


@_attrs_define
class CompaniesLegalEntity:
    id: str
    """ identifier of the legal entity """
    company_id: str
    """ company identifier """
    country: str
    """ Country code of the jurisdiction the legal entity is registered in (lowercase two-letter code, e.g. "es").
    """
    legal_name: str
    """ Legal name of the legal entity """
    currency: str
    """ The currency code in ISO 4217 format """
    tin: str | Unset = UNSET
    """ Tax identification number """
    city: str | Unset = UNSET
    """ City of the legal entity """
    state: str | Unset = UNSET
    """ State of the legal entity """
    postal_code: str | Unset = UNSET
    """ Postal code of the legal entity """
    address_line_1: str | Unset = UNSET
    """ Address line 1 of the legal entity """
    address_line_2: str | Unset = UNSET
    """ Address line 2 of the legal entity """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        company_id = self.company_id

        country = self.country

        legal_name = self.legal_name

        currency = self.currency

        tin = self.tin

        city = self.city

        state = self.state

        postal_code = self.postal_code

        address_line_1 = self.address_line_1

        address_line_2 = self.address_line_2

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "company_id": company_id,
                "country": country,
                "legal_name": legal_name,
                "currency": currency,
            }
        )
        if tin is not UNSET:
            field_dict["tin"] = tin
        if city is not UNSET:
            field_dict["city"] = city
        if state is not UNSET:
            field_dict["state"] = state
        if postal_code is not UNSET:
            field_dict["postal_code"] = postal_code
        if address_line_1 is not UNSET:
            field_dict["address_line_1"] = address_line_1
        if address_line_2 is not UNSET:
            field_dict["address_line_2"] = address_line_2

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        company_id = d.pop("company_id")

        country = d.pop("country")

        legal_name = d.pop("legal_name")

        currency = d.pop("currency")

        tin = d.pop("tin", UNSET)

        city = d.pop("city", UNSET)

        state = d.pop("state", UNSET)

        postal_code = d.pop("postal_code", UNSET)

        address_line_1 = d.pop("address_line_1", UNSET)

        address_line_2 = d.pop("address_line_2", UNSET)

        companies_legal_entity = cls(
            id=id,
            company_id=company_id,
            country=country,
            legal_name=legal_name,
            currency=currency,
            tin=tin,
            city=city,
            state=state,
            postal_code=postal_code,
            address_line_1=address_line_1,
            address_line_2=address_line_2,
        )

        companies_legal_entity.additional_properties = d
        return companies_legal_entity

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
