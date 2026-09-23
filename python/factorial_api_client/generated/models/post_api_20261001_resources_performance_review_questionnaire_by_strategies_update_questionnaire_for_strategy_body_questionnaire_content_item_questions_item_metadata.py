from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar(
    "T",
    bound="PostApi20261001ResourcesPerformanceReviewQuestionnaireByStrategiesUpdateQuestionnaireForStrategyBodyQuestionnaireContentItemQuestionsItemMetadata",
)


@_attrs_define
class PostApi20261001ResourcesPerformanceReviewQuestionnaireByStrategiesUpdateQuestionnaireForStrategyBodyQuestionnaireContentItemQuestionsItemMetadata:
    competency_id: str | Unset = UNSET
    competency_level_id: str | Unset = UNSET
    competency_level_name: str | Unset = UNSET
    competency_level_description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        competency_id = self.competency_id

        competency_level_id = self.competency_level_id

        competency_level_name = self.competency_level_name

        competency_level_description = self.competency_level_description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if competency_id is not UNSET:
            field_dict["competency_id"] = competency_id
        if competency_level_id is not UNSET:
            field_dict["competency_level_id"] = competency_level_id
        if competency_level_name is not UNSET:
            field_dict["competency_level_name"] = competency_level_name
        if competency_level_description is not UNSET:
            field_dict["competency_level_description"] = competency_level_description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        competency_id = d.pop("competency_id", UNSET)

        competency_level_id = d.pop("competency_level_id", UNSET)

        competency_level_name = d.pop("competency_level_name", UNSET)

        competency_level_description = d.pop("competency_level_description", UNSET)

        post_api_20261001_resources_performance_review_questionnaire_by_strategies_update_questionnaire_for_strategy_body_questionnaire_content_item_questions_item_metadata = cls(
            competency_id=competency_id,
            competency_level_id=competency_level_id,
            competency_level_name=competency_level_name,
            competency_level_description=competency_level_description,
        )

        post_api_20261001_resources_performance_review_questionnaire_by_strategies_update_questionnaire_for_strategy_body_questionnaire_content_item_questions_item_metadata.additional_properties = d
        return post_api_20261001_resources_performance_review_questionnaire_by_strategies_update_questionnaire_for_strategy_body_questionnaire_content_item_questions_item_metadata

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
