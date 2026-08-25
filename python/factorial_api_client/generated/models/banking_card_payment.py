from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.banking_card_payment_rejected_reason import BankingCardPaymentRejectedReason
from ..models.banking_card_payment_status import BankingCardPaymentStatus
from ..models.banking_card_payment_type import BankingCardPaymentType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BankingCardPayment")


@_attrs_define
class BankingCardPayment:
    id: str
    """ The ID of the card payment. """
    card_id: str
    """ The ID of the card. """
    amount_cents: int
    """ The amount of the card payment. """
    currency: str
    """ The currency of the card payment. """
    merchant_name: str
    """ The name of the merchant. """
    merchant_amount_cents: int
    """ The amount of the merchant. """
    merchant_currency: str
    """ The currency of the merchant. """
    approved: bool
    """ Whether the card payment was approved. """
    external_created_at: str
    """ The date and time the card payment was created in the external system. """
    status: BankingCardPaymentStatus
    """ The status of the card payment. """
    type_: BankingCardPaymentType
    """ The type of the card payment. """
    exchange_rate: float
    """ The exchange rate of the card payment. """
    created_at: str
    """ The date and time the card payment was created in factorial """
    rejected_reason: BankingCardPaymentRejectedReason | Unset = UNSET
    """ The reason the card payment was rejected. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        card_id = self.card_id

        amount_cents = self.amount_cents

        currency = self.currency

        merchant_name = self.merchant_name

        merchant_amount_cents = self.merchant_amount_cents

        merchant_currency = self.merchant_currency

        approved = self.approved

        external_created_at = self.external_created_at

        status = self.status.value

        type_ = self.type_.value

        exchange_rate = self.exchange_rate

        created_at = self.created_at

        rejected_reason: str | Unset = UNSET
        if not isinstance(self.rejected_reason, Unset):
            rejected_reason = self.rejected_reason.value if self.rejected_reason is not None else None

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "card_id": card_id,
                "amount_cents": amount_cents,
                "currency": currency,
                "merchant_name": merchant_name,
                "merchant_amount_cents": merchant_amount_cents,
                "merchant_currency": merchant_currency,
                "approved": approved,
                "external_created_at": external_created_at,
                "status": status,
                "type": type_,
                "exchange_rate": exchange_rate,
                "created_at": created_at,
            }
        )
        if rejected_reason is not UNSET:
            field_dict["rejected_reason"] = rejected_reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        card_id = d.pop("card_id")

        amount_cents = d.pop("amount_cents")

        currency = d.pop("currency")

        merchant_name = d.pop("merchant_name")

        merchant_amount_cents = d.pop("merchant_amount_cents")

        merchant_currency = d.pop("merchant_currency")

        approved = d.pop("approved")

        external_created_at = d.pop("external_created_at")

        status = BankingCardPaymentStatus(d.pop("status"))

        type_ = BankingCardPaymentType(d.pop("type"))

        exchange_rate = d.pop("exchange_rate")

        created_at = d.pop("created_at")

        _rejected_reason = d.pop("rejected_reason", UNSET)
        rejected_reason: BankingCardPaymentRejectedReason | Unset
        if isinstance(_rejected_reason, Unset):
            rejected_reason = UNSET
        else:
            rejected_reason = BankingCardPaymentRejectedReason(_rejected_reason) if _rejected_reason is not None else None

        banking_card_payment = cls(
            id=id,
            card_id=card_id,
            amount_cents=amount_cents,
            currency=currency,
            merchant_name=merchant_name,
            merchant_amount_cents=merchant_amount_cents,
            merchant_currency=merchant_currency,
            approved=approved,
            external_created_at=external_created_at,
            status=status,
            type_=type_,
            exchange_rate=exchange_rate,
            created_at=created_at,
            rejected_reason=rejected_reason,
        )

        banking_card_payment.additional_properties = d
        return banking_card_payment

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
