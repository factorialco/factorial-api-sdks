from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_api_20261001_resources_performance_review_questionnaire_by_strategies_update_questionnaire_for_strategy_body_questionnaire_content_item_type import (
    PostApi20261001ResourcesPerformanceReviewQuestionnaireByStrategiesUpdateQuestionnaireForStrategyBodyQuestionnaireContentItemType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_api_20261001_resources_performance_review_questionnaire_by_strategies_update_questionnaire_for_strategy_body_questionnaire_content_item_questions_item import (
        PostApi20261001ResourcesPerformanceReviewQuestionnaireByStrategiesUpdateQuestionnaireForStrategyBodyQuestionnaireContentItemQuestionsItem,
    )


T = TypeVar(
    "T",
    bound="PostApi20261001ResourcesPerformanceReviewQuestionnaireByStrategiesUpdateQuestionnaireForStrategyBodyQuestionnaireContentItem",
)


@_attrs_define
class PostApi20261001ResourcesPerformanceReviewQuestionnaireByStrategiesUpdateQuestionnaireForStrategyBodyQuestionnaireContentItem:
    uuid: str
    type_: PostApi20261001ResourcesPerformanceReviewQuestionnaireByStrategiesUpdateQuestionnaireForStrategyBodyQuestionnaireContentItemType
    questions: list[
        PostApi20261001ResourcesPerformanceReviewQuestionnaireByStrategiesUpdateQuestionnaireForStrategyBodyQuestionnaireContentItemQuestionsItem
    ]
    section_title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = self.uuid

        type_ = self.type_.value

        questions = []
        for questions_item_data in self.questions:
            questions_item = questions_item_data.to_dict()
            questions.append(questions_item)

        section_title = self.section_title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "type": type_,
                "questions": questions,
            }
        )
        if section_title is not UNSET:
            field_dict["section_title"] = section_title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_api_20261001_resources_performance_review_questionnaire_by_strategies_update_questionnaire_for_strategy_body_questionnaire_content_item_questions_item import (
            PostApi20261001ResourcesPerformanceReviewQuestionnaireByStrategiesUpdateQuestionnaireForStrategyBodyQuestionnaireContentItemQuestionsItem,
        )

        d = dict(src_dict)
        uuid = d.pop("uuid")

        type_ = PostApi20261001ResourcesPerformanceReviewQuestionnaireByStrategiesUpdateQuestionnaireForStrategyBodyQuestionnaireContentItemType(
            d.pop("type")
        )

        questions = []
        _questions = d.pop("questions")
        for questions_item_data in _questions:
            questions_item = PostApi20261001ResourcesPerformanceReviewQuestionnaireByStrategiesUpdateQuestionnaireForStrategyBodyQuestionnaireContentItemQuestionsItem.from_dict(
                questions_item_data
            )

            questions.append(questions_item)

        section_title = d.pop("section_title", UNSET)

        post_api_20261001_resources_performance_review_questionnaire_by_strategies_update_questionnaire_for_strategy_body_questionnaire_content_item = cls(
            uuid=uuid,
            type_=type_,
            questions=questions,
            section_title=section_title,
        )

        post_api_20261001_resources_performance_review_questionnaire_by_strategies_update_questionnaire_for_strategy_body_questionnaire_content_item.additional_properties = d
        return post_api_20261001_resources_performance_review_questionnaire_by_strategies_update_questionnaire_for_strategy_body_questionnaire_content_item

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
