from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20261001ResourcesTeamsMembershipsBody")


@_attrs_define
class PostApi20261001ResourcesTeamsMembershipsBody:
    team_id: str
    """ Team id. """
    employee_id: str
    """ Employee id. """
    lead: bool | Unset = UNSET
    """ Makes the employee a lead of the team. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        team_id = self.team_id

        employee_id = self.employee_id

        lead = self.lead

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "team_id": team_id,
                "employee_id": employee_id,
            }
        )
        if lead is not UNSET:
            field_dict["lead"] = lead

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        team_id = d.pop("team_id")

        employee_id = d.pop("employee_id")

        lead = d.pop("lead", UNSET)

        post_api_20261001_resources_teams_memberships_body = cls(
            team_id=team_id,
            employee_id=employee_id,
            lead=lead,
        )

        post_api_20261001_resources_teams_memberships_body.additional_properties = d
        return post_api_20261001_resources_teams_memberships_body

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
