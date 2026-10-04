from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.compensations_payroll_run_employees_compensation_amount_strategy_type import (
    CompensationsPayrollRunEmployeesCompensationAmountStrategyType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CompensationsPayrollRunEmployeesCompensation")


@_attrs_define
class CompensationsPayrollRunEmployeesCompensation:
    id: str
    """ Payroll run employee compensation id """
    payroll_run_employee_id: str
    """ Employee id (participant of the payroll run) """
    payroll_concept_id: str
    """ Payroll concept id """
    payroll_run_id: str
    """ Parent payroll run id """
    result_type: str
    """ Record projection type — `compensation` (input) or `payroll_result` (computed) """
    amount_strategy_type: CompensationsPayrollRunEmployeesCompensationAmountStrategyType
    """ Amount strategy discriminator """
    created_at: str
    """ When the record was created """
    updated_at: str
    """ When the record was last updated """
    amount: int | Unset = UNSET
    """ Aggregated compensation value for this concept and employee within the payroll run, in minor units. For
    `payroll_result` records, this is the value the bookkeeper computed for that concept (e.g. net pay). """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        payroll_run_employee_id = self.payroll_run_employee_id

        payroll_concept_id = self.payroll_concept_id

        payroll_run_id = self.payroll_run_id

        result_type = self.result_type

        amount_strategy_type = self.amount_strategy_type.value

        created_at = self.created_at

        updated_at = self.updated_at

        amount = self.amount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "payroll_run_employee_id": payroll_run_employee_id,
                "payroll_concept_id": payroll_concept_id,
                "payroll_run_id": payroll_run_id,
                "result_type": result_type,
                "amount_strategy_type": amount_strategy_type,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if amount is not UNSET:
            field_dict["amount"] = amount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        payroll_run_employee_id = d.pop("payroll_run_employee_id")

        payroll_concept_id = d.pop("payroll_concept_id")

        payroll_run_id = d.pop("payroll_run_id")

        result_type = d.pop("result_type")

        amount_strategy_type = CompensationsPayrollRunEmployeesCompensationAmountStrategyType(
            d.pop("amount_strategy_type")
        )

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        amount = d.pop("amount", UNSET)

        compensations_payroll_run_employees_compensation = cls(
            id=id,
            payroll_run_employee_id=payroll_run_employee_id,
            payroll_concept_id=payroll_concept_id,
            payroll_run_id=payroll_run_id,
            result_type=result_type,
            amount_strategy_type=amount_strategy_type,
            created_at=created_at,
            updated_at=updated_at,
            amount=amount,
        )

        compensations_payroll_run_employees_compensation.additional_properties = d
        return compensations_payroll_run_employees_compensation

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
