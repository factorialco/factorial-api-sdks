from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ats_feedback_evaluation_form_answers_item import (
        AtsFeedbackEvaluationFormAnswersItem,
    )


T = TypeVar("T", bound="AtsFeedback")


@_attrs_define
class AtsFeedback:
    id: str
    """ the ID of the feedback entry. """
    created_at: str
    """ the date and time when the feedback entry was created. """
    ats_candidate_id: str
    """ the ID of the candidate to whom the feedback is associated. """
    rating: int | Unset = UNSET
    """ the overall rating from 1 to 5 for the candidate's application. """
    description: str | Unset = UNSET
    """ the description of the feedback provided. """
    ats_application_id: str | Unset = UNSET
    """ the ID of the application related to the feedback. """
    ats_application_phase_id: str | Unset = UNSET
    """ the ID of the phase within the application related to the feedback. """
    ats_evaluation_forms_id: str | Unset = UNSET
    """ the ID of the evaluation form to which the feedback belongs if the evaluation forms feature is active. """
    evaluation_form_answers: list[AtsFeedbackEvaluationFormAnswersItem] | Unset = UNSET
    """ the answers from the evaluation form, if this feedback is related to an evaluation form. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        created_at = self.created_at

        ats_candidate_id = self.ats_candidate_id

        rating = self.rating

        description = self.description

        ats_application_id = self.ats_application_id

        ats_application_phase_id = self.ats_application_phase_id

        ats_evaluation_forms_id = self.ats_evaluation_forms_id

        evaluation_form_answers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.evaluation_form_answers, Unset):
            evaluation_form_answers = []
            for evaluation_form_answers_item_data in self.evaluation_form_answers:
                evaluation_form_answers_item = evaluation_form_answers_item_data.to_dict()
                evaluation_form_answers.append(evaluation_form_answers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "created_at": created_at,
                "ats_candidate_id": ats_candidate_id,
            }
        )
        if rating is not UNSET:
            field_dict["rating"] = rating
        if description is not UNSET:
            field_dict["description"] = description
        if ats_application_id is not UNSET:
            field_dict["ats_application_id"] = ats_application_id
        if ats_application_phase_id is not UNSET:
            field_dict["ats_application_phase_id"] = ats_application_phase_id
        if ats_evaluation_forms_id is not UNSET:
            field_dict["ats_evaluation_forms_id"] = ats_evaluation_forms_id
        if evaluation_form_answers is not UNSET:
            field_dict["evaluation_form_answers"] = evaluation_form_answers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ats_feedback_evaluation_form_answers_item import (
            AtsFeedbackEvaluationFormAnswersItem,
        )

        d = dict(src_dict)
        id = d.pop("id")

        created_at = d.pop("created_at")

        ats_candidate_id = d.pop("ats_candidate_id")

        rating = d.pop("rating", UNSET)

        description = d.pop("description", UNSET)

        ats_application_id = d.pop("ats_application_id", UNSET)

        ats_application_phase_id = d.pop("ats_application_phase_id", UNSET)

        ats_evaluation_forms_id = d.pop("ats_evaluation_forms_id", UNSET)

        _evaluation_form_answers = d.pop("evaluation_form_answers", UNSET)
        evaluation_form_answers: list[AtsFeedbackEvaluationFormAnswersItem] | Unset = UNSET
        if _evaluation_form_answers is not UNSET:
            evaluation_form_answers = []
            for evaluation_form_answers_item_data in _evaluation_form_answers:
                evaluation_form_answers_item = AtsFeedbackEvaluationFormAnswersItem.from_dict(
                    evaluation_form_answers_item_data
                )

                evaluation_form_answers.append(evaluation_form_answers_item)

        ats_feedback = cls(
            id=id,
            created_at=created_at,
            ats_candidate_id=ats_candidate_id,
            rating=rating,
            description=description,
            ats_application_id=ats_application_id,
            ats_application_phase_id=ats_application_phase_id,
            ats_evaluation_forms_id=ats_evaluation_forms_id,
            evaluation_form_answers=evaluation_form_answers,
        )

        ats_feedback.additional_properties = d
        return ats_feedback

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
