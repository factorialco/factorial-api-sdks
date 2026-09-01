from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.timeoff_blocked_periods_policy_time_periods_item import (
        TimeoffBlockedPeriodsPolicyTimePeriodsItem,
    )


T = TypeVar("T", bound="TimeoffBlockedPeriodsPolicy")


@_attrs_define
class TimeoffBlockedPeriodsPolicy:
    id: str
    """ Unique identifier of the blocked period """
    company_id: str
    """ Company id of the blocked period """
    name: str
    """ Name of the blocked period. """
    leave_type_ids: list[str]
    """ Leave types for which absence request has been blocked """
    time_periods: list[TimeoffBlockedPeriodsPolicyTimePeriodsItem]
    """ The tenure periods associated with the allowance. """
    strategy: str
    """ Type of access group """
    members: list[str]
    """ Employees whose timeoff will be affected """
    location_ids: list[str] | Unset = UNSET
    """ List of locations workplace identifiers where the employees are located """
    team_ids: list[str] | Unset = UNSET
    """ List of team identifiers which the selected employees belong to """
    legal_entity_ids: list[str] | Unset = UNSET
    """ List of legal entity identifiers which the selected employees belong to """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        company_id = self.company_id

        name = self.name

        leave_type_ids = self.leave_type_ids

        time_periods = []
        for time_periods_item_data in self.time_periods:
            time_periods_item = time_periods_item_data.to_dict()
            time_periods.append(time_periods_item)

        strategy = self.strategy

        members = self.members

        location_ids: list[str] | Unset = UNSET
        if not isinstance(self.location_ids, Unset):
            location_ids = self.location_ids

        team_ids: list[str] | Unset = UNSET
        if not isinstance(self.team_ids, Unset):
            team_ids = self.team_ids

        legal_entity_ids: list[str] | Unset = UNSET
        if not isinstance(self.legal_entity_ids, Unset):
            legal_entity_ids = self.legal_entity_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "company_id": company_id,
                "name": name,
                "leave_type_ids": leave_type_ids,
                "time_periods": time_periods,
                "strategy": strategy,
                "members": members,
            }
        )
        if location_ids is not UNSET:
            field_dict["location_ids"] = location_ids
        if team_ids is not UNSET:
            field_dict["team_ids"] = team_ids
        if legal_entity_ids is not UNSET:
            field_dict["legal_entity_ids"] = legal_entity_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.timeoff_blocked_periods_policy_time_periods_item import (
            TimeoffBlockedPeriodsPolicyTimePeriodsItem,
        )

        d = dict(src_dict)
        id = d.pop("id")

        company_id = d.pop("company_id")

        name = d.pop("name")

        leave_type_ids = cast(list[str], d.pop("leave_type_ids"))

        time_periods = []
        _time_periods = d.pop("time_periods")
        for time_periods_item_data in _time_periods:
            time_periods_item = TimeoffBlockedPeriodsPolicyTimePeriodsItem.from_dict(
                time_periods_item_data
            )

            time_periods.append(time_periods_item)

        strategy = d.pop("strategy")

        members = cast(list[str], d.pop("members"))

        location_ids = cast(list[str], d.pop("location_ids", UNSET))

        team_ids = cast(list[str], d.pop("team_ids", UNSET))

        legal_entity_ids = cast(list[str], d.pop("legal_entity_ids", UNSET))

        timeoff_blocked_periods_policy = cls(
            id=id,
            company_id=company_id,
            name=name,
            leave_type_ids=leave_type_ids,
            time_periods=time_periods,
            strategy=strategy,
            members=members,
            location_ids=location_ids,
            team_ids=team_ids,
            legal_entity_ids=legal_entity_ids,
        )

        timeoff_blocked_periods_policy.additional_properties = d
        return timeoff_blocked_periods_policy

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
