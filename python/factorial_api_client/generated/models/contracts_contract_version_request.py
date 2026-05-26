from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.contracts_contract_version_request_status import ContractsContractVersionRequestStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ContractsContractVersionRequest")


@_attrs_define
class ContractsContractVersionRequest:
    employee_id: int
    effective_on: str
    has_payroll: bool
    created_at: str
    updated_at: str
    status: ContractsContractVersionRequestStatus
    fr_forfait_jours: bool
    id: int | Unset = UNSET
    company_id: int | Unset = UNSET
    country: str | Unset = UNSET
    job_title: str | Unset = UNSET
    job_catalog_level_id: int | Unset = UNSET
    job_catalog_level_name: str | Unset = UNSET
    job_catalog_level: str | Unset = UNSET
    job_catalog_role: str | Unset = UNSET
    job_catalog_role_id: int | Unset = UNSET
    job_catalog_tree_node_uuid: str | Unset = UNSET
    starts_on: str | Unset = UNSET
    ends_on: str | Unset = UNSET
    has_payroll_policies: bool | Unset = UNSET
    has_trial_period: bool | Unset = UNSET
    trial_period_ends_on: str | Unset = UNSET
    salary_amount: int | Unset = UNSET
    salary_frequency: str | Unset = UNSET
    working_week_days: str | Unset = UNSET
    working_hours: int | Unset = UNSET
    working_hours_frequency: str | Unset = UNSET
    max_legal_yearly_hours: int | Unset = UNSET
    maximum_weekly_hours: int | Unset = UNSET
    adjusted_daily_minutes: int | Unset = UNSET
    created_by_name: str | Unset = UNSET
    created_by_avatar: str | Unset = UNSET
    action_type: str | Unset = UNSET
    request_details: str | Unset = UNSET
    approvers_ids: list[int] | Unset = UNSET
    approval_author_id: int | Unset = UNSET
    approval_request_created_at: str | Unset = UNSET
    approval_action_type: str | Unset = UNSET
    es_has_teleworking_contract: bool | Unset = UNSET
    es_cotization_group: int | Unset = UNSET
    es_contract_observations: str | Unset = UNSET
    es_job_description: str | Unset = UNSET
    es_contract_type_id: int | Unset = UNSET
    es_contract_type_name: str | Unset = UNSET
    es_working_day_type_id: int | Unset = UNSET
    es_working_day_type_name: str | Unset = UNSET
    es_education_level_id: int | Unset = UNSET
    es_education_level_name: str | Unset = UNSET
    es_professional_category_id: int | Unset = UNSET
    es_professional_category_name: str | Unset = UNSET
    es_contribution_type_id: int | Unset = UNSET
    es_contribution_type_name: str | Unset = UNSET
    es_agreement_code_id: int | Unset = UNSET
    es_agreement_code_name: str | Unset = UNSET
    es_cno_occupation_id: int | Unset = UNSET
    es_cno_occupation_name: str | Unset = UNSET
    es_regime_id: int | Unset = UNSET
    es_regime_name: str | Unset = UNSET
    es_tariff_group_id: int | Unset = UNSET
    es_tariff_group_name: str | Unset = UNSET
    es_occupation_code_id: int | Unset = UNSET
    es_occupation_code_name: str | Unset = UNSET
    es_classification_id: int | Unset = UNSET
    es_classification_name: str | Unset = UNSET
    es_a3innuva_job_position_id: int | Unset = UNSET
    es_a3innuva_job_position_name: str | Unset = UNSET
    fr_employee_type: str | Unset = UNSET
    fr_jours_par_an: int | Unset = UNSET
    fr_jours_par_an_cents: int | Unset = UNSET
    fr_coefficient: str | Unset = UNSET
    fr_contract_type_id: int | Unset = UNSET
    fr_level_id: int | Unset = UNSET
    fr_step_id: int | Unset = UNSET
    fr_mutual_id: int | Unset = UNSET
    fr_professional_category_id: int | Unset = UNSET
    fr_work_type_id: int | Unset = UNSET
    fr_contract_type_name: str | Unset = UNSET
    fr_mutual_name: str | Unset = UNSET
    fr_professional_category_name: str | Unset = UNSET
    fr_work_type_name: str | Unset = UNSET
    fr_level_name: str | Unset = UNSET
    fr_step_name: str | Unset = UNSET
    de_contract_type_id: int | Unset = UNSET
    de_contract_type_name: str | Unset = UNSET
    de_employment_type: int | Unset = UNSET
    de_flat_rate_tax: int | Unset = UNSET
    de_activity_type: int | Unset = UNSET
    de_personal_key_group_id: int | Unset = UNSET
    de_personal_key_group_name: str | Unset = UNSET
    de_base_salary_type_id: int | Unset = UNSET
    de_base_salary_type_name: str | Unset = UNSET
    pt_contract_type_id: int | Unset = UNSET
    pt_contract_type_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        employee_id = self.employee_id

        effective_on = self.effective_on

        has_payroll = self.has_payroll

        created_at = self.created_at

        updated_at = self.updated_at

        status = self.status.value

        fr_forfait_jours = self.fr_forfait_jours

        id = self.id

        company_id = self.company_id

        country = self.country

        job_title = self.job_title

        job_catalog_level_id = self.job_catalog_level_id

        job_catalog_level_name = self.job_catalog_level_name

        job_catalog_level = self.job_catalog_level

        job_catalog_role = self.job_catalog_role

        job_catalog_role_id = self.job_catalog_role_id

        job_catalog_tree_node_uuid = self.job_catalog_tree_node_uuid

        starts_on = self.starts_on

        ends_on = self.ends_on

        has_payroll_policies = self.has_payroll_policies

        has_trial_period = self.has_trial_period

        trial_period_ends_on = self.trial_period_ends_on

        salary_amount = self.salary_amount

        salary_frequency = self.salary_frequency

        working_week_days = self.working_week_days

        working_hours = self.working_hours

        working_hours_frequency = self.working_hours_frequency

        max_legal_yearly_hours = self.max_legal_yearly_hours

        maximum_weekly_hours = self.maximum_weekly_hours

        adjusted_daily_minutes = self.adjusted_daily_minutes

        created_by_name = self.created_by_name

        created_by_avatar = self.created_by_avatar

        action_type = self.action_type

        request_details = self.request_details

        approvers_ids: list[int] | Unset = UNSET
        if not isinstance(self.approvers_ids, Unset):
            approvers_ids = self.approvers_ids

        approval_author_id = self.approval_author_id

        approval_request_created_at = self.approval_request_created_at

        approval_action_type = self.approval_action_type

        es_has_teleworking_contract = self.es_has_teleworking_contract

        es_cotization_group = self.es_cotization_group

        es_contract_observations = self.es_contract_observations

        es_job_description = self.es_job_description

        es_contract_type_id = self.es_contract_type_id

        es_contract_type_name = self.es_contract_type_name

        es_working_day_type_id = self.es_working_day_type_id

        es_working_day_type_name = self.es_working_day_type_name

        es_education_level_id = self.es_education_level_id

        es_education_level_name = self.es_education_level_name

        es_professional_category_id = self.es_professional_category_id

        es_professional_category_name = self.es_professional_category_name

        es_contribution_type_id = self.es_contribution_type_id

        es_contribution_type_name = self.es_contribution_type_name

        es_agreement_code_id = self.es_agreement_code_id

        es_agreement_code_name = self.es_agreement_code_name

        es_cno_occupation_id = self.es_cno_occupation_id

        es_cno_occupation_name = self.es_cno_occupation_name

        es_regime_id = self.es_regime_id

        es_regime_name = self.es_regime_name

        es_tariff_group_id = self.es_tariff_group_id

        es_tariff_group_name = self.es_tariff_group_name

        es_occupation_code_id = self.es_occupation_code_id

        es_occupation_code_name = self.es_occupation_code_name

        es_classification_id = self.es_classification_id

        es_classification_name = self.es_classification_name

        es_a3innuva_job_position_id = self.es_a3innuva_job_position_id

        es_a3innuva_job_position_name = self.es_a3innuva_job_position_name

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

        fr_contract_type_name = self.fr_contract_type_name

        fr_mutual_name = self.fr_mutual_name

        fr_professional_category_name = self.fr_professional_category_name

        fr_work_type_name = self.fr_work_type_name

        fr_level_name = self.fr_level_name

        fr_step_name = self.fr_step_name

        de_contract_type_id = self.de_contract_type_id

        de_contract_type_name = self.de_contract_type_name

        de_employment_type = self.de_employment_type

        de_flat_rate_tax = self.de_flat_rate_tax

        de_activity_type = self.de_activity_type

        de_personal_key_group_id = self.de_personal_key_group_id

        de_personal_key_group_name = self.de_personal_key_group_name

        de_base_salary_type_id = self.de_base_salary_type_id

        de_base_salary_type_name = self.de_base_salary_type_name

        pt_contract_type_id = self.pt_contract_type_id

        pt_contract_type_name = self.pt_contract_type_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "employee_id": employee_id,
                "effective_on": effective_on,
                "has_payroll": has_payroll,
                "created_at": created_at,
                "updated_at": updated_at,
                "status": status,
                "fr_forfait_jours": fr_forfait_jours,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if company_id is not UNSET:
            field_dict["company_id"] = company_id
        if country is not UNSET:
            field_dict["country"] = country
        if job_title is not UNSET:
            field_dict["job_title"] = job_title
        if job_catalog_level_id is not UNSET:
            field_dict["job_catalog_level_id"] = job_catalog_level_id
        if job_catalog_level_name is not UNSET:
            field_dict["job_catalog_level_name"] = job_catalog_level_name
        if job_catalog_level is not UNSET:
            field_dict["job_catalog_level"] = job_catalog_level
        if job_catalog_role is not UNSET:
            field_dict["job_catalog_role"] = job_catalog_role
        if job_catalog_role_id is not UNSET:
            field_dict["job_catalog_role_id"] = job_catalog_role_id
        if job_catalog_tree_node_uuid is not UNSET:
            field_dict["job_catalog_tree_node_uuid"] = job_catalog_tree_node_uuid
        if starts_on is not UNSET:
            field_dict["starts_on"] = starts_on
        if ends_on is not UNSET:
            field_dict["ends_on"] = ends_on
        if has_payroll_policies is not UNSET:
            field_dict["has_payroll_policies"] = has_payroll_policies
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
        if adjusted_daily_minutes is not UNSET:
            field_dict["adjusted_daily_minutes"] = adjusted_daily_minutes
        if created_by_name is not UNSET:
            field_dict["created_by_name"] = created_by_name
        if created_by_avatar is not UNSET:
            field_dict["created_by_avatar"] = created_by_avatar
        if action_type is not UNSET:
            field_dict["action_type"] = action_type
        if request_details is not UNSET:
            field_dict["request_details"] = request_details
        if approvers_ids is not UNSET:
            field_dict["approvers_ids"] = approvers_ids
        if approval_author_id is not UNSET:
            field_dict["approval_author_id"] = approval_author_id
        if approval_request_created_at is not UNSET:
            field_dict["approval_request_created_at"] = approval_request_created_at
        if approval_action_type is not UNSET:
            field_dict["approval_action_type"] = approval_action_type
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
        if es_working_day_type_id is not UNSET:
            field_dict["es_working_day_type_id"] = es_working_day_type_id
        if es_working_day_type_name is not UNSET:
            field_dict["es_working_day_type_name"] = es_working_day_type_name
        if es_education_level_id is not UNSET:
            field_dict["es_education_level_id"] = es_education_level_id
        if es_education_level_name is not UNSET:
            field_dict["es_education_level_name"] = es_education_level_name
        if es_professional_category_id is not UNSET:
            field_dict["es_professional_category_id"] = es_professional_category_id
        if es_professional_category_name is not UNSET:
            field_dict["es_professional_category_name"] = es_professional_category_name
        if es_contribution_type_id is not UNSET:
            field_dict["es_contribution_type_id"] = es_contribution_type_id
        if es_contribution_type_name is not UNSET:
            field_dict["es_contribution_type_name"] = es_contribution_type_name
        if es_agreement_code_id is not UNSET:
            field_dict["es_agreement_code_id"] = es_agreement_code_id
        if es_agreement_code_name is not UNSET:
            field_dict["es_agreement_code_name"] = es_agreement_code_name
        if es_cno_occupation_id is not UNSET:
            field_dict["es_cno_occupation_id"] = es_cno_occupation_id
        if es_cno_occupation_name is not UNSET:
            field_dict["es_cno_occupation_name"] = es_cno_occupation_name
        if es_regime_id is not UNSET:
            field_dict["es_regime_id"] = es_regime_id
        if es_regime_name is not UNSET:
            field_dict["es_regime_name"] = es_regime_name
        if es_tariff_group_id is not UNSET:
            field_dict["es_tariff_group_id"] = es_tariff_group_id
        if es_tariff_group_name is not UNSET:
            field_dict["es_tariff_group_name"] = es_tariff_group_name
        if es_occupation_code_id is not UNSET:
            field_dict["es_occupation_code_id"] = es_occupation_code_id
        if es_occupation_code_name is not UNSET:
            field_dict["es_occupation_code_name"] = es_occupation_code_name
        if es_classification_id is not UNSET:
            field_dict["es_classification_id"] = es_classification_id
        if es_classification_name is not UNSET:
            field_dict["es_classification_name"] = es_classification_name
        if es_a3innuva_job_position_id is not UNSET:
            field_dict["es_a3innuva_job_position_id"] = es_a3innuva_job_position_id
        if es_a3innuva_job_position_name is not UNSET:
            field_dict["es_a3innuva_job_position_name"] = es_a3innuva_job_position_name
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
        if fr_contract_type_name is not UNSET:
            field_dict["fr_contract_type_name"] = fr_contract_type_name
        if fr_mutual_name is not UNSET:
            field_dict["fr_mutual_name"] = fr_mutual_name
        if fr_professional_category_name is not UNSET:
            field_dict["fr_professional_category_name"] = fr_professional_category_name
        if fr_work_type_name is not UNSET:
            field_dict["fr_work_type_name"] = fr_work_type_name
        if fr_level_name is not UNSET:
            field_dict["fr_level_name"] = fr_level_name
        if fr_step_name is not UNSET:
            field_dict["fr_step_name"] = fr_step_name
        if de_contract_type_id is not UNSET:
            field_dict["de_contract_type_id"] = de_contract_type_id
        if de_contract_type_name is not UNSET:
            field_dict["de_contract_type_name"] = de_contract_type_name
        if de_employment_type is not UNSET:
            field_dict["de_employment_type"] = de_employment_type
        if de_flat_rate_tax is not UNSET:
            field_dict["de_flat_rate_tax"] = de_flat_rate_tax
        if de_activity_type is not UNSET:
            field_dict["de_activity_type"] = de_activity_type
        if de_personal_key_group_id is not UNSET:
            field_dict["de_personal_key_group_id"] = de_personal_key_group_id
        if de_personal_key_group_name is not UNSET:
            field_dict["de_personal_key_group_name"] = de_personal_key_group_name
        if de_base_salary_type_id is not UNSET:
            field_dict["de_base_salary_type_id"] = de_base_salary_type_id
        if de_base_salary_type_name is not UNSET:
            field_dict["de_base_salary_type_name"] = de_base_salary_type_name
        if pt_contract_type_id is not UNSET:
            field_dict["pt_contract_type_id"] = pt_contract_type_id
        if pt_contract_type_name is not UNSET:
            field_dict["pt_contract_type_name"] = pt_contract_type_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        employee_id = d.pop("employee_id")

        effective_on = d.pop("effective_on")

        has_payroll = d.pop("has_payroll")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        status = ContractsContractVersionRequestStatus(d.pop("status"))

        fr_forfait_jours = d.pop("fr_forfait_jours")

        id = d.pop("id", UNSET)

        company_id = d.pop("company_id", UNSET)

        country = d.pop("country", UNSET)

        job_title = d.pop("job_title", UNSET)

        job_catalog_level_id = d.pop("job_catalog_level_id", UNSET)

        job_catalog_level_name = d.pop("job_catalog_level_name", UNSET)

        job_catalog_level = d.pop("job_catalog_level", UNSET)

        job_catalog_role = d.pop("job_catalog_role", UNSET)

        job_catalog_role_id = d.pop("job_catalog_role_id", UNSET)

        job_catalog_tree_node_uuid = d.pop("job_catalog_tree_node_uuid", UNSET)

        starts_on = d.pop("starts_on", UNSET)

        ends_on = d.pop("ends_on", UNSET)

        has_payroll_policies = d.pop("has_payroll_policies", UNSET)

        has_trial_period = d.pop("has_trial_period", UNSET)

        trial_period_ends_on = d.pop("trial_period_ends_on", UNSET)

        salary_amount = d.pop("salary_amount", UNSET)

        salary_frequency = d.pop("salary_frequency", UNSET)

        working_week_days = d.pop("working_week_days", UNSET)

        working_hours = d.pop("working_hours", UNSET)

        working_hours_frequency = d.pop("working_hours_frequency", UNSET)

        max_legal_yearly_hours = d.pop("max_legal_yearly_hours", UNSET)

        maximum_weekly_hours = d.pop("maximum_weekly_hours", UNSET)

        adjusted_daily_minutes = d.pop("adjusted_daily_minutes", UNSET)

        created_by_name = d.pop("created_by_name", UNSET)

        created_by_avatar = d.pop("created_by_avatar", UNSET)

        action_type = d.pop("action_type", UNSET)

        request_details = d.pop("request_details", UNSET)

        approvers_ids = cast(list[int], d.pop("approvers_ids", UNSET))

        approval_author_id = d.pop("approval_author_id", UNSET)

        approval_request_created_at = d.pop("approval_request_created_at", UNSET)

        approval_action_type = d.pop("approval_action_type", UNSET)

        es_has_teleworking_contract = d.pop("es_has_teleworking_contract", UNSET)

        es_cotization_group = d.pop("es_cotization_group", UNSET)

        es_contract_observations = d.pop("es_contract_observations", UNSET)

        es_job_description = d.pop("es_job_description", UNSET)

        es_contract_type_id = d.pop("es_contract_type_id", UNSET)

        es_contract_type_name = d.pop("es_contract_type_name", UNSET)

        es_working_day_type_id = d.pop("es_working_day_type_id", UNSET)

        es_working_day_type_name = d.pop("es_working_day_type_name", UNSET)

        es_education_level_id = d.pop("es_education_level_id", UNSET)

        es_education_level_name = d.pop("es_education_level_name", UNSET)

        es_professional_category_id = d.pop("es_professional_category_id", UNSET)

        es_professional_category_name = d.pop("es_professional_category_name", UNSET)

        es_contribution_type_id = d.pop("es_contribution_type_id", UNSET)

        es_contribution_type_name = d.pop("es_contribution_type_name", UNSET)

        es_agreement_code_id = d.pop("es_agreement_code_id", UNSET)

        es_agreement_code_name = d.pop("es_agreement_code_name", UNSET)

        es_cno_occupation_id = d.pop("es_cno_occupation_id", UNSET)

        es_cno_occupation_name = d.pop("es_cno_occupation_name", UNSET)

        es_regime_id = d.pop("es_regime_id", UNSET)

        es_regime_name = d.pop("es_regime_name", UNSET)

        es_tariff_group_id = d.pop("es_tariff_group_id", UNSET)

        es_tariff_group_name = d.pop("es_tariff_group_name", UNSET)

        es_occupation_code_id = d.pop("es_occupation_code_id", UNSET)

        es_occupation_code_name = d.pop("es_occupation_code_name", UNSET)

        es_classification_id = d.pop("es_classification_id", UNSET)

        es_classification_name = d.pop("es_classification_name", UNSET)

        es_a3innuva_job_position_id = d.pop("es_a3innuva_job_position_id", UNSET)

        es_a3innuva_job_position_name = d.pop("es_a3innuva_job_position_name", UNSET)

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

        fr_contract_type_name = d.pop("fr_contract_type_name", UNSET)

        fr_mutual_name = d.pop("fr_mutual_name", UNSET)

        fr_professional_category_name = d.pop("fr_professional_category_name", UNSET)

        fr_work_type_name = d.pop("fr_work_type_name", UNSET)

        fr_level_name = d.pop("fr_level_name", UNSET)

        fr_step_name = d.pop("fr_step_name", UNSET)

        de_contract_type_id = d.pop("de_contract_type_id", UNSET)

        de_contract_type_name = d.pop("de_contract_type_name", UNSET)

        de_employment_type = d.pop("de_employment_type", UNSET)

        de_flat_rate_tax = d.pop("de_flat_rate_tax", UNSET)

        de_activity_type = d.pop("de_activity_type", UNSET)

        de_personal_key_group_id = d.pop("de_personal_key_group_id", UNSET)

        de_personal_key_group_name = d.pop("de_personal_key_group_name", UNSET)

        de_base_salary_type_id = d.pop("de_base_salary_type_id", UNSET)

        de_base_salary_type_name = d.pop("de_base_salary_type_name", UNSET)

        pt_contract_type_id = d.pop("pt_contract_type_id", UNSET)

        pt_contract_type_name = d.pop("pt_contract_type_name", UNSET)

        contracts_contract_version_request = cls(
            employee_id=employee_id,
            effective_on=effective_on,
            has_payroll=has_payroll,
            created_at=created_at,
            updated_at=updated_at,
            status=status,
            fr_forfait_jours=fr_forfait_jours,
            id=id,
            company_id=company_id,
            country=country,
            job_title=job_title,
            job_catalog_level_id=job_catalog_level_id,
            job_catalog_level_name=job_catalog_level_name,
            job_catalog_level=job_catalog_level,
            job_catalog_role=job_catalog_role,
            job_catalog_role_id=job_catalog_role_id,
            job_catalog_tree_node_uuid=job_catalog_tree_node_uuid,
            starts_on=starts_on,
            ends_on=ends_on,
            has_payroll_policies=has_payroll_policies,
            has_trial_period=has_trial_period,
            trial_period_ends_on=trial_period_ends_on,
            salary_amount=salary_amount,
            salary_frequency=salary_frequency,
            working_week_days=working_week_days,
            working_hours=working_hours,
            working_hours_frequency=working_hours_frequency,
            max_legal_yearly_hours=max_legal_yearly_hours,
            maximum_weekly_hours=maximum_weekly_hours,
            adjusted_daily_minutes=adjusted_daily_minutes,
            created_by_name=created_by_name,
            created_by_avatar=created_by_avatar,
            action_type=action_type,
            request_details=request_details,
            approvers_ids=approvers_ids,
            approval_author_id=approval_author_id,
            approval_request_created_at=approval_request_created_at,
            approval_action_type=approval_action_type,
            es_has_teleworking_contract=es_has_teleworking_contract,
            es_cotization_group=es_cotization_group,
            es_contract_observations=es_contract_observations,
            es_job_description=es_job_description,
            es_contract_type_id=es_contract_type_id,
            es_contract_type_name=es_contract_type_name,
            es_working_day_type_id=es_working_day_type_id,
            es_working_day_type_name=es_working_day_type_name,
            es_education_level_id=es_education_level_id,
            es_education_level_name=es_education_level_name,
            es_professional_category_id=es_professional_category_id,
            es_professional_category_name=es_professional_category_name,
            es_contribution_type_id=es_contribution_type_id,
            es_contribution_type_name=es_contribution_type_name,
            es_agreement_code_id=es_agreement_code_id,
            es_agreement_code_name=es_agreement_code_name,
            es_cno_occupation_id=es_cno_occupation_id,
            es_cno_occupation_name=es_cno_occupation_name,
            es_regime_id=es_regime_id,
            es_regime_name=es_regime_name,
            es_tariff_group_id=es_tariff_group_id,
            es_tariff_group_name=es_tariff_group_name,
            es_occupation_code_id=es_occupation_code_id,
            es_occupation_code_name=es_occupation_code_name,
            es_classification_id=es_classification_id,
            es_classification_name=es_classification_name,
            es_a3innuva_job_position_id=es_a3innuva_job_position_id,
            es_a3innuva_job_position_name=es_a3innuva_job_position_name,
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
            fr_contract_type_name=fr_contract_type_name,
            fr_mutual_name=fr_mutual_name,
            fr_professional_category_name=fr_professional_category_name,
            fr_work_type_name=fr_work_type_name,
            fr_level_name=fr_level_name,
            fr_step_name=fr_step_name,
            de_contract_type_id=de_contract_type_id,
            de_contract_type_name=de_contract_type_name,
            de_employment_type=de_employment_type,
            de_flat_rate_tax=de_flat_rate_tax,
            de_activity_type=de_activity_type,
            de_personal_key_group_id=de_personal_key_group_id,
            de_personal_key_group_name=de_personal_key_group_name,
            de_base_salary_type_id=de_base_salary_type_id,
            de_base_salary_type_name=de_base_salary_type_name,
            pt_contract_type_id=pt_contract_type_id,
            pt_contract_type_name=pt_contract_type_name,
        )

        contracts_contract_version_request.additional_properties = d
        return contracts_contract_version_request

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
