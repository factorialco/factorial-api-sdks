from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_api_20261001_resources_timeoff_allowance_incidences_body_target_balance import (
    PostApi20261001ResourcesTimeoffAllowanceIncidencesBodyTargetBalance,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20261001ResourcesTimeoffAllowanceIncidencesBody")


@_attrs_define
class PostApi20261001ResourcesTimeoffAllowanceIncidencesBody:
    employee_id: str
    """ Employee Id """
    timeoff_allowance_id: str
    """ Allowance Id """
    days_in_cents: int
    """ How many units multiplied by 100 do you want to add/substract. Can be positive or negative """
    effective_on: str
    """ When does the incidence take effect. This is related to the allowance cycle. """
    target_balance: PostApi20261001ResourcesTimeoffAllowanceIncidencesBodyTargetBalance
    """ Which counter does the incidence affect. Can be "accrued" or "available" """
    description: str | Unset = UNSET
    """ A free text field to add a description to the incidence """
    field_skip_notifications: bool | Unset = UNSET
    """ When set to true, it prevents notifications being sent to employee when this incidence is created """
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

        target_balance = PostApi20261001ResourcesTimeoffAllowanceIncidencesBodyTargetBalance(
            d.pop("target_balance")
        )

        description = d.pop("description", UNSET)

        field_skip_notifications = d.pop("_skip_notifications", UNSET)

        post_api_20261001_resources_timeoff_allowance_incidences_body = cls(
            employee_id=employee_id,
            timeoff_allowance_id=timeoff_allowance_id,
            days_in_cents=days_in_cents,
            effective_on=effective_on,
            target_balance=target_balance,
            description=description,
            field_skip_notifications=field_skip_notifications,
        )

        post_api_20261001_resources_timeoff_allowance_incidences_body.additional_properties = d
        return post_api_20261001_resources_timeoff_allowance_incidences_body

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
