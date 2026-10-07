from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20270101ResourcesTeamsTeamsBody")


@_attrs_define
class PostApi20270101ResourcesTeamsTeamsBody:
    name: str
    """ Name of the team. """
    description: str | Unset = UNSET
    """ Description of the team """
    parent_team_id: str | Unset = UNSET
    """ ID of the parent team to nest the new team under (omit or null for a root team). Requires the nested teams
    feature and permission to manage the parent team; the hierarchy is capped at 4 levels. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        parent_team_id = self.parent_team_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if parent_team_id is not UNSET:
            field_dict["parent_team_id"] = parent_team_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description", UNSET)

        parent_team_id = d.pop("parent_team_id", UNSET)

        post_api_20270101_resources_teams_teams_body = cls(
            name=name,
            description=description,
            parent_team_id=parent_team_id,
        )

        post_api_20270101_resources_teams_teams_body.additional_properties = d
        return post_api_20270101_resources_teams_teams_body

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
