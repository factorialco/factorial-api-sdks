from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.attendance_estimated_time_source import AttendanceEstimatedTimeSource
from ..models.attendance_estimated_time_time_unit import AttendanceEstimatedTimeTimeUnit

if TYPE_CHECKING:
    from ..models.attendance_estimated_time_breaks_item import AttendanceEstimatedTimeBreaksItem
    from ..models.attendance_estimated_time_shifts_item import AttendanceEstimatedTimeShiftsItem


T = TypeVar("T", bound="AttendanceEstimatedTime")


@_attrs_define
class AttendanceEstimatedTime:
    date: str
    company_id: str
    employee_id: str
    expected_minutes: float
    """ Amount of minutes the employee has to work without taking into consideration time off leaves and bank
    holidays. """
    regular_minutes: float
    """ Amount of regular minutes the employee has to work. """
    overtime_minutes: float
    """ Amount of overtime minutes the employee has to work (only available with Shift Management). """
    breaks: list[AttendanceEstimatedTimeBreaksItem]
    time_unit: AttendanceEstimatedTimeTimeUnit
    estimated_half_days: int
    shifts: list[AttendanceEstimatedTimeShiftsItem]
    source: AttendanceEstimatedTimeSource
    """ Source of the estimated time. Could be employee's contract, work schedule or shift management. """
    id: str
    """ ID to specify the estimation time it includes the employee_id and date """
    minutes: float
    """ Amount of minutes the employee has to work. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date

        company_id = self.company_id

        employee_id = self.employee_id

        expected_minutes = self.expected_minutes

        regular_minutes = self.regular_minutes

        overtime_minutes = self.overtime_minutes

        breaks = []
        for breaks_item_data in self.breaks:
            breaks_item = breaks_item_data.to_dict()
            breaks.append(breaks_item)

        time_unit = self.time_unit.value

        estimated_half_days = self.estimated_half_days

        shifts = []
        for shifts_item_data in self.shifts:
            shifts_item = shifts_item_data.to_dict()
            shifts.append(shifts_item)

        source = self.source.value

        id = self.id

        minutes = self.minutes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "date": date,
                "company_id": company_id,
                "employee_id": employee_id,
                "expected_minutes": expected_minutes,
                "regular_minutes": regular_minutes,
                "overtime_minutes": overtime_minutes,
                "breaks": breaks,
                "time_unit": time_unit,
                "estimated_half_days": estimated_half_days,
                "shifts": shifts,
                "source": source,
                "id": id,
                "minutes": minutes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.attendance_estimated_time_breaks_item import AttendanceEstimatedTimeBreaksItem
        from ..models.attendance_estimated_time_shifts_item import AttendanceEstimatedTimeShiftsItem

        d = dict(src_dict)
        date = d.pop("date")

        company_id = d.pop("company_id")

        employee_id = d.pop("employee_id")

        expected_minutes = d.pop("expected_minutes")

        regular_minutes = d.pop("regular_minutes")

        overtime_minutes = d.pop("overtime_minutes")

        breaks = []
        _breaks = d.pop("breaks")
        for breaks_item_data in _breaks:
            breaks_item = AttendanceEstimatedTimeBreaksItem.from_dict(breaks_item_data)

            breaks.append(breaks_item)

        time_unit = AttendanceEstimatedTimeTimeUnit(d.pop("time_unit"))

        estimated_half_days = d.pop("estimated_half_days")

        shifts = []
        _shifts = d.pop("shifts")
        for shifts_item_data in _shifts:
            shifts_item = AttendanceEstimatedTimeShiftsItem.from_dict(shifts_item_data)

            shifts.append(shifts_item)

        source = AttendanceEstimatedTimeSource(d.pop("source"))

        id = d.pop("id")

        minutes = d.pop("minutes")

        attendance_estimated_time = cls(
            date=date,
            company_id=company_id,
            employee_id=employee_id,
            expected_minutes=expected_minutes,
            regular_minutes=regular_minutes,
            overtime_minutes=overtime_minutes,
            breaks=breaks,
            time_unit=time_unit,
            estimated_half_days=estimated_half_days,
            shifts=shifts,
            source=source,
            id=id,
            minutes=minutes,
        )

        attendance_estimated_time.additional_properties = d
        return attendance_estimated_time

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
