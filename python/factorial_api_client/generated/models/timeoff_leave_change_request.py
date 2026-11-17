from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.timeoff_leave_change_request_request_type import TimeoffLeaveChangeRequestRequestType
from ..models.timeoff_leave_change_request_status import TimeoffLeaveChangeRequestStatus
from ..models.timeoff_leave_change_request_withdrawal_cause import (
    TimeoffLeaveChangeRequestWithdrawalCause,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="TimeoffLeaveChangeRequest")


@_attrs_define
class TimeoffLeaveChangeRequest:
    id: str
    """ Identifier of the change request. """
    company_id: str
    """ Identifier of the company. """
    leave_id: str
    """ Identifier of the leave the request proposes to change. """
    employee_id: str
    """ Identifier of the employee who owns the leave. """
    author_id: str
    """ Access that created the request (the owner, or One on their behalf). """
    request_type: TimeoffLeaveChangeRequestRequestType
    """ update_leave or cancel_leave. """
    status: TimeoffLeaveChangeRequestStatus
    """ pending, approved, rejected or withdrawn. """
    current_start_on: str
    """ Current first day of the leave, read from the leave as it is now, so a decided request shows the leave after
    the decision. """
    current_leave_type_id: str
    """ Current leave type of the leave, read from the leave as it is now, so a decided request shows the leave
    after the decision. """
    created_at: str
    """ When the request was created. """
    updated_at: str
    """ When the request was last updated. """
    approved: bool | Unset = UNSET
    """ True once approved, false once rejected, null while pending or withdrawn. """
    withdrawn_at: str | Unset = UNSET
    """ When the request was withdrawn, if it was. """
    withdrawal_cause: TimeoffLeaveChangeRequestWithdrawalCause | Unset = UNSET
    """ Why it was withdrawn - author, leave_updated (the leave was edited directly), leave_deleted or leave_started
    (the leave or its proposed first day started before a decision). """
    start_on: str | Unset = UNSET
    """ First day once approved, the current one when the request keeps it (read from the leave as it is now). Null
    for a cancellation. """
    finish_on: str | Unset = UNSET
    """ Last day once approved, the current one when the request keeps it (read from the leave as it is now). Null
    for a cancellation. """
    half_day: str | Unset = UNSET
    """ Half day once approved, the current one when the request keeps it (read from the leave as it is now). Null
    for a cancellation. """
    start_time: str | Unset = UNSET
    """ Start time once approved, the current one when the request keeps it (read from the leave as it is now). Null
    for a cancellation. """
    hours_amount_in_cents: int | Unset = UNSET
    """ Hours in cents of an hour once approved, the current ones when the request keeps them (read from the leave
    as it is now). Null for a cancellation. """
    leave_type_id: str | Unset = UNSET
    """ Leave type once approved, the current one when the request keeps it (read from the leave as it is now). Null
    for a cancellation. """
    description: str | Unset = UNSET
    """ Proposed description, null when the request keeps it. """
    reason: str | Unset = UNSET
    """ Why the employee asks for the change. """
    rejected_reason: str | Unset = UNSET
    """ Why the approver rejected it. """
    current_finish_on: str | Unset = UNSET
    """ Current last day of the leave, read from the leave as it is now, so a decided request shows the leave after
    the decision. """
    current_half_day: str | Unset = UNSET
    """ Current half day of the leave, read from the leave as it is now, so a decided request shows the leave after
    the decision. """
    current_start_time: str | Unset = UNSET
    """ Current start time of the leave, read from the leave as it is now, so a decided request shows the leave
    after the decision. """
    current_hours_amount_in_cents: int | Unset = UNSET
    """ Current hours of the leave in cents of an hour, read from the leave as it is now, so a decided request shows
    the leave after the decision. """
    proposed_days_taken: float | Unset = UNSET
    """ Days the leave would take with the proposed values, with the same meaning as the leave's `days_taken`. 0 for
    a cancellation, and null when the reader can't see the leave's details. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        company_id = self.company_id

        leave_id = self.leave_id

        employee_id = self.employee_id

        author_id = self.author_id

        request_type = self.request_type.value

        status = self.status.value

        current_start_on = self.current_start_on

        current_leave_type_id = self.current_leave_type_id

        created_at = self.created_at

        updated_at = self.updated_at

        approved = self.approved

        withdrawn_at = self.withdrawn_at

        withdrawal_cause: str | Unset = UNSET
        if not isinstance(self.withdrawal_cause, Unset):
            withdrawal_cause = self.withdrawal_cause.value if self.withdrawal_cause is not None else None

        start_on = self.start_on

        finish_on = self.finish_on

        half_day = self.half_day

        start_time = self.start_time

        hours_amount_in_cents = self.hours_amount_in_cents

        leave_type_id = self.leave_type_id

        description = self.description

        reason = self.reason

        rejected_reason = self.rejected_reason

        current_finish_on = self.current_finish_on

        current_half_day = self.current_half_day

        current_start_time = self.current_start_time

        current_hours_amount_in_cents = self.current_hours_amount_in_cents

        proposed_days_taken = self.proposed_days_taken

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "company_id": company_id,
                "leave_id": leave_id,
                "employee_id": employee_id,
                "author_id": author_id,
                "request_type": request_type,
                "status": status,
                "current_start_on": current_start_on,
                "current_leave_type_id": current_leave_type_id,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if approved is not UNSET:
            field_dict["approved"] = approved
        if withdrawn_at is not UNSET:
            field_dict["withdrawn_at"] = withdrawn_at
        if withdrawal_cause is not UNSET:
            field_dict["withdrawal_cause"] = withdrawal_cause
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
        if rejected_reason is not UNSET:
            field_dict["rejected_reason"] = rejected_reason
        if current_finish_on is not UNSET:
            field_dict["current_finish_on"] = current_finish_on
        if current_half_day is not UNSET:
            field_dict["current_half_day"] = current_half_day
        if current_start_time is not UNSET:
            field_dict["current_start_time"] = current_start_time
        if current_hours_amount_in_cents is not UNSET:
            field_dict["current_hours_amount_in_cents"] = current_hours_amount_in_cents
        if proposed_days_taken is not UNSET:
            field_dict["proposed_days_taken"] = proposed_days_taken

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        company_id = d.pop("company_id")

        leave_id = d.pop("leave_id")

        employee_id = d.pop("employee_id")

        author_id = d.pop("author_id")

        request_type = TimeoffLeaveChangeRequestRequestType(d.pop("request_type"))

        status = TimeoffLeaveChangeRequestStatus(d.pop("status"))

        current_start_on = d.pop("current_start_on")

        current_leave_type_id = d.pop("current_leave_type_id")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        approved = d.pop("approved", UNSET)

        withdrawn_at = d.pop("withdrawn_at", UNSET)

        _withdrawal_cause = d.pop("withdrawal_cause", UNSET)
        withdrawal_cause: TimeoffLeaveChangeRequestWithdrawalCause | Unset
        if isinstance(_withdrawal_cause, Unset):
            withdrawal_cause = UNSET
        else:
            withdrawal_cause = TimeoffLeaveChangeRequestWithdrawalCause(_withdrawal_cause) if _withdrawal_cause is not None else None

        start_on = d.pop("start_on", UNSET)

        finish_on = d.pop("finish_on", UNSET)

        half_day = d.pop("half_day", UNSET)

        start_time = d.pop("start_time", UNSET)

        hours_amount_in_cents = d.pop("hours_amount_in_cents", UNSET)

        leave_type_id = d.pop("leave_type_id", UNSET)

        description = d.pop("description", UNSET)

        reason = d.pop("reason", UNSET)

        rejected_reason = d.pop("rejected_reason", UNSET)

        current_finish_on = d.pop("current_finish_on", UNSET)

        current_half_day = d.pop("current_half_day", UNSET)

        current_start_time = d.pop("current_start_time", UNSET)

        current_hours_amount_in_cents = d.pop("current_hours_amount_in_cents", UNSET)

        proposed_days_taken = d.pop("proposed_days_taken", UNSET)

        timeoff_leave_change_request = cls(
            id=id,
            company_id=company_id,
            leave_id=leave_id,
            employee_id=employee_id,
            author_id=author_id,
            request_type=request_type,
            status=status,
            current_start_on=current_start_on,
            current_leave_type_id=current_leave_type_id,
            created_at=created_at,
            updated_at=updated_at,
            approved=approved,
            withdrawn_at=withdrawn_at,
            withdrawal_cause=withdrawal_cause,
            start_on=start_on,
            finish_on=finish_on,
            half_day=half_day,
            start_time=start_time,
            hours_amount_in_cents=hours_amount_in_cents,
            leave_type_id=leave_type_id,
            description=description,
            reason=reason,
            rejected_reason=rejected_reason,
            current_finish_on=current_finish_on,
            current_half_day=current_half_day,
            current_start_time=current_start_time,
            current_hours_amount_in_cents=current_hours_amount_in_cents,
            proposed_days_taken=proposed_days_taken,
        )

        timeoff_leave_change_request.additional_properties = d
        return timeoff_leave_change_request

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
