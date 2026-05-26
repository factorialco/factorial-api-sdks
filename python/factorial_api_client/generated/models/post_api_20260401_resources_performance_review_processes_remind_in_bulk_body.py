from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_api_20260401_resources_performance_review_processes_remind_in_bulk_body_evaluation_types import (
    PostApi20260401ResourcesPerformanceReviewProcessesRemindInBulkBodyEvaluationTypes,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20260401ResourcesPerformanceReviewProcessesRemindInBulkBody")


@_attrs_define
class PostApi20260401ResourcesPerformanceReviewProcessesRemindInBulkBody:
    id: int
    """ Review process ID """
    evaluation_types: (
        PostApi20260401ResourcesPerformanceReviewProcessesRemindInBulkBodyEvaluationTypes | Unset
    ) = UNSET
    """ Reviewer strategies to remind about """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        evaluation_types: str | Unset = UNSET
        if not isinstance(self.evaluation_types, Unset):
            evaluation_types = self.evaluation_types.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if evaluation_types is not UNSET:
            field_dict["evaluation_types"] = evaluation_types

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        _evaluation_types = d.pop("evaluation_types", UNSET)
        evaluation_types: (
            PostApi20260401ResourcesPerformanceReviewProcessesRemindInBulkBodyEvaluationTypes
            | Unset
        )
        if isinstance(_evaluation_types, Unset):
            evaluation_types = UNSET
        else:
            evaluation_types = (
                PostApi20260401ResourcesPerformanceReviewProcessesRemindInBulkBodyEvaluationTypes(
                    _evaluation_types
                )
            )

        post_api_20260401_resources_performance_review_processes_remind_in_bulk_body = cls(
            id=id,
            evaluation_types=evaluation_types,
        )

        post_api_20260401_resources_performance_review_processes_remind_in_bulk_body.additional_properties = d
        return post_api_20260401_resources_performance_review_processes_remind_in_bulk_body

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
