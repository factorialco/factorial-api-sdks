from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TimeoffBlockedPeriodsPolicyTimePeriodsItem")


@_attrs_define
class TimeoffBlockedPeriodsPolicyTimePeriodsItem:
    id: str
    policy_id: str
    name: str
    period_type: str
    start_on: str | Unset = UNSET
    finish_on: str | Unset = UNSET
    duration: int | Unset = UNSET
    duration_unit: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        policy_id = self.policy_id

        name = self.name

        period_type = self.period_type

        start_on = self.start_on

        finish_on = self.finish_on

        duration = self.duration

        duration_unit = self.duration_unit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "policy_id": policy_id,
                "name": name,
                "period_type": period_type,
            }
        )
        if start_on is not UNSET:
            field_dict["start_on"] = start_on
        if finish_on is not UNSET:
            field_dict["finish_on"] = finish_on
        if duration is not UNSET:
            field_dict["duration"] = duration
        if duration_unit is not UNSET:
            field_dict["duration_unit"] = duration_unit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        policy_id = d.pop("policy_id")

        name = d.pop("name")

        period_type = d.pop("period_type")

        start_on = d.pop("start_on", UNSET)

        finish_on = d.pop("finish_on", UNSET)

        duration = d.pop("duration", UNSET)

        duration_unit = d.pop("duration_unit", UNSET)

        timeoff_blocked_periods_policy_time_periods_item = cls(
            id=id,
            policy_id=policy_id,
            name=name,
            period_type=period_type,
            start_on=start_on,
            finish_on=finish_on,
            duration=duration,
            duration_unit=duration_unit,
        )

        timeoff_blocked_periods_policy_time_periods_item.additional_properties = d
        return timeoff_blocked_periods_policy_time_periods_item

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
