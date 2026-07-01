from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EmployeeUpdatesNewHire")


@_attrs_define
class EmployeeUpdatesNewHire:
    id: str
    """ The id of the new hire incidence """
    status: str
    """ The status of the new hire incidence """
    employee_id: str
    """ The employee id of the new hire """
    first_name: str
    """ name of the employee. """
    last_name: str
    """ last name of the employee. """
    address: str
    """ address of the employee. """
    birth_name: str | Unset = UNSET
    """ The birth name of the new hire """
    identifier: str | Unset = UNSET
    """ national identifier number. """
    identifier_type: str | Unset = UNSET
    """ type of identifier (ex passport). """
    payroll_identifier: str | Unset = UNSET
    """ payroll identifier. """
    work_email: str | Unset = UNSET
    """ personal email of the employee. """
    phone_number: str | Unset = UNSET
    """ phone number of the employee. """
    gender: str | Unset = UNSET
    """ gender of the employee (male | female). """
    job_title: str | Unset = UNSET
    """ job title of the employee. """
    city: str | Unset = UNSET
    """ city of the employee. """
    country: str | Unset = UNSET
    """ country code of the employee (Spain ES, United Kingdom GB). """
    state: str | Unset = UNSET
    """ state/province/region of the employee. """
    postal_code: str | Unset = UNSET
    """ postal code of the employee. """
    date_of_birth: str | Unset = UNSET
    """ birthday of the employee. """
    nationality: str | Unset = UNSET
    """ nationality country code of the employee (Spain ES, United Kingdom GB). """
    start_date: str | Unset = UNSET
    contract_effective_date: str | Unset = UNSET
    contract_end_date: str | Unset = UNSET
    bank_account: str | Unset = UNSET
    """ bank account number of the employee. """
    salary_amount_in_cents: int | Unset = UNSET
    """ salary amount in cents. """
    salary_frequency: str | Unset = UNSET
    working_hours: int | Unset = UNSET
    working_hours_frequency: str | Unset = UNSET
    social_security_number: str | Unset = UNSET
    """ social security number of the employee. """
    manager_id: str | Unset = UNSET
    """ manager id of the employee, you can get the manager id from employees endpoint. """
    tax_id: str | Unset = UNSET
    legal_entity_id: str | Unset = UNSET
    """ The legal entity id of the new hire """
    workplace_id: str | Unset = UNSET
    """ workplace id of the employee. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        status = self.status

        employee_id = self.employee_id

        first_name = self.first_name

        last_name = self.last_name

        address = self.address

        birth_name = self.birth_name

        identifier = self.identifier

        identifier_type = self.identifier_type

        payroll_identifier = self.payroll_identifier

        work_email = self.work_email

        phone_number = self.phone_number

        gender = self.gender

        job_title = self.job_title

        city = self.city

        country = self.country

        state = self.state

        postal_code = self.postal_code

        date_of_birth = self.date_of_birth

        nationality = self.nationality

        start_date = self.start_date

        contract_effective_date = self.contract_effective_date

        contract_end_date = self.contract_end_date

        bank_account = self.bank_account

        salary_amount_in_cents = self.salary_amount_in_cents

        salary_frequency = self.salary_frequency

        working_hours = self.working_hours

        working_hours_frequency = self.working_hours_frequency

        social_security_number = self.social_security_number

        manager_id = self.manager_id

        tax_id = self.tax_id

        legal_entity_id = self.legal_entity_id

        workplace_id = self.workplace_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "status": status,
                "employee_id": employee_id,
                "first_name": first_name,
                "last_name": last_name,
                "address": address,
            }
        )
        if birth_name is not UNSET:
            field_dict["birth_name"] = birth_name
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if identifier_type is not UNSET:
            field_dict["identifier_type"] = identifier_type
        if payroll_identifier is not UNSET:
            field_dict["payroll_identifier"] = payroll_identifier
        if work_email is not UNSET:
            field_dict["work_email"] = work_email
        if phone_number is not UNSET:
            field_dict["phone_number"] = phone_number
        if gender is not UNSET:
            field_dict["gender"] = gender
        if job_title is not UNSET:
            field_dict["job_title"] = job_title
        if city is not UNSET:
            field_dict["city"] = city
        if country is not UNSET:
            field_dict["country"] = country
        if state is not UNSET:
            field_dict["state"] = state
        if postal_code is not UNSET:
            field_dict["postal_code"] = postal_code
        if date_of_birth is not UNSET:
            field_dict["date_of_birth"] = date_of_birth
        if nationality is not UNSET:
            field_dict["nationality"] = nationality
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if contract_effective_date is not UNSET:
            field_dict["contract_effective_date"] = contract_effective_date
        if contract_end_date is not UNSET:
            field_dict["contract_end_date"] = contract_end_date
        if bank_account is not UNSET:
            field_dict["bank_account"] = bank_account
        if salary_amount_in_cents is not UNSET:
            field_dict["salary_amount_in_cents"] = salary_amount_in_cents
        if salary_frequency is not UNSET:
            field_dict["salary_frequency"] = salary_frequency
        if working_hours is not UNSET:
            field_dict["working_hours"] = working_hours
        if working_hours_frequency is not UNSET:
            field_dict["working_hours_frequency"] = working_hours_frequency
        if social_security_number is not UNSET:
            field_dict["social_security_number"] = social_security_number
        if manager_id is not UNSET:
            field_dict["manager_id"] = manager_id
        if tax_id is not UNSET:
            field_dict["tax_id"] = tax_id
        if legal_entity_id is not UNSET:
            field_dict["legal_entity_id"] = legal_entity_id
        if workplace_id is not UNSET:
            field_dict["workplace_id"] = workplace_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        status = d.pop("status")

        employee_id = d.pop("employee_id")

        first_name = d.pop("first_name")

        last_name = d.pop("last_name")

        address = d.pop("address")

        birth_name = d.pop("birth_name", UNSET)

        identifier = d.pop("identifier", UNSET)

        identifier_type = d.pop("identifier_type", UNSET)

        payroll_identifier = d.pop("payroll_identifier", UNSET)

        work_email = d.pop("work_email", UNSET)

        phone_number = d.pop("phone_number", UNSET)

        gender = d.pop("gender", UNSET)

        job_title = d.pop("job_title", UNSET)

        city = d.pop("city", UNSET)

        country = d.pop("country", UNSET)

        state = d.pop("state", UNSET)

        postal_code = d.pop("postal_code", UNSET)

        date_of_birth = d.pop("date_of_birth", UNSET)

        nationality = d.pop("nationality", UNSET)

        start_date = d.pop("start_date", UNSET)

        contract_effective_date = d.pop("contract_effective_date", UNSET)

        contract_end_date = d.pop("contract_end_date", UNSET)

        bank_account = d.pop("bank_account", UNSET)

        salary_amount_in_cents = d.pop("salary_amount_in_cents", UNSET)

        salary_frequency = d.pop("salary_frequency", UNSET)

        working_hours = d.pop("working_hours", UNSET)

        working_hours_frequency = d.pop("working_hours_frequency", UNSET)

        social_security_number = d.pop("social_security_number", UNSET)

        manager_id = d.pop("manager_id", UNSET)

        tax_id = d.pop("tax_id", UNSET)

        legal_entity_id = d.pop("legal_entity_id", UNSET)

        workplace_id = d.pop("workplace_id", UNSET)

        employee_updates_new_hire = cls(
            id=id,
            status=status,
            employee_id=employee_id,
            first_name=first_name,
            last_name=last_name,
            address=address,
            birth_name=birth_name,
            identifier=identifier,
            identifier_type=identifier_type,
            payroll_identifier=payroll_identifier,
            work_email=work_email,
            phone_number=phone_number,
            gender=gender,
            job_title=job_title,
            city=city,
            country=country,
            state=state,
            postal_code=postal_code,
            date_of_birth=date_of_birth,
            nationality=nationality,
            start_date=start_date,
            contract_effective_date=contract_effective_date,
            contract_end_date=contract_end_date,
            bank_account=bank_account,
            salary_amount_in_cents=salary_amount_in_cents,
            salary_frequency=salary_frequency,
            working_hours=working_hours,
            working_hours_frequency=working_hours_frequency,
            social_security_number=social_security_number,
            manager_id=manager_id,
            tax_id=tax_id,
            legal_entity_id=legal_entity_id,
            workplace_id=workplace_id,
        )

        employee_updates_new_hire.additional_properties = d
        return employee_updates_new_hire

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
