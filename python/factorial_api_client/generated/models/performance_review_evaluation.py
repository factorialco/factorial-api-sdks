from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.performance_review_evaluation_evaluation_type import (
    PerformanceReviewEvaluationEvaluationType,
)
from ..models.performance_review_evaluation_status import PerformanceReviewEvaluationStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="PerformanceReviewEvaluation")


@_attrs_define
class PerformanceReviewEvaluation:
    id: int
    """ Evaluation ID """
    evaluation_type: PerformanceReviewEvaluationEvaluationType
    """ Evaluation type """
    published: bool
    """ Whether the evaluation is published """
    status: PerformanceReviewEvaluationStatus
    """ Evaluation status """
    review_process_target_id: str
    performance_review_process_id: int | Unset = UNSET
    """ Review process ID """
    target_access_id: int | Unset = UNSET
    """ Participant access ID """
    reviewer_access_id: int | Unset = UNSET
    """ Reviewer access ID """
    published_at: str | Unset = UNSET
    """ Date when the evaluation was published """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        evaluation_type = self.evaluation_type.value

        published = self.published

        status = self.status.value

        review_process_target_id = self.review_process_target_id

        performance_review_process_id = self.performance_review_process_id

        target_access_id = self.target_access_id

        reviewer_access_id = self.reviewer_access_id

        published_at = self.published_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "evaluation_type": evaluation_type,
                "published": published,
                "status": status,
                "review_process_target_id": review_process_target_id,
            }
        )
        if performance_review_process_id is not UNSET:
            field_dict["performance_review_process_id"] = performance_review_process_id
        if target_access_id is not UNSET:
            field_dict["target_access_id"] = target_access_id
        if reviewer_access_id is not UNSET:
            field_dict["reviewer_access_id"] = reviewer_access_id
        if published_at is not UNSET:
            field_dict["published_at"] = published_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        evaluation_type = PerformanceReviewEvaluationEvaluationType(d.pop("evaluation_type"))

        published = d.pop("published")

        status = PerformanceReviewEvaluationStatus(d.pop("status"))

        review_process_target_id = d.pop("review_process_target_id")

        performance_review_process_id = d.pop("performance_review_process_id", UNSET)

        target_access_id = d.pop("target_access_id", UNSET)

        reviewer_access_id = d.pop("reviewer_access_id", UNSET)

        published_at = d.pop("published_at", UNSET)

        performance_review_evaluation = cls(
            id=id,
            evaluation_type=evaluation_type,
            published=published,
            status=status,
            review_process_target_id=review_process_target_id,
            performance_review_process_id=performance_review_process_id,
            target_access_id=target_access_id,
            reviewer_access_id=reviewer_access_id,
            published_at=published_at,
        )

        performance_review_evaluation.additional_properties = d
        return performance_review_evaluation

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
