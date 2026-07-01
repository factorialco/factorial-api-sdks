from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TimePlanningPlanningVersion")


@_attrs_define
class TimePlanningPlanningVersion:
    effective_at: str
    """ Planning version start date """
    planning_tool: str
    """ Type of planning tool (shift_management, work_schedules, contract_hours) """
    employee_id: str
    """ Employee identifier """
    id: str | Unset = UNSET
    """ Planning version identifier """
    number_of_rest_days_in_cents: int | Unset = UNSET
    """ Amount of rest days per week if applicable (in cents) """
    work_schedule_schedule_id: str | Unset = UNSET
    """ Work schedule identifier to include if applicable """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        effective_at = self.effective_at

        planning_tool = self.planning_tool

        employee_id = self.employee_id

        id = self.id

        number_of_rest_days_in_cents = self.number_of_rest_days_in_cents

        work_schedule_schedule_id = self.work_schedule_schedule_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "effective_at": effective_at,
                "planning_tool": planning_tool,
                "employee_id": employee_id,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if number_of_rest_days_in_cents is not UNSET:
            field_dict["number_of_rest_days_in_cents"] = number_of_rest_days_in_cents
        if work_schedule_schedule_id is not UNSET:
            field_dict["work_schedule_schedule_id"] = work_schedule_schedule_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        effective_at = d.pop("effective_at")

        planning_tool = d.pop("planning_tool")

        employee_id = d.pop("employee_id")

        id = d.pop("id", UNSET)

        number_of_rest_days_in_cents = d.pop("number_of_rest_days_in_cents", UNSET)

        work_schedule_schedule_id = d.pop("work_schedule_schedule_id", UNSET)

        time_planning_planning_version = cls(
            effective_at=effective_at,
            planning_tool=planning_tool,
            employee_id=employee_id,
            id=id,
            number_of_rest_days_in_cents=number_of_rest_days_in_cents,
            work_schedule_schedule_id=work_schedule_schedule_id,
        )

        time_planning_planning_version.additional_properties = d
        return time_planning_planning_version

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
