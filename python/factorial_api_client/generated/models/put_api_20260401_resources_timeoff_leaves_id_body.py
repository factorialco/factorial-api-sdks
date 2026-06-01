from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PutApi20260401ResourcesTimeoffLeavesIdBody")


@_attrs_define
class PutApi20260401ResourcesTimeoffLeavesIdBody:
    id: int
    """ The leave id """
    employee_id: int | Unset = UNSET
    """ The employee id of the leave """
    leave_type_id: int | Unset = UNSET
    """ The leave type id """
    description: str | Unset = UNSET
    """ The description of the leave """
    start_on: str | Unset = UNSET
    """ The valid start date of the leave following the format YYYY-MM-DD """
    finish_on: str | Unset = UNSET
    """ The valid end date of the leave following the format YYYY-MM-DD """
    half_day: str | Unset = UNSET
    """ If the leave is in: [beggining_of_day, end_of_day] """
    start_time: str | Unset = UNSET
    """ The start time of a leave """
    hours_amount_in_cents: int | Unset = UNSET
    """ The hours amount in cents of a leave """
    approved: bool | Unset = UNSET
    """ Whether the leave is approved """
    skip_notifications: bool | Unset = UNSET
    """ Whether to skip notifications for this update """
    skip_validations: bool | Unset = UNSET
    """ Whether to skip validations for this update """
    skip_medical_leave: bool | Unset = UNSET
    """ Whether to skip medical leave processing for this update """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        employee_id = self.employee_id

        leave_type_id = self.leave_type_id

        description = self.description

        start_on = self.start_on

        finish_on = self.finish_on

        half_day = self.half_day

        start_time = self.start_time

        hours_amount_in_cents = self.hours_amount_in_cents

        approved = self.approved

        skip_notifications = self.skip_notifications

        skip_validations = self.skip_validations

        skip_medical_leave = self.skip_medical_leave

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if employee_id is not UNSET:
            field_dict["employee_id"] = employee_id
        if leave_type_id is not UNSET:
            field_dict["leave_type_id"] = leave_type_id
        if description is not UNSET:
            field_dict["description"] = description
        if start_on is not UNSET:
            field_dict["start_on"] = start_on
        if finish_on is not UNSET:
            field_dict["finish_on"] = finish_on
        if half_day is not UNSET:
            field_dict["half_day"] = half_day
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if hours_amount_in_cents is not UNSET:
            field_dict["hours_amount_in_cents"] = hours_amount_in_cents
        if approved is not UNSET:
            field_dict["approved"] = approved
        if skip_notifications is not UNSET:
            field_dict["skip_notifications"] = skip_notifications
        if skip_validations is not UNSET:
            field_dict["skip_validations"] = skip_validations
        if skip_medical_leave is not UNSET:
            field_dict["skip_medical_leave"] = skip_medical_leave

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        employee_id = d.pop("employee_id", UNSET)

        leave_type_id = d.pop("leave_type_id", UNSET)

        description = d.pop("description", UNSET)

        start_on = d.pop("start_on", UNSET)

        finish_on = d.pop("finish_on", UNSET)

        half_day = d.pop("half_day", UNSET)

        start_time = d.pop("start_time", UNSET)

        hours_amount_in_cents = d.pop("hours_amount_in_cents", UNSET)

        approved = d.pop("approved", UNSET)

        skip_notifications = d.pop("skip_notifications", UNSET)

        skip_validations = d.pop("skip_validations", UNSET)

        skip_medical_leave = d.pop("skip_medical_leave", UNSET)

        put_api_20260401_resources_timeoff_leaves_id_body = cls(
            id=id,
            employee_id=employee_id,
            leave_type_id=leave_type_id,
            description=description,
            start_on=start_on,
            finish_on=finish_on,
            half_day=half_day,
            start_time=start_time,
            hours_amount_in_cents=hours_amount_in_cents,
            approved=approved,
            skip_notifications=skip_notifications,
            skip_validations=skip_validations,
            skip_medical_leave=skip_medical_leave,
        )

        put_api_20260401_resources_timeoff_leaves_id_body.additional_properties = d
        return put_api_20260401_resources_timeoff_leaves_id_body

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
