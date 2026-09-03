from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_api_20261001_resources_shift_management_shifts_bulk_create_body_shifts_item_creation_mode import (
    PostApi20261001ResourcesShiftManagementShiftsBulkCreateBodyShiftsItemCreationMode,
)
from ..models.post_api_20261001_resources_shift_management_shifts_bulk_create_body_shifts_item_state import (
    PostApi20261001ResourcesShiftManagementShiftsBulkCreateBodyShiftsItemState,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20261001ResourcesShiftManagementShiftsBulkCreateBodyShiftsItem")


@_attrs_define
class PostApi20261001ResourcesShiftManagementShiftsBulkCreateBodyShiftsItem:
    start_at: str
    """ Timestamp indicating when the shift starts. Required parameter """
    end_at: str
    """ Timestamp indicating when the shift ends. Required parameter """
    state: PostApi20261001ResourcesShiftManagementShiftsBulkCreateBodyShiftsItemState
    """ Initial state of the shift. 'draft' means the shift is not yet visible to employees, 'published' means it's
    visible and confirmed, 'backup' indicates a backup shift that can be replaced. Default is 'draft' """
    creation_mode: PostApi20261001ResourcesShiftManagementShiftsBulkCreateBodyShiftsItemCreationMode
    """ Indicates how the shift is created. 'manual' means it's created by a user, 'automatic' means it's generated
    by the system (e.g., from templates or scheduling algorithms). Default is 'manual' """
    employee_id: str
    """ Identifier of the employee assigned to this shift. Required parameter """
    company_id: str
    """ Identifier of the company that owns this shift. Required parameter """
    name: str | Unset = UNSET
    """ Display name of the shift. If not explicitly set, falls back to the default shift title or template week
    name """
    notes: str | Unset = UNSET
    """ Optional notes or comments about the shift, visible to managers and schedulers """
    extra_hours: bool | Unset = UNSET
    """ Indicates whether this shift counts as extra hours beyond the employee's regular schedule. Used for overtime
    calculations """
    location_id: str | Unset = UNSET
    """ Identifier of the location where the shift takes place. Can be null if the shift uses the employee's default
    location """
    work_area_id: str | Unset = UNSET
    """ Identifier of the specific work area within the location where the shift occurs. Work areas allow further
    subdivision of locations """
    default_shift_id: str | Unset = UNSET
    """ Identifier of the default shift template used to create this shift. Default shifts provide reusable shift
    patterns (start/end times, titles) """
    template_week_id: str | Unset = UNSET
    """ Identifier of the template week used to generate this shift. Template weeks allow bulk creation of shifts
    following a pattern """
    unassigned_shift_id: str | Unset = UNSET
    """ Identifier of the unassigned shift placeholder that is being converted to create this shift. Unassigned
    shifts are temporary placeholders """
    leave_id: str | Unset = UNSET
    """ Identifier of the leave (time off) associated with this shift, if applicable. Used when shifts are created
    or modified due to leave requests """
    author_id: str | Unset = UNSET
    """ Identifier of the user/access who is creating this shift. Used for audit purposes. If null, uses the current
    authenticated user """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start_at = self.start_at

        end_at = self.end_at

        state = self.state.value

        creation_mode = self.creation_mode.value

        employee_id = self.employee_id

        company_id = self.company_id

        name = self.name

        notes = self.notes

        extra_hours = self.extra_hours

        location_id = self.location_id

        work_area_id = self.work_area_id

        default_shift_id = self.default_shift_id

        template_week_id = self.template_week_id

        unassigned_shift_id = self.unassigned_shift_id

        leave_id = self.leave_id

        author_id = self.author_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "start_at": start_at,
                "end_at": end_at,
                "state": state,
                "creation_mode": creation_mode,
                "employee_id": employee_id,
                "company_id": company_id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if notes is not UNSET:
            field_dict["notes"] = notes
        if extra_hours is not UNSET:
            field_dict["extra_hours"] = extra_hours
        if location_id is not UNSET:
            field_dict["location_id"] = location_id
        if work_area_id is not UNSET:
            field_dict["work_area_id"] = work_area_id
        if default_shift_id is not UNSET:
            field_dict["default_shift_id"] = default_shift_id
        if template_week_id is not UNSET:
            field_dict["template_week_id"] = template_week_id
        if unassigned_shift_id is not UNSET:
            field_dict["unassigned_shift_id"] = unassigned_shift_id
        if leave_id is not UNSET:
            field_dict["leave_id"] = leave_id
        if author_id is not UNSET:
            field_dict["author_id"] = author_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        start_at = d.pop("start_at")

        end_at = d.pop("end_at")

        state = PostApi20261001ResourcesShiftManagementShiftsBulkCreateBodyShiftsItemState(
            d.pop("state")
        )

        creation_mode = (
            PostApi20261001ResourcesShiftManagementShiftsBulkCreateBodyShiftsItemCreationMode(
                d.pop("creation_mode")
            )
        )

        employee_id = d.pop("employee_id")

        company_id = d.pop("company_id")

        name = d.pop("name", UNSET)

        notes = d.pop("notes", UNSET)

        extra_hours = d.pop("extra_hours", UNSET)

        location_id = d.pop("location_id", UNSET)

        work_area_id = d.pop("work_area_id", UNSET)

        default_shift_id = d.pop("default_shift_id", UNSET)

        template_week_id = d.pop("template_week_id", UNSET)

        unassigned_shift_id = d.pop("unassigned_shift_id", UNSET)

        leave_id = d.pop("leave_id", UNSET)

        author_id = d.pop("author_id", UNSET)

        post_api_20261001_resources_shift_management_shifts_bulk_create_body_shifts_item = cls(
            start_at=start_at,
            end_at=end_at,
            state=state,
            creation_mode=creation_mode,
            employee_id=employee_id,
            company_id=company_id,
            name=name,
            notes=notes,
            extra_hours=extra_hours,
            location_id=location_id,
            work_area_id=work_area_id,
            default_shift_id=default_shift_id,
            template_week_id=template_week_id,
            unassigned_shift_id=unassigned_shift_id,
            leave_id=leave_id,
            author_id=author_id,
        )

        post_api_20261001_resources_shift_management_shifts_bulk_create_body_shifts_item.additional_properties = d
        return post_api_20261001_resources_shift_management_shifts_bulk_create_body_shifts_item

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
