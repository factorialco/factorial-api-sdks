from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_api_20270101_resources_timeoff_allowance_incidences_bulk_update_body_allowance_incidences_item_target_balance import (
    PostApi20270101ResourcesTimeoffAllowanceIncidencesBulkUpdateBodyAllowanceIncidencesItemTargetBalance,
)
from ..types import UNSET, Unset

T = TypeVar(
    "T",
    bound="PostApi20270101ResourcesTimeoffAllowanceIncidencesBulkUpdateBodyAllowanceIncidencesItem",
)


@_attrs_define
class PostApi20270101ResourcesTimeoffAllowanceIncidencesBulkUpdateBodyAllowanceIncidencesItem:
    id: str
    days_in_cents: int | Unset = UNSET
    timeoff_allowance_id: str | Unset = UNSET
    description: str | Unset = UNSET
    effective_on: str | Unset = UNSET
    target_balance: (
        PostApi20270101ResourcesTimeoffAllowanceIncidencesBulkUpdateBodyAllowanceIncidencesItemTargetBalance
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        days_in_cents = self.days_in_cents

        timeoff_allowance_id = self.timeoff_allowance_id

        description = self.description

        effective_on = self.effective_on

        target_balance: str | Unset = UNSET
        if not isinstance(self.target_balance, Unset):
            target_balance = self.target_balance.value if self.target_balance is not None else None

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if days_in_cents is not UNSET:
            field_dict["days_in_cents"] = days_in_cents
        if timeoff_allowance_id is not UNSET:
            field_dict["timeoff_allowance_id"] = timeoff_allowance_id
        if description is not UNSET:
            field_dict["description"] = description
        if effective_on is not UNSET:
            field_dict["effective_on"] = effective_on
        if target_balance is not UNSET:
            field_dict["target_balance"] = target_balance

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        days_in_cents = d.pop("days_in_cents", UNSET)

        timeoff_allowance_id = d.pop("timeoff_allowance_id", UNSET)

        description = d.pop("description", UNSET)

        effective_on = d.pop("effective_on", UNSET)

        _target_balance = d.pop("target_balance", UNSET)
        target_balance: (
            PostApi20270101ResourcesTimeoffAllowanceIncidencesBulkUpdateBodyAllowanceIncidencesItemTargetBalance
            | Unset
        )
        if isinstance(_target_balance, Unset):
            target_balance = UNSET
        else:
            target_balance = PostApi20270101ResourcesTimeoffAllowanceIncidencesBulkUpdateBodyAllowanceIncidencesItemTargetBalance(
                _target_balance
            )

        post_api_20270101_resources_timeoff_allowance_incidences_bulk_update_body_allowance_incidences_item = cls(
            id=id,
            days_in_cents=days_in_cents,
            timeoff_allowance_id=timeoff_allowance_id,
            description=description,
            effective_on=effective_on,
            target_balance=target_balance,
        )

        post_api_20270101_resources_timeoff_allowance_incidences_bulk_update_body_allowance_incidences_item.additional_properties = d
        return post_api_20270101_resources_timeoff_allowance_incidences_bulk_update_body_allowance_incidences_item

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
