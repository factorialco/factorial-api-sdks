from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.attendance_shift_half_day import AttendanceShiftHalfDay
from ..models.attendance_shift_location_type import AttendanceShiftLocationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AttendanceShift")


@_attrs_define
class AttendanceShift:
    id: int
    """ Unique identifier for the shift """
    employee_id: int
    """ Identifier for the employee assigned to the shift """
    date: str
    """ Date of the shift """
    reference_date: str
    """ Reference date for the shift """
    created_at: str
    """ Timestamp when the shift record was created """
    company_id: int
    """ Identifier for the company """
    updated_at: str
    """ Timestamp when the shift record was updated """
    minutes: int
    """ Number in minutes of the shift """
    clock_in: str | Unset = UNSET
    """ Time when the employee clocked in """
    clock_out: str | Unset = UNSET
    """ Time when the employee clocked out """
    in_source: str | Unset = UNSET
    """ Source of the clock-in time """
    out_source: str | Unset = UNSET
    """ Source of the clock-out time """
    observations: str | Unset = UNSET
    """ Additional observations about the shift """
    location_type: AttendanceShiftLocationType | Unset = UNSET
    """ Type of location for the shift """
    half_day: AttendanceShiftHalfDay | Unset = UNSET
    """ Indicates which worked part of the day """
    in_location_latitude: float | Unset = UNSET
    """ Latitude of the clock-in location """
    in_location_longitude: float | Unset = UNSET
    """ Longitude of the clock-in location """
    in_location_accuracy: float | Unset = UNSET
    """ Accuracy of the clock-in location """
    out_location_latitude: float | Unset = UNSET
    """ Latitude of the clock-out location """
    out_location_longitude: float | Unset = UNSET
    """ Longitude of the clock-out location """
    out_location_accuracy: float | Unset = UNSET
    """ Accuracy of the clock-out location """
    workable: bool | Unset = UNSET
    """ Indicates if the shift is workable """
    workplace_id: int | Unset = UNSET
    """ Identifier for the location """
    time_settings_break_configuration_id: int | Unset = UNSET
    """ Identifier for the break configuration """
    clock_in_with_seconds: str | Unset = UNSET
    """ Clock in time with seconds """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        employee_id = self.employee_id

        date = self.date

        reference_date = self.reference_date

        created_at = self.created_at

        company_id = self.company_id

        updated_at = self.updated_at

        minutes = self.minutes

        clock_in = self.clock_in

        clock_out = self.clock_out

        in_source = self.in_source

        out_source = self.out_source

        observations = self.observations

        location_type: str | Unset = UNSET
        if not isinstance(self.location_type, Unset):
            location_type = self.location_type.value

        half_day: str | Unset = UNSET
        if not isinstance(self.half_day, Unset):
            half_day = self.half_day.value

        in_location_latitude = self.in_location_latitude

        in_location_longitude = self.in_location_longitude

        in_location_accuracy = self.in_location_accuracy

        out_location_latitude = self.out_location_latitude

        out_location_longitude = self.out_location_longitude

        out_location_accuracy = self.out_location_accuracy

        workable = self.workable

        workplace_id = self.workplace_id

        time_settings_break_configuration_id = self.time_settings_break_configuration_id

        clock_in_with_seconds = self.clock_in_with_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "employee_id": employee_id,
                "date": date,
                "reference_date": reference_date,
                "created_at": created_at,
                "company_id": company_id,
                "updated_at": updated_at,
                "minutes": minutes,
            }
        )
        if clock_in is not UNSET:
            field_dict["clock_in"] = clock_in
        if clock_out is not UNSET:
            field_dict["clock_out"] = clock_out
        if in_source is not UNSET:
            field_dict["in_source"] = in_source
        if out_source is not UNSET:
            field_dict["out_source"] = out_source
        if observations is not UNSET:
            field_dict["observations"] = observations
        if location_type is not UNSET:
            field_dict["location_type"] = location_type
        if half_day is not UNSET:
            field_dict["half_day"] = half_day
        if in_location_latitude is not UNSET:
            field_dict["in_location_latitude"] = in_location_latitude
        if in_location_longitude is not UNSET:
            field_dict["in_location_longitude"] = in_location_longitude
        if in_location_accuracy is not UNSET:
            field_dict["in_location_accuracy"] = in_location_accuracy
        if out_location_latitude is not UNSET:
            field_dict["out_location_latitude"] = out_location_latitude
        if out_location_longitude is not UNSET:
            field_dict["out_location_longitude"] = out_location_longitude
        if out_location_accuracy is not UNSET:
            field_dict["out_location_accuracy"] = out_location_accuracy
        if workable is not UNSET:
            field_dict["workable"] = workable
        if workplace_id is not UNSET:
            field_dict["workplace_id"] = workplace_id
        if time_settings_break_configuration_id is not UNSET:
            field_dict["time_settings_break_configuration_id"] = (
                time_settings_break_configuration_id
            )
        if clock_in_with_seconds is not UNSET:
            field_dict["clock_in_with_seconds"] = clock_in_with_seconds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        employee_id = d.pop("employee_id")

        date = d.pop("date")

        reference_date = d.pop("reference_date")

        created_at = d.pop("created_at")

        company_id = d.pop("company_id")

        updated_at = d.pop("updated_at")

        minutes = d.pop("minutes")

        clock_in = d.pop("clock_in", UNSET)

        clock_out = d.pop("clock_out", UNSET)

        in_source = d.pop("in_source", UNSET)

        out_source = d.pop("out_source", UNSET)

        observations = d.pop("observations", UNSET)

        _location_type = d.pop("location_type", UNSET)
        location_type: AttendanceShiftLocationType | Unset
        if isinstance(_location_type, Unset):
            location_type = UNSET
        else:
            location_type = AttendanceShiftLocationType(_location_type) if _location_type is not None else None

        _half_day = d.pop("half_day", UNSET)
        half_day: AttendanceShiftHalfDay | Unset
        if isinstance(_half_day, Unset):
            half_day = UNSET
        else:
            half_day = AttendanceShiftHalfDay(_half_day) if _half_day is not None else None

        in_location_latitude = d.pop("in_location_latitude", UNSET)

        in_location_longitude = d.pop("in_location_longitude", UNSET)

        in_location_accuracy = d.pop("in_location_accuracy", UNSET)

        out_location_latitude = d.pop("out_location_latitude", UNSET)

        out_location_longitude = d.pop("out_location_longitude", UNSET)

        out_location_accuracy = d.pop("out_location_accuracy", UNSET)

        workable = d.pop("workable", UNSET)

        workplace_id = d.pop("workplace_id", UNSET)

        time_settings_break_configuration_id = d.pop("time_settings_break_configuration_id", UNSET)

        clock_in_with_seconds = d.pop("clock_in_with_seconds", UNSET)

        attendance_shift = cls(
            id=id,
            employee_id=employee_id,
            date=date,
            reference_date=reference_date,
            created_at=created_at,
            company_id=company_id,
            updated_at=updated_at,
            minutes=minutes,
            clock_in=clock_in,
            clock_out=clock_out,
            in_source=in_source,
            out_source=out_source,
            observations=observations,
            location_type=location_type,
            half_day=half_day,
            in_location_latitude=in_location_latitude,
            in_location_longitude=in_location_longitude,
            in_location_accuracy=in_location_accuracy,
            out_location_latitude=out_location_latitude,
            out_location_longitude=out_location_longitude,
            out_location_accuracy=out_location_accuracy,
            workable=workable,
            workplace_id=workplace_id,
            time_settings_break_configuration_id=time_settings_break_configuration_id,
            clock_in_with_seconds=clock_in_with_seconds,
        )

        attendance_shift.additional_properties = d
        return attendance_shift

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
