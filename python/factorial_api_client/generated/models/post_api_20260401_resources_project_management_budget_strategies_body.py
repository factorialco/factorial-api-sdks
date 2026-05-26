from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_api_20260401_resources_project_management_budget_strategies_body_budget_strategy_type import (
    PostApi20260401ResourcesProjectManagementBudgetStrategiesBodyBudgetStrategyType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20260401ResourcesProjectManagementBudgetStrategiesBody")


@_attrs_define
class PostApi20260401ResourcesProjectManagementBudgetStrategiesBody:
    budget_strategy_type: (
        PostApi20260401ResourcesProjectManagementBudgetStrategiesBodyBudgetStrategyType
    )
    """ Type of budget strategy. One of project_fixed_cost => ProjectFixedCost, total_budget => TimeAndMaterials,
    without_budget => WithoutBudget """
    project_id: int
    """ Id of the project this budget strategy belongs to """
    planned_cents: int | Unset = UNSET
    """ Planned amount in cents (for project_fixed_cost / total_budget) """
    planned_minutes: int | Unset = UNSET
    """ Planned time in minutes (for total_budget) """
    fee_amount_cents: int | Unset = UNSET
    """ Fee amount in cents (for project_fixed_cost / total_budget when is billable) """
    subproject_id: int | Unset = UNSET
    """ Id of the subproject, if any """
    delegated: bool | Unset = UNSET
    """ Whether the budget strategy is delegated """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        budget_strategy_type = self.budget_strategy_type.value

        project_id = self.project_id

        planned_cents = self.planned_cents

        planned_minutes = self.planned_minutes

        fee_amount_cents = self.fee_amount_cents

        subproject_id = self.subproject_id

        delegated = self.delegated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "budget_strategy_type": budget_strategy_type,
                "project_id": project_id,
            }
        )
        if planned_cents is not UNSET:
            field_dict["planned_cents"] = planned_cents
        if planned_minutes is not UNSET:
            field_dict["planned_minutes"] = planned_minutes
        if fee_amount_cents is not UNSET:
            field_dict["fee_amount_cents"] = fee_amount_cents
        if subproject_id is not UNSET:
            field_dict["subproject_id"] = subproject_id
        if delegated is not UNSET:
            field_dict["delegated"] = delegated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        budget_strategy_type = (
            PostApi20260401ResourcesProjectManagementBudgetStrategiesBodyBudgetStrategyType(
                d.pop("budget_strategy_type")
            )
        )

        project_id = d.pop("project_id")

        planned_cents = d.pop("planned_cents", UNSET)

        planned_minutes = d.pop("planned_minutes", UNSET)

        fee_amount_cents = d.pop("fee_amount_cents", UNSET)

        subproject_id = d.pop("subproject_id", UNSET)

        delegated = d.pop("delegated", UNSET)

        post_api_20260401_resources_project_management_budget_strategies_body = cls(
            budget_strategy_type=budget_strategy_type,
            project_id=project_id,
            planned_cents=planned_cents,
            planned_minutes=planned_minutes,
            fee_amount_cents=fee_amount_cents,
            subproject_id=subproject_id,
            delegated=delegated,
        )

        post_api_20260401_resources_project_management_budget_strategies_body.additional_properties = d
        return post_api_20260401_resources_project_management_budget_strategies_body

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
