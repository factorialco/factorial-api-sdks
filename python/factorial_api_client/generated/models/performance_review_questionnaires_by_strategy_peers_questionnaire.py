from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.performance_review_questionnaires_by_strategy_peers_questionnaire_reviewer_strategy import (
    PerformanceReviewQuestionnairesByStrategyPeersQuestionnaireReviewerStrategy,
)

if TYPE_CHECKING:
    from ..models.performance_review_questionnaires_by_strategy_peers_questionnaire_content_item import (
        PerformanceReviewQuestionnairesByStrategyPeersQuestionnaireContentItem,
    )


T = TypeVar("T", bound="PerformanceReviewQuestionnairesByStrategyPeersQuestionnaire")


@_attrs_define
class PerformanceReviewQuestionnairesByStrategyPeersQuestionnaire:
    """Questionnaire for peers evaluation"""

    reviewer_strategy: PerformanceReviewQuestionnairesByStrategyPeersQuestionnaireReviewerStrategy
    content: list[PerformanceReviewQuestionnairesByStrategyPeersQuestionnaireContentItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reviewer_strategy = self.reviewer_strategy.value

        content = []
        for content_item_data in self.content:
            content_item = content_item_data.to_dict()
            content.append(content_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reviewer_strategy": reviewer_strategy,
                "content": content,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.performance_review_questionnaires_by_strategy_peers_questionnaire_content_item import (
            PerformanceReviewQuestionnairesByStrategyPeersQuestionnaireContentItem,
        )

        d = dict(src_dict)
        reviewer_strategy = (
            PerformanceReviewQuestionnairesByStrategyPeersQuestionnaireReviewerStrategy(
                d.pop("reviewer_strategy")
            )
        )

        content = []
        _content = d.pop("content")
        for content_item_data in _content:
            content_item = (
                PerformanceReviewQuestionnairesByStrategyPeersQuestionnaireContentItem.from_dict(
                    content_item_data
                )
            )

            content.append(content_item)

        performance_review_questionnaires_by_strategy_peers_questionnaire = cls(
            reviewer_strategy=reviewer_strategy,
            content=content,
        )

        performance_review_questionnaires_by_strategy_peers_questionnaire.additional_properties = d
        return performance_review_questionnaires_by_strategy_peers_questionnaire

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
