from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.put_api_20260401_resources_finance_contacts_id_body_address import (
        PutApi20260401ResourcesFinanceContactsIdBodyAddress,
    )


T = TypeVar("T", bound="PutApi20260401ResourcesFinanceContactsIdBody")


@_attrs_define
class PutApi20260401ResourcesFinanceContactsIdBody:
    id: int
    """ ID of the Contact to update. """
    address: PutApi20260401ResourcesFinanceContactsIdBodyAddress
    """ The address object containing street, city, etc. Example: { "city": "East Ariana", "country_code": "SC",
    "line1": "93402 Spencer Points", "line2": "Apt. 555", "postal_code": "61471", "state": "Oklahoma" } """
    tax_id: str | Unset = UNSET
    """ Tax identification number assigned to the Contact. """
    legal_name: str | Unset = UNSET
    """ The official or legal name of the Contact. """
    name: str | Unset = UNSET
    """ The commercial name of the Contact. """
    website: str | Unset = UNSET
    """ The website of the Contact. """
    email: str | Unset = UNSET
    """ The email of the Contact. """
    phone_number: str | Unset = UNSET
    """ The phone number of the Contact. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        address = self.address.to_dict()

        tax_id = self.tax_id

        legal_name = self.legal_name

        name = self.name

        website = self.website

        email = self.email

        phone_number = self.phone_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "address": address,
            }
        )
        if tax_id is not UNSET:
            field_dict["tax_id"] = tax_id
        if legal_name is not UNSET:
            field_dict["legal_name"] = legal_name
        if name is not UNSET:
            field_dict["name"] = name
        if website is not UNSET:
            field_dict["website"] = website
        if email is not UNSET:
            field_dict["email"] = email
        if phone_number is not UNSET:
            field_dict["phone_number"] = phone_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.put_api_20260401_resources_finance_contacts_id_body_address import (
            PutApi20260401ResourcesFinanceContactsIdBodyAddress,
        )

        d = dict(src_dict)
        id = d.pop("id")

        address = PutApi20260401ResourcesFinanceContactsIdBodyAddress.from_dict(d.pop("address"))

        tax_id = d.pop("tax_id", UNSET)

        legal_name = d.pop("legal_name", UNSET)

        name = d.pop("name", UNSET)

        website = d.pop("website", UNSET)

        email = d.pop("email", UNSET)

        phone_number = d.pop("phone_number", UNSET)

        put_api_20260401_resources_finance_contacts_id_body = cls(
            id=id,
            address=address,
            tax_id=tax_id,
            legal_name=legal_name,
            name=name,
            website=website,
            email=email,
            phone_number=phone_number,
        )

        put_api_20260401_resources_finance_contacts_id_body.additional_properties = d
        return put_api_20260401_resources_finance_contacts_id_body

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
