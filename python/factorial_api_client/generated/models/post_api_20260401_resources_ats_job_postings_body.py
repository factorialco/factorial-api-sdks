from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_api_20260401_resources_ats_job_postings_body_contract_type import (
    PostApi20260401ResourcesAtsJobPostingsBodyContractType,
)
from ..models.post_api_20260401_resources_ats_job_postings_body_cover_letter_requirement import (
    PostApi20260401ResourcesAtsJobPostingsBodyCoverLetterRequirement,
)
from ..models.post_api_20260401_resources_ats_job_postings_body_cv_requirement import (
    PostApi20260401ResourcesAtsJobPostingsBodyCvRequirement,
)
from ..models.post_api_20260401_resources_ats_job_postings_body_personal_url_requirement import (
    PostApi20260401ResourcesAtsJobPostingsBodyPersonalUrlRequirement,
)
from ..models.post_api_20260401_resources_ats_job_postings_body_phone_requirement import (
    PostApi20260401ResourcesAtsJobPostingsBodyPhoneRequirement,
)
from ..models.post_api_20260401_resources_ats_job_postings_body_photo_requirement import (
    PostApi20260401ResourcesAtsJobPostingsBodyPhotoRequirement,
)
from ..models.post_api_20260401_resources_ats_job_postings_body_salary_format import (
    PostApi20260401ResourcesAtsJobPostingsBodySalaryFormat,
)
from ..models.post_api_20260401_resources_ats_job_postings_body_salary_period import (
    PostApi20260401ResourcesAtsJobPostingsBodySalaryPeriod,
)
from ..models.post_api_20260401_resources_ats_job_postings_body_schedule_type import (
    PostApi20260401ResourcesAtsJobPostingsBodyScheduleType,
)
from ..models.post_api_20260401_resources_ats_job_postings_body_status import (
    PostApi20260401ResourcesAtsJobPostingsBodyStatus,
)
from ..models.post_api_20260401_resources_ats_job_postings_body_workplace_type import (
    PostApi20260401ResourcesAtsJobPostingsBodyWorkplaceType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20260401ResourcesAtsJobPostingsBody")


@_attrs_define
class PostApi20260401ResourcesAtsJobPostingsBody:
    title: str
    status: PostApi20260401ResourcesAtsJobPostingsBodyStatus
    cv_requirement: PostApi20260401ResourcesAtsJobPostingsBodyCvRequirement
    cover_letter_requirement: PostApi20260401ResourcesAtsJobPostingsBodyCoverLetterRequirement
    phone_requirement: PostApi20260401ResourcesAtsJobPostingsBodyPhoneRequirement
    photo_requirement: PostApi20260401ResourcesAtsJobPostingsBodyPhotoRequirement
    personal_url_requirement: PostApi20260401ResourcesAtsJobPostingsBodyPersonalUrlRequirement
    description: str | Unset = UNSET
    contract_type: PostApi20260401ResourcesAtsJobPostingsBodyContractType | Unset = UNSET
    workplace_type: PostApi20260401ResourcesAtsJobPostingsBodyWorkplaceType | Unset = UNSET
    schedule_type: PostApi20260401ResourcesAtsJobPostingsBodyScheduleType | Unset = UNSET
    team_id: int | Unset = UNSET
    location_id: int | Unset = UNSET
    salary_format: PostApi20260401ResourcesAtsJobPostingsBodySalaryFormat | Unset = UNSET
    salary_from_amount_in_cents: int | Unset = UNSET
    salary_to_amount_in_cents: int | Unset = UNSET
    salary_period: PostApi20260401ResourcesAtsJobPostingsBodySalaryPeriod | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        status = self.status.value

        cv_requirement = self.cv_requirement.value

        cover_letter_requirement = self.cover_letter_requirement.value

        phone_requirement = self.phone_requirement.value

        photo_requirement = self.photo_requirement.value

        personal_url_requirement = self.personal_url_requirement.value

        description = self.description

        contract_type: str | Unset = UNSET
        if not isinstance(self.contract_type, Unset):
            contract_type = self.contract_type.value

        workplace_type: str | Unset = UNSET
        if not isinstance(self.workplace_type, Unset):
            workplace_type = self.workplace_type.value

        schedule_type: str | Unset = UNSET
        if not isinstance(self.schedule_type, Unset):
            schedule_type = self.schedule_type.value

        team_id = self.team_id

        location_id = self.location_id

        salary_format: str | Unset = UNSET
        if not isinstance(self.salary_format, Unset):
            salary_format = self.salary_format.value

        salary_from_amount_in_cents = self.salary_from_amount_in_cents

        salary_to_amount_in_cents = self.salary_to_amount_in_cents

        salary_period: str | Unset = UNSET
        if not isinstance(self.salary_period, Unset):
            salary_period = self.salary_period.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "status": status,
                "cv_requirement": cv_requirement,
                "cover_letter_requirement": cover_letter_requirement,
                "phone_requirement": phone_requirement,
                "photo_requirement": photo_requirement,
                "personal_url_requirement": personal_url_requirement,
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
        if salary_format is not UNSET:
            field_dict["salary_format"] = salary_format
        if salary_from_amount_in_cents is not UNSET:
            field_dict["salary_from_amount_in_cents"] = salary_from_amount_in_cents
        if salary_to_amount_in_cents is not UNSET:
            field_dict["salary_to_amount_in_cents"] = salary_to_amount_in_cents
        if salary_period is not UNSET:
            field_dict["salary_period"] = salary_period

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title")

        status = PostApi20260401ResourcesAtsJobPostingsBodyStatus(d.pop("status"))

        cv_requirement = PostApi20260401ResourcesAtsJobPostingsBodyCvRequirement(
            d.pop("cv_requirement")
        )

        cover_letter_requirement = PostApi20260401ResourcesAtsJobPostingsBodyCoverLetterRequirement(
            d.pop("cover_letter_requirement")
        )

        phone_requirement = PostApi20260401ResourcesAtsJobPostingsBodyPhoneRequirement(
            d.pop("phone_requirement")
        )

        photo_requirement = PostApi20260401ResourcesAtsJobPostingsBodyPhotoRequirement(
            d.pop("photo_requirement")
        )

        personal_url_requirement = PostApi20260401ResourcesAtsJobPostingsBodyPersonalUrlRequirement(
            d.pop("personal_url_requirement")
        )

        description = d.pop("description", UNSET)

        _contract_type = d.pop("contract_type", UNSET)
        contract_type: PostApi20260401ResourcesAtsJobPostingsBodyContractType | Unset
        if isinstance(_contract_type, Unset):
            contract_type = UNSET
        else:
            contract_type = PostApi20260401ResourcesAtsJobPostingsBodyContractType(_contract_type) if _contract_type is not None else None

        _workplace_type = d.pop("workplace_type", UNSET)
        workplace_type: PostApi20260401ResourcesAtsJobPostingsBodyWorkplaceType | Unset
        if isinstance(_workplace_type, Unset):
            workplace_type = UNSET
        else:
            workplace_type = PostApi20260401ResourcesAtsJobPostingsBodyWorkplaceType(
                _workplace_type
            )

        _schedule_type = d.pop("schedule_type", UNSET)
        schedule_type: PostApi20260401ResourcesAtsJobPostingsBodyScheduleType | Unset
        if isinstance(_schedule_type, Unset):
            schedule_type = UNSET
        else:
            schedule_type = PostApi20260401ResourcesAtsJobPostingsBodyScheduleType(_schedule_type) if _schedule_type is not None else None

        team_id = d.pop("team_id", UNSET)

        location_id = d.pop("location_id", UNSET)

        _salary_format = d.pop("salary_format", UNSET)
        salary_format: PostApi20260401ResourcesAtsJobPostingsBodySalaryFormat | Unset
        if isinstance(_salary_format, Unset):
            salary_format = UNSET
        else:
            salary_format = PostApi20260401ResourcesAtsJobPostingsBodySalaryFormat(_salary_format) if _salary_format is not None else None

        salary_from_amount_in_cents = d.pop("salary_from_amount_in_cents", UNSET)

        salary_to_amount_in_cents = d.pop("salary_to_amount_in_cents", UNSET)

        _salary_period = d.pop("salary_period", UNSET)
        salary_period: PostApi20260401ResourcesAtsJobPostingsBodySalaryPeriod | Unset
        if isinstance(_salary_period, Unset):
            salary_period = UNSET
        else:
            salary_period = PostApi20260401ResourcesAtsJobPostingsBodySalaryPeriod(_salary_period) if _salary_period is not None else None

        post_api_20260401_resources_ats_job_postings_body = cls(
            title=title,
            status=status,
            cv_requirement=cv_requirement,
            cover_letter_requirement=cover_letter_requirement,
            phone_requirement=phone_requirement,
            photo_requirement=photo_requirement,
            personal_url_requirement=personal_url_requirement,
            description=description,
            contract_type=contract_type,
            workplace_type=workplace_type,
            schedule_type=schedule_type,
            team_id=team_id,
            location_id=location_id,
            salary_format=salary_format,
            salary_from_amount_in_cents=salary_from_amount_in_cents,
            salary_to_amount_in_cents=salary_to_amount_in_cents,
            salary_period=salary_period,
        )

        post_api_20260401_resources_ats_job_postings_body.additional_properties = d
        return post_api_20260401_resources_ats_job_postings_body

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
