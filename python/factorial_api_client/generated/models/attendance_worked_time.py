from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.attendance_worked_time_day_type import AttendanceWorkedTimeDayType
from ..models.attendance_worked_time_time_unit import AttendanceWorkedTimeTimeUnit

if TYPE_CHECKING:
    from ..models.attendance_worked_time_worked_time_blocks_item import (
        AttendanceWorkedTimeWorkedTimeBlocksItem,
    )


T = TypeVar("T", bound="AttendanceWorkedTime")


@_attrs_define
class AttendanceWorkedTime:
    employee_id: str
    date: str
    company_id: str
    tracked_minutes: int
    multiplied_minutes: int
    pending_minutes: int
    minutes: int
    time_unit: AttendanceWorkedTimeTimeUnit
    worked_time_blocks: list[AttendanceWorkedTimeWorkedTimeBlocksItem]
    day_type: AttendanceWorkedTimeDayType
    id: str
    """ ID to specify the worked time it includes the employee_id and date """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        employee_id = self.employee_id

        date = self.date

        company_id = self.company_id

        tracked_minutes = self.tracked_minutes

        multiplied_minutes = self.multiplied_minutes

        pending_minutes = self.pending_minutes

        minutes = self.minutes

        time_unit = self.time_unit.value

        worked_time_blocks = []
        for worked_time_blocks_item_data in self.worked_time_blocks:
            worked_time_blocks_item = worked_time_blocks_item_data.to_dict()
            worked_time_blocks.append(worked_time_blocks_item)

        day_type = self.day_type.value

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "employee_id": employee_id,
                "date": date,
                "company_id": company_id,
                "tracked_minutes": tracked_minutes,
                "multiplied_minutes": multiplied_minutes,
                "pending_minutes": pending_minutes,
                "minutes": minutes,
                "time_unit": time_unit,
                "worked_time_blocks": worked_time_blocks,
                "day_type": day_type,
                "id": id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.attendance_worked_time_worked_time_blocks_item import (
            AttendanceWorkedTimeWorkedTimeBlocksItem,
        )

        d = dict(src_dict)
        employee_id = d.pop("employee_id")

        date = d.pop("date")

        company_id = d.pop("company_id")

        tracked_minutes = d.pop("tracked_minutes")

        multiplied_minutes = d.pop("multiplied_minutes")

        pending_minutes = d.pop("pending_minutes")

        minutes = d.pop("minutes")

        time_unit = AttendanceWorkedTimeTimeUnit(d.pop("time_unit"))

        worked_time_blocks = []
        _worked_time_blocks = d.pop("worked_time_blocks")
        for worked_time_blocks_item_data in _worked_time_blocks:
            worked_time_blocks_item = AttendanceWorkedTimeWorkedTimeBlocksItem.from_dict(
                worked_time_blocks_item_data
            )

            worked_time_blocks.append(worked_time_blocks_item)

        day_type = AttendanceWorkedTimeDayType(d.pop("day_type"))

        id = d.pop("id")

        attendance_worked_time = cls(
            employee_id=employee_id,
            date=date,
            company_id=company_id,
            tracked_minutes=tracked_minutes,
            multiplied_minutes=multiplied_minutes,
            pending_minutes=pending_minutes,
            minutes=minutes,
            time_unit=time_unit,
            worked_time_blocks=worked_time_blocks,
            day_type=day_type,
            id=id,
        )

        attendance_worked_time.additional_properties = d
        return attendance_worked_time

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
