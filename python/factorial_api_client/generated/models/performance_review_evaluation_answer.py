from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.performance_review_evaluation_answer_answered_employee_potential_score_questionnaire import (
        PerformanceReviewEvaluationAnswerAnsweredEmployeePotentialScoreQuestionnaire,
    )
    from ..models.performance_review_evaluation_answer_answered_employee_score_questionnaire import (
        PerformanceReviewEvaluationAnswerAnsweredEmployeeScoreQuestionnaire,
    )
    from ..models.performance_review_evaluation_answer_answered_questionnaire_with_sections import (
        PerformanceReviewEvaluationAnswerAnsweredQuestionnaireWithSections,
    )


T = TypeVar("T", bound="PerformanceReviewEvaluationAnswer")


@_attrs_define
class PerformanceReviewEvaluationAnswer:
    id: str
    """ Review evaluation ID """
    performance_review_evaluation_id: str
    """ Review evaluation ID """
    answered_questionnaire_with_sections: (
        PerformanceReviewEvaluationAnswerAnsweredQuestionnaireWithSections
    )
    """ List of questions and their respective answers grouped by section. """
    answered_employee_score_questionnaire: (
        PerformanceReviewEvaluationAnswerAnsweredEmployeeScoreQuestionnaire | Unset
    ) = UNSET
    """ Questionnaire for getting employee score. """
    answered_employee_potential_score_questionnaire: (
        PerformanceReviewEvaluationAnswerAnsweredEmployeePotentialScoreQuestionnaire | Unset
    ) = UNSET
    """ Questionnaire for getting the employee potential score. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        performance_review_evaluation_id = self.performance_review_evaluation_id

        answered_questionnaire_with_sections = self.answered_questionnaire_with_sections.to_dict()

        answered_employee_score_questionnaire: dict[str, Any] | Unset = UNSET
        if not isinstance(self.answered_employee_score_questionnaire, Unset):
            answered_employee_score_questionnaire = (
                self.answered_employee_score_questionnaire.to_dict()
            )

        answered_employee_potential_score_questionnaire: dict[str, Any] | Unset = UNSET
        if not isinstance(self.answered_employee_potential_score_questionnaire, Unset):
            answered_employee_potential_score_questionnaire = (
                self.answered_employee_potential_score_questionnaire.to_dict()
            )

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "performance_review_evaluation_id": performance_review_evaluation_id,
                "answered_questionnaire_with_sections": answered_questionnaire_with_sections,
            }
        )
        if answered_employee_score_questionnaire is not UNSET:
            field_dict["answered_employee_score_questionnaire"] = (
                answered_employee_score_questionnaire
            )
        if answered_employee_potential_score_questionnaire is not UNSET:
            field_dict["answered_employee_potential_score_questionnaire"] = (
                answered_employee_potential_score_questionnaire
            )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.performance_review_evaluation_answer_answered_employee_potential_score_questionnaire import (
            PerformanceReviewEvaluationAnswerAnsweredEmployeePotentialScoreQuestionnaire,
        )
        from ..models.performance_review_evaluation_answer_answered_employee_score_questionnaire import (
            PerformanceReviewEvaluationAnswerAnsweredEmployeeScoreQuestionnaire,
        )
        from ..models.performance_review_evaluation_answer_answered_questionnaire_with_sections import (
            PerformanceReviewEvaluationAnswerAnsweredQuestionnaireWithSections,
        )

        d = dict(src_dict)
        id = d.pop("id")

        performance_review_evaluation_id = d.pop("performance_review_evaluation_id")

        answered_questionnaire_with_sections = (
            PerformanceReviewEvaluationAnswerAnsweredQuestionnaireWithSections.from_dict(
                d.pop("answered_questionnaire_with_sections")
            )
        )

        _answered_employee_score_questionnaire = d.pop(
            "answered_employee_score_questionnaire", UNSET
        )
        answered_employee_score_questionnaire: (
            PerformanceReviewEvaluationAnswerAnsweredEmployeeScoreQuestionnaire | Unset
        )
        if isinstance(_answered_employee_score_questionnaire, Unset):
            answered_employee_score_questionnaire = UNSET
        else:
            answered_employee_score_questionnaire = (
                PerformanceReviewEvaluationAnswerAnsweredEmployeeScoreQuestionnaire.from_dict(
                    _answered_employee_score_questionnaire
                )
            )

        _answered_employee_potential_score_questionnaire = d.pop(
            "answered_employee_potential_score_questionnaire", UNSET
        )
        answered_employee_potential_score_questionnaire: (
            PerformanceReviewEvaluationAnswerAnsweredEmployeePotentialScoreQuestionnaire | Unset
        )
        if isinstance(_answered_employee_potential_score_questionnaire, Unset):
            answered_employee_potential_score_questionnaire = UNSET
        else:
            answered_employee_potential_score_questionnaire = PerformanceReviewEvaluationAnswerAnsweredEmployeePotentialScoreQuestionnaire.from_dict(
                _answered_employee_potential_score_questionnaire
            )

        performance_review_evaluation_answer = cls(
            id=id,
            performance_review_evaluation_id=performance_review_evaluation_id,
            answered_questionnaire_with_sections=answered_questionnaire_with_sections,
            answered_employee_score_questionnaire=answered_employee_score_questionnaire,
            answered_employee_potential_score_questionnaire=answered_employee_potential_score_questionnaire,
        )

        performance_review_evaluation_answer.additional_properties = d
        return performance_review_evaluation_answer

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
