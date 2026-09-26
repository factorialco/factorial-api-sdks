from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20261001ResourcesAtsCandidatesBody")


@_attrs_define
class PostApi20261001ResourcesAtsCandidatesBody:
    first_name: str
    """ first name of the candidate. """
    last_name: str
    """ last name of the candidate. """
    company_id: str
    """ company identifier, refers to /core/me endpoint. """
    email: str | Unset = UNSET
    """ email of the candidate. """
    talent_pool: bool | Unset = UNSET
    """ is the candidate part of talent pool? """
    consent_given_at: str | Unset = UNSET
    """ date when the consent was given. """
    source: str | Unset = UNSET
    """ source of the candidate. """
    medium: str | Unset = UNSET
    """ specifies additional details related to the source of the candidate, such as the referrer name for example
    if the source is referred. """
    phone_number: str | Unset = UNSET
    """ phone number of the candidate. """
    personal_url: str | Unset = UNSET
    """ personal web resource from the candidate. """
    gender: str | Unset = UNSET
    """ gender of the candidate. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        first_name = self.first_name

        last_name = self.last_name

        company_id = self.company_id

        email = self.email

        talent_pool = self.talent_pool

        consent_given_at = self.consent_given_at

        source = self.source

        medium = self.medium

        phone_number = self.phone_number

        personal_url = self.personal_url

        gender = self.gender

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "first_name": first_name,
                "last_name": last_name,
                "company_id": company_id,
            }
        )
        if email is not UNSET:
            field_dict["email"] = email
        if talent_pool is not UNSET:
            field_dict["talent_pool"] = talent_pool
        if consent_given_at is not UNSET:
            field_dict["consent_given_at"] = consent_given_at
        if source is not UNSET:
            field_dict["source"] = source
        if medium is not UNSET:
            field_dict["medium"] = medium
        if phone_number is not UNSET:
            field_dict["phone_number"] = phone_number
        if personal_url is not UNSET:
            field_dict["personal_url"] = personal_url
        if gender is not UNSET:
            field_dict["gender"] = gender

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        first_name = d.pop("first_name")

        last_name = d.pop("last_name")

        company_id = d.pop("company_id")

        email = d.pop("email", UNSET)

        talent_pool = d.pop("talent_pool", UNSET)

        consent_given_at = d.pop("consent_given_at", UNSET)

        source = d.pop("source", UNSET)

        medium = d.pop("medium", UNSET)

        phone_number = d.pop("phone_number", UNSET)

        personal_url = d.pop("personal_url", UNSET)

        gender = d.pop("gender", UNSET)

        post_api_20261001_resources_ats_candidates_body = cls(
            first_name=first_name,
            last_name=last_name,
            company_id=company_id,
            email=email,
            talent_pool=talent_pool,
            consent_given_at=consent_given_at,
            source=source,
            medium=medium,
            phone_number=phone_number,
            personal_url=personal_url,
            gender=gender,
        )

        post_api_20261001_resources_ats_candidates_body.additional_properties = d
        return post_api_20261001_resources_ats_candidates_body

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
