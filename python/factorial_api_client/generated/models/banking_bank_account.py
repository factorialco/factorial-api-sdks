from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.banking_bank_account_account_number_type import BankingBankAccountAccountNumberType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BankingBankAccount")


@_attrs_define
class BankingBankAccount:
    id: int
    """ Factorial unique identifier. """
    external_id: str
    """ External ID for the bank account. """
    currency: str
    """ Currency. """
    country: str
    """ Country. """
    account_number: str
    """ Account number. """
    account_number_type: BankingBankAccountAccountNumberType
    """ Account number type. """
    account_balance_cents: int
    """ Account balance in cents. """
    available_balance_cents: int
    """ Available balance in cents. """
    pending_balance_cents: int
    """ Pending balance in cents. """
    updated_at: str
    """ Last updated date. """
    sort_code: str | Unset = UNSET
    """ Sort code. """
    bic: str | Unset = UNSET
    """ Bank Identifier Code. """
    iban: str | Unset = UNSET
    """ International Bank Account Number. """
    routing_number: str | Unset = UNSET
    """ Routing number. """
    beneficiary_name: str | Unset = UNSET
    """ Beneficiary name. """
    bank_name: str | Unset = UNSET
    """ Bank name. """
    account_alias: str | Unset = UNSET
    """ Account alias. """
    legal_entity_id: int | Unset = UNSET
    """ Factorial unique identifier of the legal entity. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        external_id = self.external_id

        currency = self.currency

        country = self.country

        account_number = self.account_number

        account_number_type = self.account_number_type.value

        account_balance_cents = self.account_balance_cents

        available_balance_cents = self.available_balance_cents

        pending_balance_cents = self.pending_balance_cents

        updated_at = self.updated_at

        sort_code = self.sort_code

        bic = self.bic

        iban = self.iban

        routing_number = self.routing_number

        beneficiary_name = self.beneficiary_name

        bank_name = self.bank_name

        account_alias = self.account_alias

        legal_entity_id = self.legal_entity_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "external_id": external_id,
                "currency": currency,
                "country": country,
                "account_number": account_number,
                "account_number_type": account_number_type,
                "account_balance_cents": account_balance_cents,
                "available_balance_cents": available_balance_cents,
                "pending_balance_cents": pending_balance_cents,
                "updated_at": updated_at,
            }
        )
        if sort_code is not UNSET:
            field_dict["sort_code"] = sort_code
        if bic is not UNSET:
            field_dict["bic"] = bic
        if iban is not UNSET:
            field_dict["iban"] = iban
        if routing_number is not UNSET:
            field_dict["routing_number"] = routing_number
        if beneficiary_name is not UNSET:
            field_dict["beneficiary_name"] = beneficiary_name
        if bank_name is not UNSET:
            field_dict["bank_name"] = bank_name
        if account_alias is not UNSET:
            field_dict["account_alias"] = account_alias
        if legal_entity_id is not UNSET:
            field_dict["legal_entity_id"] = legal_entity_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        external_id = d.pop("external_id")

        currency = d.pop("currency")

        country = d.pop("country")

        account_number = d.pop("account_number")

        account_number_type = BankingBankAccountAccountNumberType(d.pop("account_number_type"))

        account_balance_cents = d.pop("account_balance_cents")

        available_balance_cents = d.pop("available_balance_cents")

        pending_balance_cents = d.pop("pending_balance_cents")

        updated_at = d.pop("updated_at")

        sort_code = d.pop("sort_code", UNSET)

        bic = d.pop("bic", UNSET)

        iban = d.pop("iban", UNSET)

        routing_number = d.pop("routing_number", UNSET)

        beneficiary_name = d.pop("beneficiary_name", UNSET)

        bank_name = d.pop("bank_name", UNSET)

        account_alias = d.pop("account_alias", UNSET)

        legal_entity_id = d.pop("legal_entity_id", UNSET)

        banking_bank_account = cls(
            id=id,
            external_id=external_id,
            currency=currency,
            country=country,
            account_number=account_number,
            account_number_type=account_number_type,
            account_balance_cents=account_balance_cents,
            available_balance_cents=available_balance_cents,
            pending_balance_cents=pending_balance_cents,
            updated_at=updated_at,
            sort_code=sort_code,
            bic=bic,
            iban=iban,
            routing_number=routing_number,
            beneficiary_name=beneficiary_name,
            bank_name=bank_name,
            account_alias=account_alias,
            legal_entity_id=legal_entity_id,
        )

        banking_bank_account.additional_properties = d
        return banking_bank_account

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
