from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20270101ResourcesTimeoffLeavesBulkCreateBodyLeavesItem")


@_attrs_define
class PostApi20270101ResourcesTimeoffLeavesBulkCreateBodyLeavesItem:
    employee_id: str
    leave_type_id: str
    start_on: str
    finish_on: str
    description: str | Unset = UNSET
    half_day: str | Unset = UNSET
    start_time: str | Unset = UNSET
    hours_amount_in_cents: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        employee_id = self.employee_id

        leave_type_id = self.leave_type_id

        start_on = self.start_on

        finish_on = self.finish_on

        description = self.description

        half_day = self.half_day

        start_time = self.start_time

        hours_amount_in_cents = self.hours_amount_in_cents

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "employee_id": employee_id,
                "leave_type_id": leave_type_id,
                "start_on": start_on,
                "finish_on": finish_on,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if half_day is not UNSET:
            field_dict["half_day"] = half_day
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if hours_amount_in_cents is not UNSET:
            field_dict["hours_amount_in_cents"] = hours_amount_in_cents

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        employee_id = d.pop("employee_id")

        leave_type_id = d.pop("leave_type_id")

        start_on = d.pop("start_on")

        finish_on = d.pop("finish_on")

        description = d.pop("description", UNSET)

        half_day = d.pop("half_day", UNSET)

        start_time = d.pop("start_time", UNSET)

        hours_amount_in_cents = d.pop("hours_amount_in_cents", UNSET)

        post_api_20270101_resources_timeoff_leaves_bulk_create_body_leaves_item = cls(
            employee_id=employee_id,
            leave_type_id=leave_type_id,
            start_on=start_on,
            finish_on=finish_on,
            description=description,
            half_day=half_day,
            start_time=start_time,
            hours_amount_in_cents=hours_amount_in_cents,
        )

        post_api_20270101_resources_timeoff_leaves_bulk_create_body_leaves_item.additional_properties = d
        return post_api_20270101_resources_timeoff_leaves_bulk_create_body_leaves_item

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
