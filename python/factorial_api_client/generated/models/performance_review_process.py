from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.performance_review_process_reviewer_strategies import (
    PerformanceReviewProcessReviewerStrategies,
)
from ..models.performance_review_process_start_validation_errors import (
    PerformanceReviewProcessStartValidationErrors,
)
from ..models.performance_review_process_status import PerformanceReviewProcessStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.performance_review_process_agreements_configuration import (
        PerformanceReviewProcessAgreementsConfiguration,
    )
    from ..models.performance_review_process_competencies_assessments_configuration import (
        PerformanceReviewProcessCompetenciesAssessmentsConfiguration,
    )
    from ..models.performance_review_process_target_strategy import (
        PerformanceReviewProcessTargetStrategy,
    )


T = TypeVar("T", bound="PerformanceReviewProcess")


@_attrs_define
class PerformanceReviewProcess:
    id: str
    """ Review process ID """
    company_id: str
    """ Company ID """
    status: PerformanceReviewProcessStatus
    """ Review process status """
    start_validation_errors: PerformanceReviewProcessStartValidationErrors
    """ Missing or invalid information to be able to start the review process """
    archived: bool
    """ Whether the review process is archived or not """
    agreements_configuration: PerformanceReviewProcessAgreementsConfiguration
    """ Action plans help track goal progress, and facilitate performance review discussions. """
    competencies_assessments_configuration: (
        PerformanceReviewProcessCompetenciesAssessmentsConfiguration
    )
    """ Assess employees based on their assigned competencies through both manager and self-reviews. Ensure roles
    with designated competencies are properly set up. """
    name: str | Unset = UNSET
    """ Review process name """
    description: str | Unset = UNSET
    """ A brief description of the review process """
    target_strategy: PerformanceReviewProcessTargetStrategy | Unset = UNSET
    """ Condition that defines the employees that will be evaluated (participants). Calculated when the review
    process starts """
    reviewer_strategies: PerformanceReviewProcessReviewerStrategies | Unset = UNSET
    """ Review types that will be assigned to the review process. It'll be used to create the evaluations when the
    process starts """
    starts_at: str | Unset = UNSET
    """ Date when the review process should start """
    ends_at: str | Unset = UNSET
    """ Date when the review process should end """
    last_bulk_reminder: str | Unset = UNSET
    """ Date when the last bulk reminder was sent """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        company_id = self.company_id

        status = self.status.value

        start_validation_errors = self.start_validation_errors.value

        archived = self.archived

        agreements_configuration = self.agreements_configuration.to_dict()

        competencies_assessments_configuration = (
            self.competencies_assessments_configuration.to_dict()
        )

        name = self.name

        description = self.description

        target_strategy: dict[str, Any] | Unset = UNSET
        if not isinstance(self.target_strategy, Unset):
            target_strategy = self.target_strategy.to_dict()

        reviewer_strategies: str | Unset = UNSET
        if not isinstance(self.reviewer_strategies, Unset):
            reviewer_strategies = self.reviewer_strategies.value if self.reviewer_strategies is not None else None

        starts_at = self.starts_at

        ends_at = self.ends_at

        last_bulk_reminder = self.last_bulk_reminder

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "company_id": company_id,
                "status": status,
                "start_validation_errors": start_validation_errors,
                "archived": archived,
                "agreements_configuration": agreements_configuration,
                "competencies_assessments_configuration": competencies_assessments_configuration,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if target_strategy is not UNSET:
            field_dict["target_strategy"] = target_strategy
        if reviewer_strategies is not UNSET:
            field_dict["reviewer_strategies"] = reviewer_strategies
        if starts_at is not UNSET:
            field_dict["starts_at"] = starts_at
        if ends_at is not UNSET:
            field_dict["ends_at"] = ends_at
        if last_bulk_reminder is not UNSET:
            field_dict["last_bulk_reminder"] = last_bulk_reminder

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.performance_review_process_agreements_configuration import (
            PerformanceReviewProcessAgreementsConfiguration,
        )
        from ..models.performance_review_process_competencies_assessments_configuration import (
            PerformanceReviewProcessCompetenciesAssessmentsConfiguration,
        )
        from ..models.performance_review_process_target_strategy import (
            PerformanceReviewProcessTargetStrategy,
        )

        d = dict(src_dict)
        id = d.pop("id")

        company_id = d.pop("company_id")

        status = PerformanceReviewProcessStatus(d.pop("status"))

        start_validation_errors = PerformanceReviewProcessStartValidationErrors(
            d.pop("start_validation_errors")
        )

        archived = d.pop("archived")

        agreements_configuration = PerformanceReviewProcessAgreementsConfiguration.from_dict(
            d.pop("agreements_configuration")
        )

        competencies_assessments_configuration = (
            PerformanceReviewProcessCompetenciesAssessmentsConfiguration.from_dict(
                d.pop("competencies_assessments_configuration")
            )
        )

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _target_strategy = d.pop("target_strategy", UNSET)
        target_strategy: PerformanceReviewProcessTargetStrategy | Unset
        if isinstance(_target_strategy, Unset):
            target_strategy = UNSET
        else:
            target_strategy = PerformanceReviewProcessTargetStrategy.from_dict(_target_strategy)

        _reviewer_strategies = d.pop("reviewer_strategies", UNSET)
        reviewer_strategies: PerformanceReviewProcessReviewerStrategies | Unset
        if isinstance(_reviewer_strategies, Unset):
            reviewer_strategies = UNSET
        else:
            reviewer_strategies = PerformanceReviewProcessReviewerStrategies(_reviewer_strategies) if _reviewer_strategies is not None else None

        starts_at = d.pop("starts_at", UNSET)

        ends_at = d.pop("ends_at", UNSET)

        last_bulk_reminder = d.pop("last_bulk_reminder", UNSET)

        performance_review_process = cls(
            id=id,
            company_id=company_id,
            status=status,
            start_validation_errors=start_validation_errors,
            archived=archived,
            agreements_configuration=agreements_configuration,
            competencies_assessments_configuration=competencies_assessments_configuration,
            name=name,
            description=description,
            target_strategy=target_strategy,
            reviewer_strategies=reviewer_strategies,
            starts_at=starts_at,
            ends_at=ends_at,
            last_bulk_reminder=last_bulk_reminder,
        )

        performance_review_process.additional_properties = d
        return performance_review_process

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
