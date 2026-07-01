from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20260701ResourcesAttendanceOvertimeRequestsApproveBody")


@_attrs_define
class PostApi20260701ResourcesAttendanceOvertimeRequestsApproveBody:
    id: str
    reason: str | Unset = UNSET
    approver_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        reason = self.reason

        approver_id = self.approver_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if reason is not UNSET:
            field_dict["reason"] = reason
        if approver_id is not UNSET:
            field_dict["approver_id"] = approver_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        reason = d.pop("reason", UNSET)

        approver_id = d.pop("approver_id", UNSET)

        post_api_20260701_resources_attendance_overtime_requests_approve_body = cls(
            id=id,
            reason=reason,
            approver_id=approver_id,
        )

        post_api_20260701_resources_attendance_overtime_requests_approve_body.additional_properties = d
        return post_api_20260701_resources_attendance_overtime_requests_approve_body

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
