from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.trainings_session_attendance_status import TrainingsSessionAttendanceStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="TrainingsSessionAttendance")


@_attrs_define
class TrainingsSessionAttendance:
    id: int
    status: TrainingsSessionAttendanceStatus
    session_access_membership_id: int
    access_id: int
    employee_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        status = self.status.value

        session_access_membership_id = self.session_access_membership_id

        access_id = self.access_id

        employee_id = self.employee_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "status": status,
                "session_access_membership_id": session_access_membership_id,
                "access_id": access_id,
            }
        )
        if employee_id is not UNSET:
            field_dict["employee_id"] = employee_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        status = TrainingsSessionAttendanceStatus(d.pop("status"))

        session_access_membership_id = d.pop("session_access_membership_id")

        access_id = d.pop("access_id")

        employee_id = d.pop("employee_id", UNSET)

        trainings_session_attendance = cls(
            id=id,
            status=status,
            session_access_membership_id=session_access_membership_id,
            access_id=access_id,
            employee_id=employee_id,
        )

        trainings_session_attendance.additional_properties = d
        return trainings_session_attendance

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
