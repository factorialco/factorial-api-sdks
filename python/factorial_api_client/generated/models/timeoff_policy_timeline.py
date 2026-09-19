from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.timeoff_policy_timeline_items_item import TimeoffPolicyTimelineItemsItem


T = TypeVar("T", bound="TimeoffPolicyTimeline")


@_attrs_define
class TimeoffPolicyTimeline:
    employee_id: str
    start_limit_date: str
    end_limit_date: str
    items: list[TimeoffPolicyTimelineItemsItem]
    id: str
    """ This is the employee id since it's a virtual entity """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        employee_id = self.employee_id

        start_limit_date = self.start_limit_date

        end_limit_date = self.end_limit_date

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "employee_id": employee_id,
                "start_limit_date": start_limit_date,
                "end_limit_date": end_limit_date,
                "items": items,
                "id": id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.timeoff_policy_timeline_items_item import TimeoffPolicyTimelineItemsItem

        d = dict(src_dict)
        employee_id = d.pop("employee_id")

        start_limit_date = d.pop("start_limit_date")

        end_limit_date = d.pop("end_limit_date")

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = TimeoffPolicyTimelineItemsItem.from_dict(items_item_data)

            items.append(items_item)

        id = d.pop("id")

        timeoff_policy_timeline = cls(
            employee_id=employee_id,
            start_limit_date=start_limit_date,
            end_limit_date=end_limit_date,
            items=items,
            id=id,
        )

        timeoff_policy_timeline.additional_properties = d
        return timeoff_policy_timeline

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
