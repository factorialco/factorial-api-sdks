from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.payroll_supplement_unit import PayrollSupplementUnit
from ..types import UNSET, Unset

T = TypeVar("T", bound="PayrollSupplement")


@_attrs_define
class PayrollSupplement:
    id: int
    """ The identifier of the supplement """
    employee_id: int
    """ The identifier of the employee associated with the supplement """
    company_id: int
    """ The identifier of the company associated with the supplement """
    unit: PayrollSupplementUnit
    """ The unit of the supplement """
    contracts_compensation_id: int | Unset = UNSET
    """ The contract compensation identifier associated with the supplement """
    contracts_taxonomy_id: int | Unset = UNSET
    """ The taxonomy identifier associated with the supplement """
    amount_in_cents: int | Unset = UNSET
    """ The amount of the supplement in cents """
    effective_on: str | Unset = UNSET
    """ The date on which the supplement becomes effective """
    created_at: str | Unset = UNSET
    """ The created at date when the supplement was created """
    updated_at: str | Unset = UNSET
    """ The last updated at date when the supplement was last updated """
    description: str | Unset = UNSET
    """ The description of the supplement """
    payroll_policy_period_id: int | Unset = UNSET
    """ The payroll policy period identifier associated with the supplement """
    employee_observations: list[str] | Unset = UNSET
    """ Observations on the employee made by the admin or manager """
    raw_minutes_in_cents: int | Unset = UNSET
    """ The raw value of minutes in cents associated with the supplement """
    minutes_in_cents: int | Unset = UNSET
    """ The value of minutes in cents after adjustments """
    equivalent_minutes_in_cents: int | Unset = UNSET
    """ The equivalent value of minutes in cents for payroll processing """
    currency: str | Unset = UNSET
    """ The currency used for the supplement, typically in ISO 4217 format """
    legal_entity_id: int | Unset = UNSET
    """ The legal entity identifier associated with the supplement """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        employee_id = self.employee_id

        company_id = self.company_id

        unit = self.unit.value

        contracts_compensation_id = self.contracts_compensation_id

        contracts_taxonomy_id = self.contracts_taxonomy_id

        amount_in_cents = self.amount_in_cents

        effective_on = self.effective_on

        created_at = self.created_at

        updated_at = self.updated_at

        description = self.description

        payroll_policy_period_id = self.payroll_policy_period_id

        employee_observations: list[str] | Unset = UNSET
        if not isinstance(self.employee_observations, Unset):
            employee_observations = self.employee_observations

        raw_minutes_in_cents = self.raw_minutes_in_cents

        minutes_in_cents = self.minutes_in_cents

        equivalent_minutes_in_cents = self.equivalent_minutes_in_cents

        currency = self.currency

        legal_entity_id = self.legal_entity_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "employee_id": employee_id,
                "company_id": company_id,
                "unit": unit,
            }
        )
        if contracts_compensation_id is not UNSET:
            field_dict["contracts_compensation_id"] = contracts_compensation_id
        if contracts_taxonomy_id is not UNSET:
            field_dict["contracts_taxonomy_id"] = contracts_taxonomy_id
        if amount_in_cents is not UNSET:
            field_dict["amount_in_cents"] = amount_in_cents
        if effective_on is not UNSET:
            field_dict["effective_on"] = effective_on
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if description is not UNSET:
            field_dict["description"] = description
        if payroll_policy_period_id is not UNSET:
            field_dict["payroll_policy_period_id"] = payroll_policy_period_id
        if employee_observations is not UNSET:
            field_dict["employee_observations"] = employee_observations
        if raw_minutes_in_cents is not UNSET:
            field_dict["raw_minutes_in_cents"] = raw_minutes_in_cents
        if minutes_in_cents is not UNSET:
            field_dict["minutes_in_cents"] = minutes_in_cents
        if equivalent_minutes_in_cents is not UNSET:
            field_dict["equivalent_minutes_in_cents"] = equivalent_minutes_in_cents
        if currency is not UNSET:
            field_dict["currency"] = currency
        if legal_entity_id is not UNSET:
            field_dict["legal_entity_id"] = legal_entity_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        employee_id = d.pop("employee_id")

        company_id = d.pop("company_id")

        unit = PayrollSupplementUnit(d.pop("unit"))

        contracts_compensation_id = d.pop("contracts_compensation_id", UNSET)

        contracts_taxonomy_id = d.pop("contracts_taxonomy_id", UNSET)

        amount_in_cents = d.pop("amount_in_cents", UNSET)

        effective_on = d.pop("effective_on", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        description = d.pop("description", UNSET)

        payroll_policy_period_id = d.pop("payroll_policy_period_id", UNSET)

        employee_observations = cast(list[str], d.pop("employee_observations", UNSET))

        raw_minutes_in_cents = d.pop("raw_minutes_in_cents", UNSET)

        minutes_in_cents = d.pop("minutes_in_cents", UNSET)

        equivalent_minutes_in_cents = d.pop("equivalent_minutes_in_cents", UNSET)

        currency = d.pop("currency", UNSET)

        legal_entity_id = d.pop("legal_entity_id", UNSET)

        payroll_supplement = cls(
            id=id,
            employee_id=employee_id,
            company_id=company_id,
            unit=unit,
            contracts_compensation_id=contracts_compensation_id,
            contracts_taxonomy_id=contracts_taxonomy_id,
            amount_in_cents=amount_in_cents,
            effective_on=effective_on,
            created_at=created_at,
            updated_at=updated_at,
            description=description,
            payroll_policy_period_id=payroll_policy_period_id,
            employee_observations=employee_observations,
            raw_minutes_in_cents=raw_minutes_in_cents,
            minutes_in_cents=minutes_in_cents,
            equivalent_minutes_in_cents=equivalent_minutes_in_cents,
            currency=currency,
            legal_entity_id=legal_entity_id,
        )

        payroll_supplement.additional_properties = d
        return payroll_supplement

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
