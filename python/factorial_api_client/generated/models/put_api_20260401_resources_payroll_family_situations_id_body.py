from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.put_api_20260401_resources_payroll_family_situations_id_body_civil_status import (
    PutApi20260401ResourcesPayrollFamilySituationsIdBodyCivilStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PutApi20260401ResourcesPayrollFamilySituationsIdBody")


@_attrs_define
class PutApi20260401ResourcesPayrollFamilySituationsIdBody:
    id: int
    """ Family situation id. """
    employee_id: int
    """ Employee id. """
    civil_status: PutApi20260401ResourcesPayrollFamilySituationsIdBodyCivilStatus | Unset = UNSET
    """ Civil status of the employee. """
    number_of_dependants: int | Unset = UNSET
    """ Number of dependants of the employee. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        employee_id = self.employee_id

        civil_status: str | Unset = UNSET
        if not isinstance(self.civil_status, Unset):
            civil_status = self.civil_status.value

        number_of_dependants = self.number_of_dependants

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "employee_id": employee_id,
            }
        )
        if civil_status is not UNSET:
            field_dict["civil_status"] = civil_status
        if number_of_dependants is not UNSET:
            field_dict["number_of_dependants"] = number_of_dependants

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        employee_id = d.pop("employee_id")

        _civil_status = d.pop("civil_status", UNSET)
        civil_status: PutApi20260401ResourcesPayrollFamilySituationsIdBodyCivilStatus | Unset
        if isinstance(_civil_status, Unset):
            civil_status = UNSET
        else:
            civil_status = PutApi20260401ResourcesPayrollFamilySituationsIdBodyCivilStatus(
                _civil_status
            )

        number_of_dependants = d.pop("number_of_dependants", UNSET)

        put_api_20260401_resources_payroll_family_situations_id_body = cls(
            id=id,
            employee_id=employee_id,
            civil_status=civil_status,
            number_of_dependants=number_of_dependants,
        )

        put_api_20260401_resources_payroll_family_situations_id_body.additional_properties = d
        return put_api_20260401_resources_payroll_family_situations_id_body

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
