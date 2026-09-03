from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.contracts_compensation_time_condition import ContractsCompensationTimeCondition
from ..types import UNSET, Unset

T = TypeVar("T", bound="ContractsCompensation")


@_attrs_define
class ContractsCompensation:
    id: str
    """ Unique identifier of the compensation """
    contract_version_id: str
    """ ID of the contract version this compensation belongs to """
    contracts_taxonomy_id: str
    """ ID of the contracts taxonomy categorising this compensation """
    unit: str
    """ In which unit compensation is paid """
    description: str | Unset = UNSET
    """ Free-text description of the compensation """
    compensation_type: str | Unset = UNSET
    """ Required field. You can only use the following options: fixed, undefined, up_to, per_worked_day,
    per_worked_hour """
    amount: int | Unset = UNSET
    """ Value paid on each recurrence, stored in the smallest currency unit (for example cents). Required unless the
    compensation type is `undefined` """
    sync_with_supplements: bool | Unset = UNSET
    payroll_policy_id: str | Unset = UNSET
    recurrence_count: int | Unset = UNSET
    """ How much time will pass between payments. If recurrence is empty, assume months. For example, 12 here means
    compensation is paid yearly """
    starts_on: str | Unset = UNSET
    """ Date from which this compensation applies """
    recurrence: str | Unset = UNSET
    """ Frequency (monthly, yearly, one_time) to determine how often the employee is paid. Could be empty, use
    `recurrence_count` in that case """
    first_payment_on: str | Unset = UNSET
    """ Date of the first payout; differs from `starts_on` when payroll scheduling or accrual rules delay payment
    """
    calculation: str | Unset = UNSET
    """ Human-readable hint about the payroll formula used (for example "current period" or "average of last 3
    months") """
    currency: str | Unset = UNSET
    """ ISO 4217 currency code the amount is expressed in """
    time_condition: ContractsCompensationTimeCondition | Unset = UNSET
    minimum_amount_of_hours: int | Unset = UNSET
    minimum_amount_of_hours_in_cents: int | Unset = UNSET
    """ Compensation expected minimum amount of hours in cents """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        contract_version_id = self.contract_version_id

        contracts_taxonomy_id = self.contracts_taxonomy_id

        unit = self.unit

        description = self.description

        compensation_type = self.compensation_type

        amount = self.amount

        sync_with_supplements = self.sync_with_supplements

        payroll_policy_id = self.payroll_policy_id

        recurrence_count = self.recurrence_count

        starts_on = self.starts_on

        recurrence = self.recurrence

        first_payment_on = self.first_payment_on

        calculation = self.calculation

        currency = self.currency

        time_condition: str | Unset = UNSET
        if not isinstance(self.time_condition, Unset):
            time_condition = self.time_condition.value if self.time_condition is not None else None

        minimum_amount_of_hours = self.minimum_amount_of_hours

        minimum_amount_of_hours_in_cents = self.minimum_amount_of_hours_in_cents

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "contract_version_id": contract_version_id,
                "contracts_taxonomy_id": contracts_taxonomy_id,
                "unit": unit,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if compensation_type is not UNSET:
            field_dict["compensation_type"] = compensation_type
        if amount is not UNSET:
            field_dict["amount"] = amount
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
        if currency is not UNSET:
            field_dict["currency"] = currency
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
        id = d.pop("id")

        contract_version_id = d.pop("contract_version_id")

        contracts_taxonomy_id = d.pop("contracts_taxonomy_id")

        unit = d.pop("unit")

        description = d.pop("description", UNSET)

        compensation_type = d.pop("compensation_type", UNSET)

        amount = d.pop("amount", UNSET)

        sync_with_supplements = d.pop("sync_with_supplements", UNSET)

        payroll_policy_id = d.pop("payroll_policy_id", UNSET)

        recurrence_count = d.pop("recurrence_count", UNSET)

        starts_on = d.pop("starts_on", UNSET)

        recurrence = d.pop("recurrence", UNSET)

        first_payment_on = d.pop("first_payment_on", UNSET)

        calculation = d.pop("calculation", UNSET)

        currency = d.pop("currency", UNSET)

        _time_condition = d.pop("time_condition", UNSET)
        time_condition: ContractsCompensationTimeCondition | Unset
        if isinstance(_time_condition, Unset):
            time_condition = UNSET
        else:
            time_condition = ContractsCompensationTimeCondition(_time_condition) if _time_condition is not None else None

        minimum_amount_of_hours = d.pop("minimum_amount_of_hours", UNSET)

        minimum_amount_of_hours_in_cents = d.pop("minimum_amount_of_hours_in_cents", UNSET)

        contracts_compensation = cls(
            id=id,
            contract_version_id=contract_version_id,
            contracts_taxonomy_id=contracts_taxonomy_id,
            unit=unit,
            description=description,
            compensation_type=compensation_type,
            amount=amount,
            sync_with_supplements=sync_with_supplements,
            payroll_policy_id=payroll_policy_id,
            recurrence_count=recurrence_count,
            starts_on=starts_on,
            recurrence=recurrence,
            first_payment_on=first_payment_on,
            calculation=calculation,
            currency=currency,
            time_condition=time_condition,
            minimum_amount_of_hours=minimum_amount_of_hours,
            minimum_amount_of_hours_in_cents=minimum_amount_of_hours_in_cents,
        )

        contracts_compensation.additional_properties = d
        return contracts_compensation

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
