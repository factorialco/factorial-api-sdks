from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.put_api_20261001_resources_attendance_edit_timesheet_requests_id_body_location_type import (
    PutApi20261001ResourcesAttendanceEditTimesheetRequestsIdBodyLocationType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PutApi20261001ResourcesAttendanceEditTimesheetRequestsIdBody")


@_attrs_define
class PutApi20261001ResourcesAttendanceEditTimesheetRequestsIdBody:
    employee_id: str
    """ Id of the employee related. """
    id: str
    """ Id of the edit timesheet request to update. """
    attendance_shift_id: str | Unset = UNSET
    """ The id of the shift. """
    clock_in: str | Unset = UNSET
    """ Clock in of the shift. """
    clock_out: str | Unset = UNSET
    """ Clock in of the shift. """
    date: str | Unset = UNSET
    """ Date of the shift in case the request. """
    reference_date: str | Unset = UNSET
    """ Reference date of the shift. """
    location_type: (
        PutApi20261001ResourcesAttendanceEditTimesheetRequestsIdBodyLocationType | Unset
    ) = UNSET
    """ Type of the location. """
    observations: str | Unset = UNSET
    """ Shift observations. """
    reason: str | Unset = UNSET
    """ Reason or comment justifying the edit timesheet request. """
    time_settings_break_configuration_id: str | Unset = UNSET
    """ Id of the break. """
    workplace_id: str | Unset = UNSET
    """ Id of the workplace (location) for the shift. """
    clock_in_work_area_id: str | Unset = UNSET
    """ Id of the clock-in work area within the workplace. """
    clock_out_work_area_id: str | Unset = UNSET
    """ Id of the clock-out work area within the workplace. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        employee_id = self.employee_id

        id = self.id

        attendance_shift_id = self.attendance_shift_id

        clock_in = self.clock_in

        clock_out = self.clock_out

        date = self.date

        reference_date = self.reference_date

        location_type: str | Unset = UNSET
        if not isinstance(self.location_type, Unset):
            location_type = self.location_type.value if self.location_type is not None else None

        observations = self.observations

        reason = self.reason

        time_settings_break_configuration_id = self.time_settings_break_configuration_id

        workplace_id = self.workplace_id

        clock_in_work_area_id = self.clock_in_work_area_id

        clock_out_work_area_id = self.clock_out_work_area_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "employee_id": employee_id,
                "id": id,
            }
        )
        if attendance_shift_id is not UNSET:
            field_dict["attendance_shift_id"] = attendance_shift_id
        if clock_in is not UNSET:
            field_dict["clock_in"] = clock_in
        if clock_out is not UNSET:
            field_dict["clock_out"] = clock_out
        if date is not UNSET:
            field_dict["date"] = date
        if reference_date is not UNSET:
            field_dict["reference_date"] = reference_date
        if location_type is not UNSET:
            field_dict["location_type"] = location_type
        if observations is not UNSET:
            field_dict["observations"] = observations
        if reason is not UNSET:
            field_dict["reason"] = reason
        if time_settings_break_configuration_id is not UNSET:
            field_dict["time_settings_break_configuration_id"] = (
                time_settings_break_configuration_id
            )
        if workplace_id is not UNSET:
            field_dict["workplace_id"] = workplace_id
        if clock_in_work_area_id is not UNSET:
            field_dict["clock_in_work_area_id"] = clock_in_work_area_id
        if clock_out_work_area_id is not UNSET:
            field_dict["clock_out_work_area_id"] = clock_out_work_area_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        employee_id = d.pop("employee_id")

        id = d.pop("id")

        attendance_shift_id = d.pop("attendance_shift_id", UNSET)

        clock_in = d.pop("clock_in", UNSET)

        clock_out = d.pop("clock_out", UNSET)

        date = d.pop("date", UNSET)

        reference_date = d.pop("reference_date", UNSET)

        _location_type = d.pop("location_type", UNSET)
        location_type: (
            PutApi20261001ResourcesAttendanceEditTimesheetRequestsIdBodyLocationType | Unset
        )
        if isinstance(_location_type, Unset):
            location_type = UNSET
        else:
            location_type = (
                PutApi20261001ResourcesAttendanceEditTimesheetRequestsIdBodyLocationType(
                    _location_type
                ) if _location_type is not None else None
            )

        observations = d.pop("observations", UNSET)

        reason = d.pop("reason", UNSET)

        time_settings_break_configuration_id = d.pop("time_settings_break_configuration_id", UNSET)

        workplace_id = d.pop("workplace_id", UNSET)

        clock_in_work_area_id = d.pop("clock_in_work_area_id", UNSET)

        clock_out_work_area_id = d.pop("clock_out_work_area_id", UNSET)

        put_api_20261001_resources_attendance_edit_timesheet_requests_id_body = cls(
            employee_id=employee_id,
            id=id,
            attendance_shift_id=attendance_shift_id,
            clock_in=clock_in,
            clock_out=clock_out,
            date=date,
            reference_date=reference_date,
            location_type=location_type,
            observations=observations,
            reason=reason,
            time_settings_break_configuration_id=time_settings_break_configuration_id,
            workplace_id=workplace_id,
            clock_in_work_area_id=clock_in_work_area_id,
            clock_out_work_area_id=clock_out_work_area_id,
        )

        put_api_20261001_resources_attendance_edit_timesheet_requests_id_body.additional_properties = d
        return put_api_20261001_resources_attendance_edit_timesheet_requests_id_body

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
