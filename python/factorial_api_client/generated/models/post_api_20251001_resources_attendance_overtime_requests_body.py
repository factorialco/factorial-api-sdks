from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20251001ResourcesAttendanceOvertimeRequestsBody")


@_attrs_define
class PostApi20251001ResourcesAttendanceOvertimeRequestsBody:
    date: str
    employee_id: int
    author_id: int
    description: str | Unset = UNSET
    hours_amount: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date

        employee_id = self.employee_id

        author_id = self.author_id

        description = self.description

        hours_amount = self.hours_amount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "date": date,
                "employee_id": employee_id,
                "author_id": author_id,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if hours_amount is not UNSET:
            field_dict["hours_amount"] = hours_amount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        date = d.pop("date")

        employee_id = d.pop("employee_id")

        author_id = d.pop("author_id")

        description = d.pop("description", UNSET)

        hours_amount = d.pop("hours_amount", UNSET)

        post_api_20251001_resources_attendance_overtime_requests_body = cls(
            date=date,
            employee_id=employee_id,
            author_id=author_id,
            description=description,
            hours_amount=hours_amount,
        )

        post_api_20251001_resources_attendance_overtime_requests_body.additional_properties = d
        return post_api_20251001_resources_attendance_overtime_requests_body

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
