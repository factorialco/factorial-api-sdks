from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.performance_review_questionnaires_by_strategy_employee_score_manager_questionnaire_content_item_questions_item_answer_type import (
    PerformanceReviewQuestionnairesByStrategyEmployeeScoreManagerQuestionnaireContentItemQuestionsItemAnswerType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.performance_review_questionnaires_by_strategy_employee_score_manager_questionnaire_content_item_questions_item_metadata import (
        PerformanceReviewQuestionnairesByStrategyEmployeeScoreManagerQuestionnaireContentItemQuestionsItemMetadata,
    )
    from ..models.performance_review_questionnaires_by_strategy_employee_score_manager_questionnaire_content_item_questions_item_scale_item import (
        PerformanceReviewQuestionnairesByStrategyEmployeeScoreManagerQuestionnaireContentItemQuestionsItemScaleItem,
    )


T = TypeVar(
    "T",
    bound="PerformanceReviewQuestionnairesByStrategyEmployeeScoreManagerQuestionnaireContentItemQuestionsItem",
)


@_attrs_define
class PerformanceReviewQuestionnairesByStrategyEmployeeScoreManagerQuestionnaireContentItemQuestionsItem:
    uuid: str
    mandatory: bool
    title: str
    answer_type: PerformanceReviewQuestionnairesByStrategyEmployeeScoreManagerQuestionnaireContentItemQuestionsItemAnswerType
    with_comment: bool | Unset = UNSET
    scale: (
        list[
            PerformanceReviewQuestionnairesByStrategyEmployeeScoreManagerQuestionnaireContentItemQuestionsItemScaleItem
        ]
        | Unset
    ) = UNSET
    max_choices: int | Unset = UNSET
    choice_options: list[str] | Unset = UNSET
    metadata: (
        PerformanceReviewQuestionnairesByStrategyEmployeeScoreManagerQuestionnaireContentItemQuestionsItemMetadata
        | Unset
    ) = UNSET
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = self.uuid

        mandatory = self.mandatory

        title = self.title

        answer_type = self.answer_type.value

        with_comment = self.with_comment

        scale: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.scale, Unset):
            scale = []
            for scale_item_data in self.scale:
                scale_item = scale_item_data.to_dict()
                scale.append(scale_item)

        max_choices = self.max_choices

        choice_options: list[str] | Unset = UNSET
        if not isinstance(self.choice_options, Unset):
            choice_options = self.choice_options

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "mandatory": mandatory,
                "title": title,
                "answer_type": answer_type,
            }
        )
        if with_comment is not UNSET:
            field_dict["with_comment"] = with_comment
        if scale is not UNSET:
            field_dict["scale"] = scale
        if max_choices is not UNSET:
            field_dict["max_choices"] = max_choices
        if choice_options is not UNSET:
            field_dict["choice_options"] = choice_options
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.performance_review_questionnaires_by_strategy_employee_score_manager_questionnaire_content_item_questions_item_metadata import (
            PerformanceReviewQuestionnairesByStrategyEmployeeScoreManagerQuestionnaireContentItemQuestionsItemMetadata,
        )
        from ..models.performance_review_questionnaires_by_strategy_employee_score_manager_questionnaire_content_item_questions_item_scale_item import (
            PerformanceReviewQuestionnairesByStrategyEmployeeScoreManagerQuestionnaireContentItemQuestionsItemScaleItem,
        )

        d = dict(src_dict)
        uuid = d.pop("uuid")

        mandatory = d.pop("mandatory")

        title = d.pop("title")

        answer_type = PerformanceReviewQuestionnairesByStrategyEmployeeScoreManagerQuestionnaireContentItemQuestionsItemAnswerType(
            d.pop("answer_type")
        )

        with_comment = d.pop("with_comment", UNSET)

        _scale = d.pop("scale", UNSET)
        scale: (
            list[
                PerformanceReviewQuestionnairesByStrategyEmployeeScoreManagerQuestionnaireContentItemQuestionsItemScaleItem
            ]
            | Unset
        ) = UNSET
        if _scale is not UNSET:
            scale = []
            for scale_item_data in _scale:
                scale_item = PerformanceReviewQuestionnairesByStrategyEmployeeScoreManagerQuestionnaireContentItemQuestionsItemScaleItem.from_dict(
                    scale_item_data
                )

                scale.append(scale_item)

        max_choices = d.pop("max_choices", UNSET)

        choice_options = cast(list[str], d.pop("choice_options", UNSET))

        _metadata = d.pop("metadata", UNSET)
        metadata: (
            PerformanceReviewQuestionnairesByStrategyEmployeeScoreManagerQuestionnaireContentItemQuestionsItemMetadata
            | Unset
        )
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = PerformanceReviewQuestionnairesByStrategyEmployeeScoreManagerQuestionnaireContentItemQuestionsItemMetadata.from_dict(
                _metadata
            )

        description = d.pop("description", UNSET)

        performance_review_questionnaires_by_strategy_employee_score_manager_questionnaire_content_item_questions_item = cls(
            uuid=uuid,
            mandatory=mandatory,
            title=title,
            answer_type=answer_type,
            with_comment=with_comment,
            scale=scale,
            max_choices=max_choices,
            choice_options=choice_options,
            metadata=metadata,
            description=description,
        )

        performance_review_questionnaires_by_strategy_employee_score_manager_questionnaire_content_item_questions_item.additional_properties = d
        return performance_review_questionnaires_by_strategy_employee_score_manager_questionnaire_content_item_questions_item

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
