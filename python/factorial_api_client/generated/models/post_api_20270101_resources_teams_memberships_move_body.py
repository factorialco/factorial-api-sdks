from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20270101ResourcesTeamsMembershipsMoveBody")


@_attrs_define
class PostApi20270101ResourcesTeamsMembershipsMoveBody:
    id: str
    """ ID of the membership to move (must be a direct membership) """
    destination_team_id: str
    """ ID of the destination team """
    lead: bool | Unset = UNSET
    """ Whether the employee should be a lead in the destination team. Omit it to keep the membership's current lead
    flag; pass false to move the employee and drop their leadership. Worth being explicit when restructuring:
    omitting it carries leadership across, so a lead of a small team who lands in a large one leads the large one.
    """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        destination_team_id = self.destination_team_id

        lead = self.lead

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "destination_team_id": destination_team_id,
            }
        )
        if lead is not UNSET:
            field_dict["lead"] = lead

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        destination_team_id = d.pop("destination_team_id")

        lead = d.pop("lead", UNSET)

        post_api_20270101_resources_teams_memberships_move_body = cls(
            id=id,
            destination_team_id=destination_team_id,
            lead=lead,
        )

        post_api_20270101_resources_teams_memberships_move_body.additional_properties = d
        return post_api_20270101_resources_teams_memberships_move_body

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
