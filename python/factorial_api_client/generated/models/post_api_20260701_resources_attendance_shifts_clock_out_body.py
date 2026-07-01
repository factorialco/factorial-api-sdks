from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20260701ResourcesAttendanceShiftsClockOutBody")


@_attrs_define
class PostApi20260701ResourcesAttendanceShiftsClockOutBody:
    now: str
    """ Clock out time """
    employee_id: str | Unset = UNSET
    """ Employee identifier """
    latitude: float | Unset = UNSET
    """ Latitude from where user clocked in """
    longitude: float | Unset = UNSET
    """ Longitude from where user clocked in """
    accuracy: float | Unset = UNSET
    """ Location accuracy """
    observations: str | Unset = UNSET
    """ Notes on the shift record """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        now = self.now

        employee_id = self.employee_id

        latitude = self.latitude

        longitude = self.longitude

        accuracy = self.accuracy

        observations = self.observations

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "now": now,
            }
        )
        if employee_id is not UNSET:
            field_dict["employee_id"] = employee_id
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if accuracy is not UNSET:
            field_dict["accuracy"] = accuracy
        if observations is not UNSET:
            field_dict["observations"] = observations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        now = d.pop("now")

        employee_id = d.pop("employee_id", UNSET)

        latitude = d.pop("latitude", UNSET)

        longitude = d.pop("longitude", UNSET)

        accuracy = d.pop("accuracy", UNSET)

        observations = d.pop("observations", UNSET)

        post_api_20260701_resources_attendance_shifts_clock_out_body = cls(
            now=now,
            employee_id=employee_id,
            latitude=latitude,
            longitude=longitude,
            accuracy=accuracy,
            observations=observations,
        )

        post_api_20260701_resources_attendance_shifts_clock_out_body.additional_properties = d
        return post_api_20260701_resources_attendance_shifts_clock_out_body

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
