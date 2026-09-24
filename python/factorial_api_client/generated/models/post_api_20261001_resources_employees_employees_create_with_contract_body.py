from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_api_20261001_resources_employees_employees_create_with_contract_body_contracts_annual_working_time_distribution import (
    PostApi20261001ResourcesEmployeesEmployeesCreateWithContractBodyContractsAnnualWorkingTimeDistribution,
)
from ..models.post_api_20261001_resources_employees_employees_create_with_contract_body_contracts_bank_holiday_treatment import (
    PostApi20261001ResourcesEmployeesEmployeesCreateWithContractBodyContractsBankHolidayTreatment,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20261001ResourcesEmployeesEmployeesCreateWithContractBody")


@_attrs_define
class PostApi20261001ResourcesEmployeesEmployeesCreateWithContractBody:
    company_id: str
    """ company id of the employee, you can get it in companies/legal_entities endpoint. """
    first_name: str
    """ name of the employee. """
    last_name: str
    """ last name of the employee. """
    email: str
    """ personal email of the employee. """
    contract_effective_on: str | Unset = UNSET
    """ the day the specific contract starts, in case of hiring the same than contract_starts_on. """
    contract_starts_on: str | Unset = UNSET
    """ the day the employee is hired. """
    ends_on: str | Unset = UNSET
    """ the day the contract ends. """
    gender: str | Unset = UNSET
    """ gender of the employee (male | female). """
    identifier: str | Unset = UNSET
    """ national identifier number. """
    identifier_type: str | Unset = UNSET
    """ type of identifier (ex passport). """
    identifier_expiration_date: str | Unset = UNSET
    """ identifier expiration date. """
    birthday_on: str | Unset = UNSET
    """ birthday of the employee. """
    nationality: str | Unset = UNSET
    """ nationality country code of the employee (Spain ES, United Kingdom GB). """
    address_line1: str | Unset = UNSET
    """ address of the employee. """
    address_line_2: str | Unset = UNSET
    """ address of the employee. """
    postal_code: str | Unset = UNSET
    """ postal code of the employee. """
    city: str | Unset = UNSET
    """ city of the employee. """
    state: str | Unset = UNSET
    """ state/province/region of the employee. """
    country: str | Unset = UNSET
    """ country code of the employee (Spain ES, United Kingdom GB). """
    bank_number: str | Unset = UNSET
    """ bank account number of the employee. """
    swift_bic: str | Unset = UNSET
    """ code to identify banks and financial institutions globally. """
    manager_id: str | Unset = UNSET
    """ id of manager, you can get the manager_id from employees endpoint. """
    timeoff_manager_id: str | Unset = UNSET
    """ id of manager, you can get the manager_id from employees endpoint. """
    legal_entity_id: str | Unset = UNSET
    """ legal entity of the employee, references to companies/legal_entities. """
    company_identifier: str | Unset = UNSET
    """ identity number or string used inside a company to internally identify the employee. """
    seniority_calculation_date: str | Unset = UNSET
    """ date since when the employee is working in the company. """
    job_catalog_tree_node_uuid: str | Unset = UNSET
    """ the uuid of nodes in the job catalog tree. For now it only supports level nodes. From this point in the job
    catalog tree you can get the full ancestor path to the root node including the role. Refer to
    job_catalog/tree_nodes endpoint. """
    team_id: str | Unset = UNSET
    """ team id of the employee. """
    location_id: str | Unset = UNSET
    """ location id of the employee, references to locations/locations. """
    social_security_number: str | Unset = UNSET
    """ social security number of the employee. """
    has_trial_period: bool | Unset = UNSET
    """ does the employee have a trial period? """
    trial_period_ends_on: str | Unset = UNSET
    """ when the trial period ends. """
    contact_name: str | Unset = UNSET
    """ name of the emergency contact. """
    contact_number: str | Unset = UNSET
    """ phone number of the emergency contact. """
    phone_number: str | Unset = UNSET
    """ phone number of the employee. """
    a3_innuva_code: str | Unset = UNSET
    """ A3Innuva employee code. """
    a3_nom_code: str | Unset = UNSET
    """ A3Nom employee code. """
    contracts_bank_holiday_treatment: (
        PostApi20261001ResourcesEmployeesEmployeesCreateWithContractBodyContractsBankHolidayTreatment
        | Unset
    ) = UNSET
    """ Defines whether a bank holiday should be considered as a workable or non-workable day. """
    contracts_annual_working_time_distribution: (
        PostApi20261001ResourcesEmployeesEmployeesCreateWithContractBodyContractsAnnualWorkingTimeDistribution
        | Unset
    ) = UNSET
    """ the annual working time distribution of the employee. """
    contracts_working_time_percentage_in_cents: int | Unset = UNSET
    """ Working time percentage in cents (e.g., when an employee is working part-time, the percentage of full-time
    hours they are working). """
    contracts_max_legal_yearly_hours: int | Unset = UNSET
    """ the maximum amount of hours the employee can work in a year. """
    contracts_maximum_weekly_hours: int | Unset = UNSET
    """ the maximum amount of hours the employee can work in a week. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company_id = self.company_id

        first_name = self.first_name

        last_name = self.last_name

        email = self.email

        contract_effective_on = self.contract_effective_on

        contract_starts_on = self.contract_starts_on

        ends_on = self.ends_on

        gender = self.gender

        identifier = self.identifier

        identifier_type = self.identifier_type

        identifier_expiration_date = self.identifier_expiration_date

        birthday_on = self.birthday_on

        nationality = self.nationality

        address_line1 = self.address_line1

        address_line_2 = self.address_line_2

        postal_code = self.postal_code

        city = self.city

        state = self.state

        country = self.country

        bank_number = self.bank_number

        swift_bic = self.swift_bic

        manager_id = self.manager_id

        timeoff_manager_id = self.timeoff_manager_id

        legal_entity_id = self.legal_entity_id

        company_identifier = self.company_identifier

        seniority_calculation_date = self.seniority_calculation_date

        job_catalog_tree_node_uuid = self.job_catalog_tree_node_uuid

        team_id = self.team_id

        location_id = self.location_id

        social_security_number = self.social_security_number

        has_trial_period = self.has_trial_period

        trial_period_ends_on = self.trial_period_ends_on

        contact_name = self.contact_name

        contact_number = self.contact_number

        phone_number = self.phone_number

        a3_innuva_code = self.a3_innuva_code

        a3_nom_code = self.a3_nom_code

        contracts_bank_holiday_treatment: str | Unset = UNSET
        if not isinstance(self.contracts_bank_holiday_treatment, Unset):
            contracts_bank_holiday_treatment = self.contracts_bank_holiday_treatment.value if self.contracts_bank_holiday_treatment is not None else None

        contracts_annual_working_time_distribution: str | Unset = UNSET
        if not isinstance(self.contracts_annual_working_time_distribution, Unset):
            contracts_annual_working_time_distribution = (
                self.contracts_annual_working_time_distribution.value
            )

        contracts_working_time_percentage_in_cents = self.contracts_working_time_percentage_in_cents

        contracts_max_legal_yearly_hours = self.contracts_max_legal_yearly_hours

        contracts_maximum_weekly_hours = self.contracts_maximum_weekly_hours

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "company_id": company_id,
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
            }
        )
        if contract_effective_on is not UNSET:
            field_dict["contract_effective_on"] = contract_effective_on
        if contract_starts_on is not UNSET:
            field_dict["contract_starts_on"] = contract_starts_on
        if ends_on is not UNSET:
            field_dict["ends_on"] = ends_on
        if gender is not UNSET:
            field_dict["gender"] = gender
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if identifier_type is not UNSET:
            field_dict["identifier_type"] = identifier_type
        if identifier_expiration_date is not UNSET:
            field_dict["identifier_expiration_date"] = identifier_expiration_date
        if birthday_on is not UNSET:
            field_dict["birthday_on"] = birthday_on
        if nationality is not UNSET:
            field_dict["nationality"] = nationality
        if address_line1 is not UNSET:
            field_dict["address_line1"] = address_line1
        if address_line_2 is not UNSET:
            field_dict["address_line_2"] = address_line_2
        if postal_code is not UNSET:
            field_dict["postal_code"] = postal_code
        if city is not UNSET:
            field_dict["city"] = city
        if state is not UNSET:
            field_dict["state"] = state
        if country is not UNSET:
            field_dict["country"] = country
        if bank_number is not UNSET:
            field_dict["bank_number"] = bank_number
        if swift_bic is not UNSET:
            field_dict["swift_bic"] = swift_bic
        if manager_id is not UNSET:
            field_dict["manager_id"] = manager_id
        if timeoff_manager_id is not UNSET:
            field_dict["timeoff_manager_id"] = timeoff_manager_id
        if legal_entity_id is not UNSET:
            field_dict["legal_entity_id"] = legal_entity_id
        if company_identifier is not UNSET:
            field_dict["company_identifier"] = company_identifier
        if seniority_calculation_date is not UNSET:
            field_dict["seniority_calculation_date"] = seniority_calculation_date
        if job_catalog_tree_node_uuid is not UNSET:
            field_dict["job_catalog_tree_node_uuid"] = job_catalog_tree_node_uuid
        if team_id is not UNSET:
            field_dict["team_id"] = team_id
        if location_id is not UNSET:
            field_dict["location_id"] = location_id
        if social_security_number is not UNSET:
            field_dict["social_security_number"] = social_security_number
        if has_trial_period is not UNSET:
            field_dict["has_trial_period"] = has_trial_period
        if trial_period_ends_on is not UNSET:
            field_dict["trial_period_ends_on"] = trial_period_ends_on
        if contact_name is not UNSET:
            field_dict["contact_name"] = contact_name
        if contact_number is not UNSET:
            field_dict["contact_number"] = contact_number
        if phone_number is not UNSET:
            field_dict["phone_number"] = phone_number
        if a3_innuva_code is not UNSET:
            field_dict["a3_innuva_code"] = a3_innuva_code
        if a3_nom_code is not UNSET:
            field_dict["a3_nom_code"] = a3_nom_code
        if contracts_bank_holiday_treatment is not UNSET:
            field_dict["contracts_bank_holiday_treatment"] = contracts_bank_holiday_treatment
        if contracts_annual_working_time_distribution is not UNSET:
            field_dict["contracts_annual_working_time_distribution"] = (
                contracts_annual_working_time_distribution
            )
        if contracts_working_time_percentage_in_cents is not UNSET:
            field_dict["contracts_working_time_percentage_in_cents"] = (
                contracts_working_time_percentage_in_cents
            )
        if contracts_max_legal_yearly_hours is not UNSET:
            field_dict["contracts_max_legal_yearly_hours"] = contracts_max_legal_yearly_hours
        if contracts_maximum_weekly_hours is not UNSET:
            field_dict["contracts_maximum_weekly_hours"] = contracts_maximum_weekly_hours

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        company_id = d.pop("company_id")

        first_name = d.pop("first_name")

        last_name = d.pop("last_name")

        email = d.pop("email")

        contract_effective_on = d.pop("contract_effective_on", UNSET)

        contract_starts_on = d.pop("contract_starts_on", UNSET)

        ends_on = d.pop("ends_on", UNSET)

        gender = d.pop("gender", UNSET)

        identifier = d.pop("identifier", UNSET)

        identifier_type = d.pop("identifier_type", UNSET)

        identifier_expiration_date = d.pop("identifier_expiration_date", UNSET)

        birthday_on = d.pop("birthday_on", UNSET)

        nationality = d.pop("nationality", UNSET)

        address_line1 = d.pop("address_line1", UNSET)

        address_line_2 = d.pop("address_line_2", UNSET)

        postal_code = d.pop("postal_code", UNSET)

        city = d.pop("city", UNSET)

        state = d.pop("state", UNSET)

        country = d.pop("country", UNSET)

        bank_number = d.pop("bank_number", UNSET)

        swift_bic = d.pop("swift_bic", UNSET)

        manager_id = d.pop("manager_id", UNSET)

        timeoff_manager_id = d.pop("timeoff_manager_id", UNSET)

        legal_entity_id = d.pop("legal_entity_id", UNSET)

        company_identifier = d.pop("company_identifier", UNSET)

        seniority_calculation_date = d.pop("seniority_calculation_date", UNSET)

        job_catalog_tree_node_uuid = d.pop("job_catalog_tree_node_uuid", UNSET)

        team_id = d.pop("team_id", UNSET)

        location_id = d.pop("location_id", UNSET)

        social_security_number = d.pop("social_security_number", UNSET)

        has_trial_period = d.pop("has_trial_period", UNSET)

        trial_period_ends_on = d.pop("trial_period_ends_on", UNSET)

        contact_name = d.pop("contact_name", UNSET)

        contact_number = d.pop("contact_number", UNSET)

        phone_number = d.pop("phone_number", UNSET)

        a3_innuva_code = d.pop("a3_innuva_code", UNSET)

        a3_nom_code = d.pop("a3_nom_code", UNSET)

        _contracts_bank_holiday_treatment = d.pop("contracts_bank_holiday_treatment", UNSET)
        contracts_bank_holiday_treatment: (
            PostApi20261001ResourcesEmployeesEmployeesCreateWithContractBodyContractsBankHolidayTreatment
            | Unset
        )
        if isinstance(_contracts_bank_holiday_treatment, Unset):
            contracts_bank_holiday_treatment = UNSET
        else:
            contracts_bank_holiday_treatment = PostApi20261001ResourcesEmployeesEmployeesCreateWithContractBodyContractsBankHolidayTreatment(
                _contracts_bank_holiday_treatment
            )

        _contracts_annual_working_time_distribution = d.pop(
            "contracts_annual_working_time_distribution", UNSET
        )
        contracts_annual_working_time_distribution: (
            PostApi20261001ResourcesEmployeesEmployeesCreateWithContractBodyContractsAnnualWorkingTimeDistribution
            | Unset
        )
        if isinstance(_contracts_annual_working_time_distribution, Unset):
            contracts_annual_working_time_distribution = UNSET
        else:
            contracts_annual_working_time_distribution = PostApi20261001ResourcesEmployeesEmployeesCreateWithContractBodyContractsAnnualWorkingTimeDistribution(
                _contracts_annual_working_time_distribution
            )

        contracts_working_time_percentage_in_cents = d.pop(
            "contracts_working_time_percentage_in_cents", UNSET
        )

        contracts_max_legal_yearly_hours = d.pop("contracts_max_legal_yearly_hours", UNSET)

        contracts_maximum_weekly_hours = d.pop("contracts_maximum_weekly_hours", UNSET)

        post_api_20261001_resources_employees_employees_create_with_contract_body = cls(
            company_id=company_id,
            first_name=first_name,
            last_name=last_name,
            email=email,
            contract_effective_on=contract_effective_on,
            contract_starts_on=contract_starts_on,
            ends_on=ends_on,
            gender=gender,
            identifier=identifier,
            identifier_type=identifier_type,
            identifier_expiration_date=identifier_expiration_date,
            birthday_on=birthday_on,
            nationality=nationality,
            address_line1=address_line1,
            address_line_2=address_line_2,
            postal_code=postal_code,
            city=city,
            state=state,
            country=country,
            bank_number=bank_number,
            swift_bic=swift_bic,
            manager_id=manager_id,
            timeoff_manager_id=timeoff_manager_id,
            legal_entity_id=legal_entity_id,
            company_identifier=company_identifier,
            seniority_calculation_date=seniority_calculation_date,
            job_catalog_tree_node_uuid=job_catalog_tree_node_uuid,
            team_id=team_id,
            location_id=location_id,
            social_security_number=social_security_number,
            has_trial_period=has_trial_period,
            trial_period_ends_on=trial_period_ends_on,
            contact_name=contact_name,
            contact_number=contact_number,
            phone_number=phone_number,
            a3_innuva_code=a3_innuva_code,
            a3_nom_code=a3_nom_code,
            contracts_bank_holiday_treatment=contracts_bank_holiday_treatment,
            contracts_annual_working_time_distribution=contracts_annual_working_time_distribution,
            contracts_working_time_percentage_in_cents=contracts_working_time_percentage_in_cents,
            contracts_max_legal_yearly_hours=contracts_max_legal_yearly_hours,
            contracts_maximum_weekly_hours=contracts_maximum_weekly_hours,
        )

        post_api_20261001_resources_employees_employees_create_with_contract_body.additional_properties = d
        return post_api_20261001_resources_employees_employees_create_with_contract_body

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
