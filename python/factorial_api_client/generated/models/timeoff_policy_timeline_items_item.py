from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.timeoff_policy_timeline_items_item_policy_assignment import (
        TimeoffPolicyTimelineItemsItemPolicyAssignment,
    )


T = TypeVar("T", bound="TimeoffPolicyTimelineItemsItem")


@_attrs_define
class TimeoffPolicyTimelineItemsItem:
    policy_assignment: TimeoffPolicyTimelineItemsItemPolicyAssignment
    start_at: str
    end_at: str
    is_first_item: bool
    is_last_item: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        policy_assignment = self.policy_assignment.to_dict()

        start_at = self.start_at

        end_at = self.end_at

        is_first_item = self.is_first_item

        is_last_item = self.is_last_item

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "policy_assignment": policy_assignment,
                "start_at": start_at,
                "end_at": end_at,
                "is_first_item": is_first_item,
                "is_last_item": is_last_item,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.timeoff_policy_timeline_items_item_policy_assignment import (
            TimeoffPolicyTimelineItemsItemPolicyAssignment,
        )

        d = dict(src_dict)
        policy_assignment = TimeoffPolicyTimelineItemsItemPolicyAssignment.from_dict(
            d.pop("policy_assignment")
        )

        start_at = d.pop("start_at")

        end_at = d.pop("end_at")

        is_first_item = d.pop("is_first_item")

        is_last_item = d.pop("is_last_item")

        timeoff_policy_timeline_items_item = cls(
            policy_assignment=policy_assignment,
            start_at=start_at,
            end_at=end_at,
            is_first_item=is_first_item,
            is_last_item=is_last_item,
        )

        timeoff_policy_timeline_items_item.additional_properties = d
        return timeoff_policy_timeline_items_item

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
