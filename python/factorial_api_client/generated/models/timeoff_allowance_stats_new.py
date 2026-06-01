from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TimeoffAllowanceStatsNew")


@_attrs_define
class TimeoffAllowanceStatsNew:
    id: str
    """ A virtual ID for the allowance stat, composed of employee_id/allowance_id/reference_date. Cannot be used to
    fetch this resource. """
    allowance_id: int
    """ ID of the allowance these stats belong to. """
    employee_id: int
    """ ID of the employee these stats belong to. """
    year: int
    """ Calendar year used to scope cycle calculations. """
    cycles: str
    """ Array with cycle details (legacy hash structure, may change to a typed entity in the future). """
    carry_overs: list[str]
    """ Carry over entries between cycles (serialized array of CycleCarryOver objects). Returned as string in
    GraphQL. """
    accumulated_carry_over: str
    """ Total carried over units accumulated from previous cycles. """
    available_days: str
    """ Remaining days available (after usage and considering carry overs). """
    total_accrued_units: str
    """ Total units accrued up to the reference date. """
    total: str
    """ Total entitlement for the cycle used by the Total row in counters (accrued + carry over + incidences, with
    backend cap/rounding rules applied before incidences). """
    incidences: str
    """ Sum of incidence units (adjustments) applied to this allowance. """
    accrued_incidences: str
    """ Sum of incidence units scoped to 'accrued' target balance for the current cycle, filtered by cycle coverage
    rules. """
    available_incidences: str
    """ Sum of incidence units scoped to non-accrued target balances for the current cycle, filtered by cycle
    coverage rules. """
    policy_allowance: str
    """ Base allowance units defined by the policy (before proration and adjustments). """
    prorated_allowance_days: str
    """ Allowance days after proration based on employee tenure or configuration. """
    used_carry_over: str
    """ Units from carry over already consumed. """
    used_days: str
    """ Total used days (converted from units) up to the reference date. """
    used_units_until_reference_date: str
    """ Units consumed strictly until the given reference date (excludes future approved leaves). """
    outstanding_units: str
    """ Pending units scheduled (approved in the future) not yet counted as used until the reference date. """
    max_balance_cap: str | Unset = UNSET
    """ Maximum balance cap enforced by policy (null if unlimited or no cap). """
    total_in_decimal: str | Unset = UNSET
    """ Total allowance units in decimal form (null if not computed for the reference date yet). """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        allowance_id = self.allowance_id

        employee_id = self.employee_id

        year = self.year

        cycles = self.cycles

        carry_overs = self.carry_overs

        accumulated_carry_over = self.accumulated_carry_over

        available_days = self.available_days

        total_accrued_units = self.total_accrued_units

        total = self.total

        incidences = self.incidences

        accrued_incidences = self.accrued_incidences

        available_incidences = self.available_incidences

        policy_allowance = self.policy_allowance

        prorated_allowance_days = self.prorated_allowance_days

        used_carry_over = self.used_carry_over

        used_days = self.used_days

        used_units_until_reference_date = self.used_units_until_reference_date

        outstanding_units = self.outstanding_units

        max_balance_cap = self.max_balance_cap

        total_in_decimal = self.total_in_decimal

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "allowance_id": allowance_id,
                "employee_id": employee_id,
                "year": year,
                "cycles": cycles,
                "carry_overs": carry_overs,
                "accumulated_carry_over": accumulated_carry_over,
                "available_days": available_days,
                "total_accrued_units": total_accrued_units,
                "total": total,
                "incidences": incidences,
                "accrued_incidences": accrued_incidences,
                "available_incidences": available_incidences,
                "policy_allowance": policy_allowance,
                "prorated_allowance_days": prorated_allowance_days,
                "used_carry_over": used_carry_over,
                "used_days": used_days,
                "used_units_until_reference_date": used_units_until_reference_date,
                "outstanding_units": outstanding_units,
            }
        )
        if max_balance_cap is not UNSET:
            field_dict["max_balance_cap"] = max_balance_cap
        if total_in_decimal is not UNSET:
            field_dict["total_in_decimal"] = total_in_decimal

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        allowance_id = d.pop("allowance_id")

        employee_id = d.pop("employee_id")

        year = d.pop("year")

        cycles = d.pop("cycles")

        carry_overs = cast(list[str], d.pop("carry_overs"))

        accumulated_carry_over = d.pop("accumulated_carry_over")

        available_days = d.pop("available_days")

        total_accrued_units = d.pop("total_accrued_units")

        total = d.pop("total")

        incidences = d.pop("incidences")

        accrued_incidences = d.pop("accrued_incidences")

        available_incidences = d.pop("available_incidences")

        policy_allowance = d.pop("policy_allowance")

        prorated_allowance_days = d.pop("prorated_allowance_days")

        used_carry_over = d.pop("used_carry_over")

        used_days = d.pop("used_days")

        used_units_until_reference_date = d.pop("used_units_until_reference_date")

        outstanding_units = d.pop("outstanding_units")

        max_balance_cap = d.pop("max_balance_cap", UNSET)

        total_in_decimal = d.pop("total_in_decimal", UNSET)

        timeoff_allowance_stats_new = cls(
            id=id,
            allowance_id=allowance_id,
            employee_id=employee_id,
            year=year,
            cycles=cycles,
            carry_overs=carry_overs,
            accumulated_carry_over=accumulated_carry_over,
            available_days=available_days,
            total_accrued_units=total_accrued_units,
            total=total,
            incidences=incidences,
            accrued_incidences=accrued_incidences,
            available_incidences=available_incidences,
            policy_allowance=policy_allowance,
            prorated_allowance_days=prorated_allowance_days,
            used_carry_over=used_carry_over,
            used_days=used_days,
            used_units_until_reference_date=used_units_until_reference_date,
            outstanding_units=outstanding_units,
            max_balance_cap=max_balance_cap,
            total_in_decimal=total_in_decimal,
        )

        timeoff_allowance_stats_new.additional_properties = d
        return timeoff_allowance_stats_new

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
