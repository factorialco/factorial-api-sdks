from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="PostApi20261001ResourcesTimePlanningPlannedBreaksBulkCreateBodyPlannedBreaksItem"
)


@_attrs_define
class PostApi20261001ResourcesTimePlanningPlannedBreaksBulkCreateBodyPlannedBreaksItem:
    break_configuration_id: str
    """ Break configuration identifier """
    id: str | Unset = UNSET
    """ Planned break identifier """
    start_at: str | Unset = UNSET
    """ Break start time """
    end_at: str | Unset = UNSET
    """ Break end time """
    duration: int | Unset = UNSET
    break_type: str | Unset = UNSET
    """ Type of the break """
    default_shift_id: str | Unset = UNSET
    """ Default shift identifier """
    shift_id: str | Unset = UNSET
    """ Shift identifier """
    day_configuration_id: str | Unset = UNSET
    """ Day configuration identifier """
    shift_configuration_id: str | Unset = UNSET
    """ Shift configuration identifier """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        break_configuration_id = self.break_configuration_id

        id = self.id

        start_at = self.start_at

        end_at = self.end_at

        duration = self.duration

        break_type = self.break_type

        default_shift_id = self.default_shift_id

        shift_id = self.shift_id

        day_configuration_id = self.day_configuration_id

        shift_configuration_id = self.shift_configuration_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "break_configuration_id": break_configuration_id,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if start_at is not UNSET:
            field_dict["start_at"] = start_at
        if end_at is not UNSET:
            field_dict["end_at"] = end_at
        if duration is not UNSET:
            field_dict["duration"] = duration
        if break_type is not UNSET:
            field_dict["break_type"] = break_type
        if default_shift_id is not UNSET:
            field_dict["default_shift_id"] = default_shift_id
        if shift_id is not UNSET:
            field_dict["shift_id"] = shift_id
        if day_configuration_id is not UNSET:
            field_dict["day_configuration_id"] = day_configuration_id
        if shift_configuration_id is not UNSET:
            field_dict["shift_configuration_id"] = shift_configuration_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        break_configuration_id = d.pop("break_configuration_id")

        id = d.pop("id", UNSET)

        start_at = d.pop("start_at", UNSET)

        end_at = d.pop("end_at", UNSET)

        duration = d.pop("duration", UNSET)

        break_type = d.pop("break_type", UNSET)

        default_shift_id = d.pop("default_shift_id", UNSET)

        shift_id = d.pop("shift_id", UNSET)

        day_configuration_id = d.pop("day_configuration_id", UNSET)

        shift_configuration_id = d.pop("shift_configuration_id", UNSET)

        post_api_20261001_resources_time_planning_planned_breaks_bulk_create_body_planned_breaks_item = cls(
            break_configuration_id=break_configuration_id,
            id=id,
            start_at=start_at,
            end_at=end_at,
            duration=duration,
            break_type=break_type,
            default_shift_id=default_shift_id,
            shift_id=shift_id,
            day_configuration_id=day_configuration_id,
            shift_configuration_id=shift_configuration_id,
        )

        post_api_20261001_resources_time_planning_planned_breaks_bulk_create_body_planned_breaks_item.additional_properties = d
        return post_api_20261001_resources_time_planning_planned_breaks_bulk_create_body_planned_breaks_item

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
