from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PutApi20251001ResourcesAtsCandidatesIdBody")


@_attrs_define
class PutApi20251001ResourcesAtsCandidatesIdBody:
    id: int
    """ identifier of the candidate. """
    email: str | Unset = UNSET
    """ email of the candidate. """
    first_name: str | Unset = UNSET
    """ first name of the candidate. """
    last_name: str | Unset = UNSET
    """ last name of the candidate. """
    talent_pool: bool | Unset = UNSET
    """ is the candidate part of talent pool? """
    consent_given_at: str | Unset = UNSET
    """ date when the consent was given. """
    phone_number: str | Unset = UNSET
    """ phone number of the candidate. """
    personal_url: str | Unset = UNSET
    """ personal web resource from the candidate. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        email = self.email

        first_name = self.first_name

        last_name = self.last_name

        talent_pool = self.talent_pool

        consent_given_at = self.consent_given_at

        phone_number = self.phone_number

        personal_url = self.personal_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if email is not UNSET:
            field_dict["email"] = email
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if talent_pool is not UNSET:
            field_dict["talent_pool"] = talent_pool
        if consent_given_at is not UNSET:
            field_dict["consent_given_at"] = consent_given_at
        if phone_number is not UNSET:
            field_dict["phone_number"] = phone_number
        if personal_url is not UNSET:
            field_dict["personal_url"] = personal_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        email = d.pop("email", UNSET)

        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        talent_pool = d.pop("talent_pool", UNSET)

        consent_given_at = d.pop("consent_given_at", UNSET)

        phone_number = d.pop("phone_number", UNSET)

        personal_url = d.pop("personal_url", UNSET)

        put_api_20251001_resources_ats_candidates_id_body = cls(
            id=id,
            email=email,
            first_name=first_name,
            last_name=last_name,
            talent_pool=talent_pool,
            consent_given_at=consent_given_at,
            phone_number=phone_number,
            personal_url=personal_url,
        )

        put_api_20251001_resources_ats_candidates_id_body.additional_properties = d
        return put_api_20251001_resources_ats_candidates_id_body

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
