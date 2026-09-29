from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.put_api_20261001_resources_project_management_budget_strategies_id_body_budget_strategy_type import (
    PutApi20261001ResourcesProjectManagementBudgetStrategiesIdBodyBudgetStrategyType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PutApi20261001ResourcesProjectManagementBudgetStrategiesIdBody")


@_attrs_define
class PutApi20261001ResourcesProjectManagementBudgetStrategiesIdBody:
    id: str
    """ Id of the budget strategy to update """
    planned_cents: int | Unset = UNSET
    """ Planned amount in cents (for project_fixed_cost / total_budget) """
    planned_minutes: int | Unset = UNSET
    """ Planned time in minutes (for total_budget) """
    fee_amount_cents: int | Unset = UNSET
    """ Fee amount in cents (for project_fixed_cost / total_budget when is billable) """
    budget_strategy_type: (
        PutApi20261001ResourcesProjectManagementBudgetStrategiesIdBodyBudgetStrategyType | Unset
    ) = UNSET
    """ Type of budget strategy. One of project_fixed_cost => ProjectFixedCost, total_budget => TimeAndMaterials,
    without_budget => WithoutBudget """
    delegated: bool | Unset = UNSET
    """ Whether the budget strategy is delegated """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        planned_cents = self.planned_cents

        planned_minutes = self.planned_minutes

        fee_amount_cents = self.fee_amount_cents

        budget_strategy_type: str | Unset = UNSET
        if not isinstance(self.budget_strategy_type, Unset):
            budget_strategy_type = self.budget_strategy_type.value if self.budget_strategy_type is not None else None

        delegated = self.delegated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if planned_cents is not UNSET:
            field_dict["planned_cents"] = planned_cents
        if planned_minutes is not UNSET:
            field_dict["planned_minutes"] = planned_minutes
        if fee_amount_cents is not UNSET:
            field_dict["fee_amount_cents"] = fee_amount_cents
        if budget_strategy_type is not UNSET:
            field_dict["budget_strategy_type"] = budget_strategy_type
        if delegated is not UNSET:
            field_dict["delegated"] = delegated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        planned_cents = d.pop("planned_cents", UNSET)

        planned_minutes = d.pop("planned_minutes", UNSET)

        fee_amount_cents = d.pop("fee_amount_cents", UNSET)

        _budget_strategy_type = d.pop("budget_strategy_type", UNSET)
        budget_strategy_type: (
            PutApi20261001ResourcesProjectManagementBudgetStrategiesIdBodyBudgetStrategyType | Unset
        )
        if isinstance(_budget_strategy_type, Unset):
            budget_strategy_type = UNSET
        else:
            budget_strategy_type = (
                PutApi20261001ResourcesProjectManagementBudgetStrategiesIdBodyBudgetStrategyType(
                    _budget_strategy_type
                ) if _budget_strategy_type is not None else None
            )

        delegated = d.pop("delegated", UNSET)

        put_api_20261001_resources_project_management_budget_strategies_id_body = cls(
            id=id,
            planned_cents=planned_cents,
            planned_minutes=planned_minutes,
            fee_amount_cents=fee_amount_cents,
            budget_strategy_type=budget_strategy_type,
            delegated=delegated,
        )

        put_api_20261001_resources_project_management_budget_strategies_id_body.additional_properties = d
        return put_api_20261001_resources_project_management_budget_strategies_id_body

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
