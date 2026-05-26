from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PutApi20251001ResourcesAttendanceOvertimeRequestsIdBody")


@_attrs_define
class PutApi20251001ResourcesAttendanceOvertimeRequestsIdBody:
    id: int
    date: str | Unset = UNSET
    description: str | Unset = UNSET
    hours_amount: float | Unset = UNSET
    reason: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        date = self.date

        description = self.description

        hours_amount = self.hours_amount

        reason = self.reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if date is not UNSET:
            field_dict["date"] = date
        if description is not UNSET:
            field_dict["description"] = description
        if hours_amount is not UNSET:
            field_dict["hours_amount"] = hours_amount
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        date = d.pop("date", UNSET)

        description = d.pop("description", UNSET)

        hours_amount = d.pop("hours_amount", UNSET)

        reason = d.pop("reason", UNSET)

        put_api_20251001_resources_attendance_overtime_requests_id_body = cls(
            id=id,
            date=date,
            description=description,
            hours_amount=hours_amount,
            reason=reason,
        )

        put_api_20251001_resources_attendance_overtime_requests_id_body.additional_properties = d
        return put_api_20251001_resources_attendance_overtime_requests_id_body

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
