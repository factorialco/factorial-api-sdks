from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20270101ResourcesGoalsGoalsUpdateProgressBody")


@_attrs_define
class PostApi20270101ResourcesGoalsGoalsUpdateProgressBody:
    id: str
    """ Id of the goal to update, refers to goals/goals endpoint """
    value: float
    """ New attainment value, in the goal's unit """
    comment: str | Unset = UNSET
    """ Optional note shown with the update in the progress history (maximum 2000 characters) """
    period_starts_on: str | Unset = UNSET
    """ Start date of the target period to record the value on. Required when the goal has target periods; must be
    empty when it has none. Find the periods with goals/target_periods. """
    author_id: str | Unset = UNSET
    """ Id of the employee the update is recorded as, refers to employees/employees endpoint. Required with a
    company API key or company-level OAuth token. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        value = self.value

        comment = self.comment

        period_starts_on = self.period_starts_on

        author_id = self.author_id

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
        if author_id is not UNSET:
            field_dict["author_id"] = author_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        value = d.pop("value")

        comment = d.pop("comment", UNSET)

        period_starts_on = d.pop("period_starts_on", UNSET)

        author_id = d.pop("author_id", UNSET)

        post_api_20270101_resources_goals_goals_update_progress_body = cls(
            id=id,
            value=value,
            comment=comment,
            period_starts_on=period_starts_on,
            author_id=author_id,
        )

        post_api_20270101_resources_goals_goals_update_progress_body.additional_properties = d
        return post_api_20270101_resources_goals_goals_update_progress_body

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
