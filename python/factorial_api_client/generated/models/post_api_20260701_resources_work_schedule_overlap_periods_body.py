from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostApi20260701ResourcesWorkScheduleOverlapPeriodsBody")


@_attrs_define
class PostApi20260701ResourcesWorkScheduleOverlapPeriodsBody:
    author: str
    schedule_id: str
    create_params: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        author = self.author

        schedule_id = self.schedule_id

        create_params = self.create_params

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "author": author,
                "schedule_id": schedule_id,
                "create_params": create_params,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        author = d.pop("author")

        schedule_id = d.pop("schedule_id")

        create_params = d.pop("create_params")

        post_api_20260701_resources_work_schedule_overlap_periods_body = cls(
            author=author,
            schedule_id=schedule_id,
            create_params=create_params,
        )

        post_api_20260701_resources_work_schedule_overlap_periods_body.additional_properties = d
        return post_api_20260701_resources_work_schedule_overlap_periods_body

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
