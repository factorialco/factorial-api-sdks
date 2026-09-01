from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.timeoff_allowance_stats_new_cycle_carry_overs_item_used_item import (
        TimeoffAllowanceStatsNewCycleCarryOversItemUsedItem,
    )


T = TypeVar("T", bound="TimeoffAllowanceStatsNewCycleCarryOversItem")


@_attrs_define
class TimeoffAllowanceStatsNewCycleCarryOversItem:
    from_cycle_ending_on: str
    """ The date on which the source cycle ended, from which these carry-over units originate. """
    non_expire: bool
    """ When true, carry-over units never expire regardless of expire_in_months. """
    total: str
    """ Total carry-over units available from the source cycle (days or hours depending on allowance type). """
    used: list[TimeoffAllowanceStatsNewCycleCarryOversItemUsedItem]
    """ Individual leave entries that consumed carry-over units. """
    accumulated: str
    """ Total carry-over units accumulated (may differ from total when caps apply). """
    expired: str
    """ Carry-over units that have expired. """
    taken: str
    """ Carry-over units already consumed by leave. """
    expire_in_months: int | Unset = UNSET
    """ Number of months after the cycle end date before carry-over units expire. Null means no expiry. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_cycle_ending_on = self.from_cycle_ending_on

        non_expire = self.non_expire

        total = self.total

        used = []
        for used_item_data in self.used:
            used_item = used_item_data.to_dict()
            used.append(used_item)

        accumulated = self.accumulated

        expired = self.expired

        taken = self.taken

        expire_in_months = self.expire_in_months

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "from_cycle_ending_on": from_cycle_ending_on,
                "non_expire": non_expire,
                "total": total,
                "used": used,
                "accumulated": accumulated,
                "expired": expired,
                "taken": taken,
            }
        )
        if expire_in_months is not UNSET:
            field_dict["expire_in_months"] = expire_in_months

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.timeoff_allowance_stats_new_cycle_carry_overs_item_used_item import (
            TimeoffAllowanceStatsNewCycleCarryOversItemUsedItem,
        )

        d = dict(src_dict)
        from_cycle_ending_on = d.pop("from_cycle_ending_on")

        non_expire = d.pop("non_expire")

        total = d.pop("total")

        used = []
        _used = d.pop("used")
        for used_item_data in _used:
            used_item = TimeoffAllowanceStatsNewCycleCarryOversItemUsedItem.from_dict(
                used_item_data
            )

            used.append(used_item)

        accumulated = d.pop("accumulated")

        expired = d.pop("expired")

        taken = d.pop("taken")

        expire_in_months = d.pop("expire_in_months", UNSET)

        timeoff_allowance_stats_new_cycle_carry_overs_item = cls(
            from_cycle_ending_on=from_cycle_ending_on,
            non_expire=non_expire,
            total=total,
            used=used,
            accumulated=accumulated,
            expired=expired,
            taken=taken,
            expire_in_months=expire_in_months,
        )

        timeoff_allowance_stats_new_cycle_carry_overs_item.additional_properties = d
        return timeoff_allowance_stats_new_cycle_carry_overs_item

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
