from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_api_20251001_resources_ats_answers_body_original_question_type import (
    PostApi20251001ResourcesAtsAnswersBodyOriginalQuestionType,
)

T = TypeVar("T", bound="PostApi20251001ResourcesAtsAnswersBody")


@_attrs_define
class PostApi20251001ResourcesAtsAnswersBody:
    ats_question_id: int
    """ Identifier of the question """
    ats_application_id: int
    """ Identifier of the application """
    value: str
    """ Value of the answer """
    original_question_label: str
    """ Label of the question """
    original_question_type: PostApi20251001ResourcesAtsAnswersBodyOriginalQuestionType
    """ Type of the question """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ats_question_id = self.ats_question_id

        ats_application_id = self.ats_application_id

        value = self.value

        original_question_label = self.original_question_label

        original_question_type = self.original_question_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ats_question_id": ats_question_id,
                "ats_application_id": ats_application_id,
                "value": value,
                "original_question_label": original_question_label,
                "original_question_type": original_question_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ats_question_id = d.pop("ats_question_id")

        ats_application_id = d.pop("ats_application_id")

        value = d.pop("value")

        original_question_label = d.pop("original_question_label")

        original_question_type = PostApi20251001ResourcesAtsAnswersBodyOriginalQuestionType(
            d.pop("original_question_type")
        )

        post_api_20251001_resources_ats_answers_body = cls(
            ats_question_id=ats_question_id,
            ats_application_id=ats_application_id,
            value=value,
            original_question_label=original_question_label,
            original_question_type=original_question_type,
        )

        post_api_20251001_resources_ats_answers_body.additional_properties = d
        return post_api_20251001_resources_ats_answers_body

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
