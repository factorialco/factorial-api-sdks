from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.attendance_edit_timesheet_request_location_type import (
    AttendanceEditTimesheetRequestLocationType,
)
from ..models.attendance_edit_timesheet_request_request_type import (
    AttendanceEditTimesheetRequestRequestType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="AttendanceEditTimesheetRequest")


@_attrs_define
class AttendanceEditTimesheetRequest:
    id: int
    """ Unique identifier for the edit timesheet request """
    request_type: AttendanceEditTimesheetRequestRequestType
    """ Type of the request """
    employee_id: int
    """ Id of the shift's employee """
    approved: bool | Unset = UNSET
    """ Status of the edit timesheet request """
    workable: bool | Unset = UNSET
    """ Indicates if the shift is workable or a break """
    clock_in: str | Unset = UNSET
    """ Clock in of the shift """
    clock_out: str | Unset = UNSET
    """ Clock out of the shift """
    location_type: AttendanceEditTimesheetRequestLocationType | Unset = UNSET
    """ Location of the shift """
    reason: str | Unset = UNSET
    """ Approve or reject reason """
    attendance_shift_id: int | Unset = UNSET
    """ Id of the shift for the request """
    time_settings_break_configuration_id: int | Unset = UNSET
    """ Id of the type of break for the request """
    observations: str | Unset = UNSET
    """ Additional observations for the shift """
    date: str | Unset = UNSET
    """ Date of the shift """
    reference_date: str | Unset = UNSET
    """ Reference date for the shift """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        request_type = self.request_type.value

        employee_id = self.employee_id

        approved = self.approved

        workable = self.workable

        clock_in = self.clock_in

        clock_out = self.clock_out

        location_type: str | Unset = UNSET
        if not isinstance(self.location_type, Unset):
            location_type = self.location_type.value if self.location_type is not None else None

        reason = self.reason

        attendance_shift_id = self.attendance_shift_id

        time_settings_break_configuration_id = self.time_settings_break_configuration_id

        observations = self.observations

        date = self.date

        reference_date = self.reference_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "request_type": request_type,
                "employee_id": employee_id,
            }
        )
        if approved is not UNSET:
            field_dict["approved"] = approved
        if workable is not UNSET:
            field_dict["workable"] = workable
        if clock_in is not UNSET:
            field_dict["clock_in"] = clock_in
        if clock_out is not UNSET:
            field_dict["clock_out"] = clock_out
        if location_type is not UNSET:
            field_dict["location_type"] = location_type
        if reason is not UNSET:
            field_dict["reason"] = reason
        if attendance_shift_id is not UNSET:
            field_dict["attendance_shift_id"] = attendance_shift_id
        if time_settings_break_configuration_id is not UNSET:
            field_dict["time_settings_break_configuration_id"] = (
                time_settings_break_configuration_id
            )
        if observations is not UNSET:
            field_dict["observations"] = observations
        if date is not UNSET:
            field_dict["date"] = date
        if reference_date is not UNSET:
            field_dict["reference_date"] = reference_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        request_type = AttendanceEditTimesheetRequestRequestType(d.pop("request_type"))

        employee_id = d.pop("employee_id")

        approved = d.pop("approved", UNSET)

        workable = d.pop("workable", UNSET)

        clock_in = d.pop("clock_in", UNSET)

        clock_out = d.pop("clock_out", UNSET)

        _location_type = d.pop("location_type", UNSET)
        location_type: AttendanceEditTimesheetRequestLocationType | Unset
        if isinstance(_location_type, Unset):
            location_type = UNSET
        else:
            location_type = AttendanceEditTimesheetRequestLocationType(_location_type) if _location_type is not None else None

        reason = d.pop("reason", UNSET)

        attendance_shift_id = d.pop("attendance_shift_id", UNSET)

        time_settings_break_configuration_id = d.pop("time_settings_break_configuration_id", UNSET)

        observations = d.pop("observations", UNSET)

        date = d.pop("date", UNSET)

        reference_date = d.pop("reference_date", UNSET)

        attendance_edit_timesheet_request = cls(
            id=id,
            request_type=request_type,
            employee_id=employee_id,
            approved=approved,
            workable=workable,
            clock_in=clock_in,
            clock_out=clock_out,
            location_type=location_type,
            reason=reason,
            attendance_shift_id=attendance_shift_id,
            time_settings_break_configuration_id=time_settings_break_configuration_id,
            observations=observations,
            date=date,
            reference_date=reference_date,
        )

        attendance_edit_timesheet_request.additional_properties = d
        return attendance_edit_timesheet_request

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
