from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TeamsMembership")


@_attrs_define
class TeamsMembership:
    id: str
    """ Membership ID """
    employee_id: str
    """ Employee ID of the membership """
    team_id: str
    """ Team ID of the membership """
    lead: bool
    """ Whether the employee is a lead of the team or not """
    source_team_ids: list[str]
    """ IDs of the teams this membership originates from (nested teams). In a company with nested teams, a direct
    membership includes the team itself; an inherited one, the sub-team(s) where the employee is a direct member.
    Only populated on reads that compute source attribution — reads filtered by a single team, or by a single
    employee with `with_source_attribution` enabled. Empty otherwise, including create, update and delete responses,
    and always empty for companies without nested teams. An empty array does not distinguish "computed and genuinely
    empty" from "not computed for this read" or "could not be computed", so only apply attribution-dependent logic
    to a read you explicitly shaped for it. A team-anchored read stops attributing above roughly a thousand members
    of the filtered team: past that the attribution is not computed at all and every row comes back empty, behind a
    normal `200`. """
    parent_team_ids: list[str]
    """ IDs of the ancestor teams that receive an inherited membership through this row (nested teams) — the teams
    this membership rolls up into. Populated under the same conditions as `source_team_ids`; empty otherwise. """
    company_id: str | Unset = UNSET
    """ Company ID of the membership """
    direct: bool | Unset = UNSET
    """ Whether the employee is a direct member of the team (nested teams). Always present. `true` means direct
    member; `false` means the row exists only through inheritance from a sub-team; `null` means not computed for
    this read. Only computed on reads filtered by a single employee with `with_source_attribution` enabled — always
    `null` otherwise, including create, update and delete responses and companies without nested teams. `null` is
    also returned when directness could not be resolved for a transient reason, even with `with_source_attribution`
    enabled, so never treat `null` as `false` — retry the read instead. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        employee_id = self.employee_id

        team_id = self.team_id

        lead = self.lead

        source_team_ids = self.source_team_ids

        parent_team_ids = self.parent_team_ids

        company_id = self.company_id

        direct = self.direct

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "employee_id": employee_id,
                "team_id": team_id,
                "lead": lead,
                "source_team_ids": source_team_ids,
                "parent_team_ids": parent_team_ids,
            }
        )
        if company_id is not UNSET:
            field_dict["company_id"] = company_id
        if direct is not UNSET:
            field_dict["direct"] = direct

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        employee_id = d.pop("employee_id")

        team_id = d.pop("team_id")

        lead = d.pop("lead")

        source_team_ids = cast(list[str], d.pop("source_team_ids"))

        parent_team_ids = cast(list[str], d.pop("parent_team_ids"))

        company_id = d.pop("company_id", UNSET)

        direct = d.pop("direct", UNSET)

        teams_membership = cls(
            id=id,
            employee_id=employee_id,
            team_id=team_id,
            lead=lead,
            source_team_ids=source_team_ids,
            parent_team_ids=parent_team_ids,
            company_id=company_id,
            direct=direct,
        )

        teams_membership.additional_properties = d
        return teams_membership

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
