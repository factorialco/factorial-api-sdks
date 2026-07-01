from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_api_20260701_resources_performance_review_questionnaire_by_strategies_update_questionnaire_for_strategy_body_strategy import (
    PostApi20260701ResourcesPerformanceReviewQuestionnaireByStrategiesUpdateQuestionnaireForStrategyBodyStrategy,
)

T = TypeVar(
    "T",
    bound="PostApi20260701ResourcesPerformanceReviewQuestionnaireByStrategiesUpdateQuestionnaireForStrategyBody",
)


@_attrs_define
class PostApi20260701ResourcesPerformanceReviewQuestionnaireByStrategiesUpdateQuestionnaireForStrategyBody:
    performance_review_process_id: str
    """ Review process ID """
    strategy: PostApi20260701ResourcesPerformanceReviewQuestionnaireByStrategiesUpdateQuestionnaireForStrategyBodyStrategy
    """ Reviewer strategy to update the questionnaire for """
    questionnaire_content: list[Any]
    """ List of grouped questions to be evaluated by the reviewer.
    ###### **What should each group object look like?**

      - `uuid`: Unique identifier for the group
      - `type`: Group type (`section` or `question`). If it's `section`, the questions will be grouped under a
    section with a given title
      - `section_title`: Title of the section (optional)
      - `questions`: List of questions

    ###### **What should each question object look like?**

      - `uuid`: Unique identifier for the question
      - `mandatory`: Whether the question is mandatory or not
      - `with_comment`: Whether the reviewer can add a comment or not
      - `title`: Question
      - `answer_type`: Answer type (`text`, `rating`, `number` or `multiple_choice`)
      - `max_choices`: Maximum number of choices. If `1`, it'll be a single choice question
      - `choice_options`: List of options for single and multiple choice questions """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        performance_review_process_id = self.performance_review_process_id

        strategy = self.strategy.value

        questionnaire_content = self.questionnaire_content

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "performance_review_process_id": performance_review_process_id,
                "strategy": strategy,
                "questionnaire_content": questionnaire_content,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        performance_review_process_id = d.pop("performance_review_process_id")

        strategy = PostApi20260701ResourcesPerformanceReviewQuestionnaireByStrategiesUpdateQuestionnaireForStrategyBodyStrategy(
            d.pop("strategy")
        )

        questionnaire_content = cast(list[Any], d.pop("questionnaire_content"))

        post_api_20260701_resources_performance_review_questionnaire_by_strategies_update_questionnaire_for_strategy_body = cls(
            performance_review_process_id=performance_review_process_id,
            strategy=strategy,
            questionnaire_content=questionnaire_content,
        )

        post_api_20260701_resources_performance_review_questionnaire_by_strategies_update_questionnaire_for_strategy_body.additional_properties = d
        return post_api_20260701_resources_performance_review_questionnaire_by_strategies_update_questionnaire_for_strategy_body

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
