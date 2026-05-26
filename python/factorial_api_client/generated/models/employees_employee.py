from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.employees_employee_bank_number_format import EmployeesEmployeeBankNumberFormat
from ..types import UNSET, Unset

T = TypeVar("T", bound="EmployeesEmployee")


@_attrs_define
class EmployeesEmployee:
    id: int
    """ id of the employee. """
    access_id: int
    """ access_id associated to the employee. """
    first_name: str
    """ name of the employee. """
    last_name: str
    """ last name of the employee. """
    full_name: str
    """ full name of the employee. """
    company_id: int
    """ id of the company to which the employee belongs (not editable). """
    location_id: int
    """ location id of the employee, references to locations/locations. """
    created_at: str
    """ creation date of the employee. """
    updated_at: str
    """ date of last modification of the employee """
    is_terminating: bool
    """ is the employee being terminated? """
    attendable: bool
    """ employee included in a time tracking policy. """
    preferred_name: str | Unset = UNSET
    """ nickname of the employee or a name that defines the employee better. """
    birth_name: str | Unset = UNSET
    """ Birthname of the employee. """
    gender: str | Unset = UNSET
    """ gender of the employee (male | female). """
    identifier: str | Unset = UNSET
    """ national identifier number. """
    identifier_type: str | Unset = UNSET
    """ type of identifier (ex passport). """
    email: str | Unset = UNSET
    """ personal email of the employee. """
    login_email: str | Unset = UNSET
    """ email associated to the session. """
    birthday_on: str | Unset = UNSET
    """ birthday of the employee. """
    nationality: str | Unset = UNSET
    """ nationality country code of the employee (Spain ES, United Kingdom GB). """
    address_line_1: str | Unset = UNSET
    """ address of the employee. """
    address_line_2: str | Unset = UNSET
    """ secondary address of the employee. """
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
    bank_number_format: EmployeesEmployeeBankNumberFormat | Unset = UNSET
    """ bank number format. """
    legal_entity_id: int | Unset = UNSET
    """ legal entity of the employee, references to companies/legal_entities. """
    social_security_number: str | Unset = UNSET
    """ social security number of the employee. """
    terminated_on: str | Unset = UNSET
    """ termination date of the employee. """
    termination_reason_type: str | Unset = UNSET
    """ termination reason type of the employee """
    termination_reason: str | Unset = UNSET
    """ A reason for the termination. """
    termination_observations: str | Unset = UNSET
    """ observations about the termination. """
    manager_id: int | Unset = UNSET
    """ manager id of the employee, you can get the manager id from employees endpoint. """
    timeoff_manager_id: int | Unset = UNSET
    """ Timeoff manager id of the employee. """
    phone_number: str | Unset = UNSET
    """ phone number of the employee. """
    company_identifier: str | Unset = UNSET
    """ identity number or string used inside a company to internally identify the employee. """
    age_number: int | Unset = UNSET
    """ age of the employee. """
    termination_type_description: str | Unset = UNSET
    """ The description of the termination type. """
    contact_name: str | Unset = UNSET
    """ name of the employee contact. """
    contact_number: str | Unset = UNSET
    """ phone number of the employee contact . """
    personal_email: str | Unset = UNSET
    """ personal email of the employee. """
    seniority_calculation_date: str | Unset = UNSET
    """ date since when the employee is working in the company. """
    pronouns: str | Unset = UNSET
    """ pronouns that an employee uses to define themselves. """
    active: bool | Unset = UNSET
    """ status of the employee, true when active, false when terminated. """
    disability_percentage_cents: int | Unset = UNSET
    """ officially certified level of disability granted by public administration for individuals with physical or
    mental impairments, expressed in cents """
    identifier_expiration_date: str | Unset = UNSET
    """ identifier expiration date """
    country_of_birth: str | Unset = UNSET
    """ Country of birth of the employee. """
    birthplace: str | Unset = UNSET
    """ Birthplace of the employee. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        access_id = self.access_id

        first_name = self.first_name

        last_name = self.last_name

        full_name = self.full_name

        company_id = self.company_id

        location_id = self.location_id

        created_at = self.created_at

        updated_at = self.updated_at

        is_terminating = self.is_terminating

        attendable = self.attendable

        preferred_name = self.preferred_name

        birth_name = self.birth_name

        gender = self.gender

        identifier = self.identifier

        identifier_type = self.identifier_type

        email = self.email

        login_email = self.login_email

        birthday_on = self.birthday_on

        nationality = self.nationality

        address_line_1 = self.address_line_1

        address_line_2 = self.address_line_2

        postal_code = self.postal_code

        city = self.city

        state = self.state

        country = self.country

        bank_number = self.bank_number

        swift_bic = self.swift_bic

        bank_number_format: str | Unset = UNSET
        if not isinstance(self.bank_number_format, Unset):
            bank_number_format = self.bank_number_format.value

        legal_entity_id = self.legal_entity_id

        social_security_number = self.social_security_number

        terminated_on = self.terminated_on

        termination_reason_type = self.termination_reason_type

        termination_reason = self.termination_reason

        termination_observations = self.termination_observations

        manager_id = self.manager_id

        timeoff_manager_id = self.timeoff_manager_id

        phone_number = self.phone_number

        company_identifier = self.company_identifier

        age_number = self.age_number

        termination_type_description = self.termination_type_description

        contact_name = self.contact_name

        contact_number = self.contact_number

        personal_email = self.personal_email

        seniority_calculation_date = self.seniority_calculation_date

        pronouns = self.pronouns

        active = self.active

        disability_percentage_cents = self.disability_percentage_cents

        identifier_expiration_date = self.identifier_expiration_date

        country_of_birth = self.country_of_birth

        birthplace = self.birthplace

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "access_id": access_id,
                "first_name": first_name,
                "last_name": last_name,
                "full_name": full_name,
                "company_id": company_id,
                "location_id": location_id,
                "created_at": created_at,
                "updated_at": updated_at,
                "is_terminating": is_terminating,
                "attendable": attendable,
            }
        )
        if preferred_name is not UNSET:
            field_dict["preferred_name"] = preferred_name
        if birth_name is not UNSET:
            field_dict["birth_name"] = birth_name
        if gender is not UNSET:
            field_dict["gender"] = gender
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if identifier_type is not UNSET:
            field_dict["identifier_type"] = identifier_type
        if email is not UNSET:
            field_dict["email"] = email
        if login_email is not UNSET:
            field_dict["login_email"] = login_email
        if birthday_on is not UNSET:
            field_dict["birthday_on"] = birthday_on
        if nationality is not UNSET:
            field_dict["nationality"] = nationality
        if address_line_1 is not UNSET:
            field_dict["address_line_1"] = address_line_1
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
        if bank_number_format is not UNSET:
            field_dict["bank_number_format"] = bank_number_format
        if legal_entity_id is not UNSET:
            field_dict["legal_entity_id"] = legal_entity_id
        if social_security_number is not UNSET:
            field_dict["social_security_number"] = social_security_number
        if terminated_on is not UNSET:
            field_dict["terminated_on"] = terminated_on
        if termination_reason_type is not UNSET:
            field_dict["termination_reason_type"] = termination_reason_type
        if termination_reason is not UNSET:
            field_dict["termination_reason"] = termination_reason
        if termination_observations is not UNSET:
            field_dict["termination_observations"] = termination_observations
        if manager_id is not UNSET:
            field_dict["manager_id"] = manager_id
        if timeoff_manager_id is not UNSET:
            field_dict["timeoff_manager_id"] = timeoff_manager_id
        if phone_number is not UNSET:
            field_dict["phone_number"] = phone_number
        if company_identifier is not UNSET:
            field_dict["company_identifier"] = company_identifier
        if age_number is not UNSET:
            field_dict["age_number"] = age_number
        if termination_type_description is not UNSET:
            field_dict["termination_type_description"] = termination_type_description
        if contact_name is not UNSET:
            field_dict["contact_name"] = contact_name
        if contact_number is not UNSET:
            field_dict["contact_number"] = contact_number
        if personal_email is not UNSET:
            field_dict["personal_email"] = personal_email
        if seniority_calculation_date is not UNSET:
            field_dict["seniority_calculation_date"] = seniority_calculation_date
        if pronouns is not UNSET:
            field_dict["pronouns"] = pronouns
        if active is not UNSET:
            field_dict["active"] = active
        if disability_percentage_cents is not UNSET:
            field_dict["disability_percentage_cents"] = disability_percentage_cents
        if identifier_expiration_date is not UNSET:
            field_dict["identifier_expiration_date"] = identifier_expiration_date
        if country_of_birth is not UNSET:
            field_dict["country_of_birth"] = country_of_birth
        if birthplace is not UNSET:
            field_dict["birthplace"] = birthplace

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        access_id = d.pop("access_id")

        first_name = d.pop("first_name")

        last_name = d.pop("last_name")

        full_name = d.pop("full_name")

        company_id = d.pop("company_id")

        location_id = d.pop("location_id")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        is_terminating = d.pop("is_terminating")

        attendable = d.pop("attendable")

        preferred_name = d.pop("preferred_name", UNSET)

        birth_name = d.pop("birth_name", UNSET)

        gender = d.pop("gender", UNSET)

        identifier = d.pop("identifier", UNSET)

        identifier_type = d.pop("identifier_type", UNSET)

        email = d.pop("email", UNSET)

        login_email = d.pop("login_email", UNSET)

        birthday_on = d.pop("birthday_on", UNSET)

        nationality = d.pop("nationality", UNSET)

        address_line_1 = d.pop("address_line_1", UNSET)

        address_line_2 = d.pop("address_line_2", UNSET)

        postal_code = d.pop("postal_code", UNSET)

        city = d.pop("city", UNSET)

        state = d.pop("state", UNSET)

        country = d.pop("country", UNSET)

        bank_number = d.pop("bank_number", UNSET)

        swift_bic = d.pop("swift_bic", UNSET)

        _bank_number_format = d.pop("bank_number_format", UNSET)
        bank_number_format: EmployeesEmployeeBankNumberFormat | Unset
        if isinstance(_bank_number_format, Unset):
            bank_number_format = UNSET
        else:
            bank_number_format = EmployeesEmployeeBankNumberFormat(_bank_number_format) if _bank_number_format is not None else None

        legal_entity_id = d.pop("legal_entity_id", UNSET)

        social_security_number = d.pop("social_security_number", UNSET)

        terminated_on = d.pop("terminated_on", UNSET)

        termination_reason_type = d.pop("termination_reason_type", UNSET)

        termination_reason = d.pop("termination_reason", UNSET)

        termination_observations = d.pop("termination_observations", UNSET)

        manager_id = d.pop("manager_id", UNSET)

        timeoff_manager_id = d.pop("timeoff_manager_id", UNSET)

        phone_number = d.pop("phone_number", UNSET)

        company_identifier = d.pop("company_identifier", UNSET)

        age_number = d.pop("age_number", UNSET)

        termination_type_description = d.pop("termination_type_description", UNSET)

        contact_name = d.pop("contact_name", UNSET)

        contact_number = d.pop("contact_number", UNSET)

        personal_email = d.pop("personal_email", UNSET)

        seniority_calculation_date = d.pop("seniority_calculation_date", UNSET)

        pronouns = d.pop("pronouns", UNSET)

        active = d.pop("active", UNSET)

        disability_percentage_cents = d.pop("disability_percentage_cents", UNSET)

        identifier_expiration_date = d.pop("identifier_expiration_date", UNSET)

        country_of_birth = d.pop("country_of_birth", UNSET)

        birthplace = d.pop("birthplace", UNSET)

        employees_employee = cls(
            id=id,
            access_id=access_id,
            first_name=first_name,
            last_name=last_name,
            full_name=full_name,
            company_id=company_id,
            location_id=location_id,
            created_at=created_at,
            updated_at=updated_at,
            is_terminating=is_terminating,
            attendable=attendable,
            preferred_name=preferred_name,
            birth_name=birth_name,
            gender=gender,
            identifier=identifier,
            identifier_type=identifier_type,
            email=email,
            login_email=login_email,
            birthday_on=birthday_on,
            nationality=nationality,
            address_line_1=address_line_1,
            address_line_2=address_line_2,
            postal_code=postal_code,
            city=city,
            state=state,
            country=country,
            bank_number=bank_number,
            swift_bic=swift_bic,
            bank_number_format=bank_number_format,
            legal_entity_id=legal_entity_id,
            social_security_number=social_security_number,
            terminated_on=terminated_on,
            termination_reason_type=termination_reason_type,
            termination_reason=termination_reason,
            termination_observations=termination_observations,
            manager_id=manager_id,
            timeoff_manager_id=timeoff_manager_id,
            phone_number=phone_number,
            company_identifier=company_identifier,
            age_number=age_number,
            termination_type_description=termination_type_description,
            contact_name=contact_name,
            contact_number=contact_number,
            personal_email=personal_email,
            seniority_calculation_date=seniority_calculation_date,
            pronouns=pronouns,
            active=active,
            disability_percentage_cents=disability_percentage_cents,
            identifier_expiration_date=identifier_expiration_date,
            country_of_birth=country_of_birth,
            birthplace=birthplace,
        )

        employees_employee.additional_properties = d
        return employees_employee

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
