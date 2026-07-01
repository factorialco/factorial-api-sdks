from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ContractsContractVersionHistory")


@_attrs_define
class ContractsContractVersionHistory:
    id: str
    """ identifier for the contract version history. """
    employee_id: str
    """ employee identifier, refers to /employees/employees endpoint. """
    effective_on: str
    """ the day the specific contract starts, in case of hiring the same than starts_on. """
    has_payroll: bool
    """ boolean that indicates if the employee asociated to this contract belongs to a payroll policy. """
    original_contract_version_id: str
    """ identifier for the original contract version. """
    changed_at: str
    """ the date the contract version was changed. """
    created_at: str
    """ the date the contract version was created. """
    updated_at: str
    """ the date of the last contract version updated. """
    fr_forfait_jours: bool
    """ french flag that indicates if the employee is allowed to work within the framework of a fixed number of
    days. """
    country: str | Unset = UNSET
    """ nationality country code of the employee. """
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
    """ the day the employee is terminated. """
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
    contracts_contract_version_id: str | Unset = UNSET
    """ identifier for the current contract version. """
    trial_period_ends_on: str | Unset = UNSET
    """ when the trial period ends. """
    has_trial_period: bool | Unset = UNSET
    """ a flag that indicates if the employee has a trial period. """
    author: str | Unset = UNSET
    """ the author of the contract version change. """
    action_type: str | Unset = UNSET
    """ the type of action that was performed on the contract version. """
    adjusted_daily_minutes: int | Unset = UNSET
    """ adjusted daily minutes for the employee. """
    es_has_teleworking_contract: bool | Unset = UNSET
    """ spanish boolean that indicates if the employee has a teleworking contract. """
    es_cotization_group: int | Unset = UNSET
    """ spanish cotization group identifier. """
    es_contract_observations: str | Unset = UNSET
    """ spanish observations of the contract. """
    es_job_description: str | Unset = UNSET
    """ spanish job description of the contract. """
    es_contract_type_id: str | Unset = UNSET
    """ spanish contract type identifier. """
    es_working_day_type_id: str | Unset = UNSET
    """ spanish working day type identifier. """
    es_education_level_id: str | Unset = UNSET
    """ spanish education level identifier. """
    es_professional_category_id: str | Unset = UNSET
    """ spanish professional category identifier. """
    es_contribution_type_id: str | Unset = UNSET
    """ spanish contribution type identifier. """
    es_agreement_code_id: str | Unset = UNSET
    """ spanish agreement code identifier. """
    es_cno_occupation_id: str | Unset = UNSET
    """ spanish cno occupation identifier. """
    es_tariff_group_id: str | Unset = UNSET
    """ spanish tariff group identifier. """
    es_occupation_code_id: str | Unset = UNSET
    """ spanish occupation code identifier. """
    es_classification_id: str | Unset = UNSET
    """ spanish classification identifier. """
    fr_employee_type: str | Unset = UNSET
    """ french employee type. """
    fr_jours_par_an: int | Unset = UNSET
    """ french number of days the employee is allowed to work. """
    fr_jours_par_an_cents: int | Unset = UNSET
    """ french number of days the employee is allowed to work in cents. """
    fr_coefficient: str | Unset = UNSET
    """ french coefficient for france contracts. """
    fr_contract_type_id: str | Unset = UNSET
    """ french contract type identifier. """
    fr_level_id: str | Unset = UNSET
    """ french level identifier. """
    fr_step_id: str | Unset = UNSET
    """ french step identifier. """
    fr_mutual_id: str | Unset = UNSET
    """ french mutual identifier. """
    fr_professional_category_id: str | Unset = UNSET
    """ french professional category identifier. """
    fr_work_type_id: str | Unset = UNSET
    """ french work type identifier. """
    de_contract_type_id: str | Unset = UNSET
    """ german contract type identifier. """
    de_base_salary_type_id: str | Unset = UNSET
    """ Identifier for the German base salary type. References a payroll concept available via the /payroll/concepts
    endpoint. """
    pt_contract_type_id: str | Unset = UNSET
    """ portuguese contract type identifier. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        employee_id = self.employee_id

        effective_on = self.effective_on

        has_payroll = self.has_payroll

        original_contract_version_id = self.original_contract_version_id

        changed_at = self.changed_at

        created_at = self.created_at

        updated_at = self.updated_at

        fr_forfait_jours = self.fr_forfait_jours

        country = self.country

        job_title = self.job_title

        job_catalog_level_id = self.job_catalog_level_id

        job_catalog_tree_node_uuid = self.job_catalog_tree_node_uuid

        starts_on = self.starts_on

        ends_on = self.ends_on

        salary_amount = self.salary_amount

        salary_frequency = self.salary_frequency

        working_week_days = self.working_week_days

        working_hours = self.working_hours

        working_hours_frequency = self.working_hours_frequency

        max_legal_yearly_hours = self.max_legal_yearly_hours

        maximum_weekly_hours = self.maximum_weekly_hours

        contracts_contract_version_id = self.contracts_contract_version_id

        trial_period_ends_on = self.trial_period_ends_on

        has_trial_period = self.has_trial_period

        author = self.author

        action_type = self.action_type

        adjusted_daily_minutes = self.adjusted_daily_minutes

        es_has_teleworking_contract = self.es_has_teleworking_contract

        es_cotization_group = self.es_cotization_group

        es_contract_observations = self.es_contract_observations

        es_job_description = self.es_job_description

        es_contract_type_id = self.es_contract_type_id

        es_working_day_type_id = self.es_working_day_type_id

        es_education_level_id = self.es_education_level_id

        es_professional_category_id = self.es_professional_category_id

        es_contribution_type_id = self.es_contribution_type_id

        es_agreement_code_id = self.es_agreement_code_id

        es_cno_occupation_id = self.es_cno_occupation_id

        es_tariff_group_id = self.es_tariff_group_id

        es_occupation_code_id = self.es_occupation_code_id

        es_classification_id = self.es_classification_id

        fr_employee_type = self.fr_employee_type

        fr_jours_par_an = self.fr_jours_par_an

        fr_jours_par_an_cents = self.fr_jours_par_an_cents

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
                "id": id,
                "employee_id": employee_id,
                "effective_on": effective_on,
                "has_payroll": has_payroll,
                "original_contract_version_id": original_contract_version_id,
                "changed_at": changed_at,
                "created_at": created_at,
                "updated_at": updated_at,
                "fr_forfait_jours": fr_forfait_jours,
            }
        )
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
        if contracts_contract_version_id is not UNSET:
            field_dict["contracts_contract_version_id"] = contracts_contract_version_id
        if trial_period_ends_on is not UNSET:
            field_dict["trial_period_ends_on"] = trial_period_ends_on
        if has_trial_period is not UNSET:
            field_dict["has_trial_period"] = has_trial_period
        if author is not UNSET:
            field_dict["author"] = author
        if action_type is not UNSET:
            field_dict["action_type"] = action_type
        if adjusted_daily_minutes is not UNSET:
            field_dict["adjusted_daily_minutes"] = adjusted_daily_minutes
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
        if es_working_day_type_id is not UNSET:
            field_dict["es_working_day_type_id"] = es_working_day_type_id
        if es_education_level_id is not UNSET:
            field_dict["es_education_level_id"] = es_education_level_id
        if es_professional_category_id is not UNSET:
            field_dict["es_professional_category_id"] = es_professional_category_id
        if es_contribution_type_id is not UNSET:
            field_dict["es_contribution_type_id"] = es_contribution_type_id
        if es_agreement_code_id is not UNSET:
            field_dict["es_agreement_code_id"] = es_agreement_code_id
        if es_cno_occupation_id is not UNSET:
            field_dict["es_cno_occupation_id"] = es_cno_occupation_id
        if es_tariff_group_id is not UNSET:
            field_dict["es_tariff_group_id"] = es_tariff_group_id
        if es_occupation_code_id is not UNSET:
            field_dict["es_occupation_code_id"] = es_occupation_code_id
        if es_classification_id is not UNSET:
            field_dict["es_classification_id"] = es_classification_id
        if fr_employee_type is not UNSET:
            field_dict["fr_employee_type"] = fr_employee_type
        if fr_jours_par_an is not UNSET:
            field_dict["fr_jours_par_an"] = fr_jours_par_an
        if fr_jours_par_an_cents is not UNSET:
            field_dict["fr_jours_par_an_cents"] = fr_jours_par_an_cents
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
        d = dict(src_dict)
        id = d.pop("id")

        employee_id = d.pop("employee_id")

        effective_on = d.pop("effective_on")

        has_payroll = d.pop("has_payroll")

        original_contract_version_id = d.pop("original_contract_version_id")

        changed_at = d.pop("changed_at")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        fr_forfait_jours = d.pop("fr_forfait_jours")

        country = d.pop("country", UNSET)

        job_title = d.pop("job_title", UNSET)

        job_catalog_level_id = d.pop("job_catalog_level_id", UNSET)

        job_catalog_tree_node_uuid = d.pop("job_catalog_tree_node_uuid", UNSET)

        starts_on = d.pop("starts_on", UNSET)

        ends_on = d.pop("ends_on", UNSET)

        salary_amount = d.pop("salary_amount", UNSET)

        salary_frequency = d.pop("salary_frequency", UNSET)

        working_week_days = d.pop("working_week_days", UNSET)

        working_hours = d.pop("working_hours", UNSET)

        working_hours_frequency = d.pop("working_hours_frequency", UNSET)

        max_legal_yearly_hours = d.pop("max_legal_yearly_hours", UNSET)

        maximum_weekly_hours = d.pop("maximum_weekly_hours", UNSET)

        contracts_contract_version_id = d.pop("contracts_contract_version_id", UNSET)

        trial_period_ends_on = d.pop("trial_period_ends_on", UNSET)

        has_trial_period = d.pop("has_trial_period", UNSET)

        author = d.pop("author", UNSET)

        action_type = d.pop("action_type", UNSET)

        adjusted_daily_minutes = d.pop("adjusted_daily_minutes", UNSET)

        es_has_teleworking_contract = d.pop("es_has_teleworking_contract", UNSET)

        es_cotization_group = d.pop("es_cotization_group", UNSET)

        es_contract_observations = d.pop("es_contract_observations", UNSET)

        es_job_description = d.pop("es_job_description", UNSET)

        es_contract_type_id = d.pop("es_contract_type_id", UNSET)

        es_working_day_type_id = d.pop("es_working_day_type_id", UNSET)

        es_education_level_id = d.pop("es_education_level_id", UNSET)

        es_professional_category_id = d.pop("es_professional_category_id", UNSET)

        es_contribution_type_id = d.pop("es_contribution_type_id", UNSET)

        es_agreement_code_id = d.pop("es_agreement_code_id", UNSET)

        es_cno_occupation_id = d.pop("es_cno_occupation_id", UNSET)

        es_tariff_group_id = d.pop("es_tariff_group_id", UNSET)

        es_occupation_code_id = d.pop("es_occupation_code_id", UNSET)

        es_classification_id = d.pop("es_classification_id", UNSET)

        fr_employee_type = d.pop("fr_employee_type", UNSET)

        fr_jours_par_an = d.pop("fr_jours_par_an", UNSET)

        fr_jours_par_an_cents = d.pop("fr_jours_par_an_cents", UNSET)

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

        contracts_contract_version_history = cls(
            id=id,
            employee_id=employee_id,
            effective_on=effective_on,
            has_payroll=has_payroll,
            original_contract_version_id=original_contract_version_id,
            changed_at=changed_at,
            created_at=created_at,
            updated_at=updated_at,
            fr_forfait_jours=fr_forfait_jours,
            country=country,
            job_title=job_title,
            job_catalog_level_id=job_catalog_level_id,
            job_catalog_tree_node_uuid=job_catalog_tree_node_uuid,
            starts_on=starts_on,
            ends_on=ends_on,
            salary_amount=salary_amount,
            salary_frequency=salary_frequency,
            working_week_days=working_week_days,
            working_hours=working_hours,
            working_hours_frequency=working_hours_frequency,
            max_legal_yearly_hours=max_legal_yearly_hours,
            maximum_weekly_hours=maximum_weekly_hours,
            contracts_contract_version_id=contracts_contract_version_id,
            trial_period_ends_on=trial_period_ends_on,
            has_trial_period=has_trial_period,
            author=author,
            action_type=action_type,
            adjusted_daily_minutes=adjusted_daily_minutes,
            es_has_teleworking_contract=es_has_teleworking_contract,
            es_cotization_group=es_cotization_group,
            es_contract_observations=es_contract_observations,
            es_job_description=es_job_description,
            es_contract_type_id=es_contract_type_id,
            es_working_day_type_id=es_working_day_type_id,
            es_education_level_id=es_education_level_id,
            es_professional_category_id=es_professional_category_id,
            es_contribution_type_id=es_contribution_type_id,
            es_agreement_code_id=es_agreement_code_id,
            es_cno_occupation_id=es_cno_occupation_id,
            es_tariff_group_id=es_tariff_group_id,
            es_occupation_code_id=es_occupation_code_id,
            es_classification_id=es_classification_id,
            fr_employee_type=fr_employee_type,
            fr_jours_par_an=fr_jours_par_an,
            fr_jours_par_an_cents=fr_jours_par_an_cents,
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

        contracts_contract_version_history.additional_properties = d
        return contracts_contract_version_history

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
