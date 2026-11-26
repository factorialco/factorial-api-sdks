from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_api_20270101_resources_timeoff_leave_change_requests_body_request_type import (
    PostApi20270101ResourcesTimeoffLeaveChangeRequestsBodyRequestType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20270101ResourcesTimeoffLeaveChangeRequestsBody")


@_attrs_define
class PostApi20270101ResourcesTimeoffLeaveChangeRequestsBody:
    leave_id: str
    """ Id of the approved leave to change. """
    request_type: PostApi20270101ResourcesTimeoffLeaveChangeRequestsBodyRequestType
    """ update_leave to propose new values, cancel_leave to cancel the leave. """
    start_on: str | Unset = UNSET
    """ Proposed first day. Omit it to keep the current one. """
    finish_on: str | Unset = UNSET
    """ Proposed last day. Omit it to keep the current one. """
    half_day: str | Unset = UNSET
    """ Proposed half day (beggining_of_day or end_of_day), or an empty string to make a half-day leave a full day.
    Omit it to keep the current one. """
    start_time: str | Unset = UNSET
    """ Proposed start time for an hourly leave. Omit it to keep the current one. """
    hours_amount_in_cents: int | Unset = UNSET
    """ Proposed hours for an hourly leave, in cents of an hour. Omit it to keep the current one. """
    leave_type_id: str | Unset = UNSET
    """ Proposed leave type. Omit it to keep the current one. """
    description: str | Unset = UNSET
    """ Proposed description of the leave. Omit it to keep the current one. """
    reason: str | Unset = UNSET
    """ Why the employee asks for the change. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        leave_id = self.leave_id

        request_type = self.request_type.value

        start_on = self.start_on

        finish_on = self.finish_on

        half_day = self.half_day

        start_time = self.start_time

        hours_amount_in_cents = self.hours_amount_in_cents

        leave_type_id = self.leave_type_id

        description = self.description

        reason = self.reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "leave_id": leave_id,
                "request_type": request_type,
            }
        )
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
        if leave_type_id is not UNSET:
            field_dict["leave_type_id"] = leave_type_id
        if description is not UNSET:
            field_dict["description"] = description
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        leave_id = d.pop("leave_id")

        request_type = PostApi20270101ResourcesTimeoffLeaveChangeRequestsBodyRequestType(
            d.pop("request_type")
        )

        start_on = d.pop("start_on", UNSET)

        finish_on = d.pop("finish_on", UNSET)

        half_day = d.pop("half_day", UNSET)

        start_time = d.pop("start_time", UNSET)

        hours_amount_in_cents = d.pop("hours_amount_in_cents", UNSET)

        leave_type_id = d.pop("leave_type_id", UNSET)

        description = d.pop("description", UNSET)

        reason = d.pop("reason", UNSET)

        post_api_20270101_resources_timeoff_leave_change_requests_body = cls(
            leave_id=leave_id,
            request_type=request_type,
            start_on=start_on,
            finish_on=finish_on,
            half_day=half_day,
            start_time=start_time,
            hours_amount_in_cents=hours_amount_in_cents,
            leave_type_id=leave_type_id,
            description=description,
            reason=reason,
        )

        post_api_20270101_resources_timeoff_leave_change_requests_body.additional_properties = d
        return post_api_20270101_resources_timeoff_leave_change_requests_body

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
