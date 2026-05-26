from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostApi20260401ResourcesWorkScheduleDayConfigurationsBulkCudBody")


@_attrs_define
class PostApi20260401ResourcesWorkScheduleDayConfigurationsBulkCudBody:
    overlap_period_id: int
    day_configurations: list[Any]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        overlap_period_id = self.overlap_period_id

        day_configurations = self.day_configurations

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "overlap_period_id": overlap_period_id,
                "day_configurations": day_configurations,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        overlap_period_id = d.pop("overlap_period_id")

        day_configurations = cast(list[Any], d.pop("day_configurations"))

        post_api_20260401_resources_work_schedule_day_configurations_bulk_cud_body = cls(
            overlap_period_id=overlap_period_id,
            day_configurations=day_configurations,
        )

        post_api_20260401_resources_work_schedule_day_configurations_bulk_cud_body.additional_properties = d
        return post_api_20260401_resources_work_schedule_day_configurations_bulk_cud_body

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
