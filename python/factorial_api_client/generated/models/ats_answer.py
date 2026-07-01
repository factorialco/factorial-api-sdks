from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ats_answer_original_question_type import AtsAnswerOriginalQuestionType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AtsAnswer")


@_attrs_define
class AtsAnswer:
    id: str
    """ Identifier of the answer """
    ats_application_id: str
    """ Identifier of the application """
    original_question_label: str
    """ Question label of the answer """
    original_question_type: AtsAnswerOriginalQuestionType
    """ Original type of the question """
    created_at: str
    """ Created date of the answer """
    updated_at: str
    """ Last updated date of the answer """
    ats_question_id: str | Unset = UNSET
    """ Identifier of the question """
    value: str | Unset = UNSET
    """ Value of the answer """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        ats_application_id = self.ats_application_id

        original_question_label = self.original_question_label

        original_question_type = self.original_question_type.value

        created_at = self.created_at

        updated_at = self.updated_at

        ats_question_id = self.ats_question_id

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "ats_application_id": ats_application_id,
                "original_question_label": original_question_label,
                "original_question_type": original_question_type,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if ats_question_id is not UNSET:
            field_dict["ats_question_id"] = ats_question_id
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        ats_application_id = d.pop("ats_application_id")

        original_question_label = d.pop("original_question_label")

        original_question_type = AtsAnswerOriginalQuestionType(d.pop("original_question_type"))

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        ats_question_id = d.pop("ats_question_id", UNSET)

        value = d.pop("value", UNSET)

        ats_answer = cls(
            id=id,
            ats_application_id=ats_application_id,
            original_question_label=original_question_label,
            original_question_type=original_question_type,
            created_at=created_at,
            updated_at=updated_at,
            ats_question_id=ats_question_id,
            value=value,
        )

        ats_answer.additional_properties = d
        return ats_answer

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
