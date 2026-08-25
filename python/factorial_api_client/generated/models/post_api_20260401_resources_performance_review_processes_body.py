from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_api_20260401_resources_performance_review_processes_body_reviewer_strategies import (
    PostApi20260401ResourcesPerformanceReviewProcessesBodyReviewerStrategies,
)
from ..models.post_api_20260401_resources_performance_review_processes_body_target_strategy import (
    PostApi20260401ResourcesPerformanceReviewProcessesBodyTargetStrategy,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20260401ResourcesPerformanceReviewProcessesBody")


@_attrs_define
class PostApi20260401ResourcesPerformanceReviewProcessesBody:
    author_access_id: int
    """ Access identifier of the author of the review process """
    name: str | Unset = UNSET
    """ Name of the review process """
    description: str | Unset = UNSET
    """ A brief description of the review process """
    reviewer_strategies: (
        PostApi20260401ResourcesPerformanceReviewProcessesBodyReviewerStrategies | Unset
    ) = UNSET
    """ Review types that will be assigned to the review process. It'll be used to create the evaluations when the
    process starts """
    target_strategy: (
        PostApi20260401ResourcesPerformanceReviewProcessesBodyTargetStrategy | Unset
    ) = UNSET
    """ Condition that defines the employees that will be evaluated (participants). Calculated when the review
    process starts """
    arguments: list[int] | Unset = UNSET
    """ IDs of target strategy groups selected """
    ends_at: str | Unset = UNSET
    """ Date when the review process should end """
    agreements_enabled: bool | Unset = UNSET
    """ Action plans help track goal progress, and facilitate performance review discussions. """
    employee_score_enabled: bool | Unset = UNSET
    """ Include one question at the end of the review to rate participants' performance. This rating will be
    reflected on the results page. """
    employee_potential_score_enabled: bool | Unset = UNSET
    """ Include one question at the end of the review to rate participants' potential. This rating will be reflected
    in the 9 box grid. """
    competencies_assessments_enabled: bool | Unset = UNSET
    """ Assess employees based on their assigned competencies through both manager and self-reviews. Ensure roles
    with designated competencies are properly set up. """
    cycle_id: str | Unset = UNSET
    """ Performance cycle ID """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        author_access_id = self.author_access_id

        name = self.name

        description = self.description

        reviewer_strategies: str | Unset = UNSET
        if not isinstance(self.reviewer_strategies, Unset):
            reviewer_strategies = self.reviewer_strategies.value if self.reviewer_strategies is not None else None

        target_strategy: str | Unset = UNSET
        if not isinstance(self.target_strategy, Unset):
            target_strategy = self.target_strategy.value if self.target_strategy is not None else None

        arguments: list[int] | Unset = UNSET
        if not isinstance(self.arguments, Unset):
            arguments = self.arguments

        ends_at = self.ends_at

        agreements_enabled = self.agreements_enabled

        employee_score_enabled = self.employee_score_enabled

        employee_potential_score_enabled = self.employee_potential_score_enabled

        competencies_assessments_enabled = self.competencies_assessments_enabled

        cycle_id = self.cycle_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "author_access_id": author_access_id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if reviewer_strategies is not UNSET:
            field_dict["reviewer_strategies"] = reviewer_strategies
        if target_strategy is not UNSET:
            field_dict["target_strategy"] = target_strategy
        if arguments is not UNSET:
            field_dict["arguments"] = arguments
        if ends_at is not UNSET:
            field_dict["ends_at"] = ends_at
        if agreements_enabled is not UNSET:
            field_dict["agreements_enabled"] = agreements_enabled
        if employee_score_enabled is not UNSET:
            field_dict["employee_score_enabled"] = employee_score_enabled
        if employee_potential_score_enabled is not UNSET:
            field_dict["employee_potential_score_enabled"] = employee_potential_score_enabled
        if competencies_assessments_enabled is not UNSET:
            field_dict["competencies_assessments_enabled"] = competencies_assessments_enabled
        if cycle_id is not UNSET:
            field_dict["cycle_id"] = cycle_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        author_access_id = d.pop("author_access_id")

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _reviewer_strategies = d.pop("reviewer_strategies", UNSET)
        reviewer_strategies: (
            PostApi20260401ResourcesPerformanceReviewProcessesBodyReviewerStrategies | Unset
        )
        if isinstance(_reviewer_strategies, Unset):
            reviewer_strategies = UNSET
        else:
            reviewer_strategies = (
                PostApi20260401ResourcesPerformanceReviewProcessesBodyReviewerStrategies(
                    _reviewer_strategies
                ) if _reviewer_strategies is not None else None
            )

        _target_strategy = d.pop("target_strategy", UNSET)
        target_strategy: (
            PostApi20260401ResourcesPerformanceReviewProcessesBodyTargetStrategy | Unset
        )
        if isinstance(_target_strategy, Unset):
            target_strategy = UNSET
        else:
            target_strategy = PostApi20260401ResourcesPerformanceReviewProcessesBodyTargetStrategy(
                _target_strategy
            ) if _target_strategy is not None else None

        arguments = cast(list[int], d.pop("arguments", UNSET))

        ends_at = d.pop("ends_at", UNSET)

        agreements_enabled = d.pop("agreements_enabled", UNSET)

        employee_score_enabled = d.pop("employee_score_enabled", UNSET)

        employee_potential_score_enabled = d.pop("employee_potential_score_enabled", UNSET)

        competencies_assessments_enabled = d.pop("competencies_assessments_enabled", UNSET)

        cycle_id = d.pop("cycle_id", UNSET)

        post_api_20260401_resources_performance_review_processes_body = cls(
            author_access_id=author_access_id,
            name=name,
            description=description,
            reviewer_strategies=reviewer_strategies,
            target_strategy=target_strategy,
            arguments=arguments,
            ends_at=ends_at,
            agreements_enabled=agreements_enabled,
            employee_score_enabled=employee_score_enabled,
            employee_potential_score_enabled=employee_potential_score_enabled,
            competencies_assessments_enabled=competencies_assessments_enabled,
            cycle_id=cycle_id,
        )

        post_api_20260401_resources_performance_review_processes_body.additional_properties = d
        return post_api_20260401_resources_performance_review_processes_body

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
