from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.performance_review_employee_score_reviewer_strategy import (
    PerformanceReviewEmployeeScoreReviewerStrategy,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PerformanceReviewEmployeeScore")


@_attrs_define
class PerformanceReviewEmployeeScore:
    id: str
    """ Review emploee score ID """
    review_process_id: str
    """ Review process ID """
    review_evaluation_id: str
    """ Review evaluation ID """
    target_access_id: str
    """ Employee access ID """
    company_id: str
    """ Company identifier of the review employee score """
    reviewer_strategy: PerformanceReviewEmployeeScoreReviewerStrategy
    """ Who scored the employee """
    review_process_target_id: str
    """ Review process target ID (composed with review_process_id and target_access_id) """
    score: float
    """ Employee score within the min and max scale """
    scale_min: int
    """ Minimum score in the scale """
    scale_max: int
    """ Maximum score in the scale """
    normalized_score: float
    """ Employee score in percentage (0% to 100%) """
    published_at: str
    """ Date and time when the employee score was published """
    potential_score: int | Unset = UNSET
    """ Employee potential score within the min and max scale """
    normalized_potential_score: float | Unset = UNSET
    """ Employee potential score in percentage (0% to 100%) """
    comment: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        review_process_id = self.review_process_id

        review_evaluation_id = self.review_evaluation_id

        target_access_id = self.target_access_id

        company_id = self.company_id

        reviewer_strategy = self.reviewer_strategy.value

        review_process_target_id = self.review_process_target_id

        score = self.score

        scale_min = self.scale_min

        scale_max = self.scale_max

        normalized_score = self.normalized_score

        published_at = self.published_at

        potential_score = self.potential_score

        normalized_potential_score = self.normalized_potential_score

        comment = self.comment

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "review_process_id": review_process_id,
                "review_evaluation_id": review_evaluation_id,
                "target_access_id": target_access_id,
                "company_id": company_id,
                "reviewer_strategy": reviewer_strategy,
                "review_process_target_id": review_process_target_id,
                "score": score,
                "scale_min": scale_min,
                "scale_max": scale_max,
                "normalized_score": normalized_score,
                "published_at": published_at,
            }
        )
        if potential_score is not UNSET:
            field_dict["potential_score"] = potential_score
        if normalized_potential_score is not UNSET:
            field_dict["normalized_potential_score"] = normalized_potential_score
        if comment is not UNSET:
            field_dict["comment"] = comment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        review_process_id = d.pop("review_process_id")

        review_evaluation_id = d.pop("review_evaluation_id")

        target_access_id = d.pop("target_access_id")

        company_id = d.pop("company_id")

        reviewer_strategy = PerformanceReviewEmployeeScoreReviewerStrategy(
            d.pop("reviewer_strategy")
        )

        review_process_target_id = d.pop("review_process_target_id")

        score = d.pop("score")

        scale_min = d.pop("scale_min")

        scale_max = d.pop("scale_max")

        normalized_score = d.pop("normalized_score")

        published_at = d.pop("published_at")

        potential_score = d.pop("potential_score", UNSET)

        normalized_potential_score = d.pop("normalized_potential_score", UNSET)

        comment = d.pop("comment", UNSET)

        performance_review_employee_score = cls(
            id=id,
            review_process_id=review_process_id,
            review_evaluation_id=review_evaluation_id,
            target_access_id=target_access_id,
            company_id=company_id,
            reviewer_strategy=reviewer_strategy,
            review_process_target_id=review_process_target_id,
            score=score,
            scale_min=scale_min,
            scale_max=scale_max,
            normalized_score=normalized_score,
            published_at=published_at,
            potential_score=potential_score,
            normalized_potential_score=normalized_potential_score,
            comment=comment,
        )

        performance_review_employee_score.additional_properties = d
        return performance_review_employee_score

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
