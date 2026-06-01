from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EmployeeUpdatesAbsence")


@_attrs_define
class EmployeeUpdatesAbsence:
    id: int
    """ Identifier of the absence employee update """
    status: str
    """ The status of the employee update. """
    employee_id: int | Unset = UNSET
    """ Employee id of the absence """
    employee_full_name: str | Unset = UNSET
    """ Full name of the employee """
    approved: bool | Unset = UNSET
    """ Indicates if the absence is approved """
    description: str | Unset = UNSET
    """ A description of the absence """
    start_on: str | Unset = UNSET
    """ The start date of the absence """
    prev_start_on: str | Unset = UNSET
    """ The previous start date of the absence """
    finish_on: str | Unset = UNSET
    """ The end date of the absence """
    prev_finish_on: str | Unset = UNSET
    """ The previous end date of the absence """
    half_day: str | Unset = UNSET
    """ Indicates if the absence is taken as a half-day """
    hours_amount_in_cents: int | Unset = UNSET
    """ The total number of hours taken for the absence, represented in cents """
    leave_type_id: int | Unset = UNSET
    """ The id of the leave type """
    leave_type_name: str | Unset = UNSET
    """ The name of the leave type """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        status = self.status

        employee_id = self.employee_id

        employee_full_name = self.employee_full_name

        approved = self.approved

        description = self.description

        start_on = self.start_on

        prev_start_on = self.prev_start_on

        finish_on = self.finish_on

        prev_finish_on = self.prev_finish_on

        half_day = self.half_day

        hours_amount_in_cents = self.hours_amount_in_cents

        leave_type_id = self.leave_type_id

        leave_type_name = self.leave_type_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "status": status,
            }
        )
        if employee_id is not UNSET:
            field_dict["employee_id"] = employee_id
        if employee_full_name is not UNSET:
            field_dict["employee_full_name"] = employee_full_name
        if approved is not UNSET:
            field_dict["approved"] = approved
        if description is not UNSET:
            field_dict["description"] = description
        if start_on is not UNSET:
            field_dict["start_on"] = start_on
        if prev_start_on is not UNSET:
            field_dict["prev_start_on"] = prev_start_on
        if finish_on is not UNSET:
            field_dict["finish_on"] = finish_on
        if prev_finish_on is not UNSET:
            field_dict["prev_finish_on"] = prev_finish_on
        if half_day is not UNSET:
            field_dict["half_day"] = half_day
        if hours_amount_in_cents is not UNSET:
            field_dict["hours_amount_in_cents"] = hours_amount_in_cents
        if leave_type_id is not UNSET:
            field_dict["leave_type_id"] = leave_type_id
        if leave_type_name is not UNSET:
            field_dict["leave_type_name"] = leave_type_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        status = d.pop("status")

        employee_id = d.pop("employee_id", UNSET)

        employee_full_name = d.pop("employee_full_name", UNSET)

        approved = d.pop("approved", UNSET)

        description = d.pop("description", UNSET)

        start_on = d.pop("start_on", UNSET)

        prev_start_on = d.pop("prev_start_on", UNSET)

        finish_on = d.pop("finish_on", UNSET)

        prev_finish_on = d.pop("prev_finish_on", UNSET)

        half_day = d.pop("half_day", UNSET)

        hours_amount_in_cents = d.pop("hours_amount_in_cents", UNSET)

        leave_type_id = d.pop("leave_type_id", UNSET)

        leave_type_name = d.pop("leave_type_name", UNSET)

        employee_updates_absence = cls(
            id=id,
            status=status,
            employee_id=employee_id,
            employee_full_name=employee_full_name,
            approved=approved,
            description=description,
            start_on=start_on,
            prev_start_on=prev_start_on,
            finish_on=finish_on,
            prev_finish_on=prev_finish_on,
            half_day=half_day,
            hours_amount_in_cents=hours_amount_in_cents,
            leave_type_id=leave_type_id,
            leave_type_name=leave_type_name,
        )

        employee_updates_absence.additional_properties = d
        return employee_updates_absence

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
