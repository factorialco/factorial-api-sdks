from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PerformanceReviewQuestionnairesByStrategySelfQuestionnaire")


@_attrs_define
class PerformanceReviewQuestionnairesByStrategySelfQuestionnaire:
    """Questionnaire for self evaluation

    Example:
        {'reviewer_strategy': 'self', 'content': [{'uuid': '26f26623-043f-4110-a5cb-1fd54a69626f', 'type': 'question',
            'questions': [{'uuid': '84ba99f3-4e4f-4917-a2af-6d0aa8c2e0f2', 'mandatory': True, 'with_comment': False,
            'title': 'Do you think you are a team player?', 'answer_type': 'single_choice', 'choice_options': ['Yes',
            'No']}]}]}

    """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        performance_review_questionnaires_by_strategy_self_questionnaire = cls()

        performance_review_questionnaires_by_strategy_self_questionnaire.additional_properties = d
        return performance_review_questionnaires_by_strategy_self_questionnaire

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
