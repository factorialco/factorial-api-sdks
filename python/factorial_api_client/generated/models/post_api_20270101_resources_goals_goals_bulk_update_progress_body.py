from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_api_20270101_resources_goals_goals_bulk_update_progress_body_goals_item import (
        PostApi20270101ResourcesGoalsGoalsBulkUpdateProgressBodyGoalsItem,
    )


T = TypeVar("T", bound="PostApi20270101ResourcesGoalsGoalsBulkUpdateProgressBody")


@_attrs_define
class PostApi20270101ResourcesGoalsGoalsBulkUpdateProgressBody:
    goals: list[PostApi20270101ResourcesGoalsGoalsBulkUpdateProgressBodyGoalsItem]
    """ One entry per goal and period to update (maximum 200) """
    author_id: str | Unset = UNSET
    """ Id of the employee every update is recorded as, refers to employees/employees endpoint. Required with a
    company API key or company-level OAuth token. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        goals = []
        for goals_item_data in self.goals:
            goals_item = goals_item_data.to_dict()
            goals.append(goals_item)

        author_id = self.author_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "goals": goals,
            }
        )
        if author_id is not UNSET:
            field_dict["author_id"] = author_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_api_20270101_resources_goals_goals_bulk_update_progress_body_goals_item import (
            PostApi20270101ResourcesGoalsGoalsBulkUpdateProgressBodyGoalsItem,
        )

        d = dict(src_dict)
        goals = []
        _goals = d.pop("goals")
        for goals_item_data in _goals:
            goals_item = (
                PostApi20270101ResourcesGoalsGoalsBulkUpdateProgressBodyGoalsItem.from_dict(
                    goals_item_data
                )
            )

            goals.append(goals_item)

        author_id = d.pop("author_id", UNSET)

        post_api_20270101_resources_goals_goals_bulk_update_progress_body = cls(
            goals=goals,
            author_id=author_id,
        )

        post_api_20270101_resources_goals_goals_bulk_update_progress_body.additional_properties = d
        return post_api_20270101_resources_goals_goals_bulk_update_progress_body

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
