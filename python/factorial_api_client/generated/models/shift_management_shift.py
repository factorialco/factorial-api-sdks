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
    id: str
    """ Unique identifier for the shift """
    company_id: str
    """ Identifier of the company that owns this shift """
    state: ShiftManagementShiftState
    """ Current state of the shift. 'draft' means the shift is not yet visible to employees, 'published' means it's
    visible and confirmed, 'backup' indicates a backup shift that can be replaced """
    employee_id: str
    """ Identifier of the employee assigned to this shift """
    start_at: str
    """ Timestamp indicating when the shift starts """
    end_at: str
    """ Timestamp indicating when the shift ends """
    extra_hours: bool
    """ Indicates whether this shift counts as extra hours beyond the employee's regular schedule. Used for overtime
    calculations """
    timezone: str
    """ IANA timezone identifier (e.g., 'Europe/Madrid', 'America/New_York') used to display the shift times in the
    local timezone """
    local_start_at: str
    """ Start time of the shift converted to the local timezone. This is what employees see in their schedule """
    local_end_at: str
    """ End time of the shift converted to the local timezone. This is what employees see in their schedule """
    name: str | Unset = UNSET
    """ Display name of the shift. If not explicitly set, falls back to the default shift title or template week
    name """
    location_id: str | Unset = UNSET
    """ Identifier of the location where the shift takes place. Can be null if the shift uses the employee's default
    location """
    locations_work_area_id: str | Unset = UNSET
    """ Identifier of the specific work area within the location where the shift occurs. Work areas allow further
    subdivision of locations """
    notes: str | Unset = UNSET
    """ Optional notes or comments about the shift, visible to managers and schedulers """
    default_shift_title: str | Unset = UNSET
    """ Title from the default shift template that was used to create this shift, if applicable """
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
