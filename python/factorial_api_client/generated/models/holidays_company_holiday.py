from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.holidays_company_holiday_half_day import HolidaysCompanyHolidayHalfDay
from ..types import UNSET, Unset

T = TypeVar("T", bound="HolidaysCompanyHoliday")


@_attrs_define
class HolidaysCompanyHoliday:
    id: int
    """ Company holiday id """
    location_id: int
    """ Related location id """
    date: str
    """ Company holiday date """
    summary: str | Unset = UNSET
    """ Company holiday summary """
    description: str | Unset = UNSET
    """ Company holiday description """
    half_day: HolidaysCompanyHolidayHalfDay | Unset = UNSET
    """ If the company holiday is half-day and which part of the day """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        location_id = self.location_id

        date = self.date

        summary = self.summary

        description = self.description

        half_day: str | Unset = UNSET
        if not isinstance(self.half_day, Unset):
            half_day = self.half_day.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "location_id": location_id,
                "date": date,
            }
        )
        if summary is not UNSET:
            field_dict["summary"] = summary
        if description is not UNSET:
            field_dict["description"] = description
        if half_day is not UNSET:
            field_dict["half_day"] = half_day

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        location_id = d.pop("location_id")

        date = d.pop("date")

        summary = d.pop("summary", UNSET)

        description = d.pop("description", UNSET)

        _half_day = d.pop("half_day", UNSET)
        half_day: HolidaysCompanyHolidayHalfDay | Unset
        if isinstance(_half_day, Unset):
            half_day = UNSET
        else:
            half_day = HolidaysCompanyHolidayHalfDay(_half_day) if _half_day is not None else None

        holidays_company_holiday = cls(
            id=id,
            location_id=location_id,
            date=date,
            summary=summary,
            description=description,
            half_day=half_day,
        )

        holidays_company_holiday.additional_properties = d
        return holidays_company_holiday

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
