from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_api_20260401_resources_attendance_shifts_clock_in_body_location_type import (
    PostApi20260401ResourcesAttendanceShiftsClockInBodyLocationType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20260401ResourcesAttendanceShiftsClockInBody")


@_attrs_define
class PostApi20260401ResourcesAttendanceShiftsClockInBody:
    now: str
    """ Clock in time """
    employee_id: int | Unset = UNSET
    """ Employee identifier """
    latitude: float | Unset = UNSET
    """ Latitude from where user clocked in """
    longitude: float | Unset = UNSET
    """ Longitude from where user clocked in """
    accuracy: float | Unset = UNSET
    """ Location identifier """
    observations: str | Unset = UNSET
    """ Notes on the shift record """
    location_type: PostApi20260401ResourcesAttendanceShiftsClockInBodyLocationType | Unset = UNSET
    """ Place where user has clocked in """
    workplace_id: int | Unset = UNSET
    """ Location identifier """
    time_settings_break_configuration_id: int | Unset = UNSET
    """ Break configuration identifier """
    project_worker_id: int | Unset = UNSET
    """ Project worker identifier """
    subproject_id: int | Unset = UNSET
    """ Subproject identifier """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        now = self.now

        employee_id = self.employee_id

        latitude = self.latitude

        longitude = self.longitude

        accuracy = self.accuracy

        observations = self.observations

        location_type: str | Unset = UNSET
        if not isinstance(self.location_type, Unset):
            location_type = self.location_type.value if self.location_type is not None else None

        workplace_id = self.workplace_id

        time_settings_break_configuration_id = self.time_settings_break_configuration_id

        project_worker_id = self.project_worker_id

        subproject_id = self.subproject_id

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
        if location_type is not UNSET:
            field_dict["location_type"] = location_type
        if workplace_id is not UNSET:
            field_dict["workplace_id"] = workplace_id
        if time_settings_break_configuration_id is not UNSET:
            field_dict["time_settings_break_configuration_id"] = (
                time_settings_break_configuration_id
            )
        if project_worker_id is not UNSET:
            field_dict["project_worker_id"] = project_worker_id
        if subproject_id is not UNSET:
            field_dict["subproject_id"] = subproject_id

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

        _location_type = d.pop("location_type", UNSET)
        location_type: PostApi20260401ResourcesAttendanceShiftsClockInBodyLocationType | Unset
        if isinstance(_location_type, Unset):
            location_type = UNSET
        else:
            location_type = PostApi20260401ResourcesAttendanceShiftsClockInBodyLocationType(
                _location_type
            ) if _location_type is not None else None

        workplace_id = d.pop("workplace_id", UNSET)

        time_settings_break_configuration_id = d.pop("time_settings_break_configuration_id", UNSET)

        project_worker_id = d.pop("project_worker_id", UNSET)

        subproject_id = d.pop("subproject_id", UNSET)

        post_api_20260401_resources_attendance_shifts_clock_in_body = cls(
            now=now,
            employee_id=employee_id,
            latitude=latitude,
            longitude=longitude,
            accuracy=accuracy,
            observations=observations,
            location_type=location_type,
            workplace_id=workplace_id,
            time_settings_break_configuration_id=time_settings_break_configuration_id,
            project_worker_id=project_worker_id,
            subproject_id=subproject_id,
        )

        post_api_20260401_resources_attendance_shifts_clock_in_body.additional_properties = d
        return post_api_20260401_resources_attendance_shifts_clock_in_body

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
