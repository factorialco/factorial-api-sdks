from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TimeoffAllowanceIncidence")


@_attrs_define
class TimeoffAllowanceIncidence:
    id: str
    """ Unique identifier of the allowance incidence """
    employee_id: str
    """ Employee id of the affected employee """
    days_in_cents: int
    """ How many units * 100 does the incidence add/substract. Can be positive or negative. Example is one unit """
    timeoff_allowance_id: str
    """ To what allowance does the incidence affect. It will dictate if its days or hours """
    effective_on: str
    """ When does the incidence take effect; this is for time off cycles calculations. """
    created_at: int
    """ Unix timestamp when the DB record was created """
    updated_at: int
    """ Unix timestamp when the DB record was last updated """
    description: str | Unset = UNSET
    """ Optional comment regarding the incidence """
    target_balance: str | Unset = UNSET
    """ Whether the incidence affects the Accrued or the Available counter. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        employee_id = self.employee_id

        days_in_cents = self.days_in_cents

        timeoff_allowance_id = self.timeoff_allowance_id

        effective_on = self.effective_on

        created_at = self.created_at

        updated_at = self.updated_at

        description = self.description

        target_balance = self.target_balance

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "employee_id": employee_id,
                "days_in_cents": days_in_cents,
                "timeoff_allowance_id": timeoff_allowance_id,
                "effective_on": effective_on,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if target_balance is not UNSET:
            field_dict["target_balance"] = target_balance

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        employee_id = d.pop("employee_id")

        days_in_cents = d.pop("days_in_cents")

        timeoff_allowance_id = d.pop("timeoff_allowance_id")

        effective_on = d.pop("effective_on")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        description = d.pop("description", UNSET)

        target_balance = d.pop("target_balance", UNSET)

        timeoff_allowance_incidence = cls(
            id=id,
            employee_id=employee_id,
            days_in_cents=days_in_cents,
            timeoff_allowance_id=timeoff_allowance_id,
            effective_on=effective_on,
            created_at=created_at,
            updated_at=updated_at,
            description=description,
            target_balance=target_balance,
        )

        timeoff_allowance_incidence.additional_properties = d
        return timeoff_allowance_incidence

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
