from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.time_planning_planned_break_break_type import TimePlanningPlannedBreakBreakType
from ..types import UNSET, Unset

T = TypeVar("T", bound="TimePlanningPlannedBreak")


@_attrs_define
class TimePlanningPlannedBreak:
    id: str
    """ Planned break identifier """
    break_type: TimePlanningPlannedBreakBreakType
    """ Type of the break """
    break_configuration_id: str
    """ Break configuration identifier """
    break_configuration_name: str
    """ Name of the break configuration """
    break_configuration_paid: bool
    """ Whether the break is paid """
    start_at: str | Unset = UNSET
    """ Break start time """
    end_at: str | Unset = UNSET
    """ Break end time """
    duration: int | Unset = UNSET
    """ Duration of the break in minutes """
    default_shift_id: str | Unset = UNSET
    """ Default shift identifier """
    shift_configuration_id: str | Unset = UNSET
    """ Shift configuration identifier """
    shift_id: str | Unset = UNSET
    """ Shift identifier """
    day_configuration_id: str | Unset = UNSET
    """ Day configuration identifier """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        break_type = self.break_type.value

        break_configuration_id = self.break_configuration_id

        break_configuration_name = self.break_configuration_name

        break_configuration_paid = self.break_configuration_paid

        start_at = self.start_at

        end_at = self.end_at

        duration = self.duration

        default_shift_id = self.default_shift_id

        shift_configuration_id = self.shift_configuration_id

        shift_id = self.shift_id

        day_configuration_id = self.day_configuration_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "break_type": break_type,
                "break_configuration_id": break_configuration_id,
                "break_configuration_name": break_configuration_name,
                "break_configuration_paid": break_configuration_paid,
            }
        )
        if start_at is not UNSET:
            field_dict["start_at"] = start_at
        if end_at is not UNSET:
            field_dict["end_at"] = end_at
        if duration is not UNSET:
            field_dict["duration"] = duration
        if default_shift_id is not UNSET:
            field_dict["default_shift_id"] = default_shift_id
        if shift_configuration_id is not UNSET:
            field_dict["shift_configuration_id"] = shift_configuration_id
        if shift_id is not UNSET:
            field_dict["shift_id"] = shift_id
        if day_configuration_id is not UNSET:
            field_dict["day_configuration_id"] = day_configuration_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        break_type = TimePlanningPlannedBreakBreakType(d.pop("break_type"))

        break_configuration_id = d.pop("break_configuration_id")

        break_configuration_name = d.pop("break_configuration_name")

        break_configuration_paid = d.pop("break_configuration_paid")

        start_at = d.pop("start_at", UNSET)

        end_at = d.pop("end_at", UNSET)

        duration = d.pop("duration", UNSET)

        default_shift_id = d.pop("default_shift_id", UNSET)

        shift_configuration_id = d.pop("shift_configuration_id", UNSET)

        shift_id = d.pop("shift_id", UNSET)

        day_configuration_id = d.pop("day_configuration_id", UNSET)

        time_planning_planned_break = cls(
            id=id,
            break_type=break_type,
            break_configuration_id=break_configuration_id,
            break_configuration_name=break_configuration_name,
            break_configuration_paid=break_configuration_paid,
            start_at=start_at,
            end_at=end_at,
            duration=duration,
            default_shift_id=default_shift_id,
            shift_configuration_id=shift_configuration_id,
            shift_id=shift_id,
            day_configuration_id=day_configuration_id,
        )

        time_planning_planned_break.additional_properties = d
        return time_planning_planned_break

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
