from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20260401ResourcesAttendanceShiftsBreakStartBody")


@_attrs_define
class PostApi20260401ResourcesAttendanceShiftsBreakStartBody:
    now: str
    """ Current time of the break """
    employee_id: int | Unset = UNSET
    """ Employee id of the break """
    observations: str | Unset = UNSET
    """ Observations of the break """
    time_settings_break_configuration_id: int | Unset = UNSET
    """ Time settings configuration id of the break """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        now = self.now

        employee_id = self.employee_id

        observations = self.observations

        time_settings_break_configuration_id = self.time_settings_break_configuration_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "now": now,
            }
        )
        if employee_id is not UNSET:
            field_dict["employee_id"] = employee_id
        if observations is not UNSET:
            field_dict["observations"] = observations
        if time_settings_break_configuration_id is not UNSET:
            field_dict["time_settings_break_configuration_id"] = (
                time_settings_break_configuration_id
            )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        now = d.pop("now")

        employee_id = d.pop("employee_id", UNSET)

        observations = d.pop("observations", UNSET)

        time_settings_break_configuration_id = d.pop("time_settings_break_configuration_id", UNSET)

        post_api_20260401_resources_attendance_shifts_break_start_body = cls(
            now=now,
            employee_id=employee_id,
            observations=observations,
            time_settings_break_configuration_id=time_settings_break_configuration_id,
        )

        post_api_20260401_resources_attendance_shifts_break_start_body.additional_properties = d
        return post_api_20260401_resources_attendance_shifts_break_start_body

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
