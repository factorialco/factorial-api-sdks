from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.put_api_20251001_resources_timeoff_allowance_incidences_id_body_target_balance import (
    PutApi20251001ResourcesTimeoffAllowanceIncidencesIdBodyTargetBalance,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PutApi20251001ResourcesTimeoffAllowanceIncidencesIdBody")


@_attrs_define
class PutApi20251001ResourcesTimeoffAllowanceIncidencesIdBody:
    id: int
    days_in_cents: int | Unset = UNSET
    """ How many units multiplied by 100 do you want to add/substract. Can be positive or negative """
    timeoff_allowance_id: int | Unset = UNSET
    """ Allowance Id """
    description: str | Unset = UNSET
    """ A free text field to add a description to the incidence """
    effective_on: str | Unset = UNSET
    """ When does the incidence take effect. This is related to the allowance cycle. """
    target_balance: PutApi20251001ResourcesTimeoffAllowanceIncidencesIdBodyTargetBalance | Unset = (
        UNSET
    )
    """ Which counter does the incidence affect. Can be "accrued" or "available" """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        days_in_cents = self.days_in_cents

        timeoff_allowance_id = self.timeoff_allowance_id

        description = self.description

        effective_on = self.effective_on

        target_balance: str | Unset = UNSET
        if not isinstance(self.target_balance, Unset):
            target_balance = self.target_balance.value

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
        target_balance: PutApi20251001ResourcesTimeoffAllowanceIncidencesIdBodyTargetBalance | Unset
        if isinstance(_target_balance, Unset):
            target_balance = UNSET
        else:
            target_balance = PutApi20251001ResourcesTimeoffAllowanceIncidencesIdBodyTargetBalance(
                _target_balance
            )

        put_api_20251001_resources_timeoff_allowance_incidences_id_body = cls(
            id=id,
            days_in_cents=days_in_cents,
            timeoff_allowance_id=timeoff_allowance_id,
            description=description,
            effective_on=effective_on,
            target_balance=target_balance,
        )

        put_api_20251001_resources_timeoff_allowance_incidences_id_body.additional_properties = d
        return put_api_20251001_resources_timeoff_allowance_incidences_id_body

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
