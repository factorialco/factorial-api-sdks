from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_api_20270101_resources_timeoff_allowance_incidences_bulk_create_body_allowance_incidences_item_target_balance import (
    PostApi20270101ResourcesTimeoffAllowanceIncidencesBulkCreateBodyAllowanceIncidencesItemTargetBalance,
)
from ..types import UNSET, Unset

T = TypeVar(
    "T",
    bound="PostApi20270101ResourcesTimeoffAllowanceIncidencesBulkCreateBodyAllowanceIncidencesItem",
)


@_attrs_define
class PostApi20270101ResourcesTimeoffAllowanceIncidencesBulkCreateBodyAllowanceIncidencesItem:
    employee_id: str
    timeoff_allowance_id: str
    days_in_cents: int
    effective_on: str
    target_balance: PostApi20270101ResourcesTimeoffAllowanceIncidencesBulkCreateBodyAllowanceIncidencesItemTargetBalance
    description: str | Unset = UNSET
    field_skip_notifications: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        employee_id = self.employee_id

        timeoff_allowance_id = self.timeoff_allowance_id

        days_in_cents = self.days_in_cents

        effective_on = self.effective_on

        target_balance = self.target_balance.value

        description = self.description

        field_skip_notifications = self.field_skip_notifications

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "employee_id": employee_id,
                "timeoff_allowance_id": timeoff_allowance_id,
                "days_in_cents": days_in_cents,
                "effective_on": effective_on,
                "target_balance": target_balance,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if field_skip_notifications is not UNSET:
            field_dict["_skip_notifications"] = field_skip_notifications

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        employee_id = d.pop("employee_id")

        timeoff_allowance_id = d.pop("timeoff_allowance_id")

        days_in_cents = d.pop("days_in_cents")

        effective_on = d.pop("effective_on")

        target_balance = PostApi20270101ResourcesTimeoffAllowanceIncidencesBulkCreateBodyAllowanceIncidencesItemTargetBalance(
            d.pop("target_balance")
        )

        description = d.pop("description", UNSET)

        field_skip_notifications = d.pop("_skip_notifications", UNSET)

        post_api_20270101_resources_timeoff_allowance_incidences_bulk_create_body_allowance_incidences_item = cls(
            employee_id=employee_id,
            timeoff_allowance_id=timeoff_allowance_id,
            days_in_cents=days_in_cents,
            effective_on=effective_on,
            target_balance=target_balance,
            description=description,
            field_skip_notifications=field_skip_notifications,
        )

        post_api_20270101_resources_timeoff_allowance_incidences_bulk_create_body_allowance_incidences_item.additional_properties = d
        return post_api_20270101_resources_timeoff_allowance_incidences_bulk_create_body_allowance_incidences_item

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
