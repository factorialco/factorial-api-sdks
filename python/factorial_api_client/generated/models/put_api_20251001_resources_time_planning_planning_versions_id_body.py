from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PutApi20251001ResourcesTimePlanningPlanningVersionsIdBody")


@_attrs_define
class PutApi20251001ResourcesTimePlanningPlanningVersionsIdBody:
    id: int
    """ Planning version identifier """
    effective_at: str
    """ Start date of the planning version """
    planning_tool: str
    """ Type of planning tool (shift_management, work_schedules, contract_hours) """
    number_of_rest_days_in_cents: int | Unset = UNSET
    """ Amount of rest days per week if applicable (in cents) """
    schedule_id: int | Unset = UNSET
    """ Work schedule identifier to include if applicable """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        effective_at = self.effective_at

        planning_tool = self.planning_tool

        number_of_rest_days_in_cents = self.number_of_rest_days_in_cents

        schedule_id = self.schedule_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "effective_at": effective_at,
                "planning_tool": planning_tool,
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
        id = d.pop("id")

        effective_at = d.pop("effective_at")

        planning_tool = d.pop("planning_tool")

        number_of_rest_days_in_cents = d.pop("number_of_rest_days_in_cents", UNSET)

        schedule_id = d.pop("schedule_id", UNSET)

        put_api_20251001_resources_time_planning_planning_versions_id_body = cls(
            id=id,
            effective_at=effective_at,
            planning_tool=planning_tool,
            number_of_rest_days_in_cents=number_of_rest_days_in_cents,
            schedule_id=schedule_id,
        )

        put_api_20251001_resources_time_planning_planning_versions_id_body.additional_properties = d
        return put_api_20251001_resources_time_planning_planning_versions_id_body

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
