from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PayrollPolicyPeriod")


@_attrs_define
class PayrollPolicyPeriod:
    id: int
    """ Policy period id """
    starts_on: str
    """ The start date of the policy period """
    policy_id: int
    """ The id of the policy associated with the policy period """
    company_id: int
    """ The id of the company """
    ends_on: str
    """ The start date of the policy period """
    period: str
    """ Period for the policy """
    name: str | Unset = UNSET
    """ Policy name with start and end date """
    status: str | Unset = UNSET
    """ Policy period status """
    policy_name: str | Unset = UNSET
    """ Policy name """
    calculation_started_at: str | Unset = UNSET
    """ The date and time the calculation started """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        starts_on = self.starts_on

        policy_id = self.policy_id

        company_id = self.company_id

        ends_on = self.ends_on

        period = self.period

        name = self.name

        status = self.status

        policy_name = self.policy_name

        calculation_started_at = self.calculation_started_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "starts_on": starts_on,
                "policy_id": policy_id,
                "company_id": company_id,
                "ends_on": ends_on,
                "period": period,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if status is not UNSET:
            field_dict["status"] = status
        if policy_name is not UNSET:
            field_dict["policy_name"] = policy_name
        if calculation_started_at is not UNSET:
            field_dict["calculation_started_at"] = calculation_started_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        starts_on = d.pop("starts_on")

        policy_id = d.pop("policy_id")

        company_id = d.pop("company_id")

        ends_on = d.pop("ends_on")

        period = d.pop("period")

        name = d.pop("name", UNSET)

        status = d.pop("status", UNSET)

        policy_name = d.pop("policy_name", UNSET)

        calculation_started_at = d.pop("calculation_started_at", UNSET)

        payroll_policy_period = cls(
            id=id,
            starts_on=starts_on,
            policy_id=policy_id,
            company_id=company_id,
            ends_on=ends_on,
            period=period,
            name=name,
            status=status,
            policy_name=policy_name,
            calculation_started_at=calculation_started_at,
        )

        payroll_policy_period.additional_properties = d
        return payroll_policy_period

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
