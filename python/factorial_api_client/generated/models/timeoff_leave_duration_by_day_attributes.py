from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.timeoff_leave_duration_by_day_attributes_used_units_by_day import (
        TimeoffLeaveDurationByDayAttributesUsedUnitsByDay,
    )
    from ..models.timeoff_leave_duration_by_day_attributes_workable_units_by_day import (
        TimeoffLeaveDurationByDayAttributesWorkableUnitsByDay,
    )


T = TypeVar("T", bound="TimeoffLeaveDurationByDayAttributes")


@_attrs_define
class TimeoffLeaveDurationByDayAttributes:
    """Per-day breakdown of the leave's workable and used units, keyed by calendar date. Populated only when the read
    requests `include_duration_by_day=true`; null otherwise.

    """

    workable_units_by_day: TimeoffLeaveDurationByDayAttributesWorkableUnitsByDay
    used_units_by_day: TimeoffLeaveDurationByDayAttributesUsedUnitsByDay
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        workable_units_by_day = self.workable_units_by_day.to_dict()

        used_units_by_day = self.used_units_by_day.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "workable_units_by_day": workable_units_by_day,
                "used_units_by_day": used_units_by_day,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.timeoff_leave_duration_by_day_attributes_used_units_by_day import (
            TimeoffLeaveDurationByDayAttributesUsedUnitsByDay,
        )
        from ..models.timeoff_leave_duration_by_day_attributes_workable_units_by_day import (
            TimeoffLeaveDurationByDayAttributesWorkableUnitsByDay,
        )

        d = dict(src_dict)
        workable_units_by_day = TimeoffLeaveDurationByDayAttributesWorkableUnitsByDay.from_dict(
            d.pop("workable_units_by_day")
        )

        used_units_by_day = TimeoffLeaveDurationByDayAttributesUsedUnitsByDay.from_dict(
            d.pop("used_units_by_day")
        )

        timeoff_leave_duration_by_day_attributes = cls(
            workable_units_by_day=workable_units_by_day,
            used_units_by_day=used_units_by_day,
        )

        timeoff_leave_duration_by_day_attributes.additional_properties = d
        return timeoff_leave_duration_by_day_attributes

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
