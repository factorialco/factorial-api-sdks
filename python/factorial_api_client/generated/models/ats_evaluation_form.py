from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ats_evaluation_form_questions_item import AtsEvaluationFormQuestionsItem


T = TypeVar("T", bound="AtsEvaluationForm")


@_attrs_define
class AtsEvaluationForm:
    id: str
    """ Id of the evaluation form. """
    company_id: str
    """ Id of the company that the evaluation form belongs to. """
    name: str
    """ Name of the evaluation form. """
    questions: list[AtsEvaluationFormQuestionsItem]
    """ List of questions in the evaluation form. """
    created_at: str
    """ date and time when the evaluation form was created. """
    updated_at: str
    """ date and time when the evaluation form was last updated. """
    ats_job_posting_id: str | Unset = UNSET
    """ Id of the job posting that the evaluation form is associated with. """
    based_on_id: str | Unset = UNSET
    """ Id of the evaluation form that this evaluation form is related. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        company_id = self.company_id

        name = self.name

        questions = []
        for questions_item_data in self.questions:
            questions_item = questions_item_data.to_dict()
            questions.append(questions_item)

        created_at = self.created_at

        updated_at = self.updated_at

        ats_job_posting_id = self.ats_job_posting_id

        based_on_id = self.based_on_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "company_id": company_id,
                "name": name,
                "questions": questions,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if ats_job_posting_id is not UNSET:
            field_dict["ats_job_posting_id"] = ats_job_posting_id
        if based_on_id is not UNSET:
            field_dict["based_on_id"] = based_on_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ats_evaluation_form_questions_item import AtsEvaluationFormQuestionsItem

        d = dict(src_dict)
        id = d.pop("id")

        company_id = d.pop("company_id")

        name = d.pop("name")

        questions = []
        _questions = d.pop("questions")
        for questions_item_data in _questions:
            questions_item = AtsEvaluationFormQuestionsItem.from_dict(questions_item_data)

            questions.append(questions_item)

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        ats_job_posting_id = d.pop("ats_job_posting_id", UNSET)

        based_on_id = d.pop("based_on_id", UNSET)

        ats_evaluation_form = cls(
            id=id,
            company_id=company_id,
            name=name,
            questions=questions,
            created_at=created_at,
            updated_at=updated_at,
            ats_job_posting_id=ats_job_posting_id,
            based_on_id=based_on_id,
        )

        ats_evaluation_form.additional_properties = d
        return ats_evaluation_form

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
