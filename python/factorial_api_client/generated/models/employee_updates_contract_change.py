from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EmployeeUpdatesContractChange")


@_attrs_define
class EmployeeUpdatesContractChange:
    id: str
    """ The id of the contract change incidence """
    status: str
    """ The status of the contract change incidence """
    effective_on: str
    """ The effective date of the contract """
    employee_id: str
    """ The employee id """
    has_payroll: bool
    """ The payrollable status of the employee on the contract change """
    fr_forfait_jours: bool
    """ The forfait jours status on the contract change """
    created_at: str
    updated_at: str
    starts_on: str | Unset = UNSET
    """ The start date of the contract """
    ends_on: str | Unset = UNSET
    """ The end date of the contract """
    job_title: str | Unset = UNSET
    """ The job title on the contract change """
    job_role: str | Unset = UNSET
    """ The job role on the contract change """
    job_level: str | Unset = UNSET
    """ The job level on the contract change """
    salary_amount: int | Unset = UNSET
    """ The salary amount on the contract change in cents. """
    salary_frequency: str | Unset = UNSET
    """ The salary payment frequency on the contract change """
    working_week_days: str | Unset = UNSET
    """ The working week days on the contract change """
    working_hours: int | Unset = UNSET
    """ The working hours on the contract change """
    working_hours_frequency: str | Unset = UNSET
    """ The working hours frequency on the contract change """
    country: str | Unset = UNSET
    """ The country on the contract change """
    es_has_teleworking_contract: bool | Unset = UNSET
    """ The teleworking status on the contract change """
    es_cotization_group: int | Unset = UNSET
    """ The cotization group on the contract change """
    es_contract_observations: str | Unset = UNSET
    """ The contract observations on the contract change """
    es_job_description: str | Unset = UNSET
    """ The job description on the contract change """
    es_contract_type_id: str | Unset = UNSET
    """ The contract type id on the contract change """
    es_contract_type_name: str | Unset = UNSET
    """ The contract type name on the contract change """
    es_trial_period_ends_on: str | Unset = UNSET
    """ The trial period end date on the contract change """
    es_working_day_type_id: str | Unset = UNSET
    """ The working day type id on the contract change """
    es_education_level_id: str | Unset = UNSET
    """ The education level id on the contract change """
    es_professional_category_id: str | Unset = UNSET
    """ The professional category id on the contract change """
    fr_employee_type: str | Unset = UNSET
    """ The employee type on the contract change """
    fr_jours_par_an: int | Unset = UNSET
    """ The jours par an on the contract change """
    fr_coefficient: str | Unset = UNSET
    """ The coefficient on the contract change """
    fr_level_id: str | Unset = UNSET
    """ The level id on the contract change """
    fr_level_name: str | Unset = UNSET
    """ The level name on the contract change """
    fr_step_id: str | Unset = UNSET
    """ The step id on the contract change """
    fr_step_name: str | Unset = UNSET
    """ The step name on the contract change """
    fr_mutual_id: str | Unset = UNSET
    """ The mutual id on the contract change """
    fr_mutual_name: str | Unset = UNSET
    """ The mutual name on the contract change """
    fr_professional_category_id: str | Unset = UNSET
    """ The professional category id on the contract change """
    fr_professional_category_name: str | Unset = UNSET
    """ The professional category name on the contract change """
    fr_work_type_id: str | Unset = UNSET
    """ The work type id on the contract change """
    fr_work_type_name: str | Unset = UNSET
    """ The work type name on the contract change """
    compensation_ids: list[str] | Unset = UNSET
    fr_contract_type_id: str | Unset = UNSET
    """ The contract type id on the contract change """
    fr_contract_type_name: str | Unset = UNSET
    """ The contract type name on the contract change """
    de_contract_type_id: str | Unset = UNSET
    """ The contract type id on the contract change """
    de_contract_type_name: str | Unset = UNSET
    """ The contract type name on the contract change """
    pt_contract_type_id: str | Unset = UNSET
    """ The contract type id on the contract change """
    pt_contract_type_name: str | Unset = UNSET
    """ The contract type name on the contract change """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        status = self.status

        effective_on = self.effective_on

        employee_id = self.employee_id

        has_payroll = self.has_payroll

        fr_forfait_jours = self.fr_forfait_jours

        created_at = self.created_at

        updated_at = self.updated_at

        starts_on = self.starts_on

        ends_on = self.ends_on

        job_title = self.job_title

        job_role = self.job_role

        job_level = self.job_level

        salary_amount = self.salary_amount

        salary_frequency = self.salary_frequency

        working_week_days = self.working_week_days

        working_hours = self.working_hours

        working_hours_frequency = self.working_hours_frequency

        country = self.country

        es_has_teleworking_contract = self.es_has_teleworking_contract

        es_cotization_group = self.es_cotization_group

        es_contract_observations = self.es_contract_observations

        es_job_description = self.es_job_description

        es_contract_type_id = self.es_contract_type_id

        es_contract_type_name = self.es_contract_type_name

        es_trial_period_ends_on = self.es_trial_period_ends_on

        es_working_day_type_id = self.es_working_day_type_id

        es_education_level_id = self.es_education_level_id

        es_professional_category_id = self.es_professional_category_id

        fr_employee_type = self.fr_employee_type

        fr_jours_par_an = self.fr_jours_par_an

        fr_coefficient = self.fr_coefficient

        fr_level_id = self.fr_level_id

        fr_level_name = self.fr_level_name

        fr_step_id = self.fr_step_id

        fr_step_name = self.fr_step_name

        fr_mutual_id = self.fr_mutual_id

        fr_mutual_name = self.fr_mutual_name

        fr_professional_category_id = self.fr_professional_category_id

        fr_professional_category_name = self.fr_professional_category_name

        fr_work_type_id = self.fr_work_type_id

        fr_work_type_name = self.fr_work_type_name

        compensation_ids: list[str] | Unset = UNSET
        if not isinstance(self.compensation_ids, Unset):
            compensation_ids = self.compensation_ids

        fr_contract_type_id = self.fr_contract_type_id

        fr_contract_type_name = self.fr_contract_type_name

        de_contract_type_id = self.de_contract_type_id

        de_contract_type_name = self.de_contract_type_name

        pt_contract_type_id = self.pt_contract_type_id

        pt_contract_type_name = self.pt_contract_type_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "status": status,
                "effective_on": effective_on,
                "employee_id": employee_id,
                "has_payroll": has_payroll,
                "fr_forfait_jours": fr_forfait_jours,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if starts_on is not UNSET:
            field_dict["starts_on"] = starts_on
        if ends_on is not UNSET:
            field_dict["ends_on"] = ends_on
        if job_title is not UNSET:
            field_dict["job_title"] = job_title
        if job_role is not UNSET:
            field_dict["job_role"] = job_role
        if job_level is not UNSET:
            field_dict["job_level"] = job_level
        if salary_amount is not UNSET:
            field_dict["salary_amount"] = salary_amount
        if salary_frequency is not UNSET:
            field_dict["salary_frequency"] = salary_frequency
        if working_week_days is not UNSET:
            field_dict["working_week_days"] = working_week_days
        if working_hours is not UNSET:
            field_dict["working_hours"] = working_hours
        if working_hours_frequency is not UNSET:
            field_dict["working_hours_frequency"] = working_hours_frequency
        if country is not UNSET:
            field_dict["country"] = country
        if es_has_teleworking_contract is not UNSET:
            field_dict["es_has_teleworking_contract"] = es_has_teleworking_contract
        if es_cotization_group is not UNSET:
            field_dict["es_cotization_group"] = es_cotization_group
        if es_contract_observations is not UNSET:
            field_dict["es_contract_observations"] = es_contract_observations
        if es_job_description is not UNSET:
            field_dict["es_job_description"] = es_job_description
        if es_contract_type_id is not UNSET:
            field_dict["es_contract_type_id"] = es_contract_type_id
        if es_contract_type_name is not UNSET:
            field_dict["es_contract_type_name"] = es_contract_type_name
        if es_trial_period_ends_on is not UNSET:
            field_dict["es_trial_period_ends_on"] = es_trial_period_ends_on
        if es_working_day_type_id is not UNSET:
            field_dict["es_working_day_type_id"] = es_working_day_type_id
        if es_education_level_id is not UNSET:
            field_dict["es_education_level_id"] = es_education_level_id
        if es_professional_category_id is not UNSET:
            field_dict["es_professional_category_id"] = es_professional_category_id
        if fr_employee_type is not UNSET:
            field_dict["fr_employee_type"] = fr_employee_type
        if fr_jours_par_an is not UNSET:
            field_dict["fr_jours_par_an"] = fr_jours_par_an
        if fr_coefficient is not UNSET:
            field_dict["fr_coefficient"] = fr_coefficient
        if fr_level_id is not UNSET:
            field_dict["fr_level_id"] = fr_level_id
        if fr_level_name is not UNSET:
            field_dict["fr_level_name"] = fr_level_name
        if fr_step_id is not UNSET:
            field_dict["fr_step_id"] = fr_step_id
        if fr_step_name is not UNSET:
            field_dict["fr_step_name"] = fr_step_name
        if fr_mutual_id is not UNSET:
            field_dict["fr_mutual_id"] = fr_mutual_id
        if fr_mutual_name is not UNSET:
            field_dict["fr_mutual_name"] = fr_mutual_name
        if fr_professional_category_id is not UNSET:
            field_dict["fr_professional_category_id"] = fr_professional_category_id
        if fr_professional_category_name is not UNSET:
            field_dict["fr_professional_category_name"] = fr_professional_category_name
        if fr_work_type_id is not UNSET:
            field_dict["fr_work_type_id"] = fr_work_type_id
        if fr_work_type_name is not UNSET:
            field_dict["fr_work_type_name"] = fr_work_type_name
        if compensation_ids is not UNSET:
            field_dict["compensation_ids"] = compensation_ids
        if fr_contract_type_id is not UNSET:
            field_dict["fr_contract_type_id"] = fr_contract_type_id
        if fr_contract_type_name is not UNSET:
            field_dict["fr_contract_type_name"] = fr_contract_type_name
        if de_contract_type_id is not UNSET:
            field_dict["de_contract_type_id"] = de_contract_type_id
        if de_contract_type_name is not UNSET:
            field_dict["de_contract_type_name"] = de_contract_type_name
        if pt_contract_type_id is not UNSET:
            field_dict["pt_contract_type_id"] = pt_contract_type_id
        if pt_contract_type_name is not UNSET:
            field_dict["pt_contract_type_name"] = pt_contract_type_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        status = d.pop("status")

        effective_on = d.pop("effective_on")

        employee_id = d.pop("employee_id")

        has_payroll = d.pop("has_payroll")

        fr_forfait_jours = d.pop("fr_forfait_jours")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        starts_on = d.pop("starts_on", UNSET)

        ends_on = d.pop("ends_on", UNSET)

        job_title = d.pop("job_title", UNSET)

        job_role = d.pop("job_role", UNSET)

        job_level = d.pop("job_level", UNSET)

        salary_amount = d.pop("salary_amount", UNSET)

        salary_frequency = d.pop("salary_frequency", UNSET)

        working_week_days = d.pop("working_week_days", UNSET)

        working_hours = d.pop("working_hours", UNSET)

        working_hours_frequency = d.pop("working_hours_frequency", UNSET)

        country = d.pop("country", UNSET)

        es_has_teleworking_contract = d.pop("es_has_teleworking_contract", UNSET)

        es_cotization_group = d.pop("es_cotization_group", UNSET)

        es_contract_observations = d.pop("es_contract_observations", UNSET)

        es_job_description = d.pop("es_job_description", UNSET)

        es_contract_type_id = d.pop("es_contract_type_id", UNSET)

        es_contract_type_name = d.pop("es_contract_type_name", UNSET)

        es_trial_period_ends_on = d.pop("es_trial_period_ends_on", UNSET)

        es_working_day_type_id = d.pop("es_working_day_type_id", UNSET)

        es_education_level_id = d.pop("es_education_level_id", UNSET)

        es_professional_category_id = d.pop("es_professional_category_id", UNSET)

        fr_employee_type = d.pop("fr_employee_type", UNSET)

        fr_jours_par_an = d.pop("fr_jours_par_an", UNSET)

        fr_coefficient = d.pop("fr_coefficient", UNSET)

        fr_level_id = d.pop("fr_level_id", UNSET)

        fr_level_name = d.pop("fr_level_name", UNSET)

        fr_step_id = d.pop("fr_step_id", UNSET)

        fr_step_name = d.pop("fr_step_name", UNSET)

        fr_mutual_id = d.pop("fr_mutual_id", UNSET)

        fr_mutual_name = d.pop("fr_mutual_name", UNSET)

        fr_professional_category_id = d.pop("fr_professional_category_id", UNSET)

        fr_professional_category_name = d.pop("fr_professional_category_name", UNSET)

        fr_work_type_id = d.pop("fr_work_type_id", UNSET)

        fr_work_type_name = d.pop("fr_work_type_name", UNSET)

        compensation_ids = cast(list[str], d.pop("compensation_ids", UNSET))

        fr_contract_type_id = d.pop("fr_contract_type_id", UNSET)

        fr_contract_type_name = d.pop("fr_contract_type_name", UNSET)

        de_contract_type_id = d.pop("de_contract_type_id", UNSET)

        de_contract_type_name = d.pop("de_contract_type_name", UNSET)

        pt_contract_type_id = d.pop("pt_contract_type_id", UNSET)

        pt_contract_type_name = d.pop("pt_contract_type_name", UNSET)

        employee_updates_contract_change = cls(
            id=id,
            status=status,
            effective_on=effective_on,
            employee_id=employee_id,
            has_payroll=has_payroll,
            fr_forfait_jours=fr_forfait_jours,
            created_at=created_at,
            updated_at=updated_at,
            starts_on=starts_on,
            ends_on=ends_on,
            job_title=job_title,
            job_role=job_role,
            job_level=job_level,
            salary_amount=salary_amount,
            salary_frequency=salary_frequency,
            working_week_days=working_week_days,
            working_hours=working_hours,
            working_hours_frequency=working_hours_frequency,
            country=country,
            es_has_teleworking_contract=es_has_teleworking_contract,
            es_cotization_group=es_cotization_group,
            es_contract_observations=es_contract_observations,
            es_job_description=es_job_description,
            es_contract_type_id=es_contract_type_id,
            es_contract_type_name=es_contract_type_name,
            es_trial_period_ends_on=es_trial_period_ends_on,
            es_working_day_type_id=es_working_day_type_id,
            es_education_level_id=es_education_level_id,
            es_professional_category_id=es_professional_category_id,
            fr_employee_type=fr_employee_type,
            fr_jours_par_an=fr_jours_par_an,
            fr_coefficient=fr_coefficient,
            fr_level_id=fr_level_id,
            fr_level_name=fr_level_name,
            fr_step_id=fr_step_id,
            fr_step_name=fr_step_name,
            fr_mutual_id=fr_mutual_id,
            fr_mutual_name=fr_mutual_name,
            fr_professional_category_id=fr_professional_category_id,
            fr_professional_category_name=fr_professional_category_name,
            fr_work_type_id=fr_work_type_id,
            fr_work_type_name=fr_work_type_name,
            compensation_ids=compensation_ids,
            fr_contract_type_id=fr_contract_type_id,
            fr_contract_type_name=fr_contract_type_name,
            de_contract_type_id=de_contract_type_id,
            de_contract_type_name=de_contract_type_name,
            pt_contract_type_id=pt_contract_type_id,
            pt_contract_type_name=pt_contract_type_name,
        )

        employee_updates_contract_change.additional_properties = d
        return employee_updates_contract_change

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
