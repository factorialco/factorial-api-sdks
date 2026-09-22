from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.compensations_additional_compensation_amount_strategy_type import (
    CompensationsAdditionalCompensationAmountStrategyType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.compensations_additional_compensation_per_worked_day_definition import (
        CompensationsAdditionalCompensationPerWorkedDayDefinition,
    )


T = TypeVar("T", bound="CompensationsAdditionalCompensation")


@_attrs_define
class CompensationsAdditionalCompensation:
    id: str
    """ The identifier of the additional compensation """
    contract_version_id: str
    """ Contract version this additional compensation is attached to """
    company_id: str
    """ Company id """
    payroll_concept_id: str
    """ Payroll concept classifying this additional compensation """
    employee_id: str
    """ Employee id derived from the contract version """
    amount_strategy_type: CompensationsAdditionalCompensationAmountStrategyType
    """ Amount strategy discriminator — one of `contracts_fixed_amount_strategy`,
    `contracts_variable_amount_strategy`, `contracts_per_worked_day_amount_strategy` """
    amount_strategy_id: str
    """ Amount strategy id """
    per_worked_day_definition: CompensationsAdditionalCompensationPerWorkedDayDefinition
    """ Definition object populated for PerWorkedDay strategies. Carries `calculation_source`, `reference_time`,
    `minimum_amount_of_hours_in_minutes`, `work_locations`, `timeoff_leave_type_ids`, and `eligible_days`. `null`
    for Fixed / Variable strategies. """
    created_at: str
    """ Timestamp when the additional compensation was created """
    updated_at: str
    """ Timestamp when the additional compensation was last updated """
    recurrence: str | Unset = UNSET
    """ Recurrence label. One of `monthly`, `every_2_months`, `every_3_months`, `every_4_months`, `every_5_months`,
    `every_6_months`, `every_7_months`, `every_8_months`, `every_9_months`, `every_10_months`, `every_11_months`,
    `every_12_months`. """
    first_payment_on: str | Unset = UNSET
    """ Date of the first payment """
    description: str | Unset = UNSET
    """ Free-text description """
    amount: int | Unset = UNSET
    """ Amount value (Fixed / PerWorkedDay strategies) """
    upper_limit: int | Unset = UNSET
    """ Upper limit (Variable strategy only) """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        contract_version_id = self.contract_version_id

        company_id = self.company_id

        payroll_concept_id = self.payroll_concept_id

        employee_id = self.employee_id

        amount_strategy_type = self.amount_strategy_type.value

        amount_strategy_id = self.amount_strategy_id

        per_worked_day_definition = self.per_worked_day_definition.to_dict()

        created_at = self.created_at

        updated_at = self.updated_at

        recurrence = self.recurrence

        first_payment_on = self.first_payment_on

        description = self.description

        amount = self.amount

        upper_limit = self.upper_limit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "contract_version_id": contract_version_id,
                "company_id": company_id,
                "payroll_concept_id": payroll_concept_id,
                "employee_id": employee_id,
                "amount_strategy_type": amount_strategy_type,
                "amount_strategy_id": amount_strategy_id,
                "per_worked_day_definition": per_worked_day_definition,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if recurrence is not UNSET:
            field_dict["recurrence"] = recurrence
        if first_payment_on is not UNSET:
            field_dict["first_payment_on"] = first_payment_on
        if description is not UNSET:
            field_dict["description"] = description
        if amount is not UNSET:
            field_dict["amount"] = amount
        if upper_limit is not UNSET:
            field_dict["upper_limit"] = upper_limit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.compensations_additional_compensation_per_worked_day_definition import (
            CompensationsAdditionalCompensationPerWorkedDayDefinition,
        )

        d = dict(src_dict)
        id = d.pop("id")

        contract_version_id = d.pop("contract_version_id")

        company_id = d.pop("company_id")

        payroll_concept_id = d.pop("payroll_concept_id")

        employee_id = d.pop("employee_id")

        amount_strategy_type = CompensationsAdditionalCompensationAmountStrategyType(
            d.pop("amount_strategy_type")
        )

        amount_strategy_id = d.pop("amount_strategy_id")

        per_worked_day_definition = (
            CompensationsAdditionalCompensationPerWorkedDayDefinition.from_dict(
                d.pop("per_worked_day_definition")
            )
        )

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        recurrence = d.pop("recurrence", UNSET)

        first_payment_on = d.pop("first_payment_on", UNSET)

        description = d.pop("description", UNSET)

        amount = d.pop("amount", UNSET)

        upper_limit = d.pop("upper_limit", UNSET)

        compensations_additional_compensation = cls(
            id=id,
            contract_version_id=contract_version_id,
            company_id=company_id,
            payroll_concept_id=payroll_concept_id,
            employee_id=employee_id,
            amount_strategy_type=amount_strategy_type,
            amount_strategy_id=amount_strategy_id,
            per_worked_day_definition=per_worked_day_definition,
            created_at=created_at,
            updated_at=updated_at,
            recurrence=recurrence,
            first_payment_on=first_payment_on,
            description=description,
            amount=amount,
            upper_limit=upper_limit,
        )

        compensations_additional_compensation.additional_properties = d
        return compensations_additional_compensation

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
