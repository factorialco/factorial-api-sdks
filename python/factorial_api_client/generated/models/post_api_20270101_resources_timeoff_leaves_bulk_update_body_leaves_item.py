from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20270101ResourcesTimeoffLeavesBulkUpdateBodyLeavesItem")


@_attrs_define
class PostApi20270101ResourcesTimeoffLeavesBulkUpdateBodyLeavesItem:
    id: str
    leave_type_id: str | Unset = UNSET
    description: str | Unset = UNSET
    start_on: str | Unset = UNSET
    finish_on: str | Unset = UNSET
    half_day: str | Unset = UNSET
    start_time: str | Unset = UNSET
    hours_amount_in_cents: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        leave_type_id = self.leave_type_id

        description = self.description

        start_on = self.start_on

        finish_on = self.finish_on

        half_day = self.half_day

        start_time = self.start_time

        hours_amount_in_cents = self.hours_amount_in_cents

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        leave_type_id = d.pop("leave_type_id", UNSET)

        description = d.pop("description", UNSET)

        start_on = d.pop("start_on", UNSET)

        finish_on = d.pop("finish_on", UNSET)

        half_day = d.pop("half_day", UNSET)

        start_time = d.pop("start_time", UNSET)

        hours_amount_in_cents = d.pop("hours_amount_in_cents", UNSET)

        post_api_20270101_resources_timeoff_leaves_bulk_update_body_leaves_item = cls(
            id=id,
            leave_type_id=leave_type_id,
            description=description,
            start_on=start_on,
            finish_on=finish_on,
            half_day=half_day,
            start_time=start_time,
            hours_amount_in_cents=hours_amount_in_cents,
        )

        post_api_20270101_resources_timeoff_leaves_bulk_update_body_leaves_item.additional_properties = d
        return post_api_20270101_resources_timeoff_leaves_bulk_update_body_leaves_item

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
