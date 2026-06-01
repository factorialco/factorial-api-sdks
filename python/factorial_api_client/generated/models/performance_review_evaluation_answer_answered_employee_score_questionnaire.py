from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PerformanceReviewEvaluationAnswerAnsweredEmployeeScoreQuestionnaire")


@_attrs_define
class PerformanceReviewEvaluationAnswerAnsweredEmployeeScoreQuestionnaire:
    """Questionnaire for getting employee score.

    Example:
        {'content': [{'uuid': 'b69c9b4d-0aa6-4ada-89d5-5fdcb04c1327', 'type': 'section', 'section_title': 'Overall
            performance', 'questions': [{'question': {'uuid': 'a347a2fd-1a0a-4eee-b6c8-f74be63624fb', 'mandatory': True,
            'with_comment': True, 'title': 'How would you rate the evarall performance of the employee?', 'answer_type':
            'rating', 'scale': [{'value': 1, 'text': 'Unsatisfactory'}, {'value': 2, 'text': 'Needs Improvement'}, {'value':
            3, 'text': 'Meets Expectations'}, {'value': 4, 'text': 'Exceeds Expectations'}, {'value': 5, 'text':
            'Outstanding'}]}, 'answer': {'uuid': 'a347a2fd-1a0a-4eee-b6c8-f74be63625fb', 'answer_text': 'Example answer',
            'answer_int': 10, 'answer_float': 10.5, 'answer_choice': ['Yes'], 'answer_rating': {'value': 3, 'comment': 'The
            employee is doing well.'}}}]}]}

    """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        performance_review_evaluation_answer_answered_employee_score_questionnaire = cls()

        performance_review_evaluation_answer_answered_employee_score_questionnaire.additional_properties = d
        return performance_review_evaluation_answer_answered_employee_score_questionnaire

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
