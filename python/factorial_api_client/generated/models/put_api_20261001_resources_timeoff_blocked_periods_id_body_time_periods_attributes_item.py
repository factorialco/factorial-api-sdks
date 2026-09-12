from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="PutApi20261001ResourcesTimeoffBlockedPeriodsIdBodyTimePeriodsAttributesItem"
)


@_attrs_define
class PutApi20261001ResourcesTimeoffBlockedPeriodsIdBodyTimePeriodsAttributesItem:
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    field_destroy: bool | Unset = UNSET
    period_type: str | Unset = UNSET
    duration: int | Unset = UNSET
    duration_unit: str | Unset = UNSET
    start_on: str | Unset = UNSET
    finish_on: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        field_destroy = self.field_destroy

        period_type = self.period_type

        duration = self.duration

        duration_unit = self.duration_unit

        start_on = self.start_on

        finish_on = self.finish_on

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if field_destroy is not UNSET:
            field_dict["_destroy"] = field_destroy
        if period_type is not UNSET:
            field_dict["period_type"] = period_type
        if duration is not UNSET:
            field_dict["duration"] = duration
        if duration_unit is not UNSET:
            field_dict["duration_unit"] = duration_unit
        if start_on is not UNSET:
            field_dict["start_on"] = start_on
        if finish_on is not UNSET:
            field_dict["finish_on"] = finish_on

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        field_destroy = d.pop("_destroy", UNSET)

        period_type = d.pop("period_type", UNSET)

        duration = d.pop("duration", UNSET)

        duration_unit = d.pop("duration_unit", UNSET)

        start_on = d.pop("start_on", UNSET)

        finish_on = d.pop("finish_on", UNSET)

        put_api_20261001_resources_timeoff_blocked_periods_id_body_time_periods_attributes_item = (
            cls(
                id=id,
                name=name,
                field_destroy=field_destroy,
                period_type=period_type,
                duration=duration,
                duration_unit=duration_unit,
                start_on=start_on,
                finish_on=finish_on,
            )
        )

        put_api_20261001_resources_timeoff_blocked_periods_id_body_time_periods_attributes_item.additional_properties = d
        return (
            put_api_20261001_resources_timeoff_blocked_periods_id_body_time_periods_attributes_item
        )

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
