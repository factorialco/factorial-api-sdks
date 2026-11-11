from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_api_20270101_resources_ats_job_postings_body_category import (
    PostApi20270101ResourcesAtsJobPostingsBodyCategory,
)
from ..models.post_api_20270101_resources_ats_job_postings_body_contract_type import (
    PostApi20270101ResourcesAtsJobPostingsBodyContractType,
)
from ..models.post_api_20270101_resources_ats_job_postings_body_cover_letter_requirement import (
    PostApi20270101ResourcesAtsJobPostingsBodyCoverLetterRequirement,
)
from ..models.post_api_20270101_resources_ats_job_postings_body_cv_requirement import (
    PostApi20270101ResourcesAtsJobPostingsBodyCvRequirement,
)
from ..models.post_api_20270101_resources_ats_job_postings_body_personal_url_requirement import (
    PostApi20270101ResourcesAtsJobPostingsBodyPersonalUrlRequirement,
)
from ..models.post_api_20270101_resources_ats_job_postings_body_phone_requirement import (
    PostApi20270101ResourcesAtsJobPostingsBodyPhoneRequirement,
)
from ..models.post_api_20270101_resources_ats_job_postings_body_photo_requirement import (
    PostApi20270101ResourcesAtsJobPostingsBodyPhotoRequirement,
)
from ..models.post_api_20270101_resources_ats_job_postings_body_salary_format import (
    PostApi20270101ResourcesAtsJobPostingsBodySalaryFormat,
)
from ..models.post_api_20270101_resources_ats_job_postings_body_salary_period import (
    PostApi20270101ResourcesAtsJobPostingsBodySalaryPeriod,
)
from ..models.post_api_20270101_resources_ats_job_postings_body_schedule_type import (
    PostApi20270101ResourcesAtsJobPostingsBodyScheduleType,
)
from ..models.post_api_20270101_resources_ats_job_postings_body_status import (
    PostApi20270101ResourcesAtsJobPostingsBodyStatus,
)
from ..models.post_api_20270101_resources_ats_job_postings_body_workplace_type import (
    PostApi20270101ResourcesAtsJobPostingsBodyWorkplaceType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20270101ResourcesAtsJobPostingsBody")


@_attrs_define
class PostApi20270101ResourcesAtsJobPostingsBody:
    title: str
    status: PostApi20270101ResourcesAtsJobPostingsBodyStatus
    cv_requirement: PostApi20270101ResourcesAtsJobPostingsBodyCvRequirement
    cover_letter_requirement: PostApi20270101ResourcesAtsJobPostingsBodyCoverLetterRequirement
    phone_requirement: PostApi20270101ResourcesAtsJobPostingsBodyPhoneRequirement
    photo_requirement: PostApi20270101ResourcesAtsJobPostingsBodyPhotoRequirement
    personal_url_requirement: PostApi20270101ResourcesAtsJobPostingsBodyPersonalUrlRequirement
    description: str | Unset = UNSET
    contract_type: PostApi20270101ResourcesAtsJobPostingsBodyContractType | Unset = UNSET
    category: PostApi20270101ResourcesAtsJobPostingsBodyCategory | Unset = UNSET
    workplace_type: PostApi20270101ResourcesAtsJobPostingsBodyWorkplaceType | Unset = UNSET
    schedule_type: PostApi20270101ResourcesAtsJobPostingsBodyScheduleType | Unset = UNSET
    team_id: str | Unset = UNSET
    location_id: str | Unset = UNSET
    salary_format: PostApi20270101ResourcesAtsJobPostingsBodySalaryFormat | Unset = UNSET
    salary_from_amount_in_cents: int | Unset = UNSET
    salary_to_amount_in_cents: int | Unset = UNSET
    salary_period: PostApi20270101ResourcesAtsJobPostingsBodySalaryPeriod | Unset = UNSET
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
            contract_type = self.contract_type.value if self.contract_type is not None else None

        category: str | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.value if self.category is not None else None

        workplace_type: str | Unset = UNSET
        if not isinstance(self.workplace_type, Unset):
            workplace_type = self.workplace_type.value if self.workplace_type is not None else None

        schedule_type: str | Unset = UNSET
        if not isinstance(self.schedule_type, Unset):
            schedule_type = self.schedule_type.value if self.schedule_type is not None else None

        team_id = self.team_id

        location_id = self.location_id

        salary_format: str | Unset = UNSET
        if not isinstance(self.salary_format, Unset):
            salary_format = self.salary_format.value if self.salary_format is not None else None

        salary_from_amount_in_cents = self.salary_from_amount_in_cents

        salary_to_amount_in_cents = self.salary_to_amount_in_cents

        salary_period: str | Unset = UNSET
        if not isinstance(self.salary_period, Unset):
            salary_period = self.salary_period.value if self.salary_period is not None else None

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
        if category is not UNSET:
            field_dict["category"] = category
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

        status = PostApi20270101ResourcesAtsJobPostingsBodyStatus(d.pop("status"))

        cv_requirement = PostApi20270101ResourcesAtsJobPostingsBodyCvRequirement(
            d.pop("cv_requirement")
        )

        cover_letter_requirement = PostApi20270101ResourcesAtsJobPostingsBodyCoverLetterRequirement(
            d.pop("cover_letter_requirement")
        )

        phone_requirement = PostApi20270101ResourcesAtsJobPostingsBodyPhoneRequirement(
            d.pop("phone_requirement")
        )

        photo_requirement = PostApi20270101ResourcesAtsJobPostingsBodyPhotoRequirement(
            d.pop("photo_requirement")
        )

        personal_url_requirement = PostApi20270101ResourcesAtsJobPostingsBodyPersonalUrlRequirement(
            d.pop("personal_url_requirement")
        )

        description = d.pop("description", UNSET)

        _contract_type = d.pop("contract_type", UNSET)
        contract_type: PostApi20270101ResourcesAtsJobPostingsBodyContractType | Unset
        if isinstance(_contract_type, Unset):
            contract_type = UNSET
        else:
            contract_type = PostApi20270101ResourcesAtsJobPostingsBodyContractType(_contract_type) if _contract_type is not None else None

        _category = d.pop("category", UNSET)
        category: PostApi20270101ResourcesAtsJobPostingsBodyCategory | Unset
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = PostApi20270101ResourcesAtsJobPostingsBodyCategory(_category) if _category is not None else None

        _workplace_type = d.pop("workplace_type", UNSET)
        workplace_type: PostApi20270101ResourcesAtsJobPostingsBodyWorkplaceType | Unset
        if isinstance(_workplace_type, Unset):
            workplace_type = UNSET
        else:
            workplace_type = PostApi20270101ResourcesAtsJobPostingsBodyWorkplaceType(
                _workplace_type
            ) if _workplace_type is not None else None

        _schedule_type = d.pop("schedule_type", UNSET)
        schedule_type: PostApi20270101ResourcesAtsJobPostingsBodyScheduleType | Unset
        if isinstance(_schedule_type, Unset):
            schedule_type = UNSET
        else:
            schedule_type = PostApi20270101ResourcesAtsJobPostingsBodyScheduleType(_schedule_type) if _schedule_type is not None else None

        team_id = d.pop("team_id", UNSET)

        location_id = d.pop("location_id", UNSET)

        _salary_format = d.pop("salary_format", UNSET)
        salary_format: PostApi20270101ResourcesAtsJobPostingsBodySalaryFormat | Unset
        if isinstance(_salary_format, Unset):
            salary_format = UNSET
        else:
            salary_format = PostApi20270101ResourcesAtsJobPostingsBodySalaryFormat(_salary_format) if _salary_format is not None else None

        salary_from_amount_in_cents = d.pop("salary_from_amount_in_cents", UNSET)

        salary_to_amount_in_cents = d.pop("salary_to_amount_in_cents", UNSET)

        _salary_period = d.pop("salary_period", UNSET)
        salary_period: PostApi20270101ResourcesAtsJobPostingsBodySalaryPeriod | Unset
        if isinstance(_salary_period, Unset):
            salary_period = UNSET
        else:
            salary_period = PostApi20270101ResourcesAtsJobPostingsBodySalaryPeriod(_salary_period) if _salary_period is not None else None

        post_api_20270101_resources_ats_job_postings_body = cls(
            title=title,
            status=status,
            cv_requirement=cv_requirement,
            cover_letter_requirement=cover_letter_requirement,
            phone_requirement=phone_requirement,
            photo_requirement=photo_requirement,
            personal_url_requirement=personal_url_requirement,
            description=description,
            contract_type=contract_type,
            category=category,
            workplace_type=workplace_type,
            schedule_type=schedule_type,
            team_id=team_id,
            location_id=location_id,
            salary_format=salary_format,
            salary_from_amount_in_cents=salary_from_amount_in_cents,
            salary_to_amount_in_cents=salary_to_amount_in_cents,
            salary_period=salary_period,
        )

        post_api_20270101_resources_ats_job_postings_body.additional_properties = d
        return post_api_20270101_resources_ats_job_postings_body

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
