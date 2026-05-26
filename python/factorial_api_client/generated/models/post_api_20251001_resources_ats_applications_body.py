from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_api_20251001_resources_ats_applications_body_author_type import (
    PostApi20251001ResourcesAtsApplicationsBodyAuthorType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20251001ResourcesAtsApplicationsBody")


@_attrs_define
class PostApi20251001ResourcesAtsApplicationsBody:
    ats_job_posting_id: int
    """ Application job posting id """
    author_id: int | Unset = UNSET
    """ Application author id """
    author_type: PostApi20251001ResourcesAtsApplicationsBodyAuthorType | Unset = UNSET
    """ Application author type """
    phone: str | Unset = UNSET
    """ Application candidate phone """
    ats_candidate_id: int | Unset = UNSET
    """ Application candidate id """
    ats_application_phase_id: int | Unset = UNSET
    """ Application phase id """
    consent_to_talent_pool: bool | Unset = UNSET
    """ Whether or not the candidate has given consent to be added to the talent pool """
    cover_letter: str | Unset = UNSET
    """ Application cover letter """
    source: str | Unset = UNSET
    """ Application source """
    medium: str | Unset = UNSET
    """ Application medium """
    answers: list[Any] | Unset = UNSET
    """ answers """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ats_job_posting_id = self.ats_job_posting_id

        author_id = self.author_id

        author_type: str | Unset = UNSET
        if not isinstance(self.author_type, Unset):
            author_type = self.author_type.value

        phone = self.phone

        ats_candidate_id = self.ats_candidate_id

        ats_application_phase_id = self.ats_application_phase_id

        consent_to_talent_pool = self.consent_to_talent_pool

        cover_letter = self.cover_letter

        source = self.source

        medium = self.medium

        answers: list[Any] | Unset = UNSET
        if not isinstance(self.answers, Unset):
            answers = self.answers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ats_job_posting_id": ats_job_posting_id,
            }
        )
        if author_id is not UNSET:
            field_dict["author_id"] = author_id
        if author_type is not UNSET:
            field_dict["author_type"] = author_type
        if phone is not UNSET:
            field_dict["phone"] = phone
        if ats_candidate_id is not UNSET:
            field_dict["ats_candidate_id"] = ats_candidate_id
        if ats_application_phase_id is not UNSET:
            field_dict["ats_application_phase_id"] = ats_application_phase_id
        if consent_to_talent_pool is not UNSET:
            field_dict["consent_to_talent_pool"] = consent_to_talent_pool
        if cover_letter is not UNSET:
            field_dict["cover_letter"] = cover_letter
        if source is not UNSET:
            field_dict["source"] = source
        if medium is not UNSET:
            field_dict["medium"] = medium
        if answers is not UNSET:
            field_dict["answers"] = answers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ats_job_posting_id = d.pop("ats_job_posting_id")

        author_id = d.pop("author_id", UNSET)

        _author_type = d.pop("author_type", UNSET)
        author_type: PostApi20251001ResourcesAtsApplicationsBodyAuthorType | Unset
        if isinstance(_author_type, Unset):
            author_type = UNSET
        else:
            author_type = PostApi20251001ResourcesAtsApplicationsBodyAuthorType(_author_type) if _author_type is not None else None

        phone = d.pop("phone", UNSET)

        ats_candidate_id = d.pop("ats_candidate_id", UNSET)

        ats_application_phase_id = d.pop("ats_application_phase_id", UNSET)

        consent_to_talent_pool = d.pop("consent_to_talent_pool", UNSET)

        cover_letter = d.pop("cover_letter", UNSET)

        source = d.pop("source", UNSET)

        medium = d.pop("medium", UNSET)

        answers = cast(list[Any], d.pop("answers", UNSET))

        post_api_20251001_resources_ats_applications_body = cls(
            ats_job_posting_id=ats_job_posting_id,
            author_id=author_id,
            author_type=author_type,
            phone=phone,
            ats_candidate_id=ats_candidate_id,
            ats_application_phase_id=ats_application_phase_id,
            consent_to_talent_pool=consent_to_talent_pool,
            cover_letter=cover_letter,
            source=source,
            medium=medium,
            answers=answers,
        )

        post_api_20251001_resources_ats_applications_body.additional_properties = d
        return post_api_20251001_resources_ats_applications_body

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
