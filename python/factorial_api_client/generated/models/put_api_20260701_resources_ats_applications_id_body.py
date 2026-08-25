from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.put_api_20260701_resources_ats_applications_id_body_author_type import (
    PutApi20260701ResourcesAtsApplicationsIdBodyAuthorType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PutApi20260701ResourcesAtsApplicationsIdBody")


@_attrs_define
class PutApi20260701ResourcesAtsApplicationsIdBody:
    id: str
    """ Application id """
    author_id: str | Unset = UNSET
    """ Application author id """
    author_type: PutApi20260701ResourcesAtsApplicationsIdBodyAuthorType | Unset = UNSET
    """ Application author type """
    qualified: bool | Unset = UNSET
    """ Application is qualified """
    ats_application_phase_id: str | Unset = UNSET
    """ Application phase id """
    disqualified_reason: str | Unset = UNSET
    """ Application disqualified reason """
    phone: str | Unset = UNSET
    """ Application candidate phone """
    ats_rejection_reason_id: str | Unset = UNSET
    """ Application rejection reason id """
    source: str | Unset = UNSET
    """ Application source """
    source_id: str | Unset = UNSET
    """ Application source id """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        author_id = self.author_id

        author_type: str | Unset = UNSET
        if not isinstance(self.author_type, Unset):
            author_type = self.author_type.value if self.author_type is not None else None

        qualified = self.qualified

        ats_application_phase_id = self.ats_application_phase_id

        disqualified_reason = self.disqualified_reason

        phone = self.phone

        ats_rejection_reason_id = self.ats_rejection_reason_id

        source = self.source

        source_id = self.source_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if author_id is not UNSET:
            field_dict["author_id"] = author_id
        if author_type is not UNSET:
            field_dict["author_type"] = author_type
        if qualified is not UNSET:
            field_dict["qualified"] = qualified
        if ats_application_phase_id is not UNSET:
            field_dict["ats_application_phase_id"] = ats_application_phase_id
        if disqualified_reason is not UNSET:
            field_dict["disqualified_reason"] = disqualified_reason
        if phone is not UNSET:
            field_dict["phone"] = phone
        if ats_rejection_reason_id is not UNSET:
            field_dict["ats_rejection_reason_id"] = ats_rejection_reason_id
        if source is not UNSET:
            field_dict["source"] = source
        if source_id is not UNSET:
            field_dict["source_id"] = source_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        author_id = d.pop("author_id", UNSET)

        _author_type = d.pop("author_type", UNSET)
        author_type: PutApi20260701ResourcesAtsApplicationsIdBodyAuthorType | Unset
        if isinstance(_author_type, Unset):
            author_type = UNSET
        else:
            author_type = PutApi20260701ResourcesAtsApplicationsIdBodyAuthorType(_author_type) if _author_type is not None else None

        qualified = d.pop("qualified", UNSET)

        ats_application_phase_id = d.pop("ats_application_phase_id", UNSET)

        disqualified_reason = d.pop("disqualified_reason", UNSET)

        phone = d.pop("phone", UNSET)

        ats_rejection_reason_id = d.pop("ats_rejection_reason_id", UNSET)

        source = d.pop("source", UNSET)

        source_id = d.pop("source_id", UNSET)

        put_api_20260701_resources_ats_applications_id_body = cls(
            id=id,
            author_id=author_id,
            author_type=author_type,
            qualified=qualified,
            ats_application_phase_id=ats_application_phase_id,
            disqualified_reason=disqualified_reason,
            phone=phone,
            ats_rejection_reason_id=ats_rejection_reason_id,
            source=source,
            source_id=source_id,
        )

        put_api_20260701_resources_ats_applications_id_body.additional_properties = d
        return put_api_20260701_resources_ats_applications_id_body

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
