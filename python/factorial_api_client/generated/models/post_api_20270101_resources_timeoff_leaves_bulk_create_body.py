from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.post_api_20270101_resources_timeoff_leaves_bulk_create_body_leaves_item import (
        PostApi20270101ResourcesTimeoffLeavesBulkCreateBodyLeavesItem,
    )


T = TypeVar("T", bound="PostApi20270101ResourcesTimeoffLeavesBulkCreateBody")


@_attrs_define
class PostApi20270101ResourcesTimeoffLeavesBulkCreateBody:
    leaves: list[PostApi20270101ResourcesTimeoffLeavesBulkCreateBodyLeavesItem]
    """ The leaves to create, at most 50 """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        leaves = []
        for leaves_item_data in self.leaves:
            leaves_item = leaves_item_data.to_dict()
            leaves.append(leaves_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "leaves": leaves,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_api_20270101_resources_timeoff_leaves_bulk_create_body_leaves_item import (
            PostApi20270101ResourcesTimeoffLeavesBulkCreateBodyLeavesItem,
        )

        d = dict(src_dict)
        leaves = []
        _leaves = d.pop("leaves")
        for leaves_item_data in _leaves:
            leaves_item = PostApi20270101ResourcesTimeoffLeavesBulkCreateBodyLeavesItem.from_dict(
                leaves_item_data
            )

            leaves.append(leaves_item)

        post_api_20270101_resources_timeoff_leaves_bulk_create_body = cls(
            leaves=leaves,
        )

        post_api_20270101_resources_timeoff_leaves_bulk_create_body.additional_properties = d
        return post_api_20270101_resources_timeoff_leaves_bulk_create_body

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
