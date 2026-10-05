from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.performance_review_process_target_strategy_strategy import (
    PerformanceReviewProcessTargetStrategyStrategy,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PerformanceReviewProcessTargetStrategy")


@_attrs_define
class PerformanceReviewProcessTargetStrategy:
    """Condition that defines the employees that will be evaluated (participants). Calculated when the review process
    starts

        Example:
            {'arguments': [], 'strategy': 'all_employees'}

    """

    strategy: PerformanceReviewProcessTargetStrategyStrategy
    arguments: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        strategy = self.strategy.value

        arguments: list[str] | Unset = UNSET
        if not isinstance(self.arguments, Unset):
            arguments = self.arguments

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "strategy": strategy,
            }
        )
        if arguments is not UNSET:
            field_dict["arguments"] = arguments

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        strategy = PerformanceReviewProcessTargetStrategyStrategy(d.pop("strategy"))

        arguments = cast(list[str], d.pop("arguments", UNSET))

        performance_review_process_target_strategy = cls(
            strategy=strategy,
            arguments=arguments,
        )

        performance_review_process_target_strategy.additional_properties = d
        return performance_review_process_target_strategy

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
