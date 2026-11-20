from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20270101ResourcesShiftManagementShiftsPublishBody")


@_attrs_define
class PostApi20270101ResourcesShiftManagementShiftsPublishBody:
    start_date: str
    """ First day to publish. Shifts starting on or after this day, in the shift's local time, are included """
    end_date: str
    """ Last day to publish, inclusive. Shifts starting on or before this day, in the shift's local time, are
    included. The range can span up to 31 days """
    employee_ids: list[str] | Unset = UNSET
    """ Publishes only the shifts of these employees. An empty list publishes nothing. If not provided, publishes
    the shifts of every employee whose shifts you can manage """
    location_ids: list[str] | Unset = UNSET
    """ Publishes only the shifts of employees assigned to these locations. An empty list publishes nothing """
    team_ids: list[str] | Unset = UNSET
    """ Publishes only the shifts of employees in these teams. An empty list publishes nothing """
    legal_entity_ids: list[str] | Unset = UNSET
    """ Publishes only the shifts of employees in these legal entities. An empty list publishes nothing """
    shift_ids: list[str] | Unset = UNSET
    """ Publishes only these draft shifts. Each draft must start within the date range and match the other filters,
    otherwise nothing is published and the 422 error lists the shifts that do not. Ids of shifts you cannot access
    fail the request with a 400 that does not list them. Ids of shifts that are already published are accepted and
    left as they are, even if they fall outside the dates and filters, so a retried request succeeds. Rest days are
    not published when shift_ids is provided. If not provided, every draft shift and rest day in the range is
    published, including the ones created from the shifts planner """
    skip_conflicts: bool | Unset = UNSET
    """ When true, employees with a conflicting shift in the range are left out and everything else is published.
    Their shifts and rest days stay in draft and are not returned. When false, a single conflict stops the whole
    publish """
    send_notifications: bool | Unset = UNSET
    """ When true, notifies the employees whose shifts were published """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start_date = self.start_date

        end_date = self.end_date

        employee_ids: list[str] | Unset = UNSET
        if not isinstance(self.employee_ids, Unset):
            employee_ids = self.employee_ids

        location_ids: list[str] | Unset = UNSET
        if not isinstance(self.location_ids, Unset):
            location_ids = self.location_ids

        team_ids: list[str] | Unset = UNSET
        if not isinstance(self.team_ids, Unset):
            team_ids = self.team_ids

        legal_entity_ids: list[str] | Unset = UNSET
        if not isinstance(self.legal_entity_ids, Unset):
            legal_entity_ids = self.legal_entity_ids

        shift_ids: list[str] | Unset = UNSET
        if not isinstance(self.shift_ids, Unset):
            shift_ids = self.shift_ids

        skip_conflicts = self.skip_conflicts

        send_notifications = self.send_notifications

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "start_date": start_date,
                "end_date": end_date,
            }
        )
        if employee_ids is not UNSET:
            field_dict["employee_ids"] = employee_ids
        if location_ids is not UNSET:
            field_dict["location_ids"] = location_ids
        if team_ids is not UNSET:
            field_dict["team_ids"] = team_ids
        if legal_entity_ids is not UNSET:
            field_dict["legal_entity_ids"] = legal_entity_ids
        if shift_ids is not UNSET:
            field_dict["shift_ids"] = shift_ids
        if skip_conflicts is not UNSET:
            field_dict["skip_conflicts"] = skip_conflicts
        if send_notifications is not UNSET:
            field_dict["send_notifications"] = send_notifications

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        start_date = d.pop("start_date")

        end_date = d.pop("end_date")

        employee_ids = cast(list[str], d.pop("employee_ids", UNSET))

        location_ids = cast(list[str], d.pop("location_ids", UNSET))

        team_ids = cast(list[str], d.pop("team_ids", UNSET))

        legal_entity_ids = cast(list[str], d.pop("legal_entity_ids", UNSET))

        shift_ids = cast(list[str], d.pop("shift_ids", UNSET))

        skip_conflicts = d.pop("skip_conflicts", UNSET)

        send_notifications = d.pop("send_notifications", UNSET)

        post_api_20270101_resources_shift_management_shifts_publish_body = cls(
            start_date=start_date,
            end_date=end_date,
            employee_ids=employee_ids,
            location_ids=location_ids,
            team_ids=team_ids,
            legal_entity_ids=legal_entity_ids,
            shift_ids=shift_ids,
            skip_conflicts=skip_conflicts,
            send_notifications=send_notifications,
        )

        post_api_20270101_resources_shift_management_shifts_publish_body.additional_properties = d
        return post_api_20270101_resources_shift_management_shifts_publish_body

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
