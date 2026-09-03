from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.attendance_estimated_time_breaks_item_break_type import (
    AttendanceEstimatedTimeBreaksItemBreakType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="AttendanceEstimatedTimeBreaksItem")


@_attrs_define
class AttendanceEstimatedTimeBreaksItem:
    start_at: str
    end_at: str
    duration: int
    break_configuration_id: str
    break_configuration_name: str
    break_configuration_paid: bool
    break_type: AttendanceEstimatedTimeBreaksItemBreakType
    timezone: str
    shift_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start_at = self.start_at

        end_at = self.end_at

        duration = self.duration

        break_configuration_id = self.break_configuration_id

        break_configuration_name = self.break_configuration_name

        break_configuration_paid = self.break_configuration_paid

        break_type = self.break_type.value

        timezone = self.timezone

        shift_id = self.shift_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "start_at": start_at,
                "end_at": end_at,
                "duration": duration,
                "break_configuration_id": break_configuration_id,
                "break_configuration_name": break_configuration_name,
                "break_configuration_paid": break_configuration_paid,
                "break_type": break_type,
                "timezone": timezone,
            }
        )
        if shift_id is not UNSET:
            field_dict["shift_id"] = shift_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        start_at = d.pop("start_at")

        end_at = d.pop("end_at")

        duration = d.pop("duration")

        break_configuration_id = d.pop("break_configuration_id")

        break_configuration_name = d.pop("break_configuration_name")

        break_configuration_paid = d.pop("break_configuration_paid")

        break_type = AttendanceEstimatedTimeBreaksItemBreakType(d.pop("break_type"))

        timezone = d.pop("timezone")

        shift_id = d.pop("shift_id", UNSET)

        attendance_estimated_time_breaks_item = cls(
            start_at=start_at,
            end_at=end_at,
            duration=duration,
            break_configuration_id=break_configuration_id,
            break_configuration_name=break_configuration_name,
            break_configuration_paid=break_configuration_paid,
            break_type=break_type,
            timezone=timezone,
            shift_id=shift_id,
        )

        attendance_estimated_time_breaks_item.additional_properties = d
        return attendance_estimated_time_breaks_item

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
