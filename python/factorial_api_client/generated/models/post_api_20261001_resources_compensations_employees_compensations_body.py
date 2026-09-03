from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_api_20261001_resources_compensations_employees_compensations_body_strategy_type import (
    PostApi20261001ResourcesCompensationsEmployeesCompensationsBodyStrategyType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20261001ResourcesCompensationsEmployeesCompensationsBody")


@_attrs_define
class PostApi20261001ResourcesCompensationsEmployeesCompensationsBody:
    payroll_run_id: str
    """ Parent payroll run id, refers to compensations/payroll_runs endpoint. """
    employee_id: str
    """ Employee id (participant of the payroll run), refers to employees/employees endpoint. """
    concept_id: str
    """ Payroll concept id, refers to compensations/concepts endpoint. """
    is_overwritten: bool
    """ When true, the provided `amount` becomes `amount_overwritten` """
    amount: int | Unset = UNSET
    """ Amount value (nullable; required when is_overwritten=true) """
    strategy_type: (
        PostApi20261001ResourcesCompensationsEmployeesCompensationsBodyStrategyType | Unset
    ) = UNSET
    """ Amount strategy discriminator """
    unit_symbol: str | Unset = UNSET
    """ Unit symbol (e.g. `EUR`) """
    upper_limit: int | Unset = UNSET
    """ Upper limit for variable strategy (ignored for fixed / per_worked_day) """
    per_day_rate: int | Unset = UNSET
    """ Per-day rate (only used for per_worked_day strategy) """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        payroll_run_id = self.payroll_run_id

        employee_id = self.employee_id

        concept_id = self.concept_id

        is_overwritten = self.is_overwritten

        amount = self.amount

        strategy_type: str | Unset = UNSET
        if not isinstance(self.strategy_type, Unset):
            strategy_type = self.strategy_type.value if self.strategy_type is not None else None

        unit_symbol = self.unit_symbol

        upper_limit = self.upper_limit

        per_day_rate = self.per_day_rate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "payroll_run_id": payroll_run_id,
                "employee_id": employee_id,
                "concept_id": concept_id,
                "is_overwritten": is_overwritten,
            }
        )
        if amount is not UNSET:
            field_dict["amount"] = amount
        if strategy_type is not UNSET:
            field_dict["strategy_type"] = strategy_type
        if unit_symbol is not UNSET:
            field_dict["unit_symbol"] = unit_symbol
        if upper_limit is not UNSET:
            field_dict["upper_limit"] = upper_limit
        if per_day_rate is not UNSET:
            field_dict["per_day_rate"] = per_day_rate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        payroll_run_id = d.pop("payroll_run_id")

        employee_id = d.pop("employee_id")

        concept_id = d.pop("concept_id")

        is_overwritten = d.pop("is_overwritten")

        amount = d.pop("amount", UNSET)

        _strategy_type = d.pop("strategy_type", UNSET)
        strategy_type: (
            PostApi20261001ResourcesCompensationsEmployeesCompensationsBodyStrategyType | Unset
        )
        if isinstance(_strategy_type, Unset):
            strategy_type = UNSET
        else:
            strategy_type = (
                PostApi20261001ResourcesCompensationsEmployeesCompensationsBodyStrategyType(
                    _strategy_type
                ) if _strategy_type is not None else None
            )

        unit_symbol = d.pop("unit_symbol", UNSET)

        upper_limit = d.pop("upper_limit", UNSET)

        per_day_rate = d.pop("per_day_rate", UNSET)

        post_api_20261001_resources_compensations_employees_compensations_body = cls(
            payroll_run_id=payroll_run_id,
            employee_id=employee_id,
            concept_id=concept_id,
            is_overwritten=is_overwritten,
            amount=amount,
            strategy_type=strategy_type,
            unit_symbol=unit_symbol,
            upper_limit=upper_limit,
            per_day_rate=per_day_rate,
        )

        post_api_20261001_resources_compensations_employees_compensations_body.additional_properties = d
        return post_api_20261001_resources_compensations_employees_compensations_body

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
