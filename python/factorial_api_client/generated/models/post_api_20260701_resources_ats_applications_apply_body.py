from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20260701ResourcesAtsApplicationsApplyBody")


@_attrs_define
class PostApi20260701ResourcesAtsApplicationsApplyBody:
    first_name: str
    """ Application first name """
    last_name: str
    """ Application last name """
    ats_job_posting_id: str
    """ Application job posting id """
    email: str
    """ Application candidate email """
    company_id: str | Unset = UNSET
    """ Company id of the application """
    phone: str | Unset = UNSET
    """ Application candidate phone """
    source: str | Unset = UNSET
    """ Application source """
    medium: str | Unset = UNSET
    """ Application medium """
    cover_letter: str | Unset = UNSET
    """ Application cover letter """
    gender: str | Unset = UNSET
    """ gender of the candidate. """
    consent_to_talent_pool: bool | Unset = UNSET
    """ Application consent talent pool """
    answers: list[Any] | Unset = UNSET
    """ answers """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        first_name = self.first_name

        last_name = self.last_name

        ats_job_posting_id = self.ats_job_posting_id

        email = self.email

        company_id = self.company_id

        phone = self.phone

        source = self.source

        medium = self.medium

        cover_letter = self.cover_letter

        gender = self.gender

        consent_to_talent_pool = self.consent_to_talent_pool

        answers: list[Any] | Unset = UNSET
        if not isinstance(self.answers, Unset):
            answers = self.answers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "first_name": first_name,
                "last_name": last_name,
                "ats_job_posting_id": ats_job_posting_id,
                "email": email,
            }
        )
        if company_id is not UNSET:
            field_dict["company_id"] = company_id
        if phone is not UNSET:
            field_dict["phone"] = phone
        if source is not UNSET:
            field_dict["source"] = source
        if medium is not UNSET:
            field_dict["medium"] = medium
        if cover_letter is not UNSET:
            field_dict["cover_letter"] = cover_letter
        if gender is not UNSET:
            field_dict["gender"] = gender
        if consent_to_talent_pool is not UNSET:
            field_dict["consent_to_talent_pool"] = consent_to_talent_pool
        if answers is not UNSET:
            field_dict["answers"] = answers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        first_name = d.pop("first_name")

        last_name = d.pop("last_name")

        ats_job_posting_id = d.pop("ats_job_posting_id")

        email = d.pop("email")

        company_id = d.pop("company_id", UNSET)

        phone = d.pop("phone", UNSET)

        source = d.pop("source", UNSET)

        medium = d.pop("medium", UNSET)

        cover_letter = d.pop("cover_letter", UNSET)

        gender = d.pop("gender", UNSET)

        consent_to_talent_pool = d.pop("consent_to_talent_pool", UNSET)

        answers = cast(list[Any], d.pop("answers", UNSET))

        post_api_20260701_resources_ats_applications_apply_body = cls(
            first_name=first_name,
            last_name=last_name,
            ats_job_posting_id=ats_job_posting_id,
            email=email,
            company_id=company_id,
            phone=phone,
            source=source,
            medium=medium,
            cover_letter=cover_letter,
            gender=gender,
            consent_to_talent_pool=consent_to_talent_pool,
            answers=answers,
        )

        post_api_20260701_resources_ats_applications_apply_body.additional_properties = d
        return post_api_20260701_resources_ats_applications_apply_body

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
