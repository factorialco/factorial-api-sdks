from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_api_20251001_resources_contracts_compensations_body_time_condition import (
    PostApi20251001ResourcesContractsCompensationsBodyTimeCondition,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20251001ResourcesContractsCompensationsBody")


@_attrs_define
class PostApi20251001ResourcesContractsCompensationsBody:
    contract_version_id: int
    contracts_taxonomy_id: int
    description: str | Unset = UNSET
    compensation_type: str | Unset = UNSET
    amount: int | Unset = UNSET
    unit: str | Unset = UNSET
    sync_with_supplements: bool | Unset = UNSET
    payroll_policy_id: int | Unset = UNSET
    recurrence_count: int | Unset = UNSET
    starts_on: str | Unset = UNSET
    recurrence: str | Unset = UNSET
    first_payment_on: str | Unset = UNSET
    calculation: str | Unset = UNSET
    time_condition: PostApi20251001ResourcesContractsCompensationsBodyTimeCondition | Unset = UNSET
    minimum_amount_of_hours: int | Unset = UNSET
    minimum_amount_of_hours_in_cents: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        contract_version_id = self.contract_version_id

        contracts_taxonomy_id = self.contracts_taxonomy_id

        description = self.description

        compensation_type = self.compensation_type

        amount = self.amount

        unit = self.unit

        sync_with_supplements = self.sync_with_supplements

        payroll_policy_id = self.payroll_policy_id

        recurrence_count = self.recurrence_count

        starts_on = self.starts_on

        recurrence = self.recurrence

        first_payment_on = self.first_payment_on

        calculation = self.calculation

        time_condition: str | Unset = UNSET
        if not isinstance(self.time_condition, Unset):
            time_condition = self.time_condition.value

        minimum_amount_of_hours = self.minimum_amount_of_hours

        minimum_amount_of_hours_in_cents = self.minimum_amount_of_hours_in_cents

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "contract_version_id": contract_version_id,
                "contracts_taxonomy_id": contracts_taxonomy_id,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if compensation_type is not UNSET:
            field_dict["compensation_type"] = compensation_type
        if amount is not UNSET:
            field_dict["amount"] = amount
        if unit is not UNSET:
            field_dict["unit"] = unit
        if sync_with_supplements is not UNSET:
            field_dict["sync_with_supplements"] = sync_with_supplements
        if payroll_policy_id is not UNSET:
            field_dict["payroll_policy_id"] = payroll_policy_id
        if recurrence_count is not UNSET:
            field_dict["recurrence_count"] = recurrence_count
        if starts_on is not UNSET:
            field_dict["starts_on"] = starts_on
        if recurrence is not UNSET:
            field_dict["recurrence"] = recurrence
        if first_payment_on is not UNSET:
            field_dict["first_payment_on"] = first_payment_on
        if calculation is not UNSET:
            field_dict["calculation"] = calculation
        if time_condition is not UNSET:
            field_dict["time_condition"] = time_condition
        if minimum_amount_of_hours is not UNSET:
            field_dict["minimum_amount_of_hours"] = minimum_amount_of_hours
        if minimum_amount_of_hours_in_cents is not UNSET:
            field_dict["minimum_amount_of_hours_in_cents"] = minimum_amount_of_hours_in_cents

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        contract_version_id = d.pop("contract_version_id")

        contracts_taxonomy_id = d.pop("contracts_taxonomy_id")

        description = d.pop("description", UNSET)

        compensation_type = d.pop("compensation_type", UNSET)

        amount = d.pop("amount", UNSET)

        unit = d.pop("unit", UNSET)

        sync_with_supplements = d.pop("sync_with_supplements", UNSET)

        payroll_policy_id = d.pop("payroll_policy_id", UNSET)

        recurrence_count = d.pop("recurrence_count", UNSET)

        starts_on = d.pop("starts_on", UNSET)

        recurrence = d.pop("recurrence", UNSET)

        first_payment_on = d.pop("first_payment_on", UNSET)

        calculation = d.pop("calculation", UNSET)

        _time_condition = d.pop("time_condition", UNSET)
        time_condition: PostApi20251001ResourcesContractsCompensationsBodyTimeCondition | Unset
        if isinstance(_time_condition, Unset):
            time_condition = UNSET
        else:
            time_condition = PostApi20251001ResourcesContractsCompensationsBodyTimeCondition(
                _time_condition
            )

        minimum_amount_of_hours = d.pop("minimum_amount_of_hours", UNSET)

        minimum_amount_of_hours_in_cents = d.pop("minimum_amount_of_hours_in_cents", UNSET)

        post_api_20251001_resources_contracts_compensations_body = cls(
            contract_version_id=contract_version_id,
            contracts_taxonomy_id=contracts_taxonomy_id,
            description=description,
            compensation_type=compensation_type,
            amount=amount,
            unit=unit,
            sync_with_supplements=sync_with_supplements,
            payroll_policy_id=payroll_policy_id,
            recurrence_count=recurrence_count,
            starts_on=starts_on,
            recurrence=recurrence,
            first_payment_on=first_payment_on,
            calculation=calculation,
            time_condition=time_condition,
            minimum_amount_of_hours=minimum_amount_of_hours,
            minimum_amount_of_hours_in_cents=minimum_amount_of_hours_in_cents,
        )

        post_api_20251001_resources_contracts_compensations_body.additional_properties = d
        return post_api_20251001_resources_contracts_compensations_body

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
