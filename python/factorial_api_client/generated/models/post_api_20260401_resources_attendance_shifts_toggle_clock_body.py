from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_api_20260401_resources_attendance_shifts_toggle_clock_body_location_type import (
    PostApi20260401ResourcesAttendanceShiftsToggleClockBodyLocationType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20260401ResourcesAttendanceShiftsToggleClockBody")


@_attrs_define
class PostApi20260401ResourcesAttendanceShiftsToggleClockBody:
    employee_id: int
    """ Employee identifier """
    clock_time: str
    """ Clock in or out Timestamp """
    location_type: PostApi20260401ResourcesAttendanceShiftsToggleClockBodyLocationType | Unset = (
        UNSET
    )
    """ Place where user has clocked in """
    observations: str | Unset = UNSET
    """ Notes on the shift record """
    time_settings_break_configuration_id: int | Unset = UNSET
    """ Specific break configuration id when toggling the shift into a break and out of a break """
    project_id: int | Unset = UNSET
    """ Project identifier to associate the shift with a project. The employee must be assigned to the project,
    otherwise a 404 error is returned. Only used on clock-in; on clock-out this field is ignored, but the project
    association is preserved on the shift. Breaks are not associated with any project. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        employee_id = self.employee_id

        clock_time = self.clock_time

        location_type: str | Unset = UNSET
        if not isinstance(self.location_type, Unset):
            location_type = self.location_type.value

        observations = self.observations

        time_settings_break_configuration_id = self.time_settings_break_configuration_id

        project_id = self.project_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "employee_id": employee_id,
                "clock_time": clock_time,
            }
        )
        if location_type is not UNSET:
            field_dict["location_type"] = location_type
        if observations is not UNSET:
            field_dict["observations"] = observations
        if time_settings_break_configuration_id is not UNSET:
            field_dict["time_settings_break_configuration_id"] = (
                time_settings_break_configuration_id
            )
        if project_id is not UNSET:
            field_dict["project_id"] = project_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        employee_id = d.pop("employee_id")

        clock_time = d.pop("clock_time")

        _location_type = d.pop("location_type", UNSET)
        location_type: PostApi20260401ResourcesAttendanceShiftsToggleClockBodyLocationType | Unset
        if isinstance(_location_type, Unset):
            location_type = UNSET
        else:
            location_type = PostApi20260401ResourcesAttendanceShiftsToggleClockBodyLocationType(
                _location_type
            )

        observations = d.pop("observations", UNSET)

        time_settings_break_configuration_id = d.pop("time_settings_break_configuration_id", UNSET)

        project_id = d.pop("project_id", UNSET)

        post_api_20260401_resources_attendance_shifts_toggle_clock_body = cls(
            employee_id=employee_id,
            clock_time=clock_time,
            location_type=location_type,
            observations=observations,
            time_settings_break_configuration_id=time_settings_break_configuration_id,
            project_id=project_id,
        )

        post_api_20260401_resources_attendance_shifts_toggle_clock_body.additional_properties = d
        return post_api_20260401_resources_attendance_shifts_toggle_clock_body

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
