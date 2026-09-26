from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_api_20261001_resources_contracts_legal_entity_changes_body_contract_details_annual_working_time_distribution import (
    PostApi20261001ResourcesContractsLegalEntityChangesBodyContractDetailsAnnualWorkingTimeDistribution,
)
from ..models.post_api_20261001_resources_contracts_legal_entity_changes_body_contract_details_bank_holiday_treatment import (
    PostApi20261001ResourcesContractsLegalEntityChangesBodyContractDetailsBankHolidayTreatment,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_api_20261001_resources_contracts_legal_entity_changes_body_contract_details_country_data_inputs_item import (
        PostApi20261001ResourcesContractsLegalEntityChangesBodyContractDetailsCountryDataInputsItem,
    )


T = TypeVar("T", bound="PostApi20261001ResourcesContractsLegalEntityChangesBodyContractDetails")


@_attrs_define
class PostApi20261001ResourcesContractsLegalEntityChangesBodyContractDetails:
    """The terms of the contract version that opens the new contract. Same fields as the contract version create endpoint."""

    effective_on: str
    """ the day the new contract version takes effect. The employee moves to the target legal entity on this date.
    """
    employee_id: str
    """ employee identifier, refers to /employees/employees endpoint. """
    ends_on: str | Unset = UNSET
    """ the day the employee is terminated. """
    has_trial_period: bool | Unset = UNSET
    """ a flag that indicates if the employee has a trial period. """
    job_catalog_tree_node_uuid: str | Unset = UNSET
    """ the uuid node in the job catalog tree. For now it only supports level nodes. Refer to job_catalog/tree_nodes
    endpoint. """
    job_title: str | Unset = UNSET
    """ job title of the employee. """
    salary_amount: int | Unset = UNSET
    """ the amount of money the employee earns in cents. When adding a salary to a contract that previously had
    none, both salary_amount and salary_frequency must be provided together. """
    salary_frequency: str | Unset = UNSET
    """ the frequency of the salary payment. When adding a salary to a contract that previously had none, both
    salary_amount and salary_frequency must be provided together. """
    trial_period_ends_on: str | Unset = UNSET
    """ when the trial period ends. """
    working_hours: int | Unset = UNSET
    """ the amount of hours the employee works. """
    working_hours_frequency: str | Unset = UNSET
    """ the frequency of the working hours. """
    working_week_days: str | Unset = UNSET
    """ the days of the week the employee works. """
    max_legal_yearly_hours: int | Unset = UNSET
    """ the maximum amount of hours the employee can work in a year. """
    maximum_weekly_hours: int | Unset = UNSET
    """ the maximum amount of hours the employee can work in a week. """
    bank_holiday_treatment: (
        PostApi20261001ResourcesContractsLegalEntityChangesBodyContractDetailsBankHolidayTreatment
        | Unset
    ) = UNSET
    """ Defines whether a bank holiday should be considered as a workable or non-workable day. """
    working_time_percentage_in_cents: int | Unset = UNSET
    """ Working time percentage in cents (e.g., when an employee is working part-time, the percentage of full-time
    hours they are working). """
    annual_working_time_distribution: (
        PostApi20261001ResourcesContractsLegalEntityChangesBodyContractDetailsAnnualWorkingTimeDistribution
        | Unset
    ) = UNSET
    """ Allows companies to define how annual working hours are spread across the year to ensure compliance with
    legal limits. """
    de_base_salary_type_id: str | Unset = UNSET
    """ Identifier for the German base salary type. References a payroll concept available via the /payroll/concepts
    endpoint. """
    country_data_inputs: (
        list[
            PostApi20261001ResourcesContractsLegalEntityChangesBodyContractDetailsCountryDataInputsItem
        ]
        | Unset
    ) = UNSET
    """ List of country-specific field inputs (e.g. contract_type) for the new version. They are validated against
    the TARGET legal entity's template: discover valid field_name/value_id combinations via GET
    /resources/contracts/materialized_templates.
     """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        effective_on = self.effective_on

        employee_id = self.employee_id

        ends_on = self.ends_on

        has_trial_period = self.has_trial_period

        job_catalog_tree_node_uuid = self.job_catalog_tree_node_uuid

        job_title = self.job_title

        salary_amount = self.salary_amount

        salary_frequency = self.salary_frequency

        trial_period_ends_on = self.trial_period_ends_on

        working_hours = self.working_hours

        working_hours_frequency = self.working_hours_frequency

        working_week_days = self.working_week_days

        max_legal_yearly_hours = self.max_legal_yearly_hours

        maximum_weekly_hours = self.maximum_weekly_hours

        bank_holiday_treatment: str | Unset = UNSET
        if not isinstance(self.bank_holiday_treatment, Unset):
            bank_holiday_treatment = self.bank_holiday_treatment.value if self.bank_holiday_treatment is not None else None

        working_time_percentage_in_cents = self.working_time_percentage_in_cents

        annual_working_time_distribution: str | Unset = UNSET
        if not isinstance(self.annual_working_time_distribution, Unset):
            annual_working_time_distribution = self.annual_working_time_distribution.value if self.annual_working_time_distribution is not None else None

        de_base_salary_type_id = self.de_base_salary_type_id

        country_data_inputs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.country_data_inputs, Unset):
            country_data_inputs = []
            for country_data_inputs_item_data in self.country_data_inputs:
                country_data_inputs_item = country_data_inputs_item_data.to_dict()
                country_data_inputs.append(country_data_inputs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "effective_on": effective_on,
                "employee_id": employee_id,
            }
        )
        if ends_on is not UNSET:
            field_dict["ends_on"] = ends_on
        if has_trial_period is not UNSET:
            field_dict["has_trial_period"] = has_trial_period
        if job_catalog_tree_node_uuid is not UNSET:
            field_dict["job_catalog_tree_node_uuid"] = job_catalog_tree_node_uuid
        if job_title is not UNSET:
            field_dict["job_title"] = job_title
        if salary_amount is not UNSET:
            field_dict["salary_amount"] = salary_amount
        if salary_frequency is not UNSET:
            field_dict["salary_frequency"] = salary_frequency
        if trial_period_ends_on is not UNSET:
            field_dict["trial_period_ends_on"] = trial_period_ends_on
        if working_hours is not UNSET:
            field_dict["working_hours"] = working_hours
        if working_hours_frequency is not UNSET:
            field_dict["working_hours_frequency"] = working_hours_frequency
        if working_week_days is not UNSET:
            field_dict["working_week_days"] = working_week_days
        if max_legal_yearly_hours is not UNSET:
            field_dict["max_legal_yearly_hours"] = max_legal_yearly_hours
        if maximum_weekly_hours is not UNSET:
            field_dict["maximum_weekly_hours"] = maximum_weekly_hours
        if bank_holiday_treatment is not UNSET:
            field_dict["bank_holiday_treatment"] = bank_holiday_treatment
        if working_time_percentage_in_cents is not UNSET:
            field_dict["working_time_percentage_in_cents"] = working_time_percentage_in_cents
        if annual_working_time_distribution is not UNSET:
            field_dict["annual_working_time_distribution"] = annual_working_time_distribution
        if de_base_salary_type_id is not UNSET:
            field_dict["de_base_salary_type_id"] = de_base_salary_type_id
        if country_data_inputs is not UNSET:
            field_dict["country_data_inputs"] = country_data_inputs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_api_20261001_resources_contracts_legal_entity_changes_body_contract_details_country_data_inputs_item import (
            PostApi20261001ResourcesContractsLegalEntityChangesBodyContractDetailsCountryDataInputsItem,
        )

        d = dict(src_dict)
        effective_on = d.pop("effective_on")

        employee_id = d.pop("employee_id")

        ends_on = d.pop("ends_on", UNSET)

        has_trial_period = d.pop("has_trial_period", UNSET)

        job_catalog_tree_node_uuid = d.pop("job_catalog_tree_node_uuid", UNSET)

        job_title = d.pop("job_title", UNSET)

        salary_amount = d.pop("salary_amount", UNSET)

        salary_frequency = d.pop("salary_frequency", UNSET)

        trial_period_ends_on = d.pop("trial_period_ends_on", UNSET)

        working_hours = d.pop("working_hours", UNSET)

        working_hours_frequency = d.pop("working_hours_frequency", UNSET)

        working_week_days = d.pop("working_week_days", UNSET)

        max_legal_yearly_hours = d.pop("max_legal_yearly_hours", UNSET)

        maximum_weekly_hours = d.pop("maximum_weekly_hours", UNSET)

        _bank_holiday_treatment = d.pop("bank_holiday_treatment", UNSET)
        bank_holiday_treatment: (
            PostApi20261001ResourcesContractsLegalEntityChangesBodyContractDetailsBankHolidayTreatment
            | Unset
        )
        if isinstance(_bank_holiday_treatment, Unset):
            bank_holiday_treatment = UNSET
        else:
            bank_holiday_treatment = PostApi20261001ResourcesContractsLegalEntityChangesBodyContractDetailsBankHolidayTreatment(
                _bank_holiday_treatment
            )

        working_time_percentage_in_cents = d.pop("working_time_percentage_in_cents", UNSET)

        _annual_working_time_distribution = d.pop("annual_working_time_distribution", UNSET)
        annual_working_time_distribution: (
            PostApi20261001ResourcesContractsLegalEntityChangesBodyContractDetailsAnnualWorkingTimeDistribution
            | Unset
        )
        if isinstance(_annual_working_time_distribution, Unset):
            annual_working_time_distribution = UNSET
        else:
            annual_working_time_distribution = PostApi20261001ResourcesContractsLegalEntityChangesBodyContractDetailsAnnualWorkingTimeDistribution(
                _annual_working_time_distribution
            )

        de_base_salary_type_id = d.pop("de_base_salary_type_id", UNSET)

        _country_data_inputs = d.pop("country_data_inputs", UNSET)
        country_data_inputs: (
            list[
                PostApi20261001ResourcesContractsLegalEntityChangesBodyContractDetailsCountryDataInputsItem
            ]
            | Unset
        ) = UNSET
        if _country_data_inputs is not UNSET:
            country_data_inputs = []
            for country_data_inputs_item_data in _country_data_inputs:
                country_data_inputs_item = PostApi20261001ResourcesContractsLegalEntityChangesBodyContractDetailsCountryDataInputsItem.from_dict(
                    country_data_inputs_item_data
                )

                country_data_inputs.append(country_data_inputs_item)

        post_api_20261001_resources_contracts_legal_entity_changes_body_contract_details = cls(
            effective_on=effective_on,
            employee_id=employee_id,
            ends_on=ends_on,
            has_trial_period=has_trial_period,
            job_catalog_tree_node_uuid=job_catalog_tree_node_uuid,
            job_title=job_title,
            salary_amount=salary_amount,
            salary_frequency=salary_frequency,
            trial_period_ends_on=trial_period_ends_on,
            working_hours=working_hours,
            working_hours_frequency=working_hours_frequency,
            working_week_days=working_week_days,
            max_legal_yearly_hours=max_legal_yearly_hours,
            maximum_weekly_hours=maximum_weekly_hours,
            bank_holiday_treatment=bank_holiday_treatment,
            working_time_percentage_in_cents=working_time_percentage_in_cents,
            annual_working_time_distribution=annual_working_time_distribution,
            de_base_salary_type_id=de_base_salary_type_id,
            country_data_inputs=country_data_inputs,
        )

        post_api_20261001_resources_contracts_legal_entity_changes_body_contract_details.additional_properties = d
        return post_api_20261001_resources_contracts_legal_entity_changes_body_contract_details

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
