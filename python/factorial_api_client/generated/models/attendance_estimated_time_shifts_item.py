from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AttendanceEstimatedTimeShiftsItem")


@_attrs_define
class AttendanceEstimatedTimeShiftsItem:
    id: str
    start_at: str
    end_at: str
    location_id: str | Unset = UNSET
    timezone: str | Unset = UNSET
    extra_hours: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        start_at = self.start_at

        end_at = self.end_at

        location_id = self.location_id

        timezone = self.timezone

        extra_hours = self.extra_hours

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "start_at": start_at,
                "end_at": end_at,
            }
        )
        if location_id is not UNSET:
            field_dict["location_id"] = location_id
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if extra_hours is not UNSET:
            field_dict["extra_hours"] = extra_hours

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        start_at = d.pop("start_at")

        end_at = d.pop("end_at")

        location_id = d.pop("location_id", UNSET)

        timezone = d.pop("timezone", UNSET)

        extra_hours = d.pop("extra_hours", UNSET)

        attendance_estimated_time_shifts_item = cls(
            id=id,
            start_at=start_at,
            end_at=end_at,
            location_id=location_id,
            timezone=timezone,
            extra_hours=extra_hours,
        )

        attendance_estimated_time_shifts_item.additional_properties = d
        return attendance_estimated_time_shifts_item

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
