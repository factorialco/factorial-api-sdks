from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.contracts_contract_version_annual_working_time_distribution import (
    ContractsContractVersionAnnualWorkingTimeDistribution,
)
from ..models.contracts_contract_version_bank_holiday_treatment import (
    ContractsContractVersionBankHolidayTreatment,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contracts_contract_version_version_data import ContractsContractVersionVersionData


T = TypeVar("T", bound="ContractsContractVersion")


@_attrs_define
class ContractsContractVersion:
    company_id: str
    """ identifier for company. """
    employee_id: str
    """ employee identifier, refers to /employees/employees endpoint. """
    effective_on: str
    """ the day the specific contract starts, in case of hiring the same than starts_on. """
    has_payroll: bool
    """ boolean that indicates if the employee asociated to this contract belongs to a payroll policy. """
    bank_holiday_treatment: ContractsContractVersionBankHolidayTreatment
    """ Defines whether a bank holiday should be considered as a workable or non-workable day. """
    created_at: str
    """ the date the contract version was created. """
    updated_at: str
    """ the date of the last contract version updated. """
    fr_forfait_jours: bool
    """ flag that indicates if the employee is allowed to work within the framework of a fixed number of days. """
    id: str | Unset = UNSET
    """ identifier for the contract version. """
    country: str | Unset = UNSET
    """ nationality country code of the employee (Spain ES, United Kingdom GB). """
    job_title: str | Unset = UNSET
    """ job title of the employee. """
    job_catalog_level_id: str | Unset = UNSET
    """ job catalog level identifier, refers to /job_catalog/levels endpoint. """
    job_catalog_tree_node_uuid: str | Unset = UNSET
    """ the uuid node in the job catalog tree. For now it only supports level nodes. From this point in the job
    catalog tree you can get the full ancestor path to the root node including the role. Refer to
    job_catalog/tree_nodes endpoint. """
    starts_on: str | Unset = UNSET
    """ the day the employee is hired. """
    ends_on: str | Unset = UNSET
    """ the day the employee is terminated. It has nothing to do with trial period, these are concepts totally
    unrelated. """
    has_trial_period: bool | Unset = UNSET
    """ a flag that indicates if the contract version has ever had a trial period. """
    trial_period_ends_on: str | Unset = UNSET
    """ when the trial period ends. If there is no date, it means that the employee has never been in trial. This
    date is not related with the end date of a contract. """
    salary_amount: int | Unset = UNSET
    """ the amount of money the employee earns in cents. """
    salary_frequency: str | Unset = UNSET
    """ the frequency of the salary payment. """
    working_week_days: str | Unset = UNSET
    """ the days of the week the employee works. """
    working_hours: int | Unset = UNSET
    """ the amount of hours the employee works. """
    working_hours_frequency: str | Unset = UNSET
    """ the frequency of the working hours. """
    max_legal_yearly_hours: int | Unset = UNSET
    """ the maximum amount of hours the employee can work in a year. """
    maximum_weekly_hours: int | Unset = UNSET
    """ the maximum amount of hours the employee can work in a week. """
    working_time_percentage_in_cents: int | Unset = UNSET
    """ Working time percentage in cents (e.g., when an employee is working part-time, the percentage of full-time
    hours they are working). """
    annual_working_time_distribution: (
        ContractsContractVersionAnnualWorkingTimeDistribution | Unset
    ) = UNSET
    """ Allows companies to define how annual working hours are spread across the year to ensure compliance with
    legal limits. """
    version_data: ContractsContractVersionVersionData | Unset = UNSET
    """ Country-specific contract data (template fragments and fields). """
    min_rest_minutes_between_days: int | Unset = UNSET
    """ the minimum amount of minutes the employee must rest between working periods. """
    max_work_minutes_per_day: int | Unset = UNSET
    """ the maximum amount of minutes the employee can work in a day. """
    max_work_days_in_row: int | Unset = UNSET
    """ the maximum amount of days the employee can work in a row. """
    min_rest_hours_in_row: int | Unset = UNSET
    """ the minimum amount of hours the employee must rest in a row. """
    es_has_teleworking_contract: bool | Unset = UNSET
    """ flag that indicates if the contract has teleworking. """
    es_cotization_group: int | Unset = UNSET
    """ the group of cotization of the employee. """
    contracts_es_tariff_group_id: str | Unset = UNSET
    """ the group of cotization of the employee. """
    es_contract_observations: str | Unset = UNSET
    """ observations of the contract. """
    es_job_description: str | Unset = UNSET
    """ the job description of the employee. """
    es_contract_type_id: str | Unset = UNSET
    """ contract type identifier. """
    es_working_day_type_id: str | Unset = UNSET
    """ working day type identifier. """
    es_education_level_id: str | Unset = UNSET
    """ education level identifier. """
    es_professional_category_id: str | Unset = UNSET
    """ professional category identifier. """
    fr_employee_type: str | Unset = UNSET
    """ employee type. """
    fr_jours_par_an: int | Unset = UNSET
    """ the number of days the employee is allowed to work. """
    fr_coefficient: str | Unset = UNSET
    """ coefficient for france contracts. """
    fr_contract_type_id: str | Unset = UNSET
    """ contract type identifier. """
    fr_level_id: str | Unset = UNSET
    """ level identifier. """
    fr_step_id: str | Unset = UNSET
    """ step identifier. """
    fr_mutual_id: str | Unset = UNSET
    """ mutual identifier. """
    fr_professional_category_id: str | Unset = UNSET
    """ professional category identifier. """
    fr_work_type_id: str | Unset = UNSET
    """ work type identifier. """
    de_contract_type_id: str | Unset = UNSET
    """ contract type identifier. """
    de_base_salary_type_id: str | Unset = UNSET
    """ Identifier for the German base salary type. References a payroll concept available via the /payroll/concepts
    endpoint. """
    pt_contract_type_id: str | Unset = UNSET
    """ contract type identifier. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company_id = self.company_id

        employee_id = self.employee_id

        effective_on = self.effective_on

        has_payroll = self.has_payroll

        bank_holiday_treatment = self.bank_holiday_treatment.value

        created_at = self.created_at

        updated_at = self.updated_at

        fr_forfait_jours = self.fr_forfait_jours

        id = self.id

        country = self.country

        job_title = self.job_title

        job_catalog_level_id = self.job_catalog_level_id

        job_catalog_tree_node_uuid = self.job_catalog_tree_node_uuid

        starts_on = self.starts_on

        ends_on = self.ends_on

        has_trial_period = self.has_trial_period

        trial_period_ends_on = self.trial_period_ends_on

        salary_amount = self.salary_amount

        salary_frequency = self.salary_frequency

        working_week_days = self.working_week_days

        working_hours = self.working_hours

        working_hours_frequency = self.working_hours_frequency

        max_legal_yearly_hours = self.max_legal_yearly_hours

        maximum_weekly_hours = self.maximum_weekly_hours

        working_time_percentage_in_cents = self.working_time_percentage_in_cents

        annual_working_time_distribution: str | Unset = UNSET
        if not isinstance(self.annual_working_time_distribution, Unset):
            annual_working_time_distribution = self.annual_working_time_distribution.value

        version_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.version_data, Unset):
            version_data = self.version_data.to_dict()

        min_rest_minutes_between_days = self.min_rest_minutes_between_days

        max_work_minutes_per_day = self.max_work_minutes_per_day

        max_work_days_in_row = self.max_work_days_in_row

        min_rest_hours_in_row = self.min_rest_hours_in_row

        es_has_teleworking_contract = self.es_has_teleworking_contract

        es_cotization_group = self.es_cotization_group

        contracts_es_tariff_group_id = self.contracts_es_tariff_group_id

        es_contract_observations = self.es_contract_observations

        es_job_description = self.es_job_description

        es_contract_type_id = self.es_contract_type_id

        es_working_day_type_id = self.es_working_day_type_id

        es_education_level_id = self.es_education_level_id

        es_professional_category_id = self.es_professional_category_id

        fr_employee_type = self.fr_employee_type

        fr_jours_par_an = self.fr_jours_par_an

        fr_coefficient = self.fr_coefficient

        fr_contract_type_id = self.fr_contract_type_id

        fr_level_id = self.fr_level_id

        fr_step_id = self.fr_step_id

        fr_mutual_id = self.fr_mutual_id

        fr_professional_category_id = self.fr_professional_category_id

        fr_work_type_id = self.fr_work_type_id

        de_contract_type_id = self.de_contract_type_id

        de_base_salary_type_id = self.de_base_salary_type_id

        pt_contract_type_id = self.pt_contract_type_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "company_id": company_id,
                "employee_id": employee_id,
                "effective_on": effective_on,
                "has_payroll": has_payroll,
                "bank_holiday_treatment": bank_holiday_treatment,
                "created_at": created_at,
                "updated_at": updated_at,
                "fr_forfait_jours": fr_forfait_jours,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if country is not UNSET:
            field_dict["country"] = country
        if job_title is not UNSET:
            field_dict["job_title"] = job_title
        if job_catalog_level_id is not UNSET:
            field_dict["job_catalog_level_id"] = job_catalog_level_id
        if job_catalog_tree_node_uuid is not UNSET:
            field_dict["job_catalog_tree_node_uuid"] = job_catalog_tree_node_uuid
        if starts_on is not UNSET:
            field_dict["starts_on"] = starts_on
        if ends_on is not UNSET:
            field_dict["ends_on"] = ends_on
        if has_trial_period is not UNSET:
            field_dict["has_trial_period"] = has_trial_period
        if trial_period_ends_on is not UNSET:
            field_dict["trial_period_ends_on"] = trial_period_ends_on
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
        if max_legal_yearly_hours is not UNSET:
            field_dict["max_legal_yearly_hours"] = max_legal_yearly_hours
        if maximum_weekly_hours is not UNSET:
            field_dict["maximum_weekly_hours"] = maximum_weekly_hours
        if working_time_percentage_in_cents is not UNSET:
            field_dict["working_time_percentage_in_cents"] = working_time_percentage_in_cents
        if annual_working_time_distribution is not UNSET:
            field_dict["annual_working_time_distribution"] = annual_working_time_distribution
        if version_data is not UNSET:
            field_dict["version_data"] = version_data
        if min_rest_minutes_between_days is not UNSET:
            field_dict["min_rest_minutes_between_days"] = min_rest_minutes_between_days
        if max_work_minutes_per_day is not UNSET:
            field_dict["max_work_minutes_per_day"] = max_work_minutes_per_day
        if max_work_days_in_row is not UNSET:
            field_dict["max_work_days_in_row"] = max_work_days_in_row
        if min_rest_hours_in_row is not UNSET:
            field_dict["min_rest_hours_in_row"] = min_rest_hours_in_row
        if es_has_teleworking_contract is not UNSET:
            field_dict["es_has_teleworking_contract"] = es_has_teleworking_contract
        if es_cotization_group is not UNSET:
            field_dict["es_cotization_group"] = es_cotization_group
        if contracts_es_tariff_group_id is not UNSET:
            field_dict["contracts_es_tariff_group_id"] = contracts_es_tariff_group_id
        if es_contract_observations is not UNSET:
            field_dict["es_contract_observations"] = es_contract_observations
        if es_job_description is not UNSET:
            field_dict["es_job_description"] = es_job_description
        if es_contract_type_id is not UNSET:
            field_dict["es_contract_type_id"] = es_contract_type_id
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
        if fr_contract_type_id is not UNSET:
            field_dict["fr_contract_type_id"] = fr_contract_type_id
        if fr_level_id is not UNSET:
            field_dict["fr_level_id"] = fr_level_id
        if fr_step_id is not UNSET:
            field_dict["fr_step_id"] = fr_step_id
        if fr_mutual_id is not UNSET:
            field_dict["fr_mutual_id"] = fr_mutual_id
        if fr_professional_category_id is not UNSET:
            field_dict["fr_professional_category_id"] = fr_professional_category_id
        if fr_work_type_id is not UNSET:
            field_dict["fr_work_type_id"] = fr_work_type_id
        if de_contract_type_id is not UNSET:
            field_dict["de_contract_type_id"] = de_contract_type_id
        if de_base_salary_type_id is not UNSET:
            field_dict["de_base_salary_type_id"] = de_base_salary_type_id
        if pt_contract_type_id is not UNSET:
            field_dict["pt_contract_type_id"] = pt_contract_type_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contracts_contract_version_version_data import (
            ContractsContractVersionVersionData,
        )

        d = dict(src_dict)
        company_id = d.pop("company_id")

        employee_id = d.pop("employee_id")

        effective_on = d.pop("effective_on")

        has_payroll = d.pop("has_payroll")

        bank_holiday_treatment = ContractsContractVersionBankHolidayTreatment(
            d.pop("bank_holiday_treatment")
        )

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        fr_forfait_jours = d.pop("fr_forfait_jours")

        id = d.pop("id", UNSET)

        country = d.pop("country", UNSET)

        job_title = d.pop("job_title", UNSET)

        job_catalog_level_id = d.pop("job_catalog_level_id", UNSET)

        job_catalog_tree_node_uuid = d.pop("job_catalog_tree_node_uuid", UNSET)

        starts_on = d.pop("starts_on", UNSET)

        ends_on = d.pop("ends_on", UNSET)

        has_trial_period = d.pop("has_trial_period", UNSET)

        trial_period_ends_on = d.pop("trial_period_ends_on", UNSET)

        salary_amount = d.pop("salary_amount", UNSET)

        salary_frequency = d.pop("salary_frequency", UNSET)

        working_week_days = d.pop("working_week_days", UNSET)

        working_hours = d.pop("working_hours", UNSET)

        working_hours_frequency = d.pop("working_hours_frequency", UNSET)

        max_legal_yearly_hours = d.pop("max_legal_yearly_hours", UNSET)

        maximum_weekly_hours = d.pop("maximum_weekly_hours", UNSET)

        working_time_percentage_in_cents = d.pop("working_time_percentage_in_cents", UNSET)

        _annual_working_time_distribution = d.pop("annual_working_time_distribution", UNSET)
        annual_working_time_distribution: (
            ContractsContractVersionAnnualWorkingTimeDistribution | Unset
        )
        if isinstance(_annual_working_time_distribution, Unset):
            annual_working_time_distribution = UNSET
        else:
            annual_working_time_distribution = (
                ContractsContractVersionAnnualWorkingTimeDistribution(
                    _annual_working_time_distribution
                )
            )

        _version_data = d.pop("version_data", UNSET)
        version_data: ContractsContractVersionVersionData | Unset
        if isinstance(_version_data, Unset):
            version_data = UNSET
        else:
            version_data = ContractsContractVersionVersionData.from_dict(_version_data)

        min_rest_minutes_between_days = d.pop("min_rest_minutes_between_days", UNSET)

        max_work_minutes_per_day = d.pop("max_work_minutes_per_day", UNSET)

        max_work_days_in_row = d.pop("max_work_days_in_row", UNSET)

        min_rest_hours_in_row = d.pop("min_rest_hours_in_row", UNSET)

        es_has_teleworking_contract = d.pop("es_has_teleworking_contract", UNSET)

        es_cotization_group = d.pop("es_cotization_group", UNSET)

        contracts_es_tariff_group_id = d.pop("contracts_es_tariff_group_id", UNSET)

        es_contract_observations = d.pop("es_contract_observations", UNSET)

        es_job_description = d.pop("es_job_description", UNSET)

        es_contract_type_id = d.pop("es_contract_type_id", UNSET)

        es_working_day_type_id = d.pop("es_working_day_type_id", UNSET)

        es_education_level_id = d.pop("es_education_level_id", UNSET)

        es_professional_category_id = d.pop("es_professional_category_id", UNSET)

        fr_employee_type = d.pop("fr_employee_type", UNSET)

        fr_jours_par_an = d.pop("fr_jours_par_an", UNSET)

        fr_coefficient = d.pop("fr_coefficient", UNSET)

        fr_contract_type_id = d.pop("fr_contract_type_id", UNSET)

        fr_level_id = d.pop("fr_level_id", UNSET)

        fr_step_id = d.pop("fr_step_id", UNSET)

        fr_mutual_id = d.pop("fr_mutual_id", UNSET)

        fr_professional_category_id = d.pop("fr_professional_category_id", UNSET)

        fr_work_type_id = d.pop("fr_work_type_id", UNSET)

        de_contract_type_id = d.pop("de_contract_type_id", UNSET)

        de_base_salary_type_id = d.pop("de_base_salary_type_id", UNSET)

        pt_contract_type_id = d.pop("pt_contract_type_id", UNSET)

        contracts_contract_version = cls(
            company_id=company_id,
            employee_id=employee_id,
            effective_on=effective_on,
            has_payroll=has_payroll,
            bank_holiday_treatment=bank_holiday_treatment,
            created_at=created_at,
            updated_at=updated_at,
            fr_forfait_jours=fr_forfait_jours,
            id=id,
            country=country,
            job_title=job_title,
            job_catalog_level_id=job_catalog_level_id,
            job_catalog_tree_node_uuid=job_catalog_tree_node_uuid,
            starts_on=starts_on,
            ends_on=ends_on,
            has_trial_period=has_trial_period,
            trial_period_ends_on=trial_period_ends_on,
            salary_amount=salary_amount,
            salary_frequency=salary_frequency,
            working_week_days=working_week_days,
            working_hours=working_hours,
            working_hours_frequency=working_hours_frequency,
            max_legal_yearly_hours=max_legal_yearly_hours,
            maximum_weekly_hours=maximum_weekly_hours,
            working_time_percentage_in_cents=working_time_percentage_in_cents,
            annual_working_time_distribution=annual_working_time_distribution,
            version_data=version_data,
            min_rest_minutes_between_days=min_rest_minutes_between_days,
            max_work_minutes_per_day=max_work_minutes_per_day,
            max_work_days_in_row=max_work_days_in_row,
            min_rest_hours_in_row=min_rest_hours_in_row,
            es_has_teleworking_contract=es_has_teleworking_contract,
            es_cotization_group=es_cotization_group,
            contracts_es_tariff_group_id=contracts_es_tariff_group_id,
            es_contract_observations=es_contract_observations,
            es_job_description=es_job_description,
            es_contract_type_id=es_contract_type_id,
            es_working_day_type_id=es_working_day_type_id,
            es_education_level_id=es_education_level_id,
            es_professional_category_id=es_professional_category_id,
            fr_employee_type=fr_employee_type,
            fr_jours_par_an=fr_jours_par_an,
            fr_coefficient=fr_coefficient,
            fr_contract_type_id=fr_contract_type_id,
            fr_level_id=fr_level_id,
            fr_step_id=fr_step_id,
            fr_mutual_id=fr_mutual_id,
            fr_professional_category_id=fr_professional_category_id,
            fr_work_type_id=fr_work_type_id,
            de_contract_type_id=de_contract_type_id,
            de_base_salary_type_id=de_base_salary_type_id,
            pt_contract_type_id=pt_contract_type_id,
        )

        contracts_contract_version.additional_properties = d
        return contracts_contract_version

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
