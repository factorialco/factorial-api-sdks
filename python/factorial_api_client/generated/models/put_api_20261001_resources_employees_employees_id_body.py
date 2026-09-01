from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PutApi20261001ResourcesEmployeesEmployeesIdBody")


@_attrs_define
class PutApi20261001ResourcesEmployeesEmployeesIdBody:
    id: str
    """ id of the employee. """
    access_id: str | Unset = UNSET
    """ access_id of the creator. """
    gender: str | Unset = UNSET
    """ gender of the employee (male | female). """
    first_name: str | Unset = UNSET
    """ name of the employee. """
    last_name: str | Unset = UNSET
    """ last name of the employee. """
    identifier: str | Unset = UNSET
    """ national identifier number. """
    identifier_type: str | Unset = UNSET
    """ type of identifier (ex passport). """
    birthday_on: str | Unset = UNSET
    """ birthday of the employee. """
    nationality: str | Unset = UNSET
    """ nationality country code of the employee (Spain ES, United Kingdom GB). """
    address_line_1: str | Unset = UNSET
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
    social_security_number: str | Unset = UNSET
    """ social security number of the employee. """
    has_work_permit: bool | Unset = UNSET
    """ does the employee have work permit? """
    phone_number: str | Unset = UNSET
    """ phone number of the employee. """
    company_identifier: str | Unset = UNSET
    """ identity number or string used inside a company to internally identify the employee. """
    seniority_calculation_date: str | Unset = UNSET
    """ date since when the employee is working in the company. """
    legal_entity_id: str | Unset = UNSET
    """ legal entity of the employee, references to companies/legal_entities. """
    location_id: str | Unset = UNSET
    """ location id of the employee, references to locations/locations. """
    preferred_name: str | Unset = UNSET
    """ nickname of the employee or a name that defines the employee better. """
    pronouns: str | Unset = UNSET
    """ pronouns that an employee uses to define themselves. """
    contact_name: str | Unset = UNSET
    """ name of the employee contact. """
    contact_number: str | Unset = UNSET
    """ phone number of the employee contact . """
    personal_email: str | Unset = UNSET
    """ personal email of the employee. """
    communications_email: str | Unset = UNSET
    """ Email address for company communications and notifications. Separate from login email. """
    disability_percentage_cents: int | Unset = UNSET
    """ officially certified level of disability granted by public administration for individuals with physical or
    mental impairments, expressed in cents """
    identifier_expiration_date: str | Unset = UNSET
    """ identifier expiration date """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        access_id = self.access_id

        gender = self.gender

        first_name = self.first_name

        last_name = self.last_name

        identifier = self.identifier

        identifier_type = self.identifier_type

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

        manager_id = self.manager_id

        timeoff_manager_id = self.timeoff_manager_id

        social_security_number = self.social_security_number

        has_work_permit = self.has_work_permit

        phone_number = self.phone_number

        company_identifier = self.company_identifier

        seniority_calculation_date = self.seniority_calculation_date

        legal_entity_id = self.legal_entity_id

        location_id = self.location_id

        preferred_name = self.preferred_name

        pronouns = self.pronouns

        contact_name = self.contact_name

        contact_number = self.contact_number

        personal_email = self.personal_email

        communications_email = self.communications_email

        disability_percentage_cents = self.disability_percentage_cents

        identifier_expiration_date = self.identifier_expiration_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if access_id is not UNSET:
            field_dict["access_id"] = access_id
        if gender is not UNSET:
            field_dict["gender"] = gender
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if identifier_type is not UNSET:
            field_dict["identifier_type"] = identifier_type
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
        if manager_id is not UNSET:
            field_dict["manager_id"] = manager_id
        if timeoff_manager_id is not UNSET:
            field_dict["timeoff_manager_id"] = timeoff_manager_id
        if social_security_number is not UNSET:
            field_dict["social_security_number"] = social_security_number
        if has_work_permit is not UNSET:
            field_dict["has_work_permit"] = has_work_permit
        if phone_number is not UNSET:
            field_dict["phone_number"] = phone_number
        if company_identifier is not UNSET:
            field_dict["company_identifier"] = company_identifier
        if seniority_calculation_date is not UNSET:
            field_dict["seniority_calculation_date"] = seniority_calculation_date
        if legal_entity_id is not UNSET:
            field_dict["legal_entity_id"] = legal_entity_id
        if location_id is not UNSET:
            field_dict["location_id"] = location_id
        if preferred_name is not UNSET:
            field_dict["preferred_name"] = preferred_name
        if pronouns is not UNSET:
            field_dict["pronouns"] = pronouns
        if contact_name is not UNSET:
            field_dict["contact_name"] = contact_name
        if contact_number is not UNSET:
            field_dict["contact_number"] = contact_number
        if personal_email is not UNSET:
            field_dict["personal_email"] = personal_email
        if communications_email is not UNSET:
            field_dict["communications_email"] = communications_email
        if disability_percentage_cents is not UNSET:
            field_dict["disability_percentage_cents"] = disability_percentage_cents
        if identifier_expiration_date is not UNSET:
            field_dict["identifier_expiration_date"] = identifier_expiration_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        access_id = d.pop("access_id", UNSET)

        gender = d.pop("gender", UNSET)

        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        identifier = d.pop("identifier", UNSET)

        identifier_type = d.pop("identifier_type", UNSET)

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

        manager_id = d.pop("manager_id", UNSET)

        timeoff_manager_id = d.pop("timeoff_manager_id", UNSET)

        social_security_number = d.pop("social_security_number", UNSET)

        has_work_permit = d.pop("has_work_permit", UNSET)

        phone_number = d.pop("phone_number", UNSET)

        company_identifier = d.pop("company_identifier", UNSET)

        seniority_calculation_date = d.pop("seniority_calculation_date", UNSET)

        legal_entity_id = d.pop("legal_entity_id", UNSET)

        location_id = d.pop("location_id", UNSET)

        preferred_name = d.pop("preferred_name", UNSET)

        pronouns = d.pop("pronouns", UNSET)

        contact_name = d.pop("contact_name", UNSET)

        contact_number = d.pop("contact_number", UNSET)

        personal_email = d.pop("personal_email", UNSET)

        communications_email = d.pop("communications_email", UNSET)

        disability_percentage_cents = d.pop("disability_percentage_cents", UNSET)

        identifier_expiration_date = d.pop("identifier_expiration_date", UNSET)

        put_api_20261001_resources_employees_employees_id_body = cls(
            id=id,
            access_id=access_id,
            gender=gender,
            first_name=first_name,
            last_name=last_name,
            identifier=identifier,
            identifier_type=identifier_type,
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
            manager_id=manager_id,
            timeoff_manager_id=timeoff_manager_id,
            social_security_number=social_security_number,
            has_work_permit=has_work_permit,
            phone_number=phone_number,
            company_identifier=company_identifier,
            seniority_calculation_date=seniority_calculation_date,
            legal_entity_id=legal_entity_id,
            location_id=location_id,
            preferred_name=preferred_name,
            pronouns=pronouns,
            contact_name=contact_name,
            contact_number=contact_number,
            personal_email=personal_email,
            communications_email=communications_email,
            disability_percentage_cents=disability_percentage_cents,
            identifier_expiration_date=identifier_expiration_date,
        )

        put_api_20261001_resources_employees_employees_id_body.additional_properties = d
        return put_api_20261001_resources_employees_employees_id_body

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
