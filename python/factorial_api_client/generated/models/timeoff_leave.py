from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.timeoff_leave_duration_by_day_attributes import (
        TimeoffLeaveDurationByDayAttributes,
    )


T = TypeVar("T", bound="TimeoffLeave")


@_attrs_define
class TimeoffLeave:
    id: str
    """ Identifier of the Leave """
    company_id: str
    """ ID of the company the leave belongs to """
    employee_id: str
    """ ID of the employee taking the leave """
    start_on: str
    """ First day of the leave """
    updated_at: str
    """ The updated at date of the leave """
    days_taken: float
    """ Number of days taken for paid leave. Reflects the summed per-day used total when the per-day breakdown is
    computed; otherwise the leave's calendar-day duration. """
    finish_on: str | Unset = UNSET
    """ Last day of the leave (inclusive); null while an open-ended leave has no end yet """
    half_day: str | Unset = UNSET
    """ Which half of the day a half-day leave covers — `beginning_of_day` or `end_of_day`; null for full-day leaves
    """
    description: str | Unset = UNSET
    """ Free-text description of the leave """
    reason: str | Unset = UNSET
    """ The reason provided by the employee for taking the leave """
    leave_type_id: str | Unset = UNSET
    """ ID of the leave type this leave is of """
    leave_type_name: str | Unset = UNSET
    """ Denormalised name of the leave type """
    approved: bool | Unset = UNSET
    """ Tri-state approval status — true = approved, false = rejected, null = pending approval """
    employee_full_name: str | Unset = UNSET
    """ The full name of the employee taking the leave """
    start_time: str | Unset = UNSET
    """ The start time of the leave """
    hours_amount_in_cents: int | Unset = UNSET
    """ Total hours the leave consumes, in hundredths of an hour (e.g. 800 = 8 hours); set for hourly leaves """
    created_at: str | Unset = UNSET
    """ The created at date of the leave """
    deleted_at: str | Unset = UNSET
    """ The date when the leave was deleted """
    duration_attributes: str | Unset = UNSET
    """ The duration attributes of the leave """
    duration_by_day_attributes: TimeoffLeaveDurationByDayAttributes | Unset = UNSET
    """ Per-day breakdown of the leave's workable and used units, keyed by calendar date. Populated only when the
    read requests `include_duration_by_day=true`; null otherwise. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        company_id = self.company_id

        employee_id = self.employee_id

        start_on = self.start_on

        updated_at = self.updated_at

        days_taken = self.days_taken

        finish_on = self.finish_on

        half_day = self.half_day

        description = self.description

        reason = self.reason

        leave_type_id = self.leave_type_id

        leave_type_name = self.leave_type_name

        approved = self.approved

        employee_full_name = self.employee_full_name

        start_time = self.start_time

        hours_amount_in_cents = self.hours_amount_in_cents

        created_at = self.created_at

        deleted_at = self.deleted_at

        duration_attributes = self.duration_attributes

        duration_by_day_attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.duration_by_day_attributes, Unset):
            duration_by_day_attributes = self.duration_by_day_attributes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "company_id": company_id,
                "employee_id": employee_id,
                "start_on": start_on,
                "updated_at": updated_at,
                "days_taken": days_taken,
            }
        )
        if finish_on is not UNSET:
            field_dict["finish_on"] = finish_on
        if half_day is not UNSET:
            field_dict["half_day"] = half_day
        if description is not UNSET:
            field_dict["description"] = description
        if reason is not UNSET:
            field_dict["reason"] = reason
        if leave_type_id is not UNSET:
            field_dict["leave_type_id"] = leave_type_id
        if leave_type_name is not UNSET:
            field_dict["leave_type_name"] = leave_type_name
        if approved is not UNSET:
            field_dict["approved"] = approved
        if employee_full_name is not UNSET:
            field_dict["employee_full_name"] = employee_full_name
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if hours_amount_in_cents is not UNSET:
            field_dict["hours_amount_in_cents"] = hours_amount_in_cents
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if deleted_at is not UNSET:
            field_dict["deleted_at"] = deleted_at
        if duration_attributes is not UNSET:
            field_dict["duration_attributes"] = duration_attributes
        if duration_by_day_attributes is not UNSET:
            field_dict["duration_by_day_attributes"] = duration_by_day_attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.timeoff_leave_duration_by_day_attributes import (
            TimeoffLeaveDurationByDayAttributes,
        )

        d = dict(src_dict)
        id = d.pop("id")

        company_id = d.pop("company_id")

        employee_id = d.pop("employee_id")

        start_on = d.pop("start_on")

        updated_at = d.pop("updated_at")

        days_taken = d.pop("days_taken")

        finish_on = d.pop("finish_on", UNSET)

        half_day = d.pop("half_day", UNSET)

        description = d.pop("description", UNSET)

        reason = d.pop("reason", UNSET)

        leave_type_id = d.pop("leave_type_id", UNSET)

        leave_type_name = d.pop("leave_type_name", UNSET)

        approved = d.pop("approved", UNSET)

        employee_full_name = d.pop("employee_full_name", UNSET)

        start_time = d.pop("start_time", UNSET)

        hours_amount_in_cents = d.pop("hours_amount_in_cents", UNSET)

        created_at = d.pop("created_at", UNSET)

        deleted_at = d.pop("deleted_at", UNSET)

        duration_attributes = d.pop("duration_attributes", UNSET)

        _duration_by_day_attributes = d.pop("duration_by_day_attributes", UNSET)
        duration_by_day_attributes: TimeoffLeaveDurationByDayAttributes | Unset
        if isinstance(_duration_by_day_attributes, Unset):
            duration_by_day_attributes = UNSET
        else:
            duration_by_day_attributes = TimeoffLeaveDurationByDayAttributes.from_dict(
                _duration_by_day_attributes
            )

        timeoff_leave = cls(
            id=id,
            company_id=company_id,
            employee_id=employee_id,
            start_on=start_on,
            updated_at=updated_at,
            days_taken=days_taken,
            finish_on=finish_on,
            half_day=half_day,
            description=description,
            reason=reason,
            leave_type_id=leave_type_id,
            leave_type_name=leave_type_name,
            approved=approved,
            employee_full_name=employee_full_name,
            start_time=start_time,
            hours_amount_in_cents=hours_amount_in_cents,
            created_at=created_at,
            deleted_at=deleted_at,
            duration_attributes=duration_attributes,
            duration_by_day_attributes=duration_by_day_attributes,
        )

        timeoff_leave.additional_properties = d
        return timeoff_leave

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
