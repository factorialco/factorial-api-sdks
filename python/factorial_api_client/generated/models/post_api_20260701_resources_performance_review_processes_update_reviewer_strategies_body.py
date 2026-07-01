from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_api_20260701_resources_performance_review_processes_update_reviewer_strategies_body_reviewer_strategies import (
    PostApi20260701ResourcesPerformanceReviewProcessesUpdateReviewerStrategiesBodyReviewerStrategies,
)

T = TypeVar(
    "T", bound="PostApi20260701ResourcesPerformanceReviewProcessesUpdateReviewerStrategiesBody"
)


@_attrs_define
class PostApi20260701ResourcesPerformanceReviewProcessesUpdateReviewerStrategiesBody:
    id: str
    """ Review process ID """
    reviewer_strategies: PostApi20260701ResourcesPerformanceReviewProcessesUpdateReviewerStrategiesBodyReviewerStrategies
    """ New review types to be applied """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        reviewer_strategies = self.reviewer_strategies.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "reviewer_strategies": reviewer_strategies,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        reviewer_strategies = PostApi20260701ResourcesPerformanceReviewProcessesUpdateReviewerStrategiesBodyReviewerStrategies(
            d.pop("reviewer_strategies")
        )

        post_api_20260701_resources_performance_review_processes_update_reviewer_strategies_body = (
            cls(
                id=id,
                reviewer_strategies=reviewer_strategies,
            )
        )

        post_api_20260701_resources_performance_review_processes_update_reviewer_strategies_body.additional_properties = d
        return (
            post_api_20260701_resources_performance_review_processes_update_reviewer_strategies_body
        )

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
