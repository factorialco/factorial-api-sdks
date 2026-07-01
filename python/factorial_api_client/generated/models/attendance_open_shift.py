from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.attendance_open_shift_status import AttendanceOpenShiftStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="AttendanceOpenShift")


@_attrs_define
class AttendanceOpenShift:
    id: str
    """ Open Shift identifier. """
    employee_id: str
    """ Employee identifier from the open shift. """
    date: str
    """ Date of the open shift. """
    reference_date: str
    """ Reference date for the shift """
    clock_in: str
    """ Clock in time from the shift. Ignore the date part. """
    status: AttendanceOpenShiftStatus
    """ Status of the shift """
    workable: bool
    """ Indicates if the shift is a break or a workable shift. """
    automatic_clock_in: bool
    """ Indicates if the shift is automatic or not """
    clock_out: str | Unset = UNSET
    """ For open shifts, this field is null. """
    location_type: str | Unset = UNSET
    """ String representing the location type of the shift. Examples work_from_home, office, etc. """
    workplace_id: str | Unset = UNSET
    """ Identifier for the workplace assinged to the shift. """
    time_settings_break_configuration_id: str | Unset = UNSET
    """ If the shift is a break, this field will have the break configuration id. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        employee_id = self.employee_id

        date = self.date

        reference_date = self.reference_date

        clock_in = self.clock_in

        status = self.status.value

        workable = self.workable

        automatic_clock_in = self.automatic_clock_in

        clock_out = self.clock_out

        location_type = self.location_type

        workplace_id = self.workplace_id

        time_settings_break_configuration_id = self.time_settings_break_configuration_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "employee_id": employee_id,
                "date": date,
                "reference_date": reference_date,
                "clock_in": clock_in,
                "status": status,
                "workable": workable,
                "automatic_clock_in": automatic_clock_in,
            }
        )
        if clock_out is not UNSET:
            field_dict["clock_out"] = clock_out
        if location_type is not UNSET:
            field_dict["location_type"] = location_type
        if workplace_id is not UNSET:
            field_dict["workplace_id"] = workplace_id
        if time_settings_break_configuration_id is not UNSET:
            field_dict["time_settings_break_configuration_id"] = (
                time_settings_break_configuration_id
            )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        employee_id = d.pop("employee_id")

        date = d.pop("date")

        reference_date = d.pop("reference_date")

        clock_in = d.pop("clock_in")

        status = AttendanceOpenShiftStatus(d.pop("status"))

        workable = d.pop("workable")

        automatic_clock_in = d.pop("automatic_clock_in")

        clock_out = d.pop("clock_out", UNSET)

        location_type = d.pop("location_type", UNSET)

        workplace_id = d.pop("workplace_id", UNSET)

        time_settings_break_configuration_id = d.pop("time_settings_break_configuration_id", UNSET)

        attendance_open_shift = cls(
            id=id,
            employee_id=employee_id,
            date=date,
            reference_date=reference_date,
            clock_in=clock_in,
            status=status,
            workable=workable,
            automatic_clock_in=automatic_clock_in,
            clock_out=clock_out,
            location_type=location_type,
            workplace_id=workplace_id,
            time_settings_break_configuration_id=time_settings_break_configuration_id,
        )

        attendance_open_shift.additional_properties = d
        return attendance_open_shift

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
