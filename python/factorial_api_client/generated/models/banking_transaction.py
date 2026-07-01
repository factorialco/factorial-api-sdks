from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.banking_transaction_type import BankingTransactionType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BankingTransaction")


@_attrs_define
class BankingTransaction:
    id: str
    """ Factorial unique identifier. """
    bank_account_id: str
    """ Factorial Banking Bank Account unique identifier. """
    amount_cents: int
    """ Amount in cents. """
    currency: str
    """ Currency. """
    type_: BankingTransactionType
    """ Type of transaction. """
    booking_date: str
    """ Booking date of the transaction. """
    value_date: str
    """ Value date of the transaction. """
    card_payment_id: str
    """ Factorial unique identifier of the card payment. """
    updated_at: str
    """ Date when the transaction was last updated. """
    balance_after_cents: int | Unset = UNSET
    """ Balance after the transaction in cents. """
    description: str | Unset = UNSET
    """ Description of the transaction. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        bank_account_id = self.bank_account_id

        amount_cents = self.amount_cents

        currency = self.currency

        type_ = self.type_.value

        booking_date = self.booking_date

        value_date = self.value_date

        card_payment_id = self.card_payment_id

        updated_at = self.updated_at

        balance_after_cents = self.balance_after_cents

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "bank_account_id": bank_account_id,
                "amount_cents": amount_cents,
                "currency": currency,
                "type": type_,
                "booking_date": booking_date,
                "value_date": value_date,
                "card_payment_id": card_payment_id,
                "updated_at": updated_at,
            }
        )
        if balance_after_cents is not UNSET:
            field_dict["balance_after_cents"] = balance_after_cents
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        bank_account_id = d.pop("bank_account_id")

        amount_cents = d.pop("amount_cents")

        currency = d.pop("currency")

        type_ = BankingTransactionType(d.pop("type"))

        booking_date = d.pop("booking_date")

        value_date = d.pop("value_date")

        card_payment_id = d.pop("card_payment_id")

        updated_at = d.pop("updated_at")

        balance_after_cents = d.pop("balance_after_cents", UNSET)

        description = d.pop("description", UNSET)

        banking_transaction = cls(
            id=id,
            bank_account_id=bank_account_id,
            amount_cents=amount_cents,
            currency=currency,
            type_=type_,
            booking_date=booking_date,
            value_date=value_date,
            card_payment_id=card_payment_id,
            updated_at=updated_at,
            balance_after_cents=balance_after_cents,
            description=description,
        )

        banking_transaction.additional_properties = d
        return banking_transaction

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
