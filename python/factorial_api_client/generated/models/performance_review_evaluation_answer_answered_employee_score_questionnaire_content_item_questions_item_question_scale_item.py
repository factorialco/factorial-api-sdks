from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar(
    "T",
    bound="PerformanceReviewEvaluationAnswerAnsweredEmployeeScoreQuestionnaireContentItemQuestionsItemQuestionScaleItem",
)


@_attrs_define
class PerformanceReviewEvaluationAnswerAnsweredEmployeeScoreQuestionnaireContentItemQuestionsItemQuestionScaleItem:
    value: int
    text: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        text = self.text

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "value": value,
                "text": text,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        value = d.pop("value")

        text = d.pop("text")

        performance_review_evaluation_answer_answered_employee_score_questionnaire_content_item_questions_item_question_scale_item = cls(
            value=value,
            text=text,
        )

        performance_review_evaluation_answer_answered_employee_score_questionnaire_content_item_questions_item_question_scale_item.additional_properties = d
        return performance_review_evaluation_answer_answered_employee_score_questionnaire_content_item_questions_item_question_scale_item

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
