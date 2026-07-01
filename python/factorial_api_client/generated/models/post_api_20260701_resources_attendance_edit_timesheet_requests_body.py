from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_api_20260701_resources_attendance_edit_timesheet_requests_body_location_type import (
    PostApi20260701ResourcesAttendanceEditTimesheetRequestsBodyLocationType,
)
from ..models.post_api_20260701_resources_attendance_edit_timesheet_requests_body_request_type import (
    PostApi20260701ResourcesAttendanceEditTimesheetRequestsBodyRequestType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20260701ResourcesAttendanceEditTimesheetRequestsBody")


@_attrs_define
class PostApi20260701ResourcesAttendanceEditTimesheetRequestsBody:
    employee_id: str
    request_type: PostApi20260701ResourcesAttendanceEditTimesheetRequestsBodyRequestType
    reason: str | Unset = UNSET
    date: str | Unset = UNSET
    clock_in: str | Unset = UNSET
    clock_out: str | Unset = UNSET
    workable: bool | Unset = UNSET
    attendance_shift_id: str | Unset = UNSET
    reference_date: str | Unset = UNSET
    time_settings_break_configuration_id: str | Unset = UNSET
    location_type: (
        PostApi20260701ResourcesAttendanceEditTimesheetRequestsBodyLocationType | Unset
    ) = UNSET
    observations: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        employee_id = self.employee_id

        request_type = self.request_type.value

        reason = self.reason

        date = self.date

        clock_in = self.clock_in

        clock_out = self.clock_out

        workable = self.workable

        attendance_shift_id = self.attendance_shift_id

        reference_date = self.reference_date

        time_settings_break_configuration_id = self.time_settings_break_configuration_id

        location_type: str | Unset = UNSET
        if not isinstance(self.location_type, Unset):
            location_type = self.location_type.value

        observations = self.observations

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "employee_id": employee_id,
                "request_type": request_type,
            }
        )
        if reason is not UNSET:
            field_dict["reason"] = reason
        if date is not UNSET:
            field_dict["date"] = date
        if clock_in is not UNSET:
            field_dict["clock_in"] = clock_in
        if clock_out is not UNSET:
            field_dict["clock_out"] = clock_out
        if workable is not UNSET:
            field_dict["workable"] = workable
        if attendance_shift_id is not UNSET:
            field_dict["attendance_shift_id"] = attendance_shift_id
        if reference_date is not UNSET:
            field_dict["reference_date"] = reference_date
        if time_settings_break_configuration_id is not UNSET:
            field_dict["time_settings_break_configuration_id"] = (
                time_settings_break_configuration_id
            )
        if location_type is not UNSET:
            field_dict["location_type"] = location_type
        if observations is not UNSET:
            field_dict["observations"] = observations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        employee_id = d.pop("employee_id")

        request_type = PostApi20260701ResourcesAttendanceEditTimesheetRequestsBodyRequestType(
            d.pop("request_type")
        )

        reason = d.pop("reason", UNSET)

        date = d.pop("date", UNSET)

        clock_in = d.pop("clock_in", UNSET)

        clock_out = d.pop("clock_out", UNSET)

        workable = d.pop("workable", UNSET)

        attendance_shift_id = d.pop("attendance_shift_id", UNSET)

        reference_date = d.pop("reference_date", UNSET)

        time_settings_break_configuration_id = d.pop("time_settings_break_configuration_id", UNSET)

        _location_type = d.pop("location_type", UNSET)
        location_type: (
            PostApi20260701ResourcesAttendanceEditTimesheetRequestsBodyLocationType | Unset
        )
        if isinstance(_location_type, Unset):
            location_type = UNSET
        else:
            location_type = PostApi20260701ResourcesAttendanceEditTimesheetRequestsBodyLocationType(
                _location_type
            )

        observations = d.pop("observations", UNSET)

        post_api_20260701_resources_attendance_edit_timesheet_requests_body = cls(
            employee_id=employee_id,
            request_type=request_type,
            reason=reason,
            date=date,
            clock_in=clock_in,
            clock_out=clock_out,
            workable=workable,
            attendance_shift_id=attendance_shift_id,
            reference_date=reference_date,
            time_settings_break_configuration_id=time_settings_break_configuration_id,
            location_type=location_type,
            observations=observations,
        )

        post_api_20260701_resources_attendance_edit_timesheet_requests_body.additional_properties = d
        return post_api_20260701_resources_attendance_edit_timesheet_requests_body

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
