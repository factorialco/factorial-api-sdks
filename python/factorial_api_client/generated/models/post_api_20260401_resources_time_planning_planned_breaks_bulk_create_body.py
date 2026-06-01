from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostApi20260401ResourcesTimePlanningPlannedBreaksBulkCreateBody")


@_attrs_define
class PostApi20260401ResourcesTimePlanningPlannedBreaksBulkCreateBody:
    planned_breaks: list[Any]
    """ List of planned breaks to create """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        planned_breaks = self.planned_breaks

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "planned_breaks": planned_breaks,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        planned_breaks = cast(list[Any], d.pop("planned_breaks"))

        post_api_20260401_resources_time_planning_planned_breaks_bulk_create_body = cls(
            planned_breaks=planned_breaks,
        )

        post_api_20260401_resources_time_planning_planned_breaks_bulk_create_body.additional_properties = d
        return post_api_20260401_resources_time_planning_planned_breaks_bulk_create_body

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
