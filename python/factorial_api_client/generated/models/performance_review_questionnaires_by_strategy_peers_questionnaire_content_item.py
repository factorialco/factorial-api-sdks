from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.performance_review_questionnaires_by_strategy_peers_questionnaire_content_item_type import (
    PerformanceReviewQuestionnairesByStrategyPeersQuestionnaireContentItemType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.performance_review_questionnaires_by_strategy_peers_questionnaire_content_item_questions_item import (
        PerformanceReviewQuestionnairesByStrategyPeersQuestionnaireContentItemQuestionsItem,
    )


T = TypeVar("T", bound="PerformanceReviewQuestionnairesByStrategyPeersQuestionnaireContentItem")


@_attrs_define
class PerformanceReviewQuestionnairesByStrategyPeersQuestionnaireContentItem:
    uuid: str
    type_: PerformanceReviewQuestionnairesByStrategyPeersQuestionnaireContentItemType
    questions: list[
        PerformanceReviewQuestionnairesByStrategyPeersQuestionnaireContentItemQuestionsItem
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
        from ..models.performance_review_questionnaires_by_strategy_peers_questionnaire_content_item_questions_item import (
            PerformanceReviewQuestionnairesByStrategyPeersQuestionnaireContentItemQuestionsItem,
        )

        d = dict(src_dict)
        uuid = d.pop("uuid")

        type_ = PerformanceReviewQuestionnairesByStrategyPeersQuestionnaireContentItemType(
            d.pop("type")
        )

        questions = []
        _questions = d.pop("questions")
        for questions_item_data in _questions:
            questions_item = PerformanceReviewQuestionnairesByStrategyPeersQuestionnaireContentItemQuestionsItem.from_dict(
                questions_item_data
            )

            questions.append(questions_item)

        section_title = d.pop("section_title", UNSET)

        performance_review_questionnaires_by_strategy_peers_questionnaire_content_item = cls(
            uuid=uuid,
            type_=type_,
            questions=questions,
            section_title=section_title,
        )

        performance_review_questionnaires_by_strategy_peers_questionnaire_content_item.additional_properties = d
        return performance_review_questionnaires_by_strategy_peers_questionnaire_content_item

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
