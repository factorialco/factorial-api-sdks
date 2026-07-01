from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ats_application_cv import AtsApplicationCv


T = TypeVar("T", bound="AtsApplication")


@_attrs_define
class AtsApplication:
    id: str
    """ Id of the application """
    company_id: str
    """ Company id of the application """
    ats_job_posting_id: str
    """ Job posting id of the application """
    ats_candidate_id: str
    """ Candidate id of the application """
    created_at: str
    """ Application created at date """
    employee_id: str | Unset = UNSET
    """ Employee id of the application """
    phone: str | Unset = UNSET
    """ Candidate phone of the application """
    qualified: bool | Unset = UNSET
    """ Qualified of the application """
    ats_application_phase_id: str | Unset = UNSET
    """ Application phase id """
    cover_letter: str | Unset = UNSET
    """ Application cover letter """
    cv: AtsApplicationCv | Unset = UNSET
    """ CV file attachment of the application (includes filename, url, byte_size, content_type, created_at) """
    ats_conversation_id: str | Unset = UNSET
    """ Application conversation id """
    medium: str | Unset = UNSET
    """ Application medium """
    rating_average: int | Unset = UNSET
    """ Application average rating """
    ats_rejection_reason_id: str | Unset = UNSET
    """ Application rejection reason id """
    source_id: str | Unset = UNSET
    """ Application source id """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        company_id = self.company_id

        ats_job_posting_id = self.ats_job_posting_id

        ats_candidate_id = self.ats_candidate_id

        created_at = self.created_at

        employee_id = self.employee_id

        phone = self.phone

        qualified = self.qualified

        ats_application_phase_id = self.ats_application_phase_id

        cover_letter = self.cover_letter

        cv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cv, Unset):
            cv = self.cv.to_dict()

        ats_conversation_id = self.ats_conversation_id

        medium = self.medium

        rating_average = self.rating_average

        ats_rejection_reason_id = self.ats_rejection_reason_id

        source_id = self.source_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "company_id": company_id,
                "ats_job_posting_id": ats_job_posting_id,
                "ats_candidate_id": ats_candidate_id,
                "created_at": created_at,
            }
        )
        if employee_id is not UNSET:
            field_dict["employee_id"] = employee_id
        if phone is not UNSET:
            field_dict["phone"] = phone
        if qualified is not UNSET:
            field_dict["qualified"] = qualified
        if ats_application_phase_id is not UNSET:
            field_dict["ats_application_phase_id"] = ats_application_phase_id
        if cover_letter is not UNSET:
            field_dict["cover_letter"] = cover_letter
        if cv is not UNSET:
            field_dict["cv"] = cv
        if ats_conversation_id is not UNSET:
            field_dict["ats_conversation_id"] = ats_conversation_id
        if medium is not UNSET:
            field_dict["medium"] = medium
        if rating_average is not UNSET:
            field_dict["rating_average"] = rating_average
        if ats_rejection_reason_id is not UNSET:
            field_dict["ats_rejection_reason_id"] = ats_rejection_reason_id
        if source_id is not UNSET:
            field_dict["source_id"] = source_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ats_application_cv import AtsApplicationCv

        d = dict(src_dict)
        id = d.pop("id")

        company_id = d.pop("company_id")

        ats_job_posting_id = d.pop("ats_job_posting_id")

        ats_candidate_id = d.pop("ats_candidate_id")

        created_at = d.pop("created_at")

        employee_id = d.pop("employee_id", UNSET)

        phone = d.pop("phone", UNSET)

        qualified = d.pop("qualified", UNSET)

        ats_application_phase_id = d.pop("ats_application_phase_id", UNSET)

        cover_letter = d.pop("cover_letter", UNSET)

        _cv = d.pop("cv", UNSET)
        cv: AtsApplicationCv | Unset
        if isinstance(_cv, Unset):
            cv = UNSET
        else:
            cv = AtsApplicationCv.from_dict(_cv)

        ats_conversation_id = d.pop("ats_conversation_id", UNSET)

        medium = d.pop("medium", UNSET)

        rating_average = d.pop("rating_average", UNSET)

        ats_rejection_reason_id = d.pop("ats_rejection_reason_id", UNSET)

        source_id = d.pop("source_id", UNSET)

        ats_application = cls(
            id=id,
            company_id=company_id,
            ats_job_posting_id=ats_job_posting_id,
            ats_candidate_id=ats_candidate_id,
            created_at=created_at,
            employee_id=employee_id,
            phone=phone,
            qualified=qualified,
            ats_application_phase_id=ats_application_phase_id,
            cover_letter=cover_letter,
            cv=cv,
            ats_conversation_id=ats_conversation_id,
            medium=medium,
            rating_average=rating_average,
            ats_rejection_reason_id=ats_rejection_reason_id,
            source_id=source_id,
        )

        ats_application.additional_properties = d
        return ats_application

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
