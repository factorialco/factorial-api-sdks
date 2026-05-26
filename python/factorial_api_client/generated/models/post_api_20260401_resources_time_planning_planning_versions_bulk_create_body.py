from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20260401ResourcesTimePlanningPlanningVersionsBulkCreateBody")


@_attrs_define
class PostApi20260401ResourcesTimePlanningPlanningVersionsBulkCreateBody:
    effective_at: str
    """ Start date of the planning version """
    planning_tool: str
    """ Type of planning tool (shift_management, work_schedules, contract_hours) """
    employee_ids: list[int]
    """ List of employee identifiers """
    number_of_rest_days_in_cents: int | Unset = UNSET
    """ Amount of rest days per week if applicable (in cents) """
    schedule_id: int | Unset = UNSET
    """ Work schedule identifier to include if applicable """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        effective_at = self.effective_at

        planning_tool = self.planning_tool

        employee_ids = self.employee_ids

        number_of_rest_days_in_cents = self.number_of_rest_days_in_cents

        schedule_id = self.schedule_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "effective_at": effective_at,
                "planning_tool": planning_tool,
                "employee_ids": employee_ids,
            }
        )
        if number_of_rest_days_in_cents is not UNSET:
            field_dict["number_of_rest_days_in_cents"] = number_of_rest_days_in_cents
        if schedule_id is not UNSET:
            field_dict["schedule_id"] = schedule_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        effective_at = d.pop("effective_at")

        planning_tool = d.pop("planning_tool")

        employee_ids = cast(list[int], d.pop("employee_ids"))

        number_of_rest_days_in_cents = d.pop("number_of_rest_days_in_cents", UNSET)

        schedule_id = d.pop("schedule_id", UNSET)

        post_api_20260401_resources_time_planning_planning_versions_bulk_create_body = cls(
            effective_at=effective_at,
            planning_tool=planning_tool,
            employee_ids=employee_ids,
            number_of_rest_days_in_cents=number_of_rest_days_in_cents,
            schedule_id=schedule_id,
        )

        post_api_20260401_resources_time_planning_planning_versions_bulk_create_body.additional_properties = d
        return post_api_20260401_resources_time_planning_planning_versions_bulk_create_body

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
