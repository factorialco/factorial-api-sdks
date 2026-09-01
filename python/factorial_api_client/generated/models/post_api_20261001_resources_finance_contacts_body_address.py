from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20261001ResourcesFinanceContactsBodyAddress")


@_attrs_define
class PostApi20261001ResourcesFinanceContactsBodyAddress:
    """The address object containing street, city, etc.

    Example:
        {'city': 'East Ariana', 'country_code': 'SC', 'line1': '93402 Spencer Points', 'line2': 'Apt. 555',
            'postal_code': '61471', 'state': 'Oklahoma'}

    """

    line1: str
    """ Street address line 1. """
    city: str
    """ City where the Contact is located. """
    postal_code: str
    """ Postal or ZIP code. """
    state: str
    """ State or region for the Contact. """
    country_code: str
    """ Two-letter ISO country code. """
    line2: str | Unset = UNSET
    """ Street address line 2 or additional info. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        line1 = self.line1

        city = self.city

        postal_code = self.postal_code

        state = self.state

        country_code = self.country_code

        line2 = self.line2

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "line1": line1,
                "city": city,
                "postal_code": postal_code,
                "state": state,
                "country_code": country_code,
            }
        )
        if line2 is not UNSET:
            field_dict["line2"] = line2

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        line1 = d.pop("line1")

        city = d.pop("city")

        postal_code = d.pop("postal_code")

        state = d.pop("state")

        country_code = d.pop("country_code")

        line2 = d.pop("line2", UNSET)

        post_api_20261001_resources_finance_contacts_body_address = cls(
            line1=line1,
            city=city,
            postal_code=postal_code,
            state=state,
            country_code=country_code,
            line2=line2,
        )

        post_api_20261001_resources_finance_contacts_body_address.additional_properties = d
        return post_api_20261001_resources_finance_contacts_body_address

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
