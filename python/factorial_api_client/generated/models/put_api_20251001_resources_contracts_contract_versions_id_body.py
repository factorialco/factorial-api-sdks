from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.put_api_20251001_resources_contracts_contract_versions_id_body_annual_working_time_distribution import (
    PutApi20251001ResourcesContractsContractVersionsIdBodyAnnualWorkingTimeDistribution,
)
from ..models.put_api_20251001_resources_contracts_contract_versions_id_body_bank_holiday_treatment import (
    PutApi20251001ResourcesContractsContractVersionsIdBodyBankHolidayTreatment,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PutApi20251001ResourcesContractsContractVersionsIdBody")


@_attrs_define
class PutApi20251001ResourcesContractsContractVersionsIdBody:
    id: int
    """ contract version identifier. """
    employee_id: int | Unset = UNSET
    """ employee identifier, refers to /employees/employees endpoint. """
    effective_on: str | Unset = UNSET
    """ the day the specific contract starts, in case of hiring the same than starts_on. """
    starts_on: str | Unset = UNSET
    """ the day the employee is hired. """
    ends_on: str | Unset = UNSET
    """ the day the employee is terminated. """
    working_hours_frequency: str | Unset = UNSET
    """ the frequency of the working hours. """
    working_week_days: str | Unset = UNSET
    """ the days of the week the employee works. """
    working_hours: int | Unset = UNSET
    """ the amount of hours the employee works. """
    salary_frequency: str | Unset = UNSET
    """ the frequency of the salary payment. When adding a salary to a contract that previously had none, both
    salary_amount and salary_frequency must be provided together. """
    salary_amount: int | Unset = UNSET
    """ the amount of money the employee earns. When adding a salary to a contract that previously had none, both
    salary_amount and salary_frequency must be provided together. """
    job_title: str | Unset = UNSET
    """ job title of the employee. """
    es_cotization_group: int | Unset = UNSET
    """ cotization group identifier. """
    es_professional_category_id: int | Unset = UNSET
    """ professional category identifier. """
    es_education_level_id: int | Unset = UNSET
    """ education level identifier. """
    es_contract_type_id: int | Unset = UNSET
    """ contract type identifier. """
    es_working_day_type_id: int | Unset = UNSET
    """ working day type identifier. """
    has_trial_period: bool | Unset = UNSET
    """ a flag that indicates if the employee has a trial period. """
    trial_period_ends_on: str | Unset = UNSET
    """ when the trial period ends. """
    bank_holiday_treatment: (
        PutApi20251001ResourcesContractsContractVersionsIdBodyBankHolidayTreatment | Unset
    ) = UNSET
    """ Defines whether a bank holiday should be considered as a workable or non-workable day. """
    working_time_percentage_in_cents: int | Unset = UNSET
    """ Working time percentage in cents (e.g., when an employee is working part-time, the percentage of full-time
    hours they are working). """
    annual_working_time_distribution: (
        PutApi20251001ResourcesContractsContractVersionsIdBodyAnnualWorkingTimeDistribution | Unset
    ) = UNSET
    """ Allows companies to define how annual working hours are spread across the year to ensure compliance with
    legal limits. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        employee_id = self.employee_id

        effective_on = self.effective_on

        starts_on = self.starts_on

        ends_on = self.ends_on

        working_hours_frequency = self.working_hours_frequency

        working_week_days = self.working_week_days

        working_hours = self.working_hours

        salary_frequency = self.salary_frequency

        salary_amount = self.salary_amount

        job_title = self.job_title

        es_cotization_group = self.es_cotization_group

        es_professional_category_id = self.es_professional_category_id

        es_education_level_id = self.es_education_level_id

        es_contract_type_id = self.es_contract_type_id

        es_working_day_type_id = self.es_working_day_type_id

        has_trial_period = self.has_trial_period

        trial_period_ends_on = self.trial_period_ends_on

        bank_holiday_treatment: str | Unset = UNSET
        if not isinstance(self.bank_holiday_treatment, Unset):
            bank_holiday_treatment = self.bank_holiday_treatment.value

        working_time_percentage_in_cents = self.working_time_percentage_in_cents

        annual_working_time_distribution: str | Unset = UNSET
        if not isinstance(self.annual_working_time_distribution, Unset):
            annual_working_time_distribution = self.annual_working_time_distribution.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if employee_id is not UNSET:
            field_dict["employee_id"] = employee_id
        if effective_on is not UNSET:
            field_dict["effective_on"] = effective_on
        if starts_on is not UNSET:
            field_dict["starts_on"] = starts_on
        if ends_on is not UNSET:
            field_dict["ends_on"] = ends_on
        if working_hours_frequency is not UNSET:
            field_dict["working_hours_frequency"] = working_hours_frequency
        if working_week_days is not UNSET:
            field_dict["working_week_days"] = working_week_days
        if working_hours is not UNSET:
            field_dict["working_hours"] = working_hours
        if salary_frequency is not UNSET:
            field_dict["salary_frequency"] = salary_frequency
        if salary_amount is not UNSET:
            field_dict["salary_amount"] = salary_amount
        if job_title is not UNSET:
            field_dict["job_title"] = job_title
        if es_cotization_group is not UNSET:
            field_dict["es_cotization_group"] = es_cotization_group
        if es_professional_category_id is not UNSET:
            field_dict["es_professional_category_id"] = es_professional_category_id
        if es_education_level_id is not UNSET:
            field_dict["es_education_level_id"] = es_education_level_id
        if es_contract_type_id is not UNSET:
            field_dict["es_contract_type_id"] = es_contract_type_id
        if es_working_day_type_id is not UNSET:
            field_dict["es_working_day_type_id"] = es_working_day_type_id
        if has_trial_period is not UNSET:
            field_dict["has_trial_period"] = has_trial_period
        if trial_period_ends_on is not UNSET:
            field_dict["trial_period_ends_on"] = trial_period_ends_on
        if bank_holiday_treatment is not UNSET:
            field_dict["bank_holiday_treatment"] = bank_holiday_treatment
        if working_time_percentage_in_cents is not UNSET:
            field_dict["working_time_percentage_in_cents"] = working_time_percentage_in_cents
        if annual_working_time_distribution is not UNSET:
            field_dict["annual_working_time_distribution"] = annual_working_time_distribution

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        employee_id = d.pop("employee_id", UNSET)

        effective_on = d.pop("effective_on", UNSET)

        starts_on = d.pop("starts_on", UNSET)

        ends_on = d.pop("ends_on", UNSET)

        working_hours_frequency = d.pop("working_hours_frequency", UNSET)

        working_week_days = d.pop("working_week_days", UNSET)

        working_hours = d.pop("working_hours", UNSET)

        salary_frequency = d.pop("salary_frequency", UNSET)

        salary_amount = d.pop("salary_amount", UNSET)

        job_title = d.pop("job_title", UNSET)

        es_cotization_group = d.pop("es_cotization_group", UNSET)

        es_professional_category_id = d.pop("es_professional_category_id", UNSET)

        es_education_level_id = d.pop("es_education_level_id", UNSET)

        es_contract_type_id = d.pop("es_contract_type_id", UNSET)

        es_working_day_type_id = d.pop("es_working_day_type_id", UNSET)

        has_trial_period = d.pop("has_trial_period", UNSET)

        trial_period_ends_on = d.pop("trial_period_ends_on", UNSET)

        _bank_holiday_treatment = d.pop("bank_holiday_treatment", UNSET)
        bank_holiday_treatment: (
            PutApi20251001ResourcesContractsContractVersionsIdBodyBankHolidayTreatment | Unset
        )
        if isinstance(_bank_holiday_treatment, Unset):
            bank_holiday_treatment = UNSET
        else:
            bank_holiday_treatment = (
                PutApi20251001ResourcesContractsContractVersionsIdBodyBankHolidayTreatment(
                    _bank_holiday_treatment
                )
            )

        working_time_percentage_in_cents = d.pop("working_time_percentage_in_cents", UNSET)

        _annual_working_time_distribution = d.pop("annual_working_time_distribution", UNSET)
        annual_working_time_distribution: (
            PutApi20251001ResourcesContractsContractVersionsIdBodyAnnualWorkingTimeDistribution
            | Unset
        )
        if isinstance(_annual_working_time_distribution, Unset):
            annual_working_time_distribution = UNSET
        else:
            annual_working_time_distribution = (
                PutApi20251001ResourcesContractsContractVersionsIdBodyAnnualWorkingTimeDistribution(
                    _annual_working_time_distribution
                )
            )

        put_api_20251001_resources_contracts_contract_versions_id_body = cls(
            id=id,
            employee_id=employee_id,
            effective_on=effective_on,
            starts_on=starts_on,
            ends_on=ends_on,
            working_hours_frequency=working_hours_frequency,
            working_week_days=working_week_days,
            working_hours=working_hours,
            salary_frequency=salary_frequency,
            salary_amount=salary_amount,
            job_title=job_title,
            es_cotization_group=es_cotization_group,
            es_professional_category_id=es_professional_category_id,
            es_education_level_id=es_education_level_id,
            es_contract_type_id=es_contract_type_id,
            es_working_day_type_id=es_working_day_type_id,
            has_trial_period=has_trial_period,
            trial_period_ends_on=trial_period_ends_on,
            bank_holiday_treatment=bank_holiday_treatment,
            working_time_percentage_in_cents=working_time_percentage_in_cents,
            annual_working_time_distribution=annual_working_time_distribution,
        )

        put_api_20251001_resources_contracts_contract_versions_id_body.additional_properties = d
        return put_api_20251001_resources_contracts_contract_versions_id_body

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
