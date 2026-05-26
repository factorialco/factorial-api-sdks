from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.put_api_20251001_resources_attendance_shifts_id_body_location_type import (
    PutApi20251001ResourcesAttendanceShiftsIdBodyLocationType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PutApi20251001ResourcesAttendanceShiftsIdBody")


@_attrs_define
class PutApi20251001ResourcesAttendanceShiftsIdBody:
    id: int
    """ Id of the shift """
    clock_in: str | Unset = UNSET
    """ Time of the clock in """
    clock_out: str | Unset = UNSET
    """ Time of the clock out """
    date: str | Unset = UNSET
    """ Date of the shift """
    reference_date: str | Unset = UNSET
    """ reference date of the shift """
    observations: str | Unset = UNSET
    """ Comments added to the shift """
    location_type: PutApi20251001ResourcesAttendanceShiftsIdBodyLocationType | Unset = UNSET
    """ Type of the location """
    workplace_id: int | Unset = UNSET
    """ Id of the location related """
    time_settings_break_configuration_id: int | Unset = UNSET
    """ Id of the break configuration """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        clock_in = self.clock_in

        clock_out = self.clock_out

        date = self.date

        reference_date = self.reference_date

        observations = self.observations

        location_type: str | Unset = UNSET
        if not isinstance(self.location_type, Unset):
            location_type = self.location_type.value

        workplace_id = self.workplace_id

        time_settings_break_configuration_id = self.time_settings_break_configuration_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if clock_in is not UNSET:
            field_dict["clock_in"] = clock_in
        if clock_out is not UNSET:
            field_dict["clock_out"] = clock_out
        if date is not UNSET:
            field_dict["date"] = date
        if reference_date is not UNSET:
            field_dict["reference_date"] = reference_date
        if observations is not UNSET:
            field_dict["observations"] = observations
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

        clock_in = d.pop("clock_in", UNSET)

        clock_out = d.pop("clock_out", UNSET)

        date = d.pop("date", UNSET)

        reference_date = d.pop("reference_date", UNSET)

        observations = d.pop("observations", UNSET)

        _location_type = d.pop("location_type", UNSET)
        location_type: PutApi20251001ResourcesAttendanceShiftsIdBodyLocationType | Unset
        if isinstance(_location_type, Unset):
            location_type = UNSET
        else:
            location_type = PutApi20251001ResourcesAttendanceShiftsIdBodyLocationType(
                _location_type
            )

        workplace_id = d.pop("workplace_id", UNSET)

        time_settings_break_configuration_id = d.pop("time_settings_break_configuration_id", UNSET)

        put_api_20251001_resources_attendance_shifts_id_body = cls(
            id=id,
            clock_in=clock_in,
            clock_out=clock_out,
            date=date,
            reference_date=reference_date,
            observations=observations,
            location_type=location_type,
            workplace_id=workplace_id,
            time_settings_break_configuration_id=time_settings_break_configuration_id,
        )

        put_api_20251001_resources_attendance_shifts_id_body.additional_properties = d
        return put_api_20251001_resources_attendance_shifts_id_body

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
