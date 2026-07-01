from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_api_20260701_resources_payroll_employees_identifiers_body_country import (
    PostApi20260701ResourcesPayrollEmployeesIdentifiersBodyCountry,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20260701ResourcesPayrollEmployeesIdentifiersBody")


@_attrs_define
class PostApi20260701ResourcesPayrollEmployeesIdentifiersBody:
    employee_id: str
    """ identifier of the employee """
    country: PostApi20260701ResourcesPayrollEmployeesIdentifiersBodyCountry
    """ country code of the employee pt | it | de """
    social_security_number: str | Unset = UNSET
    """ social security number of the employee """
    tax_id: str | Unset = UNSET
    """ tax id of the employee """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        employee_id = self.employee_id

        country = self.country.value

        social_security_number = self.social_security_number

        tax_id = self.tax_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "employee_id": employee_id,
                "country": country,
            }
        )
        if social_security_number is not UNSET:
            field_dict["social_security_number"] = social_security_number
        if tax_id is not UNSET:
            field_dict["tax_id"] = tax_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        employee_id = d.pop("employee_id")

        country = PostApi20260701ResourcesPayrollEmployeesIdentifiersBodyCountry(d.pop("country"))

        social_security_number = d.pop("social_security_number", UNSET)

        tax_id = d.pop("tax_id", UNSET)

        post_api_20260701_resources_payroll_employees_identifiers_body = cls(
            employee_id=employee_id,
            country=country,
            social_security_number=social_security_number,
            tax_id=tax_id,
        )

        post_api_20260701_resources_payroll_employees_identifiers_body.additional_properties = d
        return post_api_20260701_resources_payroll_employees_identifiers_body

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
