from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20260401ResourcesAtsFeedbacksBody")


@_attrs_define
class PostApi20260401ResourcesAtsFeedbacksBody:
    ats_candidate_id: int
    """ the ID of the candidate to whom the new feedback will be associated. """
    rating: int | Unset = UNSET
    """ the overall rating from 1 to 5 to be given to the candidate's application. """
    ats_application_id: int | Unset = UNSET
    """ the ID of the application related to the feedback. """
    ats_application_phase_id: int | Unset = UNSET
    """ the ID of the phase within the application related to the feedback. """
    description: str | Unset = UNSET
    """ a string describing the feedback provided. """
    mention_ids: list[int] | Unset = UNSET
    """ the IDs of the accesses for sending notifications if they have it enabled. They must have permissions to see
    the assosiated application. """
    ats_evaluation_forms_id: int | Unset = UNSET
    """ IDs of the form to which the feedback belongs if the evaluation forms feature is active. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ats_candidate_id = self.ats_candidate_id

        rating = self.rating

        ats_application_id = self.ats_application_id

        ats_application_phase_id = self.ats_application_phase_id

        description = self.description

        mention_ids: list[int] | Unset = UNSET
        if not isinstance(self.mention_ids, Unset):
            mention_ids = self.mention_ids

        ats_evaluation_forms_id = self.ats_evaluation_forms_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ats_candidate_id": ats_candidate_id,
            }
        )
        if rating is not UNSET:
            field_dict["rating"] = rating
        if ats_application_id is not UNSET:
            field_dict["ats_application_id"] = ats_application_id
        if ats_application_phase_id is not UNSET:
            field_dict["ats_application_phase_id"] = ats_application_phase_id
        if description is not UNSET:
            field_dict["description"] = description
        if mention_ids is not UNSET:
            field_dict["mention_ids"] = mention_ids
        if ats_evaluation_forms_id is not UNSET:
            field_dict["ats_evaluation_forms_id"] = ats_evaluation_forms_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ats_candidate_id = d.pop("ats_candidate_id")

        rating = d.pop("rating", UNSET)

        ats_application_id = d.pop("ats_application_id", UNSET)

        ats_application_phase_id = d.pop("ats_application_phase_id", UNSET)

        description = d.pop("description", UNSET)

        mention_ids = cast(list[int], d.pop("mention_ids", UNSET))

        ats_evaluation_forms_id = d.pop("ats_evaluation_forms_id", UNSET)

        post_api_20260401_resources_ats_feedbacks_body = cls(
            ats_candidate_id=ats_candidate_id,
            rating=rating,
            ats_application_id=ats_application_id,
            ats_application_phase_id=ats_application_phase_id,
            description=description,
            mention_ids=mention_ids,
            ats_evaluation_forms_id=ats_evaluation_forms_id,
        )

        post_api_20260401_resources_ats_feedbacks_body.additional_properties = d
        return post_api_20260401_resources_ats_feedbacks_body

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
