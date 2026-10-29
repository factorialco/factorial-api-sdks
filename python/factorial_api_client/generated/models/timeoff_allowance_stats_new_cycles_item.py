from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TimeoffAllowanceStatsNewCyclesItem")


@_attrs_define
class TimeoffAllowanceStatsNewCyclesItem:
    id: str
    """ Virtual ID of the cycle, composed of allowance_id/start_at/end_at. """
    start_at: str
    """ First day this counter covers for the employee. It is the latest of the policy cycle start
    (regular_start_at), the employee's hire date and the day the employee moved onto this policy, so it is later
    than regular_start_at when the counter opened part-way through the cycle (for example after a policy change).
    """
    end_at: str
    """ Last day this counter covers for the employee. It is the earliest of the policy cycle end (regular_end_at),
    the employee's termination date and the day before the employee moved off this policy, so it is earlier than
    regular_end_at when the counter closed part-way through the cycle. """
    regular_start_at: str
    """ First day of the policy's own cycle, regardless of when the employee joined the policy. """
    regular_end_at: str
    """ Last day of the policy's own cycle, regardless of when the employee left the policy. """
    allowance_id: str
    """ ID of the allowance this cycle belongs to. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        start_at = self.start_at

        end_at = self.end_at

        regular_start_at = self.regular_start_at

        regular_end_at = self.regular_end_at

        allowance_id = self.allowance_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "start_at": start_at,
                "end_at": end_at,
                "regular_start_at": regular_start_at,
                "regular_end_at": regular_end_at,
                "allowance_id": allowance_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        start_at = d.pop("start_at")

        end_at = d.pop("end_at")

        regular_start_at = d.pop("regular_start_at")

        regular_end_at = d.pop("regular_end_at")

        allowance_id = d.pop("allowance_id")

        timeoff_allowance_stats_new_cycles_item = cls(
            id=id,
            start_at=start_at,
            end_at=end_at,
            regular_start_at=regular_start_at,
            regular_end_at=regular_end_at,
            allowance_id=allowance_id,
        )

        timeoff_allowance_stats_new_cycles_item.additional_properties = d
        return timeoff_allowance_stats_new_cycles_item

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
