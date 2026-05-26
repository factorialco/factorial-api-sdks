from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.performance_review_process_custom_template_reviewer_strategies import (
    PerformanceReviewProcessCustomTemplateReviewerStrategies,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.performance_review_process_custom_template_target_strategy import (
        PerformanceReviewProcessCustomTemplateTargetStrategy,
    )
    from ..models.performance_review_process_custom_template_visibility_settings import (
        PerformanceReviewProcessCustomTemplateVisibilitySettings,
    )


T = TypeVar("T", bound="PerformanceReviewProcessCustomTemplate")


@_attrs_define
class PerformanceReviewProcessCustomTemplate:
    id: int
    """ Review process template ID """
    company_id: int
    """ Company ID """
    name: str
    """ Review process name """
    created_at: str
    """ Creation date of the template """
    author_id: int | Unset = UNSET
    """ Author of the custom template. """
    description: str | Unset = UNSET
    """ A brief description of the review process """
    template_description: str | Unset = UNSET
    """ A brief description of the review process template """
    target_strategy: PerformanceReviewProcessCustomTemplateTargetStrategy | Unset = UNSET
    """ Condition that defines the employees that will be evaluated (participants). Calculated when the review
    process starts """
    reviewer_strategies: PerformanceReviewProcessCustomTemplateReviewerStrategies | Unset = UNSET
    """ Review types that will be assigned to the review process. It'll be used to create the evaluations when the
    process starts """
    agreements_enabled: bool | Unset = UNSET
    """ Action plans help track goal progress, and facilitate performance review discussions. """
    employee_potential_score_enabled: bool | Unset = UNSET
    """ Include one question at the end of the review to rate participants' potential. This rating will be reflected
    in the 9 box grid. """
    competencies_assessments_enabled: bool | Unset = UNSET
    """ Assess employees based on their assigned competencies through both manager and self-reviews. Ensure roles
    with designated competencies are properly set up. """
    visibility_settings: PerformanceReviewProcessCustomTemplateVisibilitySettings | Unset = UNSET
    """ Visibility settings for the custom template """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        company_id = self.company_id

        name = self.name

        created_at = self.created_at

        author_id = self.author_id

        description = self.description

        template_description = self.template_description

        target_strategy: dict[str, Any] | Unset = UNSET
        if not isinstance(self.target_strategy, Unset):
            target_strategy = self.target_strategy.to_dict()

        reviewer_strategies: str | Unset = UNSET
        if not isinstance(self.reviewer_strategies, Unset):
            reviewer_strategies = self.reviewer_strategies.value

        agreements_enabled = self.agreements_enabled

        employee_potential_score_enabled = self.employee_potential_score_enabled

        competencies_assessments_enabled = self.competencies_assessments_enabled

        visibility_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.visibility_settings, Unset):
            visibility_settings = self.visibility_settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "company_id": company_id,
                "name": name,
                "created_at": created_at,
            }
        )
        if author_id is not UNSET:
            field_dict["author_id"] = author_id
        if description is not UNSET:
            field_dict["description"] = description
        if template_description is not UNSET:
            field_dict["template_description"] = template_description
        if target_strategy is not UNSET:
            field_dict["target_strategy"] = target_strategy
        if reviewer_strategies is not UNSET:
            field_dict["reviewer_strategies"] = reviewer_strategies
        if agreements_enabled is not UNSET:
            field_dict["agreements_enabled"] = agreements_enabled
        if employee_potential_score_enabled is not UNSET:
            field_dict["employee_potential_score_enabled"] = employee_potential_score_enabled
        if competencies_assessments_enabled is not UNSET:
            field_dict["competencies_assessments_enabled"] = competencies_assessments_enabled
        if visibility_settings is not UNSET:
            field_dict["visibility_settings"] = visibility_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.performance_review_process_custom_template_target_strategy import (
            PerformanceReviewProcessCustomTemplateTargetStrategy,
        )
        from ..models.performance_review_process_custom_template_visibility_settings import (
            PerformanceReviewProcessCustomTemplateVisibilitySettings,
        )

        d = dict(src_dict)
        id = d.pop("id")

        company_id = d.pop("company_id")

        name = d.pop("name")

        created_at = d.pop("created_at")

        author_id = d.pop("author_id", UNSET)

        description = d.pop("description", UNSET)

        template_description = d.pop("template_description", UNSET)

        _target_strategy = d.pop("target_strategy", UNSET)
        target_strategy: PerformanceReviewProcessCustomTemplateTargetStrategy | Unset
        if isinstance(_target_strategy, Unset):
            target_strategy = UNSET
        else:
            target_strategy = PerformanceReviewProcessCustomTemplateTargetStrategy.from_dict(
                _target_strategy
            )

        _reviewer_strategies = d.pop("reviewer_strategies", UNSET)
        reviewer_strategies: PerformanceReviewProcessCustomTemplateReviewerStrategies | Unset
        if isinstance(_reviewer_strategies, Unset):
            reviewer_strategies = UNSET
        else:
            reviewer_strategies = PerformanceReviewProcessCustomTemplateReviewerStrategies(
                _reviewer_strategies
            )

        agreements_enabled = d.pop("agreements_enabled", UNSET)

        employee_potential_score_enabled = d.pop("employee_potential_score_enabled", UNSET)

        competencies_assessments_enabled = d.pop("competencies_assessments_enabled", UNSET)

        _visibility_settings = d.pop("visibility_settings", UNSET)
        visibility_settings: PerformanceReviewProcessCustomTemplateVisibilitySettings | Unset
        if isinstance(_visibility_settings, Unset):
            visibility_settings = UNSET
        else:
            visibility_settings = (
                PerformanceReviewProcessCustomTemplateVisibilitySettings.from_dict(
                    _visibility_settings
                )
            )

        performance_review_process_custom_template = cls(
            id=id,
            company_id=company_id,
            name=name,
            created_at=created_at,
            author_id=author_id,
            description=description,
            template_description=template_description,
            target_strategy=target_strategy,
            reviewer_strategies=reviewer_strategies,
            agreements_enabled=agreements_enabled,
            employee_potential_score_enabled=employee_potential_score_enabled,
            competencies_assessments_enabled=competencies_assessments_enabled,
            visibility_settings=visibility_settings,
        )

        performance_review_process_custom_template.additional_properties = d
        return performance_review_process_custom_template

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
