from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PutApi20261001ResourcesAtsFeedbacksIdBody")


@_attrs_define
class PutApi20261001ResourcesAtsFeedbacksIdBody:
    id: str | Unset = UNSET
    """ the ID of the feedback entry to be updated. """
    rating: int | Unset = UNSET
    """ the overall rating from 1 to 5 for the candidate's application. """
    description: str | Unset = UNSET
    """ the description of the feedback provided. """
    ats_application_phase_id: str | Unset = UNSET
    """ the ID of the phase within the application related to the feedback. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        rating = self.rating

        description = self.description

        ats_application_phase_id = self.ats_application_phase_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if rating is not UNSET:
            field_dict["rating"] = rating
        if description is not UNSET:
            field_dict["description"] = description
        if ats_application_phase_id is not UNSET:
            field_dict["ats_application_phase_id"] = ats_application_phase_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        rating = d.pop("rating", UNSET)

        description = d.pop("description", UNSET)

        ats_application_phase_id = d.pop("ats_application_phase_id", UNSET)

        put_api_20261001_resources_ats_feedbacks_id_body = cls(
            id=id,
            rating=rating,
            description=description,
            ats_application_phase_id=ats_application_phase_id,
        )

        put_api_20261001_resources_ats_feedbacks_id_body.additional_properties = d
        return put_api_20261001_resources_ats_feedbacks_id_body

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
