from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_api_20260401_resources_banking_bank_accounts_create_manual_body_account_number_type import (
    PostApi20260401ResourcesBankingBankAccountsCreateManualBodyAccountNumberType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20260401ResourcesBankingBankAccountsCreateManualBody")


@_attrs_define
class PostApi20260401ResourcesBankingBankAccountsCreateManualBody:
    legal_entity_id: str
    """ Factorial unique identifier of the legal entity. """
    currency: str
    """ Currency of bank account. """
    account_number: str
    """ Account number. """
    account_number_type: (
        PostApi20260401ResourcesBankingBankAccountsCreateManualBodyAccountNumberType
    )
    """ Account number type. """
    account_alias: str | Unset = UNSET
    """ Alias for the bank account. """
    ledger_account_id: int | Unset = UNSET
    """ Factorial unique identifier of the ledger account. """
    bank_account_membership_employee_ids: list[int] | Unset = UNSET
    """ An array of bank account membership employee IDs. """
    external_id: str | Unset = UNSET
    """ External ID for the bank account. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        legal_entity_id = self.legal_entity_id

        currency = self.currency

        account_number = self.account_number

        account_number_type = self.account_number_type.value

        account_alias = self.account_alias

        ledger_account_id = self.ledger_account_id

        bank_account_membership_employee_ids: list[int] | Unset = UNSET
        if not isinstance(self.bank_account_membership_employee_ids, Unset):
            bank_account_membership_employee_ids = self.bank_account_membership_employee_ids

        external_id = self.external_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "legal_entity_id": legal_entity_id,
                "currency": currency,
                "account_number": account_number,
                "account_number_type": account_number_type,
            }
        )
        if account_alias is not UNSET:
            field_dict["account_alias"] = account_alias
        if ledger_account_id is not UNSET:
            field_dict["ledger_account_id"] = ledger_account_id
        if bank_account_membership_employee_ids is not UNSET:
            field_dict["bank_account_membership_employee_ids"] = (
                bank_account_membership_employee_ids
            )
        if external_id is not UNSET:
            field_dict["external_id"] = external_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        legal_entity_id = d.pop("legal_entity_id")

        currency = d.pop("currency")

        account_number = d.pop("account_number")

        account_number_type = (
            PostApi20260401ResourcesBankingBankAccountsCreateManualBodyAccountNumberType(
                d.pop("account_number_type")
            )
        )

        account_alias = d.pop("account_alias", UNSET)

        ledger_account_id = d.pop("ledger_account_id", UNSET)

        bank_account_membership_employee_ids = cast(
            list[int], d.pop("bank_account_membership_employee_ids", UNSET)
        )

        external_id = d.pop("external_id", UNSET)

        post_api_20260401_resources_banking_bank_accounts_create_manual_body = cls(
            legal_entity_id=legal_entity_id,
            currency=currency,
            account_number=account_number,
            account_number_type=account_number_type,
            account_alias=account_alias,
            ledger_account_id=ledger_account_id,
            bank_account_membership_employee_ids=bank_account_membership_employee_ids,
            external_id=external_id,
        )

        post_api_20260401_resources_banking_bank_accounts_create_manual_body.additional_properties = d
        return post_api_20260401_resources_banking_bank_accounts_create_manual_body

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
