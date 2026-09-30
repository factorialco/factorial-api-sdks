from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.contracts_contract_activity_period_type import ContractsContractActivityPeriodType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ContractsContractActivityPeriod")


@_attrs_define
class ContractsContractActivityPeriod:
    id: str
    """ Identifier of the period, built from the contract id and the period start date. Periods are derived rather
    than stored, so this id is stable only while the underlying contract versions do not change. """
    contract_id: str
    """ ID of the contract this period belongs to. """
    employee_id: str
    """ ID of the employee who holds the contract. """
    type_: ContractsContractActivityPeriodType
    """ Whether the employee is working during this period (activity) or not (inactivity). Only discontinuous
    contracts produce inactivity periods. """
    activity_period_starts_on: str
    """ First day of the period. """
    activity_period_ends_on: str | Unset = UNSET
    """ Last day of the period, or null when the period is still open ended. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        contract_id = self.contract_id

        employee_id = self.employee_id

        type_ = self.type_.value

        activity_period_starts_on = self.activity_period_starts_on

        activity_period_ends_on = self.activity_period_ends_on

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "contract_id": contract_id,
                "employee_id": employee_id,
                "type": type_,
                "activity_period_starts_on": activity_period_starts_on,
            }
        )
        if activity_period_ends_on is not UNSET:
            field_dict["activity_period_ends_on"] = activity_period_ends_on

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        contract_id = d.pop("contract_id")

        employee_id = d.pop("employee_id")

        type_ = ContractsContractActivityPeriodType(d.pop("type"))

        activity_period_starts_on = d.pop("activity_period_starts_on")

        activity_period_ends_on = d.pop("activity_period_ends_on", UNSET)

        contracts_contract_activity_period = cls(
            id=id,
            contract_id=contract_id,
            employee_id=employee_id,
            type_=type_,
            activity_period_starts_on=activity_period_starts_on,
            activity_period_ends_on=activity_period_ends_on,
        )

        contracts_contract_activity_period.additional_properties = d
        return contracts_contract_activity_period

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
