from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.contracts_contract_schedule import ContractsContractSchedule
from ..types import UNSET, Unset

T = TypeVar("T", bound="ContractsContract")


@_attrs_define
class ContractsContract:
    id: str
    """ contract identifier """
    employee_id: str
    """ employee identifier """
    country: str
    """ ISO country code the contract is governed by """
    company_id: str
    """ ID of the company that owns the contract """
    legal_entity_id: str
    """ ID of the legal entity the employee is contracted under """
    starts_on: str
    """ contract start date """
    is_discontinuous: bool
    """ Whether this is a discontinuous (intermittent) contract """
    schedule: ContractsContractSchedule
    """ Whether the contract is already over, currently in force, or has not started yet """
    ends_on: str | Unset = UNSET
    """ contract end date """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        employee_id = self.employee_id

        country = self.country

        company_id = self.company_id

        legal_entity_id = self.legal_entity_id

        starts_on = self.starts_on

        is_discontinuous = self.is_discontinuous

        schedule = self.schedule.value

        ends_on = self.ends_on

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "employee_id": employee_id,
                "country": country,
                "company_id": company_id,
                "legal_entity_id": legal_entity_id,
                "starts_on": starts_on,
                "is_discontinuous": is_discontinuous,
                "schedule": schedule,
            }
        )
        if ends_on is not UNSET:
            field_dict["ends_on"] = ends_on

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        employee_id = d.pop("employee_id")

        country = d.pop("country")

        company_id = d.pop("company_id")

        legal_entity_id = d.pop("legal_entity_id")

        starts_on = d.pop("starts_on")

        is_discontinuous = d.pop("is_discontinuous")

        schedule = ContractsContractSchedule(d.pop("schedule"))

        ends_on = d.pop("ends_on", UNSET)

        contracts_contract = cls(
            id=id,
            employee_id=employee_id,
            country=country,
            company_id=company_id,
            legal_entity_id=legal_entity_id,
            starts_on=starts_on,
            is_discontinuous=is_discontinuous,
            schedule=schedule,
            ends_on=ends_on,
        )

        contracts_contract.additional_properties = d
        return contracts_contract

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
