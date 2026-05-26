from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TimeoffLeave")


@_attrs_define
class TimeoffLeave:
    id: int
    """ Identifier of the Leave """
    company_id: int
    """ Company identifier of the employee of the leave """
    employee_id: int
    """ Employee identifier of the leave """
    start_on: str
    """ The start date of the leave """
    updated_at: str
    """ The updated at date of the leave """
    finish_on: str | Unset = UNSET
    """ The end date of the leave """
    half_day: str | Unset = UNSET
    """ Indicates if the leave is taken as a half-day """
    description: str | Unset = UNSET
    """ A description of the leave """
    reason: str | Unset = UNSET
    """ The reason provided by the employee for taking the leave """
    leave_type_id: int | Unset = UNSET
    """ The identifier for the type of leave """
    leave_type_name: str | Unset = UNSET
    """ The name of the leave type """
    approved: bool | Unset = UNSET
    """ Indicates whether the leave has been approved """
    employee_full_name: str | Unset = UNSET
    """ The full name of the employee taking the leave """
    start_time: str | Unset = UNSET
    """ The start time of the leave """
    hours_amount_in_cents: int | Unset = UNSET
    """ The total number of hours taken for the leave, represented in cents """
    created_at: str | Unset = UNSET
    """ The created at date of the leave """
    deleted_at: str | Unset = UNSET
    """ The date when the leave was deleted """
    duration_attributes: str | Unset = UNSET
    """ The duration attributes of the leave """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        company_id = self.company_id

        employee_id = self.employee_id

        start_on = self.start_on

        updated_at = self.updated_at

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "company_id": company_id,
                "employee_id": employee_id,
                "start_on": start_on,
                "updated_at": updated_at,
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        company_id = d.pop("company_id")

        employee_id = d.pop("employee_id")

        start_on = d.pop("start_on")

        updated_at = d.pop("updated_at")

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

        timeoff_leave = cls(
            id=id,
            company_id=company_id,
            employee_id=employee_id,
            start_on=start_on,
            updated_at=updated_at,
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
