from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.timeoff_french_leave_day_count_unit import TimeoffFrenchLeaveDayCountUnit

T = TypeVar("T", bound="TimeoffFrenchLeaveDayCount")


@_attrs_define
class TimeoffFrenchLeaveDayCount:
    leave_id: str
    """ Identifier of the leave this count belongs to """
    amount: float
    """ The counted quantity, expressed in the unit given by `unit` """
    unit: TimeoffFrenchLeaveDayCountUnit
    """ Whether the amount is a number of days or of hours """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        leave_id = self.leave_id

        amount = self.amount

        unit = self.unit.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "leave_id": leave_id,
                "amount": amount,
                "unit": unit,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        leave_id = d.pop("leave_id")

        amount = d.pop("amount")

        unit = TimeoffFrenchLeaveDayCountUnit(d.pop("unit"))

        timeoff_french_leave_day_count = cls(
            leave_id=leave_id,
            amount=amount,
            unit=unit,
        )

        timeoff_french_leave_day_count.additional_properties = d
        return timeoff_french_leave_day_count

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
