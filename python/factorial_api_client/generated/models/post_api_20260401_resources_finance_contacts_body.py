from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_api_20260401_resources_finance_contacts_body_address import (
        PostApi20260401ResourcesFinanceContactsBodyAddress,
    )


T = TypeVar("T", bound="PostApi20260401ResourcesFinanceContactsBody")


@_attrs_define
class PostApi20260401ResourcesFinanceContactsBody:
    name: str
    """ The commercial name of the Contact. """
    address: PostApi20260401ResourcesFinanceContactsBodyAddress
    """ The address object containing street, city, etc. """
    tax_id: str | Unset = UNSET
    """ Tax identification number assigned to the Contact. """
    legal_name: str | Unset = UNSET
    """ The official or legal name of the Contact. """
    iban: str | Unset = UNSET
    """ International Bank Account Number if provided. """
    bank_code: str | Unset = UNSET
    """ Bank or branch code for the Contact if relevant. """
    external_id: str | Unset = UNSET
    """ The external id of the contact. """
    project_ids: list[int] | Unset = UNSET
    """ List of project IDs associated with the Contact. """
    website: str | Unset = UNSET
    """ The website of the Contact. """
    email: str | Unset = UNSET
    """ The email of the Contact. """
    phone_number: str | Unset = UNSET
    """ The phone number of the Contact. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        address = self.address.to_dict()

        tax_id = self.tax_id

        legal_name = self.legal_name

        iban = self.iban

        bank_code = self.bank_code

        external_id = self.external_id

        project_ids: list[int] | Unset = UNSET
        if not isinstance(self.project_ids, Unset):
            project_ids = self.project_ids

        website = self.website

        email = self.email

        phone_number = self.phone_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "address": address,
            }
        )
        if tax_id is not UNSET:
            field_dict["tax_id"] = tax_id
        if legal_name is not UNSET:
            field_dict["legal_name"] = legal_name
        if iban is not UNSET:
            field_dict["iban"] = iban
        if bank_code is not UNSET:
            field_dict["bank_code"] = bank_code
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if project_ids is not UNSET:
            field_dict["project_ids"] = project_ids
        if website is not UNSET:
            field_dict["website"] = website
        if email is not UNSET:
            field_dict["email"] = email
        if phone_number is not UNSET:
            field_dict["phone_number"] = phone_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_api_20260401_resources_finance_contacts_body_address import (
            PostApi20260401ResourcesFinanceContactsBodyAddress,
        )

        d = dict(src_dict)
        name = d.pop("name")

        address = PostApi20260401ResourcesFinanceContactsBodyAddress.from_dict(d.pop("address"))

        tax_id = d.pop("tax_id", UNSET)

        legal_name = d.pop("legal_name", UNSET)

        iban = d.pop("iban", UNSET)

        bank_code = d.pop("bank_code", UNSET)

        external_id = d.pop("external_id", UNSET)

        project_ids = cast(list[int], d.pop("project_ids", UNSET))

        website = d.pop("website", UNSET)

        email = d.pop("email", UNSET)

        phone_number = d.pop("phone_number", UNSET)

        post_api_20260401_resources_finance_contacts_body = cls(
            name=name,
            address=address,
            tax_id=tax_id,
            legal_name=legal_name,
            iban=iban,
            bank_code=bank_code,
            external_id=external_id,
            project_ids=project_ids,
            website=website,
            email=email,
            phone_number=phone_number,
        )

        post_api_20260401_resources_finance_contacts_body.additional_properties = d
        return post_api_20260401_resources_finance_contacts_body

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
