from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TimeoffPolicyTimelineItemsItemPolicyAssignment")


@_attrs_define
class TimeoffPolicyTimelineItemsItemPolicyAssignment:
    timeoff_policy_id: str
    employee_id: str
    effective_at: str
    id: str | Unset = UNSET
    timeoff_policy_name: str | Unset = UNSET
    is_initial: bool | Unset = UNSET
    end_effective_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timeoff_policy_id = self.timeoff_policy_id

        employee_id = self.employee_id

        effective_at = self.effective_at

        id = self.id

        timeoff_policy_name = self.timeoff_policy_name

        is_initial = self.is_initial

        end_effective_at = self.end_effective_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timeoff_policy_id": timeoff_policy_id,
                "employee_id": employee_id,
                "effective_at": effective_at,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if timeoff_policy_name is not UNSET:
            field_dict["timeoff_policy_name"] = timeoff_policy_name
        if is_initial is not UNSET:
            field_dict["is_initial"] = is_initial
        if end_effective_at is not UNSET:
            field_dict["end_effective_at"] = end_effective_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        timeoff_policy_id = d.pop("timeoff_policy_id")

        employee_id = d.pop("employee_id")

        effective_at = d.pop("effective_at")

        id = d.pop("id", UNSET)

        timeoff_policy_name = d.pop("timeoff_policy_name", UNSET)

        is_initial = d.pop("is_initial", UNSET)

        end_effective_at = d.pop("end_effective_at", UNSET)

        timeoff_policy_timeline_items_item_policy_assignment = cls(
            timeoff_policy_id=timeoff_policy_id,
            employee_id=employee_id,
            effective_at=effective_at,
            id=id,
            timeoff_policy_name=timeoff_policy_name,
            is_initial=is_initial,
            end_effective_at=end_effective_at,
        )

        timeoff_policy_timeline_items_item_policy_assignment.additional_properties = d
        return timeoff_policy_timeline_items_item_policy_assignment

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
