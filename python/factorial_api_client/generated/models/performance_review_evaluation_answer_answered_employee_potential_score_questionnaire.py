from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.performance_review_evaluation_answer_answered_employee_potential_score_questionnaire_content_item import (
        PerformanceReviewEvaluationAnswerAnsweredEmployeePotentialScoreQuestionnaireContentItem,
    )


T = TypeVar(
    "T", bound="PerformanceReviewEvaluationAnswerAnsweredEmployeePotentialScoreQuestionnaire"
)


@_attrs_define
class PerformanceReviewEvaluationAnswerAnsweredEmployeePotentialScoreQuestionnaire:
    """Questionnaire for getting the employee potential score."""

    content: list[
        PerformanceReviewEvaluationAnswerAnsweredEmployeePotentialScoreQuestionnaireContentItem
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content = []
        for content_item_data in self.content:
            content_item = content_item_data.to_dict()
            content.append(content_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content": content,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.performance_review_evaluation_answer_answered_employee_potential_score_questionnaire_content_item import (
            PerformanceReviewEvaluationAnswerAnsweredEmployeePotentialScoreQuestionnaireContentItem,
        )

        d = dict(src_dict)
        content = []
        _content = d.pop("content")
        for content_item_data in _content:
            content_item = PerformanceReviewEvaluationAnswerAnsweredEmployeePotentialScoreQuestionnaireContentItem.from_dict(
                content_item_data
            )

            content.append(content_item)

        performance_review_evaluation_answer_answered_employee_potential_score_questionnaire = cls(
            content=content,
        )

        performance_review_evaluation_answer_answered_employee_potential_score_questionnaire.additional_properties = d
        return performance_review_evaluation_answer_answered_employee_potential_score_questionnaire

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
