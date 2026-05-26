from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PutApi20251001ResourcesFinanceContactsIdBodyAddress")


@_attrs_define
class PutApi20251001ResourcesFinanceContactsIdBodyAddress:
    """The address object containing street, city, etc. Example: { "city": "East Ariana", "country_code": "SC", "line1":
    "93402 Spencer Points", "line2": "Apt. 555", "postal_code": "61471", "state": "Oklahoma" }

        Example:
            {'city': 'East Ariana', 'country_code': 'SC', 'line1': '93402 Spencer Points', 'line2': 'Apt. 555',
                'postal_code': '61471', 'state': 'Oklahoma'}

    """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        put_api_20251001_resources_finance_contacts_id_body_address = cls()

        put_api_20251001_resources_finance_contacts_id_body_address.additional_properties = d
        return put_api_20251001_resources_finance_contacts_id_body_address

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
