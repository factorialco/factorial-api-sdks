from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.compensations_payroll_result_amount_strategy_type import (
    CompensationsPayrollResultAmountStrategyType,
)
from ..models.compensations_payroll_result_source_type import CompensationsPayrollResultSourceType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CompensationsPayrollResult")


@_attrs_define
class CompensationsPayrollResult:
    id: str
    """ Payroll result id """
    payroll_run_id: str
    """ Parent payroll run id """
    payroll_run_employee_id: str
    """ Employee id (participant of the payroll run) """
    payroll_concept_id: str
    """ Payroll concept id """
    amount_strategy_type: CompensationsPayrollResultAmountStrategyType
    """ Amount strategy discriminator """
    amount_is_overwritten: bool
    """ Whether the amount is a manual override """
    source_type: CompensationsPayrollResultSourceType
    """ Source type discriminator (always present for payroll_result) """
    source_id: str
    """ Source id (always present for payroll_result) """
    created_at: str
    """ Timestamp when the payroll_result row was created """
    updated_at: str
    """ Timestamp when the payroll_result row was last updated """
    amount: int | Unset = UNSET
    """ Effective compensation value — the manual override when `amount_is_overwritten` is true, otherwise the
    strategy-computed value """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        payroll_run_id = self.payroll_run_id

        payroll_run_employee_id = self.payroll_run_employee_id

        payroll_concept_id = self.payroll_concept_id

        amount_strategy_type = self.amount_strategy_type.value

        amount_is_overwritten = self.amount_is_overwritten

        source_type = self.source_type.value

        source_id = self.source_id

        created_at = self.created_at

        updated_at = self.updated_at

        amount = self.amount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "payroll_run_id": payroll_run_id,
                "payroll_run_employee_id": payroll_run_employee_id,
                "payroll_concept_id": payroll_concept_id,
                "amount_strategy_type": amount_strategy_type,
                "amount_is_overwritten": amount_is_overwritten,
                "source_type": source_type,
                "source_id": source_id,
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

        payroll_run_id = d.pop("payroll_run_id")

        payroll_run_employee_id = d.pop("payroll_run_employee_id")

        payroll_concept_id = d.pop("payroll_concept_id")

        amount_strategy_type = CompensationsPayrollResultAmountStrategyType(
            d.pop("amount_strategy_type")
        )

        amount_is_overwritten = d.pop("amount_is_overwritten")

        source_type = CompensationsPayrollResultSourceType(d.pop("source_type"))

        source_id = d.pop("source_id")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        amount = d.pop("amount", UNSET)

        compensations_payroll_result = cls(
            id=id,
            payroll_run_id=payroll_run_id,
            payroll_run_employee_id=payroll_run_employee_id,
            payroll_concept_id=payroll_concept_id,
            amount_strategy_type=amount_strategy_type,
            amount_is_overwritten=amount_is_overwritten,
            source_type=source_type,
            source_id=source_id,
            created_at=created_at,
            updated_at=updated_at,
            amount=amount,
        )

        compensations_payroll_result.additional_properties = d
        return compensations_payroll_result

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
