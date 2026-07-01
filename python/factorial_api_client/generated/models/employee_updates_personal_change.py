from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EmployeeUpdatesPersonalChange")


@_attrs_define
class EmployeeUpdatesPersonalChange:
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
    work_email: str | Unset = UNSET
    """ personal email of the employee. """
    phone_number: str | Unset = UNSET
    """ phone number of the employee. """
    identifier_type: str | Unset = UNSET
    """ type of identifier (ex passport). """
    identifier: str | Unset = UNSET
    """ national identifier number. """
    social_security_number: str | Unset = UNSET
    """ social security number of the employee. """
    tax_id: str | Unset = UNSET
    gender: str | Unset = UNSET
    """ gender of the employee (male | female). """
    date_of_birth: str | Unset = UNSET
    """ birthday of the employee. """
    nationality: str | Unset = UNSET
    """ nationality country code of the employee (Spain ES, United Kingdom GB). """
    address_line_1: str | Unset = UNSET
    """ address line 1 of the employee. """
    address_line_2: str | Unset = UNSET
    """ address line 1 of the employee. """
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
    job_title: str | Unset = UNSET
    """ job title of the employee. """
    workplace_id: str | Unset = UNSET
    """ workplace id of the employee. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        status = self.status

        employee_id = self.employee_id

        first_name = self.first_name

        last_name = self.last_name

        work_email = self.work_email

        phone_number = self.phone_number

        identifier_type = self.identifier_type

        identifier = self.identifier

        social_security_number = self.social_security_number

        tax_id = self.tax_id

        gender = self.gender

        date_of_birth = self.date_of_birth

        nationality = self.nationality

        address_line_1 = self.address_line_1

        address_line_2 = self.address_line_2

        postal_code = self.postal_code

        city = self.city

        state = self.state

        country = self.country

        bank_number = self.bank_number

        job_title = self.job_title

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
            }
        )
        if work_email is not UNSET:
            field_dict["work_email"] = work_email
        if phone_number is not UNSET:
            field_dict["phone_number"] = phone_number
        if identifier_type is not UNSET:
            field_dict["identifier_type"] = identifier_type
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if social_security_number is not UNSET:
            field_dict["social_security_number"] = social_security_number
        if tax_id is not UNSET:
            field_dict["tax_id"] = tax_id
        if gender is not UNSET:
            field_dict["gender"] = gender
        if date_of_birth is not UNSET:
            field_dict["date_of_birth"] = date_of_birth
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
        if job_title is not UNSET:
            field_dict["job_title"] = job_title
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

        work_email = d.pop("work_email", UNSET)

        phone_number = d.pop("phone_number", UNSET)

        identifier_type = d.pop("identifier_type", UNSET)

        identifier = d.pop("identifier", UNSET)

        social_security_number = d.pop("social_security_number", UNSET)

        tax_id = d.pop("tax_id", UNSET)

        gender = d.pop("gender", UNSET)

        date_of_birth = d.pop("date_of_birth", UNSET)

        nationality = d.pop("nationality", UNSET)

        address_line_1 = d.pop("address_line_1", UNSET)

        address_line_2 = d.pop("address_line_2", UNSET)

        postal_code = d.pop("postal_code", UNSET)

        city = d.pop("city", UNSET)

        state = d.pop("state", UNSET)

        country = d.pop("country", UNSET)

        bank_number = d.pop("bank_number", UNSET)

        job_title = d.pop("job_title", UNSET)

        workplace_id = d.pop("workplace_id", UNSET)

        employee_updates_personal_change = cls(
            id=id,
            status=status,
            employee_id=employee_id,
            first_name=first_name,
            last_name=last_name,
            work_email=work_email,
            phone_number=phone_number,
            identifier_type=identifier_type,
            identifier=identifier,
            social_security_number=social_security_number,
            tax_id=tax_id,
            gender=gender,
            date_of_birth=date_of_birth,
            nationality=nationality,
            address_line_1=address_line_1,
            address_line_2=address_line_2,
            postal_code=postal_code,
            city=city,
            state=state,
            country=country,
            bank_number=bank_number,
            job_title=job_title,
            workplace_id=workplace_id,
        )

        employee_updates_personal_change.additional_properties = d
        return employee_updates_personal_change

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
