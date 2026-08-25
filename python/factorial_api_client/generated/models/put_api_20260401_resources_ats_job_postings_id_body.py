from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.put_api_20260401_resources_ats_job_postings_id_body_contract_type import (
    PutApi20260401ResourcesAtsJobPostingsIdBodyContractType,
)
from ..models.put_api_20260401_resources_ats_job_postings_id_body_cover_letter_requirement import (
    PutApi20260401ResourcesAtsJobPostingsIdBodyCoverLetterRequirement,
)
from ..models.put_api_20260401_resources_ats_job_postings_id_body_cv_requirement import (
    PutApi20260401ResourcesAtsJobPostingsIdBodyCvRequirement,
)
from ..models.put_api_20260401_resources_ats_job_postings_id_body_personal_url_requirement import (
    PutApi20260401ResourcesAtsJobPostingsIdBodyPersonalUrlRequirement,
)
from ..models.put_api_20260401_resources_ats_job_postings_id_body_phone_requirement import (
    PutApi20260401ResourcesAtsJobPostingsIdBodyPhoneRequirement,
)
from ..models.put_api_20260401_resources_ats_job_postings_id_body_photo_requirement import (
    PutApi20260401ResourcesAtsJobPostingsIdBodyPhotoRequirement,
)
from ..models.put_api_20260401_resources_ats_job_postings_id_body_salary_format import (
    PutApi20260401ResourcesAtsJobPostingsIdBodySalaryFormat,
)
from ..models.put_api_20260401_resources_ats_job_postings_id_body_salary_period import (
    PutApi20260401ResourcesAtsJobPostingsIdBodySalaryPeriod,
)
from ..models.put_api_20260401_resources_ats_job_postings_id_body_schedule_type import (
    PutApi20260401ResourcesAtsJobPostingsIdBodyScheduleType,
)
from ..models.put_api_20260401_resources_ats_job_postings_id_body_status import (
    PutApi20260401ResourcesAtsJobPostingsIdBodyStatus,
)
from ..models.put_api_20260401_resources_ats_job_postings_id_body_workplace_type import (
    PutApi20260401ResourcesAtsJobPostingsIdBodyWorkplaceType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PutApi20260401ResourcesAtsJobPostingsIdBody")


@_attrs_define
class PutApi20260401ResourcesAtsJobPostingsIdBody:
    id: int
    title: str | Unset = UNSET
    description: str | Unset = UNSET
    contract_type: PutApi20260401ResourcesAtsJobPostingsIdBodyContractType | Unset = UNSET
    workplace_type: PutApi20260401ResourcesAtsJobPostingsIdBodyWorkplaceType | Unset = UNSET
    status: PutApi20260401ResourcesAtsJobPostingsIdBodyStatus | Unset = UNSET
    schedule_type: PutApi20260401ResourcesAtsJobPostingsIdBodyScheduleType | Unset = UNSET
    team_id: int | Unset = UNSET
    location_id: int | Unset = UNSET
    salary_format: PutApi20260401ResourcesAtsJobPostingsIdBodySalaryFormat | Unset = UNSET
    salary_from_amount_in_cents: int | Unset = UNSET
    salary_to_amount_in_cents: int | Unset = UNSET
    cv_requirement: PutApi20260401ResourcesAtsJobPostingsIdBodyCvRequirement | Unset = UNSET
    cover_letter_requirement: (
        PutApi20260401ResourcesAtsJobPostingsIdBodyCoverLetterRequirement | Unset
    ) = UNSET
    phone_requirement: PutApi20260401ResourcesAtsJobPostingsIdBodyPhoneRequirement | Unset = UNSET
    photo_requirement: PutApi20260401ResourcesAtsJobPostingsIdBodyPhotoRequirement | Unset = UNSET
    personal_url_requirement: (
        PutApi20260401ResourcesAtsJobPostingsIdBodyPersonalUrlRequirement | Unset
    ) = UNSET
    salary_period: PutApi20260401ResourcesAtsJobPostingsIdBodySalaryPeriod | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        description = self.description

        contract_type: str | Unset = UNSET
        if not isinstance(self.contract_type, Unset):
            contract_type = self.contract_type.value if self.contract_type is not None else None

        workplace_type: str | Unset = UNSET
        if not isinstance(self.workplace_type, Unset):
            workplace_type = self.workplace_type.value if self.workplace_type is not None else None

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value if self.status is not None else None

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

        cv_requirement: str | Unset = UNSET
        if not isinstance(self.cv_requirement, Unset):
            cv_requirement = self.cv_requirement.value if self.cv_requirement is not None else None

        cover_letter_requirement: str | Unset = UNSET
        if not isinstance(self.cover_letter_requirement, Unset):
            cover_letter_requirement = self.cover_letter_requirement.value if self.cover_letter_requirement is not None else None

        phone_requirement: str | Unset = UNSET
        if not isinstance(self.phone_requirement, Unset):
            phone_requirement = self.phone_requirement.value if self.phone_requirement is not None else None

        photo_requirement: str | Unset = UNSET
        if not isinstance(self.photo_requirement, Unset):
            photo_requirement = self.photo_requirement.value if self.photo_requirement is not None else None

        personal_url_requirement: str | Unset = UNSET
        if not isinstance(self.personal_url_requirement, Unset):
            personal_url_requirement = self.personal_url_requirement.value if self.personal_url_requirement is not None else None

        salary_period: str | Unset = UNSET
        if not isinstance(self.salary_period, Unset):
            salary_period = self.salary_period.value if self.salary_period is not None else None

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if contract_type is not UNSET:
            field_dict["contract_type"] = contract_type
        if workplace_type is not UNSET:
            field_dict["workplace_type"] = workplace_type
        if status is not UNSET:
            field_dict["status"] = status
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
        if cv_requirement is not UNSET:
            field_dict["cv_requirement"] = cv_requirement
        if cover_letter_requirement is not UNSET:
            field_dict["cover_letter_requirement"] = cover_letter_requirement
        if phone_requirement is not UNSET:
            field_dict["phone_requirement"] = phone_requirement
        if photo_requirement is not UNSET:
            field_dict["photo_requirement"] = photo_requirement
        if personal_url_requirement is not UNSET:
            field_dict["personal_url_requirement"] = personal_url_requirement
        if salary_period is not UNSET:
            field_dict["salary_period"] = salary_period

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        _contract_type = d.pop("contract_type", UNSET)
        contract_type: PutApi20260401ResourcesAtsJobPostingsIdBodyContractType | Unset
        if isinstance(_contract_type, Unset):
            contract_type = UNSET
        else:
            contract_type = PutApi20260401ResourcesAtsJobPostingsIdBodyContractType(_contract_type) if _contract_type is not None else None

        _workplace_type = d.pop("workplace_type", UNSET)
        workplace_type: PutApi20260401ResourcesAtsJobPostingsIdBodyWorkplaceType | Unset
        if isinstance(_workplace_type, Unset):
            workplace_type = UNSET
        else:
            workplace_type = PutApi20260401ResourcesAtsJobPostingsIdBodyWorkplaceType(
                _workplace_type
            ) if _workplace_type is not None else None

        _status = d.pop("status", UNSET)
        status: PutApi20260401ResourcesAtsJobPostingsIdBodyStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = PutApi20260401ResourcesAtsJobPostingsIdBodyStatus(_status) if _status is not None else None

        _schedule_type = d.pop("schedule_type", UNSET)
        schedule_type: PutApi20260401ResourcesAtsJobPostingsIdBodyScheduleType | Unset
        if isinstance(_schedule_type, Unset):
            schedule_type = UNSET
        else:
            schedule_type = PutApi20260401ResourcesAtsJobPostingsIdBodyScheduleType(_schedule_type) if _schedule_type is not None else None

        team_id = d.pop("team_id", UNSET)

        location_id = d.pop("location_id", UNSET)

        _salary_format = d.pop("salary_format", UNSET)
        salary_format: PutApi20260401ResourcesAtsJobPostingsIdBodySalaryFormat | Unset
        if isinstance(_salary_format, Unset):
            salary_format = UNSET
        else:
            salary_format = PutApi20260401ResourcesAtsJobPostingsIdBodySalaryFormat(_salary_format) if _salary_format is not None else None

        salary_from_amount_in_cents = d.pop("salary_from_amount_in_cents", UNSET)

        salary_to_amount_in_cents = d.pop("salary_to_amount_in_cents", UNSET)

        _cv_requirement = d.pop("cv_requirement", UNSET)
        cv_requirement: PutApi20260401ResourcesAtsJobPostingsIdBodyCvRequirement | Unset
        if isinstance(_cv_requirement, Unset):
            cv_requirement = UNSET
        else:
            cv_requirement = PutApi20260401ResourcesAtsJobPostingsIdBodyCvRequirement(
                _cv_requirement
            ) if _cv_requirement is not None else None

        _cover_letter_requirement = d.pop("cover_letter_requirement", UNSET)
        cover_letter_requirement: (
            PutApi20260401ResourcesAtsJobPostingsIdBodyCoverLetterRequirement | Unset
        )
        if isinstance(_cover_letter_requirement, Unset):
            cover_letter_requirement = UNSET
        else:
            cover_letter_requirement = (
                PutApi20260401ResourcesAtsJobPostingsIdBodyCoverLetterRequirement(
                    _cover_letter_requirement
                ) if _cover_letter_requirement is not None else None
            )

        _phone_requirement = d.pop("phone_requirement", UNSET)
        phone_requirement: PutApi20260401ResourcesAtsJobPostingsIdBodyPhoneRequirement | Unset
        if isinstance(_phone_requirement, Unset):
            phone_requirement = UNSET
        else:
            phone_requirement = PutApi20260401ResourcesAtsJobPostingsIdBodyPhoneRequirement(
                _phone_requirement
            ) if _phone_requirement is not None else None

        _photo_requirement = d.pop("photo_requirement", UNSET)
        photo_requirement: PutApi20260401ResourcesAtsJobPostingsIdBodyPhotoRequirement | Unset
        if isinstance(_photo_requirement, Unset):
            photo_requirement = UNSET
        else:
            photo_requirement = PutApi20260401ResourcesAtsJobPostingsIdBodyPhotoRequirement(
                _photo_requirement
            ) if _photo_requirement is not None else None

        _personal_url_requirement = d.pop("personal_url_requirement", UNSET)
        personal_url_requirement: (
            PutApi20260401ResourcesAtsJobPostingsIdBodyPersonalUrlRequirement | Unset
        )
        if isinstance(_personal_url_requirement, Unset):
            personal_url_requirement = UNSET
        else:
            personal_url_requirement = (
                PutApi20260401ResourcesAtsJobPostingsIdBodyPersonalUrlRequirement(
                    _personal_url_requirement
                ) if _personal_url_requirement is not None else None
            )

        _salary_period = d.pop("salary_period", UNSET)
        salary_period: PutApi20260401ResourcesAtsJobPostingsIdBodySalaryPeriod | Unset
        if isinstance(_salary_period, Unset):
            salary_period = UNSET
        else:
            salary_period = PutApi20260401ResourcesAtsJobPostingsIdBodySalaryPeriod(_salary_period) if _salary_period is not None else None

        put_api_20260401_resources_ats_job_postings_id_body = cls(
            id=id,
            title=title,
            description=description,
            contract_type=contract_type,
            workplace_type=workplace_type,
            status=status,
            schedule_type=schedule_type,
            team_id=team_id,
            location_id=location_id,
            salary_format=salary_format,
            salary_from_amount_in_cents=salary_from_amount_in_cents,
            salary_to_amount_in_cents=salary_to_amount_in_cents,
            cv_requirement=cv_requirement,
            cover_letter_requirement=cover_letter_requirement,
            phone_requirement=phone_requirement,
            photo_requirement=photo_requirement,
            personal_url_requirement=personal_url_requirement,
            salary_period=salary_period,
        )

        put_api_20260401_resources_ats_job_postings_id_body.additional_properties = d
        return put_api_20260401_resources_ats_job_postings_id_body

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
