from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.shift_management_shift_state import ShiftManagementShiftState
from ..types import UNSET, Unset

T = TypeVar("T", bound="ShiftManagementShift")


@_attrs_define
class ShiftManagementShift:
    id: int
    """ Shift identifier """
    company_id: int
    """ Company identifier """
    state: ShiftManagementShiftState
    """ The state of the shift. """
    employee_id: int
    """ Employee identifier """
    start_at: str
    """ Start date of the shift """
    end_at: str
    """ End date of the shift """
    extra_hours: bool
    """ Flag to indicate if the shift has extra hours """
    timezone: str
    """ Shift timezone """
    local_start_at: str
    """ Local start date of the shift """
    local_end_at: str
    """ Local end date of the shift """
    name: str | Unset = UNSET
    """ Name of the shift, doing a fallback to the default shift title or template week name """
    location_id: int | Unset = UNSET
    """ Shift location identifier """
    locations_work_area_id: int | Unset = UNSET
    """ Shift work area identifier """
    notes: str | Unset = UNSET
    """ Shift notes """
    default_shift_title: str | Unset = UNSET
    """ Default shift title """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        company_id = self.company_id

        state = self.state.value

        employee_id = self.employee_id

        start_at = self.start_at

        end_at = self.end_at

        extra_hours = self.extra_hours

        timezone = self.timezone

        local_start_at = self.local_start_at

        local_end_at = self.local_end_at

        name = self.name

        location_id = self.location_id

        locations_work_area_id = self.locations_work_area_id

        notes = self.notes

        default_shift_title = self.default_shift_title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "company_id": company_id,
                "state": state,
                "employee_id": employee_id,
                "start_at": start_at,
                "end_at": end_at,
                "extra_hours": extra_hours,
                "timezone": timezone,
                "local_start_at": local_start_at,
                "local_end_at": local_end_at,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if location_id is not UNSET:
            field_dict["location_id"] = location_id
        if locations_work_area_id is not UNSET:
            field_dict["locations_work_area_id"] = locations_work_area_id
        if notes is not UNSET:
            field_dict["notes"] = notes
        if default_shift_title is not UNSET:
            field_dict["default_shift_title"] = default_shift_title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        company_id = d.pop("company_id")

        state = ShiftManagementShiftState(d.pop("state"))

        employee_id = d.pop("employee_id")

        start_at = d.pop("start_at")

        end_at = d.pop("end_at")

        extra_hours = d.pop("extra_hours")

        timezone = d.pop("timezone")

        local_start_at = d.pop("local_start_at")

        local_end_at = d.pop("local_end_at")

        name = d.pop("name", UNSET)

        location_id = d.pop("location_id", UNSET)

        locations_work_area_id = d.pop("locations_work_area_id", UNSET)

        notes = d.pop("notes", UNSET)

        default_shift_title = d.pop("default_shift_title", UNSET)

        shift_management_shift = cls(
            id=id,
            company_id=company_id,
            state=state,
            employee_id=employee_id,
            start_at=start_at,
            end_at=end_at,
            extra_hours=extra_hours,
            timezone=timezone,
            local_start_at=local_start_at,
            local_end_at=local_end_at,
            name=name,
            location_id=location_id,
            locations_work_area_id=locations_work_area_id,
            notes=notes,
            default_shift_title=default_shift_title,
        )

        shift_management_shift.additional_properties = d
        return shift_management_shift

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
