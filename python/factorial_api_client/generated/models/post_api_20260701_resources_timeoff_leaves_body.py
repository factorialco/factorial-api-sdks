from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20260701ResourcesTimeoffLeavesBody")


@_attrs_define
class PostApi20260701ResourcesTimeoffLeavesBody:
    employee_id: str
    """ The employee id of the leave """
    start_on: str
    """ The valid start date of the leave following the format YYYY-MM-DD """
    leave_type_id: str | Unset = UNSET
    """ The leave type id """
    description: str | Unset = UNSET
    """ The description of the leave """
    finish_on: str | Unset = UNSET
    """ The valid end date of the leave following the format YYYY-MM-DD """
    half_day: str | Unset = UNSET
    """ If the leave is in: [beggining_of_day, end_of_day] """
    start_time: str | Unset = UNSET
    """ The start time of a leave """
    hours_amount_in_cents: int | Unset = UNSET
    """ The hours amount in cents of a leave """
    medical_leave_type: int | Unset = UNSET
    """ The medical leave type """
    effective_on: str | Unset = UNSET
    """ The effective on date of a leave following the format YYYY-MM-DD """
    medical_discharge_reason: str | Unset = UNSET
    """ The medical discharge reason of a leave """
    colegiate_number: int | Unset = UNSET
    """ The colegiate number of a leave """
    has_previous_relapse: bool | Unset = UNSET
    """ If the leave has previous relapse """
    relapse_leave_id: str | Unset = UNSET
    """ The leave relapse id """
    relapse_on: str | Unset = UNSET
    """ The leave relapse on date following the format YYYY-MM-DD """
    accident_on: str | Unset = UNSET
    """ The leave accident on date following the format YYYY-MM-DD """
    paternity_birth_on: str | Unset = UNSET
    """ The leave paternity birth on date following the format YYYY-MM-DD """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        employee_id = self.employee_id

        start_on = self.start_on

        leave_type_id = self.leave_type_id

        description = self.description

        finish_on = self.finish_on

        half_day = self.half_day

        start_time = self.start_time

        hours_amount_in_cents = self.hours_amount_in_cents

        medical_leave_type = self.medical_leave_type

        effective_on = self.effective_on

        medical_discharge_reason = self.medical_discharge_reason

        colegiate_number = self.colegiate_number

        has_previous_relapse = self.has_previous_relapse

        relapse_leave_id = self.relapse_leave_id

        relapse_on = self.relapse_on

        accident_on = self.accident_on

        paternity_birth_on = self.paternity_birth_on

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "employee_id": employee_id,
                "start_on": start_on,
            }
        )
        if leave_type_id is not UNSET:
            field_dict["leave_type_id"] = leave_type_id
        if description is not UNSET:
            field_dict["description"] = description
        if finish_on is not UNSET:
            field_dict["finish_on"] = finish_on
        if half_day is not UNSET:
            field_dict["half_day"] = half_day
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if hours_amount_in_cents is not UNSET:
            field_dict["hours_amount_in_cents"] = hours_amount_in_cents
        if medical_leave_type is not UNSET:
            field_dict["medical_leave_type"] = medical_leave_type
        if effective_on is not UNSET:
            field_dict["effective_on"] = effective_on
        if medical_discharge_reason is not UNSET:
            field_dict["medical_discharge_reason"] = medical_discharge_reason
        if colegiate_number is not UNSET:
            field_dict["colegiate_number"] = colegiate_number
        if has_previous_relapse is not UNSET:
            field_dict["has_previous_relapse"] = has_previous_relapse
        if relapse_leave_id is not UNSET:
            field_dict["relapse_leave_id"] = relapse_leave_id
        if relapse_on is not UNSET:
            field_dict["relapse_on"] = relapse_on
        if accident_on is not UNSET:
            field_dict["accident_on"] = accident_on
        if paternity_birth_on is not UNSET:
            field_dict["paternity_birth_on"] = paternity_birth_on

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        employee_id = d.pop("employee_id")

        start_on = d.pop("start_on")

        leave_type_id = d.pop("leave_type_id", UNSET)

        description = d.pop("description", UNSET)

        finish_on = d.pop("finish_on", UNSET)

        half_day = d.pop("half_day", UNSET)

        start_time = d.pop("start_time", UNSET)

        hours_amount_in_cents = d.pop("hours_amount_in_cents", UNSET)

        medical_leave_type = d.pop("medical_leave_type", UNSET)

        effective_on = d.pop("effective_on", UNSET)

        medical_discharge_reason = d.pop("medical_discharge_reason", UNSET)

        colegiate_number = d.pop("colegiate_number", UNSET)

        has_previous_relapse = d.pop("has_previous_relapse", UNSET)

        relapse_leave_id = d.pop("relapse_leave_id", UNSET)

        relapse_on = d.pop("relapse_on", UNSET)

        accident_on = d.pop("accident_on", UNSET)

        paternity_birth_on = d.pop("paternity_birth_on", UNSET)

        post_api_20260701_resources_timeoff_leaves_body = cls(
            employee_id=employee_id,
            start_on=start_on,
            leave_type_id=leave_type_id,
            description=description,
            finish_on=finish_on,
            half_day=half_day,
            start_time=start_time,
            hours_amount_in_cents=hours_amount_in_cents,
            medical_leave_type=medical_leave_type,
            effective_on=effective_on,
            medical_discharge_reason=medical_discharge_reason,
            colegiate_number=colegiate_number,
            has_previous_relapse=has_previous_relapse,
            relapse_leave_id=relapse_leave_id,
            relapse_on=relapse_on,
            accident_on=accident_on,
            paternity_birth_on=paternity_birth_on,
        )

        post_api_20260701_resources_timeoff_leaves_body.additional_properties = d
        return post_api_20260701_resources_timeoff_leaves_body

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
