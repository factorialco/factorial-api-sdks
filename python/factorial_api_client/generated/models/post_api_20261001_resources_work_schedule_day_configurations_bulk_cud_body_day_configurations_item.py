from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar(
    "T",
    bound="PostApi20261001ResourcesWorkScheduleDayConfigurationsBulkCudBodyDayConfigurationsItem",
)


@_attrs_define
class PostApi20261001ResourcesWorkScheduleDayConfigurationsBulkCudBodyDayConfigurationsItem:
    weekday: str
    duration_in_seconds: int
    id: str | Unset = UNSET
    start_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        weekday = self.weekday

        duration_in_seconds = self.duration_in_seconds

        id = self.id

        start_at = self.start_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "weekday": weekday,
                "duration_in_seconds": duration_in_seconds,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if start_at is not UNSET:
            field_dict["start_at"] = start_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        weekday = d.pop("weekday")

        duration_in_seconds = d.pop("duration_in_seconds")

        id = d.pop("id", UNSET)

        start_at = d.pop("start_at", UNSET)

        post_api_20261001_resources_work_schedule_day_configurations_bulk_cud_body_day_configurations_item = cls(
            weekday=weekday,
            duration_in_seconds=duration_in_seconds,
            id=id,
            start_at=start_at,
        )

        post_api_20261001_resources_work_schedule_day_configurations_bulk_cud_body_day_configurations_item.additional_properties = d
        return post_api_20261001_resources_work_schedule_day_configurations_bulk_cud_body_day_configurations_item

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
