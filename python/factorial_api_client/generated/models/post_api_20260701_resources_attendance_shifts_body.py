from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_api_20260701_resources_attendance_shifts_body_location_type import (
    PostApi20260701ResourcesAttendanceShiftsBodyLocationType,
)
from ..models.post_api_20260701_resources_attendance_shifts_body_source import (
    PostApi20260701ResourcesAttendanceShiftsBodySource,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20260701ResourcesAttendanceShiftsBody")


@_attrs_define
class PostApi20260701ResourcesAttendanceShiftsBody:
    date: str
    """ Date of the shift """
    employee_id: str | Unset = UNSET
    """ Id of the employee related """
    reference_date: str | Unset = UNSET
    """ Reference date of the shift """
    day: int | Unset = UNSET
    """ number of days of the shift """
    clock_in: str | Unset = UNSET
    """ Time of the clock in """
    clock_out: str | Unset = UNSET
    """ Time of the clock out """
    observations: str | Unset = UNSET
    """ Comments added to the shift """
    half_day: str | Unset = UNSET
    """ Boolean that indicates if the shift is a half day """
    workable: bool | Unset = UNSET
    """ Boolean that indicates if the shift is workable """
    location_type: PostApi20260701ResourcesAttendanceShiftsBodyLocationType | Unset = UNSET
    """ Type of the location """
    source: PostApi20260701ResourcesAttendanceShiftsBodySource | Unset = UNSET
    """ Source of the shift creation """
    time_settings_break_configuration_id: str | Unset = UNSET
    """ Id of the break configuration """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date

        employee_id = self.employee_id

        reference_date = self.reference_date

        day = self.day

        clock_in = self.clock_in

        clock_out = self.clock_out

        observations = self.observations

        half_day = self.half_day

        workable = self.workable

        location_type: str | Unset = UNSET
        if not isinstance(self.location_type, Unset):
            location_type = self.location_type.value

        source: str | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value

        time_settings_break_configuration_id = self.time_settings_break_configuration_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "date": date,
            }
        )
        if employee_id is not UNSET:
            field_dict["employee_id"] = employee_id
        if reference_date is not UNSET:
            field_dict["reference_date"] = reference_date
        if day is not UNSET:
            field_dict["day"] = day
        if clock_in is not UNSET:
            field_dict["clock_in"] = clock_in
        if clock_out is not UNSET:
            field_dict["clock_out"] = clock_out
        if observations is not UNSET:
            field_dict["observations"] = observations
        if half_day is not UNSET:
            field_dict["half_day"] = half_day
        if workable is not UNSET:
            field_dict["workable"] = workable
        if location_type is not UNSET:
            field_dict["location_type"] = location_type
        if source is not UNSET:
            field_dict["source"] = source
        if time_settings_break_configuration_id is not UNSET:
            field_dict["time_settings_break_configuration_id"] = (
                time_settings_break_configuration_id
            )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        date = d.pop("date")

        employee_id = d.pop("employee_id", UNSET)

        reference_date = d.pop("reference_date", UNSET)

        day = d.pop("day", UNSET)

        clock_in = d.pop("clock_in", UNSET)

        clock_out = d.pop("clock_out", UNSET)

        observations = d.pop("observations", UNSET)

        half_day = d.pop("half_day", UNSET)

        workable = d.pop("workable", UNSET)

        _location_type = d.pop("location_type", UNSET)
        location_type: PostApi20260701ResourcesAttendanceShiftsBodyLocationType | Unset
        if isinstance(_location_type, Unset):
            location_type = UNSET
        else:
            location_type = PostApi20260701ResourcesAttendanceShiftsBodyLocationType(_location_type) if _location_type is not None else None

        _source = d.pop("source", UNSET)
        source: PostApi20260701ResourcesAttendanceShiftsBodySource | Unset
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = PostApi20260701ResourcesAttendanceShiftsBodySource(_source) if _source is not None else None

        time_settings_break_configuration_id = d.pop("time_settings_break_configuration_id", UNSET)

        post_api_20260701_resources_attendance_shifts_body = cls(
            date=date,
            employee_id=employee_id,
            reference_date=reference_date,
            day=day,
            clock_in=clock_in,
            clock_out=clock_out,
            observations=observations,
            half_day=half_day,
            workable=workable,
            location_type=location_type,
            source=source,
            time_settings_break_configuration_id=time_settings_break_configuration_id,
        )

        post_api_20260701_resources_attendance_shifts_body.additional_properties = d
        return post_api_20260701_resources_attendance_shifts_body

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
