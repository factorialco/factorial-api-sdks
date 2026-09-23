from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CompensationsCycle")


@_attrs_define
class CompensationsCycle:
    id: str
    """ Unique identifier of the compensation cycle """
    company_id: str
    """ ID of the company that owns the cycle """
    recurrence: str
    """ How often the cycle recurs (e.g. `monthly`) """
    first_payment: str | Unset = UNSET
    """ Date of the first payment in the cycle """
    currency: str | Unset = UNSET
    """ ISO 4217 currency code the cycle pays in """
    country: str | Unset = UNSET
    """ ISO country code the cycle applies to """
    closure_day: int | Unset = UNSET
    """ Day of the period on which the cycle's runs close """
    alerts_day: int | Unset = UNSET
    """ Day of the period on which alerts for the cycle are dispatched """
    archived_at: str | Unset = UNSET
    """ Timestamp of archival (null if active) """
    created_at: str | Unset = UNSET
    """ Timestamp when the cycle record was created """
    updated_at: str | Unset = UNSET
    """ Timestamp when the cycle record was last updated """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        company_id = self.company_id

        recurrence = self.recurrence

        first_payment = self.first_payment

        currency = self.currency

        country = self.country

        closure_day = self.closure_day

        alerts_day = self.alerts_day

        archived_at = self.archived_at

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "company_id": company_id,
                "recurrence": recurrence,
            }
        )
        if first_payment is not UNSET:
            field_dict["first_payment"] = first_payment
        if currency is not UNSET:
            field_dict["currency"] = currency
        if country is not UNSET:
            field_dict["country"] = country
        if closure_day is not UNSET:
            field_dict["closure_day"] = closure_day
        if alerts_day is not UNSET:
            field_dict["alerts_day"] = alerts_day
        if archived_at is not UNSET:
            field_dict["archived_at"] = archived_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        company_id = d.pop("company_id")

        recurrence = d.pop("recurrence")

        first_payment = d.pop("first_payment", UNSET)

        currency = d.pop("currency", UNSET)

        country = d.pop("country", UNSET)

        closure_day = d.pop("closure_day", UNSET)

        alerts_day = d.pop("alerts_day", UNSET)

        archived_at = d.pop("archived_at", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        compensations_cycle = cls(
            id=id,
            company_id=company_id,
            recurrence=recurrence,
            first_payment=first_payment,
            currency=currency,
            country=country,
            closure_day=closure_day,
            alerts_day=alerts_day,
            archived_at=archived_at,
            created_at=created_at,
            updated_at=updated_at,
        )

        compensations_cycle.additional_properties = d
        return compensations_cycle

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
