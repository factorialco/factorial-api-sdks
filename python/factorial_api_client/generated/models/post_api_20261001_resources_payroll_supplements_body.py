from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20261001ResourcesPayrollSupplementsBody")


@_attrs_define
class PostApi20261001ResourcesPayrollSupplementsBody:
    amount_in_cents: int
    """ Supplement amount in cents """
    employee_id: str
    """ The employee id of the suplement """
    effective_on: str
    """ Supplement effective on date following the format YYYY-MM-DD """
    contracts_taxonomy_id: str
    """ Supplement contract taxonomy id """
    payroll_policy_period_id: str
    """ Supplement payroll policy period id """
    contracts_compensation_id: str | Unset = UNSET
    """ Supplement contract compensation id """
    unit: str | Unset = UNSET
    """ Supplement unit """
    worked_days: int | Unset = UNSET
    """ Supplement worked days """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount_in_cents = self.amount_in_cents

        employee_id = self.employee_id

        effective_on = self.effective_on

        contracts_taxonomy_id = self.contracts_taxonomy_id

        payroll_policy_period_id = self.payroll_policy_period_id

        contracts_compensation_id = self.contracts_compensation_id

        unit = self.unit

        worked_days = self.worked_days

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "amount_in_cents": amount_in_cents,
                "employee_id": employee_id,
                "effective_on": effective_on,
                "contracts_taxonomy_id": contracts_taxonomy_id,
                "payroll_policy_period_id": payroll_policy_period_id,
            }
        )
        if contracts_compensation_id is not UNSET:
            field_dict["contracts_compensation_id"] = contracts_compensation_id
        if unit is not UNSET:
            field_dict["unit"] = unit
        if worked_days is not UNSET:
            field_dict["worked_days"] = worked_days

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount_in_cents = d.pop("amount_in_cents")

        employee_id = d.pop("employee_id")

        effective_on = d.pop("effective_on")

        contracts_taxonomy_id = d.pop("contracts_taxonomy_id")

        payroll_policy_period_id = d.pop("payroll_policy_period_id")

        contracts_compensation_id = d.pop("contracts_compensation_id", UNSET)

        unit = d.pop("unit", UNSET)

        worked_days = d.pop("worked_days", UNSET)

        post_api_20261001_resources_payroll_supplements_body = cls(
            amount_in_cents=amount_in_cents,
            employee_id=employee_id,
            effective_on=effective_on,
            contracts_taxonomy_id=contracts_taxonomy_id,
            payroll_policy_period_id=payroll_policy_period_id,
            contracts_compensation_id=contracts_compensation_id,
            unit=unit,
            worked_days=worked_days,
        )

        post_api_20261001_resources_payroll_supplements_body.additional_properties = d
        return post_api_20261001_resources_payroll_supplements_body

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
