from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.performance_review_evaluation_answer_answered_employee_potential_score_questionnaire_content_item_questions_item_answer_answer_rating import (
        PerformanceReviewEvaluationAnswerAnsweredEmployeePotentialScoreQuestionnaireContentItemQuestionsItemAnswerAnswerRating,
    )


T = TypeVar(
    "T",
    bound="PerformanceReviewEvaluationAnswerAnsweredEmployeePotentialScoreQuestionnaireContentItemQuestionsItemAnswer",
)


@_attrs_define
class PerformanceReviewEvaluationAnswerAnsweredEmployeePotentialScoreQuestionnaireContentItemQuestionsItemAnswer:
    uuid: str
    answer_text: str | Unset = UNSET
    answer_int: int | Unset = UNSET
    answer_float: float | Unset = UNSET
    answer_choice: list[str] | Unset = UNSET
    answer_rating: (
        PerformanceReviewEvaluationAnswerAnsweredEmployeePotentialScoreQuestionnaireContentItemQuestionsItemAnswerAnswerRating
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = self.uuid

        answer_text = self.answer_text

        answer_int = self.answer_int

        answer_float = self.answer_float

        answer_choice: list[str] | Unset = UNSET
        if not isinstance(self.answer_choice, Unset):
            answer_choice = self.answer_choice

        answer_rating: dict[str, Any] | Unset = UNSET
        if not isinstance(self.answer_rating, Unset):
            answer_rating = self.answer_rating.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
            }
        )
        if answer_text is not UNSET:
            field_dict["answer_text"] = answer_text
        if answer_int is not UNSET:
            field_dict["answer_int"] = answer_int
        if answer_float is not UNSET:
            field_dict["answer_float"] = answer_float
        if answer_choice is not UNSET:
            field_dict["answer_choice"] = answer_choice
        if answer_rating is not UNSET:
            field_dict["answer_rating"] = answer_rating

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.performance_review_evaluation_answer_answered_employee_potential_score_questionnaire_content_item_questions_item_answer_answer_rating import (
            PerformanceReviewEvaluationAnswerAnsweredEmployeePotentialScoreQuestionnaireContentItemQuestionsItemAnswerAnswerRating,
        )

        d = dict(src_dict)
        uuid = d.pop("uuid")

        answer_text = d.pop("answer_text", UNSET)

        answer_int = d.pop("answer_int", UNSET)

        answer_float = d.pop("answer_float", UNSET)

        answer_choice = cast(list[str], d.pop("answer_choice", UNSET))

        _answer_rating = d.pop("answer_rating", UNSET)
        answer_rating: (
            PerformanceReviewEvaluationAnswerAnsweredEmployeePotentialScoreQuestionnaireContentItemQuestionsItemAnswerAnswerRating
            | Unset
        )
        if isinstance(_answer_rating, Unset):
            answer_rating = UNSET
        else:
            answer_rating = PerformanceReviewEvaluationAnswerAnsweredEmployeePotentialScoreQuestionnaireContentItemQuestionsItemAnswerAnswerRating.from_dict(
                _answer_rating
            )

        performance_review_evaluation_answer_answered_employee_potential_score_questionnaire_content_item_questions_item_answer = cls(
            uuid=uuid,
            answer_text=answer_text,
            answer_int=answer_int,
            answer_float=answer_float,
            answer_choice=answer_choice,
            answer_rating=answer_rating,
        )

        performance_review_evaluation_answer_answered_employee_potential_score_questionnaire_content_item_questions_item_answer.additional_properties = d
        return performance_review_evaluation_answer_answered_employee_potential_score_questionnaire_content_item_questions_item_answer

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
