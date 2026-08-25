from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ats_job_posting_contract_type import AtsJobPostingContractType
from ..models.ats_job_posting_cover_letter_requirement import AtsJobPostingCoverLetterRequirement
from ..models.ats_job_posting_cv_requirement import AtsJobPostingCvRequirement
from ..models.ats_job_posting_personal_url_requirement import AtsJobPostingPersonalUrlRequirement
from ..models.ats_job_posting_phone_requirement import AtsJobPostingPhoneRequirement
from ..models.ats_job_posting_photo_requirement import AtsJobPostingPhotoRequirement
from ..models.ats_job_posting_salary_format import AtsJobPostingSalaryFormat
from ..models.ats_job_posting_salary_period import AtsJobPostingSalaryPeriod
from ..models.ats_job_posting_schedule_type import AtsJobPostingScheduleType
from ..models.ats_job_posting_status import AtsJobPostingStatus
from ..models.ats_job_posting_workplace_type import AtsJobPostingWorkplaceType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AtsJobPosting")


@_attrs_define
class AtsJobPosting:
    id: int
    """ Unique identifier for the job posting """
    company_id: int
    """ Identifier of the company associated with the job posting """
    ats_company_id: int
    """ Identifier of the ATS company associated with the job posting """
    title: str
    """ Title of the job posting """
    remote: bool
    """ Indicates if the job posting is remote """
    status: AtsJobPostingStatus
    """ The current status of the job posting (e.g., draft, published, archived) """
    cv_requirement: AtsJobPostingCvRequirement
    """ Requirement for the CV (e.g, mandatory, optional, do_not_ask) """
    cover_letter_requirement: AtsJobPostingCoverLetterRequirement
    """ Requirement for the cover letter (e.g, mandatory, optional, do_not_ask) """
    phone_requirement: AtsJobPostingPhoneRequirement
    """ Requirement for the phone number (e.g, mandatory, optional, do_not_ask) """
    photo_requirement: AtsJobPostingPhotoRequirement
    """ Requirement for the phone number (e.g, mandatory, optional, do_not_ask) """
    personal_url_requirement: AtsJobPostingPersonalUrlRequirement
    """ Requirement for the personal URL (e.g, mandatory, optional, do_not_ask) """
    salary_period: AtsJobPostingSalaryPeriod
    """ The period of the salary (e.g., annual, monthly, daily) """
    created_at: str
    """ Date in ISO 8601 format when the job posting was created """
    description: str | Unset = UNSET
    """ Description of the job posting """
    contract_type: AtsJobPostingContractType | Unset = UNSET
    workplace_type: AtsJobPostingWorkplaceType | Unset = UNSET
    schedule_type: AtsJobPostingScheduleType | Unset = UNSET
    """ The schedule type of the job posting (e.g., full_time, part_time) """
    team_id: int | Unset = UNSET
    """ Identifier of the team associated with the job posting """
    location_id: int | Unset = UNSET
    """ Identifier of the location associated with the job posting """
    legal_entity_id: int | Unset = UNSET
    """ Identifier of the legal entity associated with the job posting """
    salary_format: AtsJobPostingSalaryFormat | Unset = UNSET
    """ The format of the salary (e.g., range, fixed_amount) """
    salary_from_amount_in_cents: int | Unset = UNSET
    """ The minimum salary amount in cents """
    salary_to_amount_in_cents: int | Unset = UNSET
    """ The maximum salary amount in cents """
    hide_salary: bool | Unset = UNSET
    """ Indicates whether the salary information for the job posting should be hidden from applicants. """
    url: str | Unset = UNSET
    """ If published, the public URL of the job posting. Otherwise will be null """
    published_at: str | Unset = UNSET
    """ Published date in ISO 8601 format of the job. If never been published the value will be null """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        company_id = self.company_id

        ats_company_id = self.ats_company_id

        title = self.title

        remote = self.remote

        status = self.status.value

        cv_requirement = self.cv_requirement.value

        cover_letter_requirement = self.cover_letter_requirement.value

        phone_requirement = self.phone_requirement.value

        photo_requirement = self.photo_requirement.value

        personal_url_requirement = self.personal_url_requirement.value

        salary_period = self.salary_period.value

        created_at = self.created_at

        description = self.description

        contract_type: str | Unset = UNSET
        if not isinstance(self.contract_type, Unset):
            contract_type = self.contract_type.value if self.contract_type is not None else None

        workplace_type: str | Unset = UNSET
        if not isinstance(self.workplace_type, Unset):
            workplace_type = self.workplace_type.value if self.workplace_type is not None else None

        schedule_type: str | Unset = UNSET
        if not isinstance(self.schedule_type, Unset):
            schedule_type = self.schedule_type.value if self.schedule_type is not None else None

        team_id = self.team_id

        location_id = self.location_id

        legal_entity_id = self.legal_entity_id

        salary_format: str | Unset = UNSET
        if not isinstance(self.salary_format, Unset):
            salary_format = self.salary_format.value if self.salary_format is not None else None

        salary_from_amount_in_cents = self.salary_from_amount_in_cents

        salary_to_amount_in_cents = self.salary_to_amount_in_cents

        hide_salary = self.hide_salary

        url = self.url

        published_at = self.published_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "company_id": company_id,
                "ats_company_id": ats_company_id,
                "title": title,
                "remote": remote,
                "status": status,
                "cv_requirement": cv_requirement,
                "cover_letter_requirement": cover_letter_requirement,
                "phone_requirement": phone_requirement,
                "photo_requirement": photo_requirement,
                "personal_url_requirement": personal_url_requirement,
                "salary_period": salary_period,
                "created_at": created_at,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if contract_type is not UNSET:
            field_dict["contract_type"] = contract_type
        if workplace_type is not UNSET:
            field_dict["workplace_type"] = workplace_type
        if schedule_type is not UNSET:
            field_dict["schedule_type"] = schedule_type
        if team_id is not UNSET:
            field_dict["team_id"] = team_id
        if location_id is not UNSET:
            field_dict["location_id"] = location_id
        if legal_entity_id is not UNSET:
            field_dict["legal_entity_id"] = legal_entity_id
        if salary_format is not UNSET:
            field_dict["salary_format"] = salary_format
        if salary_from_amount_in_cents is not UNSET:
            field_dict["salary_from_amount_in_cents"] = salary_from_amount_in_cents
        if salary_to_amount_in_cents is not UNSET:
            field_dict["salary_to_amount_in_cents"] = salary_to_amount_in_cents
        if hide_salary is not UNSET:
            field_dict["hide_salary"] = hide_salary
        if url is not UNSET:
            field_dict["url"] = url
        if published_at is not UNSET:
            field_dict["published_at"] = published_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        company_id = d.pop("company_id")

        ats_company_id = d.pop("ats_company_id")

        title = d.pop("title")

        remote = d.pop("remote")

        status = AtsJobPostingStatus(d.pop("status"))

        cv_requirement = AtsJobPostingCvRequirement(d.pop("cv_requirement"))

        cover_letter_requirement = AtsJobPostingCoverLetterRequirement(
            d.pop("cover_letter_requirement")
        )

        phone_requirement = AtsJobPostingPhoneRequirement(d.pop("phone_requirement"))

        photo_requirement = AtsJobPostingPhotoRequirement(d.pop("photo_requirement"))

        personal_url_requirement = AtsJobPostingPersonalUrlRequirement(
            d.pop("personal_url_requirement")
        )

        salary_period = AtsJobPostingSalaryPeriod(d.pop("salary_period"))

        created_at = d.pop("created_at")

        description = d.pop("description", UNSET)

        _contract_type = d.pop("contract_type", UNSET)
        contract_type: AtsJobPostingContractType | Unset
        if isinstance(_contract_type, Unset):
            contract_type = UNSET
        else:
            contract_type = AtsJobPostingContractType(_contract_type) if _contract_type is not None else None

        _workplace_type = d.pop("workplace_type", UNSET)
        workplace_type: AtsJobPostingWorkplaceType | Unset
        if isinstance(_workplace_type, Unset):
            workplace_type = UNSET
        else:
            workplace_type = AtsJobPostingWorkplaceType(_workplace_type) if _workplace_type is not None else None

        _schedule_type = d.pop("schedule_type", UNSET)
        schedule_type: AtsJobPostingScheduleType | Unset
        if isinstance(_schedule_type, Unset):
            schedule_type = UNSET
        else:
            schedule_type = AtsJobPostingScheduleType(_schedule_type) if _schedule_type is not None else None

        team_id = d.pop("team_id", UNSET)

        location_id = d.pop("location_id", UNSET)

        legal_entity_id = d.pop("legal_entity_id", UNSET)

        _salary_format = d.pop("salary_format", UNSET)
        salary_format: AtsJobPostingSalaryFormat | Unset
        if isinstance(_salary_format, Unset):
            salary_format = UNSET
        else:
            salary_format = AtsJobPostingSalaryFormat(_salary_format) if _salary_format is not None else None

        salary_from_amount_in_cents = d.pop("salary_from_amount_in_cents", UNSET)

        salary_to_amount_in_cents = d.pop("salary_to_amount_in_cents", UNSET)

        hide_salary = d.pop("hide_salary", UNSET)

        url = d.pop("url", UNSET)

        published_at = d.pop("published_at", UNSET)

        ats_job_posting = cls(
            id=id,
            company_id=company_id,
            ats_company_id=ats_company_id,
            title=title,
            remote=remote,
            status=status,
            cv_requirement=cv_requirement,
            cover_letter_requirement=cover_letter_requirement,
            phone_requirement=phone_requirement,
            photo_requirement=photo_requirement,
            personal_url_requirement=personal_url_requirement,
            salary_period=salary_period,
            created_at=created_at,
            description=description,
            contract_type=contract_type,
            workplace_type=workplace_type,
            schedule_type=schedule_type,
            team_id=team_id,
            location_id=location_id,
            legal_entity_id=legal_entity_id,
            salary_format=salary_format,
            salary_from_amount_in_cents=salary_from_amount_in_cents,
            salary_to_amount_in_cents=salary_to_amount_in_cents,
            hide_salary=hide_salary,
            url=url,
            published_at=published_at,
        )

        ats_job_posting.additional_properties = d
        return ats_job_posting

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
