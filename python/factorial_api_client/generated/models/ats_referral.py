from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AtsReferral")


@_attrs_define
class AtsReferral:
    id: str
    """ Referral identifier. """
    access_id: str
    """ The access that made the referral. """
    company_id: str
    """ Identifier of the company. """
    ats_candidate_id: str
    """ The referred candidate. """
    ats_application_id: str
    """ The application created for the referral. """
    created_at: str
    """ When the referral was made. """
    updated_at: str
    """ When the referral was last updated. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        access_id = self.access_id

        company_id = self.company_id

        ats_candidate_id = self.ats_candidate_id

        ats_application_id = self.ats_application_id

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "access_id": access_id,
                "company_id": company_id,
                "ats_candidate_id": ats_candidate_id,
                "ats_application_id": ats_application_id,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        access_id = d.pop("access_id")

        company_id = d.pop("company_id")

        ats_candidate_id = d.pop("ats_candidate_id")

        ats_application_id = d.pop("ats_application_id")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        ats_referral = cls(
            id=id,
            access_id=access_id,
            company_id=company_id,
            ats_candidate_id=ats_candidate_id,
            ats_application_id=ats_application_id,
            created_at=created_at,
            updated_at=updated_at,
        )

        ats_referral.additional_properties = d
        return ats_referral

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
