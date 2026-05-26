from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectManagementTimeRecord")


@_attrs_define
class ProjectManagementTimeRecord:
    id: int
    """ Id of the time record """
    project_worker_id: int
    """ Id of the project worker """
    attendance_shift_id: int
    """ Id of the attendance shift """
    subproject_id: int | Unset = UNSET
    """ Id of the subproject """
    date: str | Unset = UNSET
    """ Reference date of the shift """
    imputed_minutes: int | Unset = UNSET
    """ Minutes difference between the clock in and clock out """
    clock_in: str | Unset = UNSET
    """ Clock in time """
    clock_out: str | Unset = UNSET
    """ Clock out time """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        project_worker_id = self.project_worker_id

        attendance_shift_id = self.attendance_shift_id

        subproject_id = self.subproject_id

        date = self.date

        imputed_minutes = self.imputed_minutes

        clock_in = self.clock_in

        clock_out = self.clock_out

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "project_worker_id": project_worker_id,
                "attendance_shift_id": attendance_shift_id,
            }
        )
        if subproject_id is not UNSET:
            field_dict["subproject_id"] = subproject_id
        if date is not UNSET:
            field_dict["date"] = date
        if imputed_minutes is not UNSET:
            field_dict["imputed_minutes"] = imputed_minutes
        if clock_in is not UNSET:
            field_dict["clock_in"] = clock_in
        if clock_out is not UNSET:
            field_dict["clock_out"] = clock_out

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        project_worker_id = d.pop("project_worker_id")

        attendance_shift_id = d.pop("attendance_shift_id")

        subproject_id = d.pop("subproject_id", UNSET)

        date = d.pop("date", UNSET)

        imputed_minutes = d.pop("imputed_minutes", UNSET)

        clock_in = d.pop("clock_in", UNSET)

        clock_out = d.pop("clock_out", UNSET)

        project_management_time_record = cls(
            id=id,
            project_worker_id=project_worker_id,
            attendance_shift_id=attendance_shift_id,
            subproject_id=subproject_id,
            date=date,
            imputed_minutes=imputed_minutes,
            clock_in=clock_in,
            clock_out=clock_out,
        )

        project_management_time_record.additional_properties = d
        return project_management_time_record

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
