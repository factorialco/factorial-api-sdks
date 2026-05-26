from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TeamsTeam")


@_attrs_define
class TeamsTeam:
    id: int
    name: str
    company_id: int
    description: str | Unset = UNSET
    avatar: str | Unset = UNSET
    employee_ids: list[int] | Unset = UNSET
    lead_ids: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        company_id = self.company_id

        description = self.description

        avatar = self.avatar

        employee_ids: list[int] | Unset = UNSET
        if not isinstance(self.employee_ids, Unset):
            employee_ids = self.employee_ids

        lead_ids: list[int] | Unset = UNSET
        if not isinstance(self.lead_ids, Unset):
            lead_ids = self.lead_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "company_id": company_id,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if employee_ids is not UNSET:
            field_dict["employee_ids"] = employee_ids
        if lead_ids is not UNSET:
            field_dict["lead_ids"] = lead_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        company_id = d.pop("company_id")

        description = d.pop("description", UNSET)

        avatar = d.pop("avatar", UNSET)

        employee_ids = cast(list[int], d.pop("employee_ids", UNSET))

        lead_ids = cast(list[int], d.pop("lead_ids", UNSET))

        teams_team = cls(
            id=id,
            name=name,
            company_id=company_id,
            description=description,
            avatar=avatar,
            employee_ids=employee_ids,
            lead_ids=lead_ids,
        )

        teams_team.additional_properties = d
        return teams_team

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
