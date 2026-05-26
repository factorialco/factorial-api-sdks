from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.attendance_overtime_request_status import AttendanceOvertimeRequestStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="AttendanceOvertimeRequest")


@_attrs_define
class AttendanceOvertimeRequest:
    id: int
    employee_id: int
    author_id: int
    status: AttendanceOvertimeRequestStatus
    date: str
    hours_amount_in_cents: int
    approver: bool
    is_editable: bool
    """ Defines if the overtime request can be edited """
    approver_id: int | Unset = UNSET
    description: str | Unset = UNSET
    reason: str | Unset = UNSET
    created_at: str | Unset = UNSET
    approver_full_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        employee_id = self.employee_id

        author_id = self.author_id

        status = self.status.value

        date = self.date

        hours_amount_in_cents = self.hours_amount_in_cents

        approver = self.approver

        is_editable = self.is_editable

        approver_id = self.approver_id

        description = self.description

        reason = self.reason

        created_at = self.created_at

        approver_full_name = self.approver_full_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "employee_id": employee_id,
                "author_id": author_id,
                "status": status,
                "date": date,
                "hours_amount_in_cents": hours_amount_in_cents,
                "approver": approver,
                "is_editable": is_editable,
            }
        )
        if approver_id is not UNSET:
            field_dict["approver_id"] = approver_id
        if description is not UNSET:
            field_dict["description"] = description
        if reason is not UNSET:
            field_dict["reason"] = reason
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if approver_full_name is not UNSET:
            field_dict["approver_full_name"] = approver_full_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        employee_id = d.pop("employee_id")

        author_id = d.pop("author_id")

        status = AttendanceOvertimeRequestStatus(d.pop("status"))

        date = d.pop("date")

        hours_amount_in_cents = d.pop("hours_amount_in_cents")

        approver = d.pop("approver")

        is_editable = d.pop("is_editable")

        approver_id = d.pop("approver_id", UNSET)

        description = d.pop("description", UNSET)

        reason = d.pop("reason", UNSET)

        created_at = d.pop("created_at", UNSET)

        approver_full_name = d.pop("approver_full_name", UNSET)

        attendance_overtime_request = cls(
            id=id,
            employee_id=employee_id,
            author_id=author_id,
            status=status,
            date=date,
            hours_amount_in_cents=hours_amount_in_cents,
            approver=approver,
            is_editable=is_editable,
            approver_id=approver_id,
            description=description,
            reason=reason,
            created_at=created_at,
            approver_full_name=approver_full_name,
        )

        attendance_overtime_request.additional_properties = d
        return attendance_overtime_request

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
