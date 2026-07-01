from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ats_candidate_gender import AtsCandidateGender
from ..types import UNSET, Unset

T = TypeVar("T", bound="AtsCandidate")


@_attrs_define
class AtsCandidate:
    id: str
    """ identifier of the candidate. """
    first_name: str
    """ name of the candidate. """
    last_name: str
    """ last name of the candidate. """
    full_name: str
    """ full name of the candidate. """
    talent_pool: bool
    """ is the candidate part of talent pool? """
    created_at: str
    """ creation date of the candidate. """
    updated_at: str
    """ last update of the candidate. """
    company_id: str | Unset = UNSET
    """ company identifier. """
    email: str | Unset = UNSET
    """ email of the candidate. """
    phone_number: str | Unset = UNSET
    """ phone number of the candidate. """
    consent_given_at: str | Unset = UNSET
    """ date when the consent was given. """
    inactive_since: str | Unset = UNSET
    """ date when the candidate became inactive. """
    ats_job_posting_ids: list[str] | Unset = UNSET
    """ list of job posting identifiers. """
    personal_url: str | Unset = UNSET
    """ personal web resource from the candidate. """
    consent_expiration_date: str | Unset = UNSET
    """ date when the consent expires. """
    consent_to_talent_pool: bool | Unset = UNSET
    """ consent to talent pool. """
    medium: str | Unset = UNSET
    """ specifies additional details related to the source of the candidate, such as the referrer name for example
    if the source is referred. """
    source_id: str | Unset = UNSET
    """ candidate source identifier, refers to ats/candidate_sources endpoint. """
    gender: AtsCandidateGender | Unset = UNSET
    """ gender of the candidate. """
    score: float | Unset = UNSET
    """ score of the candidate. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        first_name = self.first_name

        last_name = self.last_name

        full_name = self.full_name

        talent_pool = self.talent_pool

        created_at = self.created_at

        updated_at = self.updated_at

        company_id = self.company_id

        email = self.email

        phone_number = self.phone_number

        consent_given_at = self.consent_given_at

        inactive_since = self.inactive_since

        ats_job_posting_ids: list[str] | Unset = UNSET
        if not isinstance(self.ats_job_posting_ids, Unset):
            ats_job_posting_ids = self.ats_job_posting_ids

        personal_url = self.personal_url

        consent_expiration_date = self.consent_expiration_date

        consent_to_talent_pool = self.consent_to_talent_pool

        medium = self.medium

        source_id = self.source_id

        gender: str | Unset = UNSET
        if not isinstance(self.gender, Unset):
            gender = self.gender.value

        score = self.score

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "first_name": first_name,
                "last_name": last_name,
                "full_name": full_name,
                "talent_pool": talent_pool,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if company_id is not UNSET:
            field_dict["company_id"] = company_id
        if email is not UNSET:
            field_dict["email"] = email
        if phone_number is not UNSET:
            field_dict["phone_number"] = phone_number
        if consent_given_at is not UNSET:
            field_dict["consent_given_at"] = consent_given_at
        if inactive_since is not UNSET:
            field_dict["inactive_since"] = inactive_since
        if ats_job_posting_ids is not UNSET:
            field_dict["ats_job_posting_ids"] = ats_job_posting_ids
        if personal_url is not UNSET:
            field_dict["personal_url"] = personal_url
        if consent_expiration_date is not UNSET:
            field_dict["consent_expiration_date"] = consent_expiration_date
        if consent_to_talent_pool is not UNSET:
            field_dict["consent_to_talent_pool"] = consent_to_talent_pool
        if medium is not UNSET:
            field_dict["medium"] = medium
        if source_id is not UNSET:
            field_dict["source_id"] = source_id
        if gender is not UNSET:
            field_dict["gender"] = gender
        if score is not UNSET:
            field_dict["score"] = score

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        first_name = d.pop("first_name")

        last_name = d.pop("last_name")

        full_name = d.pop("full_name")

        talent_pool = d.pop("talent_pool")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        company_id = d.pop("company_id", UNSET)

        email = d.pop("email", UNSET)

        phone_number = d.pop("phone_number", UNSET)

        consent_given_at = d.pop("consent_given_at", UNSET)

        inactive_since = d.pop("inactive_since", UNSET)

        ats_job_posting_ids = cast(list[str], d.pop("ats_job_posting_ids", UNSET))

        personal_url = d.pop("personal_url", UNSET)

        consent_expiration_date = d.pop("consent_expiration_date", UNSET)

        consent_to_talent_pool = d.pop("consent_to_talent_pool", UNSET)

        medium = d.pop("medium", UNSET)

        source_id = d.pop("source_id", UNSET)

        _gender = d.pop("gender", UNSET)
        gender: AtsCandidateGender | Unset
        if isinstance(_gender, Unset):
            gender = UNSET
        else:
            gender = AtsCandidateGender(_gender) if _gender is not None else None

        score = d.pop("score", UNSET)

        ats_candidate = cls(
            id=id,
            first_name=first_name,
            last_name=last_name,
            full_name=full_name,
            talent_pool=talent_pool,
            created_at=created_at,
            updated_at=updated_at,
            company_id=company_id,
            email=email,
            phone_number=phone_number,
            consent_given_at=consent_given_at,
            inactive_since=inactive_since,
            ats_job_posting_ids=ats_job_posting_ids,
            personal_url=personal_url,
            consent_expiration_date=consent_expiration_date,
            consent_to_talent_pool=consent_to_talent_pool,
            medium=medium,
            source_id=source_id,
            gender=gender,
            score=score,
        )

        ats_candidate.additional_properties = d
        return ats_candidate

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
