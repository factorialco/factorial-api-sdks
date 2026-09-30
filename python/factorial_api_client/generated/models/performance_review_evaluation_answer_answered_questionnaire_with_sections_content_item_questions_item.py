from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.performance_review_evaluation_answer_answered_questionnaire_with_sections_content_item_questions_item_answer import (
        PerformanceReviewEvaluationAnswerAnsweredQuestionnaireWithSectionsContentItemQuestionsItemAnswer,
    )
    from ..models.performance_review_evaluation_answer_answered_questionnaire_with_sections_content_item_questions_item_question import (
        PerformanceReviewEvaluationAnswerAnsweredQuestionnaireWithSectionsContentItemQuestionsItemQuestion,
    )


T = TypeVar(
    "T",
    bound="PerformanceReviewEvaluationAnswerAnsweredQuestionnaireWithSectionsContentItemQuestionsItem",
)


@_attrs_define
class PerformanceReviewEvaluationAnswerAnsweredQuestionnaireWithSectionsContentItemQuestionsItem:
    question: PerformanceReviewEvaluationAnswerAnsweredQuestionnaireWithSectionsContentItemQuestionsItemQuestion
    answer: (
        PerformanceReviewEvaluationAnswerAnsweredQuestionnaireWithSectionsContentItemQuestionsItemAnswer
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        question = self.question.to_dict()

        answer: dict[str, Any] | Unset = UNSET
        if not isinstance(self.answer, Unset):
            answer = self.answer.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "question": question,
            }
        )
        if answer is not UNSET:
            field_dict["answer"] = answer

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.performance_review_evaluation_answer_answered_questionnaire_with_sections_content_item_questions_item_answer import (
            PerformanceReviewEvaluationAnswerAnsweredQuestionnaireWithSectionsContentItemQuestionsItemAnswer,
        )
        from ..models.performance_review_evaluation_answer_answered_questionnaire_with_sections_content_item_questions_item_question import (
            PerformanceReviewEvaluationAnswerAnsweredQuestionnaireWithSectionsContentItemQuestionsItemQuestion,
        )

        d = dict(src_dict)
        question = PerformanceReviewEvaluationAnswerAnsweredQuestionnaireWithSectionsContentItemQuestionsItemQuestion.from_dict(
            d.pop("question")
        )

        _answer = d.pop("answer", UNSET)
        answer: (
            PerformanceReviewEvaluationAnswerAnsweredQuestionnaireWithSectionsContentItemQuestionsItemAnswer
            | Unset
        )
        if isinstance(_answer, Unset):
            answer = UNSET
        else:
            answer = PerformanceReviewEvaluationAnswerAnsweredQuestionnaireWithSectionsContentItemQuestionsItemAnswer.from_dict(
                _answer
            )

        performance_review_evaluation_answer_answered_questionnaire_with_sections_content_item_questions_item = cls(
            question=question,
            answer=answer,
        )

        performance_review_evaluation_answer_answered_questionnaire_with_sections_content_item_questions_item.additional_properties = d
        return performance_review_evaluation_answer_answered_questionnaire_with_sections_content_item_questions_item

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
