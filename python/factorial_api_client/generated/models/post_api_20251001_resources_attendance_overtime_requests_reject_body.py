from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20251001ResourcesAttendanceOvertimeRequestsRejectBody")


@_attrs_define
class PostApi20251001ResourcesAttendanceOvertimeRequestsRejectBody:
    id: int
    reason: str
    approver_id: int | Unset = UNSET
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
                "reason": reason,
            }
        )
        if approver_id is not UNSET:
            field_dict["approver_id"] = approver_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        reason = d.pop("reason")

        approver_id = d.pop("approver_id", UNSET)

        post_api_20251001_resources_attendance_overtime_requests_reject_body = cls(
            id=id,
            reason=reason,
            approver_id=approver_id,
        )

        post_api_20251001_resources_attendance_overtime_requests_reject_body.additional_properties = d
        return post_api_20251001_resources_attendance_overtime_requests_reject_body

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
