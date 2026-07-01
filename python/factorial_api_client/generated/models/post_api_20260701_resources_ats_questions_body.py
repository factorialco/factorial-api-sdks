from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_api_20260701_resources_ats_questions_body_question_type import (
    PostApi20260701ResourcesAtsQuestionsBodyQuestionType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20260701ResourcesAtsQuestionsBody")


@_attrs_define
class PostApi20260701ResourcesAtsQuestionsBody:
    ats_job_posting_id: str
    """ job posting identifier. """
    company_id: str
    """ company identifier, refers to /core/me endpoint. """
    label: str
    """ text of the question. """
    position: int
    """ position of the question in the list. """
    question_type: PostApi20260701ResourcesAtsQuestionsBodyQuestionType
    """ type of the question. """
    mandatory: bool | Unset = UNSET
    """ is the question mandatory or not """
    auto_disqualify: bool | Unset = UNSET
    """ if the question autodisqualifies the candidate depending on it's response. """
    options: list[Any] | Unset = UNSET
    """ options for the question. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ats_job_posting_id = self.ats_job_posting_id

        company_id = self.company_id

        label = self.label

        position = self.position

        question_type = self.question_type.value

        mandatory = self.mandatory

        auto_disqualify = self.auto_disqualify

        options: list[Any] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = self.options

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ats_job_posting_id": ats_job_posting_id,
                "company_id": company_id,
                "label": label,
                "position": position,
                "question_type": question_type,
            }
        )
        if mandatory is not UNSET:
            field_dict["mandatory"] = mandatory
        if auto_disqualify is not UNSET:
            field_dict["auto_disqualify"] = auto_disqualify
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ats_job_posting_id = d.pop("ats_job_posting_id")

        company_id = d.pop("company_id")

        label = d.pop("label")

        position = d.pop("position")

        question_type = PostApi20260701ResourcesAtsQuestionsBodyQuestionType(d.pop("question_type"))

        mandatory = d.pop("mandatory", UNSET)

        auto_disqualify = d.pop("auto_disqualify", UNSET)

        options = cast(list[Any], d.pop("options", UNSET))

        post_api_20260701_resources_ats_questions_body = cls(
            ats_job_posting_id=ats_job_posting_id,
            company_id=company_id,
            label=label,
            position=position,
            question_type=question_type,
            mandatory=mandatory,
            auto_disqualify=auto_disqualify,
            options=options,
        )

        post_api_20260701_resources_ats_questions_body.additional_properties = d
        return post_api_20260701_resources_ats_questions_body

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
