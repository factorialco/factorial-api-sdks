from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_api_20261001_resources_compensations_additional_compensations_body_amount_strategy_type import (
    PostApi20261001ResourcesCompensationsAdditionalCompensationsBodyAmountStrategyType,
)
from ..models.post_api_20261001_resources_compensations_additional_compensations_body_recurrence import (
    PostApi20261001ResourcesCompensationsAdditionalCompensationsBodyRecurrence,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_api_20261001_resources_compensations_additional_compensations_body_per_worked_day_definition import (
        PostApi20261001ResourcesCompensationsAdditionalCompensationsBodyPerWorkedDayDefinition,
    )


T = TypeVar("T", bound="PostApi20261001ResourcesCompensationsAdditionalCompensationsBody")


@_attrs_define
class PostApi20261001ResourcesCompensationsAdditionalCompensationsBody:
    contract_version_id: str
    """ Target contract version id, refers to contracts/contract_versions endpoint. """
    payroll_concept_id: str
    """ Payroll concept id, refers to compensations/concepts endpoint. """
    amount_strategy_type: (
        PostApi20261001ResourcesCompensationsAdditionalCompensationsBodyAmountStrategyType
    )
    """ Amount strategy discriminator """
    per_worked_day_definition: (
        PostApi20261001ResourcesCompensationsAdditionalCompensationsBodyPerWorkedDayDefinition
    )
    """ Definition object required when `amount_strategy_type = contracts_per_worked_day_amount_strategy`. Carries
    `calculation_source`, `reference_time`, `minimum_amount_of_hours_in_minutes`, `work_locations`,
    `timeoff_leave_type_ids`, and `eligible_days`. """
    amount: int | Unset = UNSET
    """ Amount value (required for Fixed and PerWorkedDay strategies) """
    upper_limit: int | Unset = UNSET
    """ Upper limit for Variable strategy (ignored for others) """
    description: str | Unset = UNSET
    """ Free-text description """
    recurrence: (
        PostApi20261001ResourcesCompensationsAdditionalCompensationsBodyRecurrence | Unset
    ) = UNSET
    """ Recurrence label. One of `monthly`, `every_2_months`, `every_3_months`, `every_4_months`, `every_5_months`,
    `every_6_months`, `every_7_months`, `every_8_months`, `every_9_months`, `every_10_months`, `every_11_months`,
    `every_12_months`. """
    first_payment_on: str | Unset = UNSET
    """ Date of the first payment (must be on or after the contract version's effective month) """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        contract_version_id = self.contract_version_id

        payroll_concept_id = self.payroll_concept_id

        amount_strategy_type = self.amount_strategy_type.value

        per_worked_day_definition = self.per_worked_day_definition.to_dict()

        amount = self.amount

        upper_limit = self.upper_limit

        description = self.description

        recurrence: str | Unset = UNSET
        if not isinstance(self.recurrence, Unset):
            recurrence = self.recurrence.value if self.recurrence is not None else None

        first_payment_on = self.first_payment_on

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "contract_version_id": contract_version_id,
                "payroll_concept_id": payroll_concept_id,
                "amount_strategy_type": amount_strategy_type,
                "per_worked_day_definition": per_worked_day_definition,
            }
        )
        if amount is not UNSET:
            field_dict["amount"] = amount
        if upper_limit is not UNSET:
            field_dict["upper_limit"] = upper_limit
        if description is not UNSET:
            field_dict["description"] = description
        if recurrence is not UNSET:
            field_dict["recurrence"] = recurrence
        if first_payment_on is not UNSET:
            field_dict["first_payment_on"] = first_payment_on

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_api_20261001_resources_compensations_additional_compensations_body_per_worked_day_definition import (
            PostApi20261001ResourcesCompensationsAdditionalCompensationsBodyPerWorkedDayDefinition,
        )

        d = dict(src_dict)
        contract_version_id = d.pop("contract_version_id")

        payroll_concept_id = d.pop("payroll_concept_id")

        amount_strategy_type = (
            PostApi20261001ResourcesCompensationsAdditionalCompensationsBodyAmountStrategyType(
                d.pop("amount_strategy_type")
            )
        )

        per_worked_day_definition = PostApi20261001ResourcesCompensationsAdditionalCompensationsBodyPerWorkedDayDefinition.from_dict(
            d.pop("per_worked_day_definition")
        )

        amount = d.pop("amount", UNSET)

        upper_limit = d.pop("upper_limit", UNSET)

        description = d.pop("description", UNSET)

        _recurrence = d.pop("recurrence", UNSET)
        recurrence: (
            PostApi20261001ResourcesCompensationsAdditionalCompensationsBodyRecurrence | Unset
        )
        if isinstance(_recurrence, Unset):
            recurrence = UNSET
        else:
            recurrence = PostApi20261001ResourcesCompensationsAdditionalCompensationsBodyRecurrence(
                _recurrence
            ) if _recurrence is not None else None

        first_payment_on = d.pop("first_payment_on", UNSET)

        post_api_20261001_resources_compensations_additional_compensations_body = cls(
            contract_version_id=contract_version_id,
            payroll_concept_id=payroll_concept_id,
            amount_strategy_type=amount_strategy_type,
            per_worked_day_definition=per_worked_day_definition,
            amount=amount,
            upper_limit=upper_limit,
            description=description,
            recurrence=recurrence,
            first_payment_on=first_payment_on,
        )

        post_api_20261001_resources_compensations_additional_compensations_body.additional_properties = d
        return post_api_20261001_resources_compensations_additional_compensations_body

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
