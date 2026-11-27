from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.put_api_20270101_resources_finance_contacts_id_body_contact_types import (
    PutApi20270101ResourcesFinanceContactsIdBodyContactTypes,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.put_api_20270101_resources_finance_contacts_id_body_address import (
        PutApi20270101ResourcesFinanceContactsIdBodyAddress,
    )


T = TypeVar("T", bound="PutApi20270101ResourcesFinanceContactsIdBody")


@_attrs_define
class PutApi20270101ResourcesFinanceContactsIdBody:
    id: str
    """ ID of the Contact to update. """
    address: PutApi20270101ResourcesFinanceContactsIdBodyAddress
    """ The address object containing street, city, etc. Example: { "city": "East Ariana", "country_code": "SC",
    "line1": "93402 Spencer Points", "line2": "Apt. 555", "postal_code": "61471", "state": "Oklahoma" } """
    tax_id: str | Unset = UNSET
    """ Tax identification number assigned to the Contact. """
    legal_name: str | Unset = UNSET
    """ The official or legal name of the Contact. """
    name: str | Unset = UNSET
    """ The commercial name of the Contact. """
    contact_types: PutApi20270101ResourcesFinanceContactsIdBodyContactTypes | Unset = UNSET
    """ Types to add to the Contact, vendor and/or client. A type the Contact already has is kept. """
    website: str | Unset = UNSET
    """ The website of the Contact. """
    email: str | Unset = UNSET
    """ The email of the Contact. """
    phone_number: str | Unset = UNSET
    """ The phone number of the Contact. """
    legal_entity_ids: list[str] | Unset = UNSET
    """ Legal entity IDs the Contact belongs to. Replaces the current set; empty means all of the company's legal
    entities. IDs outside the company are ignored. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        address = self.address.to_dict()

        tax_id = self.tax_id

        legal_name = self.legal_name

        name = self.name

        contact_types: str | Unset = UNSET
        if not isinstance(self.contact_types, Unset):
            contact_types = self.contact_types.value if self.contact_types is not None else None

        website = self.website

        email = self.email

        phone_number = self.phone_number

        legal_entity_ids: list[str] | Unset = UNSET
        if not isinstance(self.legal_entity_ids, Unset):
            legal_entity_ids = self.legal_entity_ids

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
        if contact_types is not UNSET:
            field_dict["contact_types"] = contact_types
        if website is not UNSET:
            field_dict["website"] = website
        if email is not UNSET:
            field_dict["email"] = email
        if phone_number is not UNSET:
            field_dict["phone_number"] = phone_number
        if legal_entity_ids is not UNSET:
            field_dict["legal_entity_ids"] = legal_entity_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.put_api_20270101_resources_finance_contacts_id_body_address import (
            PutApi20270101ResourcesFinanceContactsIdBodyAddress,
        )

        d = dict(src_dict)
        id = d.pop("id")

        address = PutApi20270101ResourcesFinanceContactsIdBodyAddress.from_dict(d.pop("address"))

        tax_id = d.pop("tax_id", UNSET)

        legal_name = d.pop("legal_name", UNSET)

        name = d.pop("name", UNSET)

        _contact_types = d.pop("contact_types", UNSET)
        contact_types: PutApi20270101ResourcesFinanceContactsIdBodyContactTypes | Unset
        if isinstance(_contact_types, Unset):
            contact_types = UNSET
        else:
            contact_types = PutApi20270101ResourcesFinanceContactsIdBodyContactTypes(_contact_types) if _contact_types is not None else None

        website = d.pop("website", UNSET)

        email = d.pop("email", UNSET)

        phone_number = d.pop("phone_number", UNSET)

        legal_entity_ids = cast(list[str], d.pop("legal_entity_ids", UNSET))

        put_api_20270101_resources_finance_contacts_id_body = cls(
            id=id,
            address=address,
            tax_id=tax_id,
            legal_name=legal_name,
            name=name,
            contact_types=contact_types,
            website=website,
            email=email,
            phone_number=phone_number,
            legal_entity_ids=legal_entity_ids,
        )

        put_api_20270101_resources_finance_contacts_id_body.additional_properties = d
        return put_api_20270101_resources_finance_contacts_id_body

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
