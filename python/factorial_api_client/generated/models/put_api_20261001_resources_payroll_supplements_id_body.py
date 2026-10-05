from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PutApi20261001ResourcesPayrollSupplementsIdBody")


@_attrs_define
class PutApi20261001ResourcesPayrollSupplementsIdBody:
    id: str
    """ The supplement id """
    employee_id: str | Unset = UNSET
    """ The employee id of the supplement """
    contracts_compensation_id: str | Unset = UNSET
    """ The supplement contract compensation id """
    contracts_taxonomy_id: str | Unset = UNSET
    """ The supplement contract taxonomy id """
    amount_in_cents: int | Unset = UNSET
    """ Supplement amount in cents """
    effective_on: str | Unset = UNSET
    """ Supplement effective on date following the format YYYY-MM-DD """
    unit: str | Unset = UNSET
    """ Supplement unit """
    payroll_policy_period_id: str | Unset = UNSET
    """ Supplement payroll policy period  id """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        employee_id = self.employee_id

        contracts_compensation_id = self.contracts_compensation_id

        contracts_taxonomy_id = self.contracts_taxonomy_id

        amount_in_cents = self.amount_in_cents

        effective_on = self.effective_on

        unit = self.unit

        payroll_policy_period_id = self.payroll_policy_period_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if employee_id is not UNSET:
            field_dict["employee_id"] = employee_id
        if contracts_compensation_id is not UNSET:
            field_dict["contracts_compensation_id"] = contracts_compensation_id
        if contracts_taxonomy_id is not UNSET:
            field_dict["contracts_taxonomy_id"] = contracts_taxonomy_id
        if amount_in_cents is not UNSET:
            field_dict["amount_in_cents"] = amount_in_cents
        if effective_on is not UNSET:
            field_dict["effective_on"] = effective_on
        if unit is not UNSET:
            field_dict["unit"] = unit
        if payroll_policy_period_id is not UNSET:
            field_dict["payroll_policy_period_id"] = payroll_policy_period_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        employee_id = d.pop("employee_id", UNSET)

        contracts_compensation_id = d.pop("contracts_compensation_id", UNSET)

        contracts_taxonomy_id = d.pop("contracts_taxonomy_id", UNSET)

        amount_in_cents = d.pop("amount_in_cents", UNSET)

        effective_on = d.pop("effective_on", UNSET)

        unit = d.pop("unit", UNSET)

        payroll_policy_period_id = d.pop("payroll_policy_period_id", UNSET)

        put_api_20261001_resources_payroll_supplements_id_body = cls(
            id=id,
            employee_id=employee_id,
            contracts_compensation_id=contracts_compensation_id,
            contracts_taxonomy_id=contracts_taxonomy_id,
            amount_in_cents=amount_in_cents,
            effective_on=effective_on,
            unit=unit,
            payroll_policy_period_id=payroll_policy_period_id,
        )

        put_api_20261001_resources_payroll_supplements_id_body.additional_properties = d
        return put_api_20261001_resources_payroll_supplements_id_body

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
