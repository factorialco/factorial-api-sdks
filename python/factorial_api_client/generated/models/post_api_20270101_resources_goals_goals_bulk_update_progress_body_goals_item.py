from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20270101ResourcesGoalsGoalsBulkUpdateProgressBodyGoalsItem")


@_attrs_define
class PostApi20270101ResourcesGoalsGoalsBulkUpdateProgressBodyGoalsItem:
    id: str
    """ Id of the goal to update, refers to goals/goals endpoint """
    value: float
    """ New attainment value, in the goal's unit """
    comment: str | Unset = UNSET
    """ Optional note shown with the update in the progress history (maximum 2000 characters) """
    period_starts_on: str | Unset = UNSET
    """ Start date of the target period to record the value on. Required when the goal has target periods; must be
    empty when it has none. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        value = self.value

        comment = self.comment

        period_starts_on = self.period_starts_on

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "value": value,
            }
        )
        if comment is not UNSET:
            field_dict["comment"] = comment
        if period_starts_on is not UNSET:
            field_dict["period_starts_on"] = period_starts_on

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        value = d.pop("value")

        comment = d.pop("comment", UNSET)

        period_starts_on = d.pop("period_starts_on", UNSET)

        post_api_20270101_resources_goals_goals_bulk_update_progress_body_goals_item = cls(
            id=id,
            value=value,
            comment=comment,
            period_starts_on=period_starts_on,
        )

        post_api_20270101_resources_goals_goals_bulk_update_progress_body_goals_item.additional_properties = d
        return post_api_20270101_resources_goals_goals_bulk_update_progress_body_goals_item

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
