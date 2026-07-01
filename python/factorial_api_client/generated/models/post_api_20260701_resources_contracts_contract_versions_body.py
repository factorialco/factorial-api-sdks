from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_api_20260701_resources_contracts_contract_versions_body_annual_working_time_distribution import (
    PostApi20260701ResourcesContractsContractVersionsBodyAnnualWorkingTimeDistribution,
)
from ..models.post_api_20260701_resources_contracts_contract_versions_body_bank_holiday_treatment import (
    PostApi20260701ResourcesContractsContractVersionsBodyBankHolidayTreatment,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20260701ResourcesContractsContractVersionsBody")


@_attrs_define
class PostApi20260701ResourcesContractsContractVersionsBody:
    employee_id: str
    """ employee identifier, refers to /employees/employees endpoint. """
    effective_on: str
    """ the day the specific contract starts, in case of hiring the same than starts_on. """
    starts_on: str
    """ the day the employee is hired. """
    ends_on: str | Unset = UNSET
    """ the day the employee is terminated. """
    working_hours_frequency: str | Unset = UNSET
    """ the frequency of the working hours. """
    working_week_days: str | Unset = UNSET
    """ the days of the week the employee works. """
    working_hours: int | Unset = UNSET
    """ the amount of hours the employee works. """
    max_legal_yearly_hours: int | Unset = UNSET
    """ the maximum amount of hours the employee can work in a year. """
    maximum_weekly_hours: int | Unset = UNSET
    """ the maximum amount of hours the employee can work in a week. """
    min_rest_minutes_between_days: int | Unset = UNSET
    """ the minimum amount of minutes the employee must rest between working periods. """
    max_work_minutes_per_day: int | Unset = UNSET
    """ the maximum amount of minutes the employee can work in a day. """
    max_work_days_in_row: int | Unset = UNSET
    """ the maximum amount of days the employee can work in a row. """
    min_rest_hours_in_row: int | Unset = UNSET
    """ the minimum amount of hours the employee must rest in a row. """
    salary_frequency: str | Unset = UNSET
    """ the frequency of the salary payment. When adding a salary to a contract that previously had none, both
    salary_amount and salary_frequency must be provided together. """
    salary_amount: int | Unset = UNSET
    """ the amount of money the employee earns in cents. """
    job_title: str | Unset = UNSET
    """ job title of the employee. """
    has_trial_period: bool | Unset = UNSET
    """ a flag that indicates if the employee has a trial period. """
    trial_period_ends_on: str | Unset = UNSET
    """ when the trial period ends. """
    working_time_percentage_in_cents: int | Unset = UNSET
    """ Working time percentage in cents (e.g., when an employee is working part-time, the percentage of full-time
    hours they are working). """
    annual_working_time_distribution: (
        PostApi20260701ResourcesContractsContractVersionsBodyAnnualWorkingTimeDistribution | Unset
    ) = UNSET
    """ Allows companies to define how annual working hours are spread across the year to ensure compliance with
    legal limits. """
    copy_current_contract_version: bool | Unset = UNSET
    """ wether to copy the current contract version. """
    bank_holiday_treatment: (
        PostApi20260701ResourcesContractsContractVersionsBodyBankHolidayTreatment | Unset
    ) = UNSET
    """ Defines whether a bank holiday should be considered as a workable or non-workable day. """
    job_catalog_tree_node_uuid: str | Unset = UNSET
    """ the uuid node in the job catalog tree. For now it only supports level nodes. From this point in the job
    catalog tree you can get the full ancestor path to the root node including the role. Refer to
    job_catalog/tree_nodes endpoint. """
    de_base_salary_type_id: str | Unset = UNSET
    """ Identifier for the German base salary type. References a payroll concept available via the /payroll/concepts
    endpoint. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        employee_id = self.employee_id

        effective_on = self.effective_on

        starts_on = self.starts_on

        ends_on = self.ends_on

        working_hours_frequency = self.working_hours_frequency

        working_week_days = self.working_week_days

        working_hours = self.working_hours

        max_legal_yearly_hours = self.max_legal_yearly_hours

        maximum_weekly_hours = self.maximum_weekly_hours

        min_rest_minutes_between_days = self.min_rest_minutes_between_days

        max_work_minutes_per_day = self.max_work_minutes_per_day

        max_work_days_in_row = self.max_work_days_in_row

        min_rest_hours_in_row = self.min_rest_hours_in_row

        salary_frequency = self.salary_frequency

        salary_amount = self.salary_amount

        job_title = self.job_title

        has_trial_period = self.has_trial_period

        trial_period_ends_on = self.trial_period_ends_on

        working_time_percentage_in_cents = self.working_time_percentage_in_cents

        annual_working_time_distribution: str | Unset = UNSET
        if not isinstance(self.annual_working_time_distribution, Unset):
            annual_working_time_distribution = self.annual_working_time_distribution.value

        copy_current_contract_version = self.copy_current_contract_version

        bank_holiday_treatment: str | Unset = UNSET
        if not isinstance(self.bank_holiday_treatment, Unset):
            bank_holiday_treatment = self.bank_holiday_treatment.value

        job_catalog_tree_node_uuid = self.job_catalog_tree_node_uuid

        de_base_salary_type_id = self.de_base_salary_type_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "employee_id": employee_id,
                "effective_on": effective_on,
                "starts_on": starts_on,
            }
        )
        if ends_on is not UNSET:
            field_dict["ends_on"] = ends_on
        if working_hours_frequency is not UNSET:
            field_dict["working_hours_frequency"] = working_hours_frequency
        if working_week_days is not UNSET:
            field_dict["working_week_days"] = working_week_days
        if working_hours is not UNSET:
            field_dict["working_hours"] = working_hours
        if max_legal_yearly_hours is not UNSET:
            field_dict["max_legal_yearly_hours"] = max_legal_yearly_hours
        if maximum_weekly_hours is not UNSET:
            field_dict["maximum_weekly_hours"] = maximum_weekly_hours
        if min_rest_minutes_between_days is not UNSET:
            field_dict["min_rest_minutes_between_days"] = min_rest_minutes_between_days
        if max_work_minutes_per_day is not UNSET:
            field_dict["max_work_minutes_per_day"] = max_work_minutes_per_day
        if max_work_days_in_row is not UNSET:
            field_dict["max_work_days_in_row"] = max_work_days_in_row
        if min_rest_hours_in_row is not UNSET:
            field_dict["min_rest_hours_in_row"] = min_rest_hours_in_row
        if salary_frequency is not UNSET:
            field_dict["salary_frequency"] = salary_frequency
        if salary_amount is not UNSET:
            field_dict["salary_amount"] = salary_amount
        if job_title is not UNSET:
            field_dict["job_title"] = job_title
        if has_trial_period is not UNSET:
            field_dict["has_trial_period"] = has_trial_period
        if trial_period_ends_on is not UNSET:
            field_dict["trial_period_ends_on"] = trial_period_ends_on
        if working_time_percentage_in_cents is not UNSET:
            field_dict["working_time_percentage_in_cents"] = working_time_percentage_in_cents
        if annual_working_time_distribution is not UNSET:
            field_dict["annual_working_time_distribution"] = annual_working_time_distribution
        if copy_current_contract_version is not UNSET:
            field_dict["copy_current_contract_version"] = copy_current_contract_version
        if bank_holiday_treatment is not UNSET:
            field_dict["bank_holiday_treatment"] = bank_holiday_treatment
        if job_catalog_tree_node_uuid is not UNSET:
            field_dict["job_catalog_tree_node_uuid"] = job_catalog_tree_node_uuid
        if de_base_salary_type_id is not UNSET:
            field_dict["de_base_salary_type_id"] = de_base_salary_type_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        employee_id = d.pop("employee_id")

        effective_on = d.pop("effective_on")

        starts_on = d.pop("starts_on")

        ends_on = d.pop("ends_on", UNSET)

        working_hours_frequency = d.pop("working_hours_frequency", UNSET)

        working_week_days = d.pop("working_week_days", UNSET)

        working_hours = d.pop("working_hours", UNSET)

        max_legal_yearly_hours = d.pop("max_legal_yearly_hours", UNSET)

        maximum_weekly_hours = d.pop("maximum_weekly_hours", UNSET)

        min_rest_minutes_between_days = d.pop("min_rest_minutes_between_days", UNSET)

        max_work_minutes_per_day = d.pop("max_work_minutes_per_day", UNSET)

        max_work_days_in_row = d.pop("max_work_days_in_row", UNSET)

        min_rest_hours_in_row = d.pop("min_rest_hours_in_row", UNSET)

        salary_frequency = d.pop("salary_frequency", UNSET)

        salary_amount = d.pop("salary_amount", UNSET)

        job_title = d.pop("job_title", UNSET)

        has_trial_period = d.pop("has_trial_period", UNSET)

        trial_period_ends_on = d.pop("trial_period_ends_on", UNSET)

        working_time_percentage_in_cents = d.pop("working_time_percentage_in_cents", UNSET)

        _annual_working_time_distribution = d.pop("annual_working_time_distribution", UNSET)
        annual_working_time_distribution: (
            PostApi20260701ResourcesContractsContractVersionsBodyAnnualWorkingTimeDistribution
            | Unset
        )
        if isinstance(_annual_working_time_distribution, Unset):
            annual_working_time_distribution = UNSET
        else:
            annual_working_time_distribution = (
                PostApi20260701ResourcesContractsContractVersionsBodyAnnualWorkingTimeDistribution(
                    _annual_working_time_distribution
                )
            )

        copy_current_contract_version = d.pop("copy_current_contract_version", UNSET)

        _bank_holiday_treatment = d.pop("bank_holiday_treatment", UNSET)
        bank_holiday_treatment: (
            PostApi20260701ResourcesContractsContractVersionsBodyBankHolidayTreatment | Unset
        )
        if isinstance(_bank_holiday_treatment, Unset):
            bank_holiday_treatment = UNSET
        else:
            bank_holiday_treatment = (
                PostApi20260701ResourcesContractsContractVersionsBodyBankHolidayTreatment(
                    _bank_holiday_treatment
                )
            )

        job_catalog_tree_node_uuid = d.pop("job_catalog_tree_node_uuid", UNSET)

        de_base_salary_type_id = d.pop("de_base_salary_type_id", UNSET)

        post_api_20260701_resources_contracts_contract_versions_body = cls(
            employee_id=employee_id,
            effective_on=effective_on,
            starts_on=starts_on,
            ends_on=ends_on,
            working_hours_frequency=working_hours_frequency,
            working_week_days=working_week_days,
            working_hours=working_hours,
            max_legal_yearly_hours=max_legal_yearly_hours,
            maximum_weekly_hours=maximum_weekly_hours,
            min_rest_minutes_between_days=min_rest_minutes_between_days,
            max_work_minutes_per_day=max_work_minutes_per_day,
            max_work_days_in_row=max_work_days_in_row,
            min_rest_hours_in_row=min_rest_hours_in_row,
            salary_frequency=salary_frequency,
            salary_amount=salary_amount,
            job_title=job_title,
            has_trial_period=has_trial_period,
            trial_period_ends_on=trial_period_ends_on,
            working_time_percentage_in_cents=working_time_percentage_in_cents,
            annual_working_time_distribution=annual_working_time_distribution,
            copy_current_contract_version=copy_current_contract_version,
            bank_holiday_treatment=bank_holiday_treatment,
            job_catalog_tree_node_uuid=job_catalog_tree_node_uuid,
            de_base_salary_type_id=de_base_salary_type_id,
        )

        post_api_20260701_resources_contracts_contract_versions_body.additional_properties = d
        return post_api_20260701_resources_contracts_contract_versions_body

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
