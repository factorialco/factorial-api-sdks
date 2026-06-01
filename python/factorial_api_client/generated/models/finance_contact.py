from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.finance_contact_preferred_payment_method import FinanceContactPreferredPaymentMethod
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.finance_contact_address import FinanceContactAddress


T = TypeVar("T", bound="FinanceContact")


@_attrs_define
class FinanceContact:
    id: int
    """ Unique identifier for the Contact. """
    name: str
    """ The commercial name of the Contact. """
    address: FinanceContactAddress
    """ The address object containing street, city, etc. """
    updated_at: str
    """ Timestamp when the Contact was last updated. """
    legal_name: str | Unset = UNSET
    """ The official or legal name of the Contact. """
    tax_id: str | Unset = UNSET
    """ Tax identification number assigned to the Contact. """
    external_id: str | Unset = UNSET
    """ The external id of the contact. """
    iban: str | Unset = UNSET
    """ International Bank Account Number if provided. """
    bank_code: str | Unset = UNSET
    """ Bank or branch code for the Contact if relevant. """
    preferred_payment_method: FinanceContactPreferredPaymentMethod | Unset = UNSET
    """ Preferred payment method for the Contact (e.g. wire_transfer, paypal). """
    website: str | Unset = UNSET
    """ The website of the Contact. """
    email: str | Unset = UNSET
    """ The email of the Contact. """
    phone_number: str | Unset = UNSET
    """ The phone number of the Contact. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        address = self.address.to_dict()

        updated_at = self.updated_at

        legal_name = self.legal_name

        tax_id = self.tax_id

        external_id = self.external_id

        iban = self.iban

        bank_code = self.bank_code

        preferred_payment_method: str | Unset = UNSET
        if not isinstance(self.preferred_payment_method, Unset):
            preferred_payment_method = self.preferred_payment_method.value

        website = self.website

        email = self.email

        phone_number = self.phone_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "address": address,
                "updated_at": updated_at,
            }
        )
        if legal_name is not UNSET:
            field_dict["legal_name"] = legal_name
        if tax_id is not UNSET:
            field_dict["tax_id"] = tax_id
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if iban is not UNSET:
            field_dict["iban"] = iban
        if bank_code is not UNSET:
            field_dict["bank_code"] = bank_code
        if preferred_payment_method is not UNSET:
            field_dict["preferred_payment_method"] = preferred_payment_method
        if website is not UNSET:
            field_dict["website"] = website
        if email is not UNSET:
            field_dict["email"] = email
        if phone_number is not UNSET:
            field_dict["phone_number"] = phone_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.finance_contact_address import FinanceContactAddress

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        address = FinanceContactAddress.from_dict(d.pop("address"))

        updated_at = d.pop("updated_at")

        legal_name = d.pop("legal_name", UNSET)

        tax_id = d.pop("tax_id", UNSET)

        external_id = d.pop("external_id", UNSET)

        iban = d.pop("iban", UNSET)

        bank_code = d.pop("bank_code", UNSET)

        _preferred_payment_method = d.pop("preferred_payment_method", UNSET)
        preferred_payment_method: FinanceContactPreferredPaymentMethod | Unset
        if isinstance(_preferred_payment_method, Unset):
            preferred_payment_method = UNSET
        else:
            preferred_payment_method = FinanceContactPreferredPaymentMethod(
                _preferred_payment_method
            )

        website = d.pop("website", UNSET)

        email = d.pop("email", UNSET)

        phone_number = d.pop("phone_number", UNSET)

        finance_contact = cls(
            id=id,
            name=name,
            address=address,
            updated_at=updated_at,
            legal_name=legal_name,
            tax_id=tax_id,
            external_id=external_id,
            iban=iban,
            bank_code=bank_code,
            preferred_payment_method=preferred_payment_method,
            website=website,
            email=email,
            phone_number=phone_number,
        )

        finance_contact.additional_properties = d
        return finance_contact

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
