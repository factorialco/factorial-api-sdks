from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PutApi20260401ResourcesTimeoffBlockedPeriodsIdBody")


@_attrs_define
class PutApi20260401ResourcesTimeoffBlockedPeriodsIdBody:
    id: int
    name: str
    """ Name of the blocked period. """
    leave_type_ids: list[int]
    """ List of leave type identifiers for which employees can not request timeoff edited """
    time_periods_attributes: list[Any]
    """ The tenure periods associated with the allowance edited. """
    strategy: str
    """ Type of access group """
    members: list[int] | Unset = UNSET
    """ List of employees manually selected """
    query: str | Unset = UNSET
    team_ids: list[int] | Unset = UNSET
    """ List of team identifiers which the selected employees belong to """
    location_ids: list[int] | Unset = UNSET
    """ List of locations workplace identifiers where the employees are located """
    legal_entity_ids: list[int] | Unset = UNSET
    """ List of legal entity identifiers which the selected employees belong to """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        leave_type_ids = self.leave_type_ids

        time_periods_attributes = self.time_periods_attributes

        strategy = self.strategy

        members: list[int] | Unset = UNSET
        if not isinstance(self.members, Unset):
            members = self.members

        query = self.query

        team_ids: list[int] | Unset = UNSET
        if not isinstance(self.team_ids, Unset):
            team_ids = self.team_ids

        location_ids: list[int] | Unset = UNSET
        if not isinstance(self.location_ids, Unset):
            location_ids = self.location_ids

        legal_entity_ids: list[int] | Unset = UNSET
        if not isinstance(self.legal_entity_ids, Unset):
            legal_entity_ids = self.legal_entity_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "leave_type_ids": leave_type_ids,
                "time_periods_attributes": time_periods_attributes,
                "strategy": strategy,
            }
        )
        if members is not UNSET:
            field_dict["members"] = members
        if query is not UNSET:
            field_dict["query"] = query
        if team_ids is not UNSET:
            field_dict["team_ids"] = team_ids
        if location_ids is not UNSET:
            field_dict["location_ids"] = location_ids
        if legal_entity_ids is not UNSET:
            field_dict["legal_entity_ids"] = legal_entity_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        leave_type_ids = cast(list[int], d.pop("leave_type_ids"))

        time_periods_attributes = cast(list[Any], d.pop("time_periods_attributes"))

        strategy = d.pop("strategy")

        members = cast(list[int], d.pop("members", UNSET))

        query = d.pop("query", UNSET)

        team_ids = cast(list[int], d.pop("team_ids", UNSET))

        location_ids = cast(list[int], d.pop("location_ids", UNSET))

        legal_entity_ids = cast(list[int], d.pop("legal_entity_ids", UNSET))

        put_api_20260401_resources_timeoff_blocked_periods_id_body = cls(
            id=id,
            name=name,
            leave_type_ids=leave_type_ids,
            time_periods_attributes=time_periods_attributes,
            strategy=strategy,
            members=members,
            query=query,
            team_ids=team_ids,
            location_ids=location_ids,
            legal_entity_ids=legal_entity_ids,
        )

        put_api_20260401_resources_timeoff_blocked_periods_id_body.additional_properties = d
        return put_api_20260401_resources_timeoff_blocked_periods_id_body

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
