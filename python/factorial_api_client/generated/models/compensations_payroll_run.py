from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.compensations_payroll_run_payment_type import CompensationsPayrollRunPaymentType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CompensationsPayrollRun")


@_attrs_define
class CompensationsPayrollRun:
    id: str
    """ Payroll run id """
    label: str
    """ Localized label for the run (month and year) """
    starts_on: str
    """ Start date of the run period """
    ends_on: str
    """ End date of the run period """
    status: str
    """ Run status (open, in_review, completed, etc.) """
    locked: bool
    """ Whether the run is locked """
    company_id: str
    """ Owning company id """
    locked_at: str | Unset = UNSET
    """ When the run was locked, if it is locked """
    cycle_id: str | Unset = UNSET
    """ Parent cycle id (nil for off-cycle runs) """
    payment_type: CompensationsPayrollRunPaymentType | Unset = UNSET
    """ Payment type (regular / extra_pay) """
    closure_date: str | Unset = UNSET
    """ Effective closure date (override if present, otherwise computed closure_date) """
    alerts_date: str | Unset = UNSET
    """ Date when alerts are dispatched """
    created_at: str | Unset = UNSET
    """ Timestamp when the run record was created """
    updated_at: str | Unset = UNSET
    """ Timestamp when the run record was last updated """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        label = self.label

        starts_on = self.starts_on

        ends_on = self.ends_on

        status = self.status

        locked = self.locked

        company_id = self.company_id

        locked_at = self.locked_at

        cycle_id = self.cycle_id

        payment_type: str | Unset = UNSET
        if not isinstance(self.payment_type, Unset):
            payment_type = self.payment_type.value if self.payment_type is not None else None

        closure_date = self.closure_date

        alerts_date = self.alerts_date

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "label": label,
                "starts_on": starts_on,
                "ends_on": ends_on,
                "status": status,
                "locked": locked,
                "company_id": company_id,
            }
        )
        if locked_at is not UNSET:
            field_dict["locked_at"] = locked_at
        if cycle_id is not UNSET:
            field_dict["cycle_id"] = cycle_id
        if payment_type is not UNSET:
            field_dict["payment_type"] = payment_type
        if closure_date is not UNSET:
            field_dict["closure_date"] = closure_date
        if alerts_date is not UNSET:
            field_dict["alerts_date"] = alerts_date
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        label = d.pop("label")

        starts_on = d.pop("starts_on")

        ends_on = d.pop("ends_on")

        status = d.pop("status")

        locked = d.pop("locked")

        company_id = d.pop("company_id")

        locked_at = d.pop("locked_at", UNSET)

        cycle_id = d.pop("cycle_id", UNSET)

        _payment_type = d.pop("payment_type", UNSET)
        payment_type: CompensationsPayrollRunPaymentType | Unset
        if isinstance(_payment_type, Unset):
            payment_type = UNSET
        else:
            payment_type = CompensationsPayrollRunPaymentType(_payment_type) if _payment_type is not None else None

        closure_date = d.pop("closure_date", UNSET)

        alerts_date = d.pop("alerts_date", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        compensations_payroll_run = cls(
            id=id,
            label=label,
            starts_on=starts_on,
            ends_on=ends_on,
            status=status,
            locked=locked,
            company_id=company_id,
            locked_at=locked_at,
            cycle_id=cycle_id,
            payment_type=payment_type,
            closure_date=closure_date,
            alerts_date=alerts_date,
            created_at=created_at,
            updated_at=updated_at,
        )

        compensations_payroll_run.additional_properties = d
        return compensations_payroll_run

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
