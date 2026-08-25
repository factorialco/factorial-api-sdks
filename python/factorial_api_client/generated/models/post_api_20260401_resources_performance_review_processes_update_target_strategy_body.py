from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_api_20260401_resources_performance_review_processes_update_target_strategy_body_target_strategy import (
    PostApi20260401ResourcesPerformanceReviewProcessesUpdateTargetStrategyBodyTargetStrategy,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20260401ResourcesPerformanceReviewProcessesUpdateTargetStrategyBody")


@_attrs_define
class PostApi20260401ResourcesPerformanceReviewProcessesUpdateTargetStrategyBody:
    id: int
    """ Review process ID """
    target_strategy: (
        PostApi20260401ResourcesPerformanceReviewProcessesUpdateTargetStrategyBodyTargetStrategy
        | Unset
    ) = UNSET
    """ Condition that defines the employees that will be evaluated (participants) """
    arguments: list[int] | Unset = UNSET
    """ IDs of target strategy groups selected """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        target_strategy: str | Unset = UNSET
        if not isinstance(self.target_strategy, Unset):
            target_strategy = self.target_strategy.value if self.target_strategy is not None else None

        arguments: list[int] | Unset = UNSET
        if not isinstance(self.arguments, Unset):
            arguments = self.arguments

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if target_strategy is not UNSET:
            field_dict["target_strategy"] = target_strategy
        if arguments is not UNSET:
            field_dict["arguments"] = arguments

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        _target_strategy = d.pop("target_strategy", UNSET)
        target_strategy: (
            PostApi20260401ResourcesPerformanceReviewProcessesUpdateTargetStrategyBodyTargetStrategy
            | Unset
        )
        if isinstance(_target_strategy, Unset):
            target_strategy = UNSET
        else:
            target_strategy = PostApi20260401ResourcesPerformanceReviewProcessesUpdateTargetStrategyBodyTargetStrategy(
                _target_strategy
            )

        arguments = cast(list[int], d.pop("arguments", UNSET))

        post_api_20260401_resources_performance_review_processes_update_target_strategy_body = cls(
            id=id,
            target_strategy=target_strategy,
            arguments=arguments,
        )

        post_api_20260401_resources_performance_review_processes_update_target_strategy_body.additional_properties = d
        return post_api_20260401_resources_performance_review_processes_update_target_strategy_body

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
