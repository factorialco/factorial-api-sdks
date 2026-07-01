from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ats_question_question_type import AtsQuestionQuestionType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AtsQuestion")


@_attrs_define
class AtsQuestion:
    id: str
    """ question identifier """
    ats_job_posting_id: str
    """ job posting identifier. """
    label: str
    """ text of the question. """
    position: int
    """ position of the question in the list. """
    mandatory: bool
    """ is the question mandatory or not """
    auto_disqualify: bool
    """ if the question autodisqualifies the candidate depending on it's response. """
    question_type: AtsQuestionQuestionType
    """ type of the question. """
    created_at: str
    """ creation date """
    updated_at: str
    """ last update date """
    options: list[Any] | Unset = UNSET
    """ options for the question. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        ats_job_posting_id = self.ats_job_posting_id

        label = self.label

        position = self.position

        mandatory = self.mandatory

        auto_disqualify = self.auto_disqualify

        question_type = self.question_type.value

        created_at = self.created_at

        updated_at = self.updated_at

        options: list[Any] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = self.options

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "ats_job_posting_id": ats_job_posting_id,
                "label": label,
                "position": position,
                "mandatory": mandatory,
                "auto_disqualify": auto_disqualify,
                "question_type": question_type,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        ats_job_posting_id = d.pop("ats_job_posting_id")

        label = d.pop("label")

        position = d.pop("position")

        mandatory = d.pop("mandatory")

        auto_disqualify = d.pop("auto_disqualify")

        question_type = AtsQuestionQuestionType(d.pop("question_type"))

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        options = cast(list[Any], d.pop("options", UNSET))

        ats_question = cls(
            id=id,
            ats_job_posting_id=ats_job_posting_id,
            label=label,
            position=position,
            mandatory=mandatory,
            auto_disqualify=auto_disqualify,
            question_type=question_type,
            created_at=created_at,
            updated_at=updated_at,
            options=options,
        )

        ats_question.additional_properties = d
        return ats_question

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
