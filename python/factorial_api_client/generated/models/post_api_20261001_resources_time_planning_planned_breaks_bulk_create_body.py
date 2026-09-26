from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.post_api_20261001_resources_time_planning_planned_breaks_bulk_create_body_planned_breaks_item import (
        PostApi20261001ResourcesTimePlanningPlannedBreaksBulkCreateBodyPlannedBreaksItem,
    )


T = TypeVar("T", bound="PostApi20261001ResourcesTimePlanningPlannedBreaksBulkCreateBody")


@_attrs_define
class PostApi20261001ResourcesTimePlanningPlannedBreaksBulkCreateBody:
    planned_breaks: list[
        PostApi20261001ResourcesTimePlanningPlannedBreaksBulkCreateBodyPlannedBreaksItem
    ]
    """ List of planned breaks to create """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        planned_breaks = []
        for planned_breaks_item_data in self.planned_breaks:
            planned_breaks_item = planned_breaks_item_data.to_dict()
            planned_breaks.append(planned_breaks_item)

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
        from ..models.post_api_20261001_resources_time_planning_planned_breaks_bulk_create_body_planned_breaks_item import (
            PostApi20261001ResourcesTimePlanningPlannedBreaksBulkCreateBodyPlannedBreaksItem,
        )

        d = dict(src_dict)
        planned_breaks = []
        _planned_breaks = d.pop("planned_breaks")
        for planned_breaks_item_data in _planned_breaks:
            planned_breaks_item = PostApi20261001ResourcesTimePlanningPlannedBreaksBulkCreateBodyPlannedBreaksItem.from_dict(
                planned_breaks_item_data
            )

            planned_breaks.append(planned_breaks_item)

        post_api_20261001_resources_time_planning_planned_breaks_bulk_create_body = cls(
            planned_breaks=planned_breaks,
        )

        post_api_20261001_resources_time_planning_planned_breaks_bulk_create_body.additional_properties = d
        return post_api_20261001_resources_time_planning_planned_breaks_bulk_create_body

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
