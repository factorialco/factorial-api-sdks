from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20251001ResourcesShiftManagementShiftsBody")


@_attrs_define
class PostApi20251001ResourcesShiftManagementShiftsBody:
    start_at: str
    """ Start date of the shift """
    end_at: str
    """ End date of the shift """
    employee_id: int
    """ Employee identifier """
    company_id: int
    """ Company identifier """
    name: str | Unset = UNSET
    """ Name of the shift """
    notes: str | Unset = UNSET
    """ Shift notes """
    location_id: int | Unset = UNSET
    """ Location identifier """
    work_area_id: int | Unset = UNSET
    """ Location work area identifier """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start_at = self.start_at

        end_at = self.end_at

        employee_id = self.employee_id

        company_id = self.company_id

        name = self.name

        notes = self.notes

        location_id = self.location_id

        work_area_id = self.work_area_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "start_at": start_at,
                "end_at": end_at,
                "employee_id": employee_id,
                "company_id": company_id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if notes is not UNSET:
            field_dict["notes"] = notes
        if location_id is not UNSET:
            field_dict["location_id"] = location_id
        if work_area_id is not UNSET:
            field_dict["work_area_id"] = work_area_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        start_at = d.pop("start_at")

        end_at = d.pop("end_at")

        employee_id = d.pop("employee_id")

        company_id = d.pop("company_id")

        name = d.pop("name", UNSET)

        notes = d.pop("notes", UNSET)

        location_id = d.pop("location_id", UNSET)

        work_area_id = d.pop("work_area_id", UNSET)

        post_api_20251001_resources_shift_management_shifts_body = cls(
            start_at=start_at,
            end_at=end_at,
            employee_id=employee_id,
            company_id=company_id,
            name=name,
            notes=notes,
            location_id=location_id,
            work_area_id=work_area_id,
        )

        post_api_20251001_resources_shift_management_shifts_body.additional_properties = d
        return post_api_20251001_resources_shift_management_shifts_body

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
