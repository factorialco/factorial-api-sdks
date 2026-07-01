from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

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
    company_id: str | Unset = UNSET
    """ Company ID of the membership """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        employee_id = self.employee_id

        team_id = self.team_id

        lead = self.lead

        company_id = self.company_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "employee_id": employee_id,
                "team_id": team_id,
                "lead": lead,
            }
        )
        if company_id is not UNSET:
            field_dict["company_id"] = company_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        employee_id = d.pop("employee_id")

        team_id = d.pop("team_id")

        lead = d.pop("lead")

        company_id = d.pop("company_id", UNSET)

        teams_membership = cls(
            id=id,
            employee_id=employee_id,
            team_id=team_id,
            lead=lead,
            company_id=company_id,
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
