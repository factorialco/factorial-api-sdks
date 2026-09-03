from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.put_api_20261001_resources_compensations_employees_compensations_id_body_strategy_type import (
    PutApi20261001ResourcesCompensationsEmployeesCompensationsIdBodyStrategyType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PutApi20261001ResourcesCompensationsEmployeesCompensationsIdBody")


@_attrs_define
class PutApi20261001ResourcesCompensationsEmployeesCompensationsIdBody:
    id: str
    """ Employee compensation id """
    is_overwritten: bool
    """ When true, the provided `amount` becomes `amount_overwritten` """
    amount: int | Unset = UNSET
    amount_overwritten: int | Unset = UNSET
    """ Manual override of the strategy-computed amount; not allowed on fixed-strategy rows (422
    `overwrite_not_applicable`) """
    strategy_type: (
        PutApi20261001ResourcesCompensationsEmployeesCompensationsIdBodyStrategyType | Unset
    ) = UNSET
    """ Amount strategy discriminator """
    unit_symbol: str | Unset = UNSET
    """ Unit symbol (e.g. `EUR`) """
    upper_limit: int | Unset = UNSET
    """ Upper limit for variable-strategy compensations (nullable; ignored on fixed / per_worked_day strategies) """
    per_day_rate: int | Unset = UNSET
    """ Per-day rate for per_worked_day strategies (nullable; ignored on fixed / variable strategies) """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        is_overwritten = self.is_overwritten

        amount = self.amount

        amount_overwritten = self.amount_overwritten

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
                "id": id,
                "is_overwritten": is_overwritten,
            }
        )
        if amount is not UNSET:
            field_dict["amount"] = amount
        if amount_overwritten is not UNSET:
            field_dict["amount_overwritten"] = amount_overwritten
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
        id = d.pop("id")

        is_overwritten = d.pop("is_overwritten")

        amount = d.pop("amount", UNSET)

        amount_overwritten = d.pop("amount_overwritten", UNSET)

        _strategy_type = d.pop("strategy_type", UNSET)
        strategy_type: (
            PutApi20261001ResourcesCompensationsEmployeesCompensationsIdBodyStrategyType | Unset
        )
        if isinstance(_strategy_type, Unset):
            strategy_type = UNSET
        else:
            strategy_type = (
                PutApi20261001ResourcesCompensationsEmployeesCompensationsIdBodyStrategyType(
                    _strategy_type
                ) if _strategy_type is not None else None
            )

        unit_symbol = d.pop("unit_symbol", UNSET)

        upper_limit = d.pop("upper_limit", UNSET)

        per_day_rate = d.pop("per_day_rate", UNSET)

        put_api_20261001_resources_compensations_employees_compensations_id_body = cls(
            id=id,
            is_overwritten=is_overwritten,
            amount=amount,
            amount_overwritten=amount_overwritten,
            strategy_type=strategy_type,
            unit_symbol=unit_symbol,
            upper_limit=upper_limit,
            per_day_rate=per_day_rate,
        )

        put_api_20261001_resources_compensations_employees_compensations_id_body.additional_properties = d
        return put_api_20261001_resources_compensations_employees_compensations_id_body

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
