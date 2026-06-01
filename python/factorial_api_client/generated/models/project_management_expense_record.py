from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectManagementExpenseRecord")


@_attrs_define
class ProjectManagementExpenseRecord:
    id: int
    project_worker_id: int
    expense_id: int
    subproject_id: int | Unset = UNSET
    original_amount_currency: str | Unset = UNSET
    original_amount_cents: int | Unset = UNSET
    legal_entity_amount_currency: str | Unset = UNSET
    legal_entity_amount_cents: str | Unset = UNSET
    effective_on: str | Unset = UNSET
    exchange_rate: float | Unset = UNSET
    status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        project_worker_id = self.project_worker_id

        expense_id = self.expense_id

        subproject_id = self.subproject_id

        original_amount_currency = self.original_amount_currency

        original_amount_cents = self.original_amount_cents

        legal_entity_amount_currency = self.legal_entity_amount_currency

        legal_entity_amount_cents = self.legal_entity_amount_cents

        effective_on = self.effective_on

        exchange_rate = self.exchange_rate

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "project_worker_id": project_worker_id,
                "expense_id": expense_id,
            }
        )
        if subproject_id is not UNSET:
            field_dict["subproject_id"] = subproject_id
        if original_amount_currency is not UNSET:
            field_dict["original_amount_currency"] = original_amount_currency
        if original_amount_cents is not UNSET:
            field_dict["original_amount_cents"] = original_amount_cents
        if legal_entity_amount_currency is not UNSET:
            field_dict["legal_entity_amount_currency"] = legal_entity_amount_currency
        if legal_entity_amount_cents is not UNSET:
            field_dict["legal_entity_amount_cents"] = legal_entity_amount_cents
        if effective_on is not UNSET:
            field_dict["effective_on"] = effective_on
        if exchange_rate is not UNSET:
            field_dict["exchange_rate"] = exchange_rate
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        project_worker_id = d.pop("project_worker_id")

        expense_id = d.pop("expense_id")

        subproject_id = d.pop("subproject_id", UNSET)

        original_amount_currency = d.pop("original_amount_currency", UNSET)

        original_amount_cents = d.pop("original_amount_cents", UNSET)

        legal_entity_amount_currency = d.pop("legal_entity_amount_currency", UNSET)

        legal_entity_amount_cents = d.pop("legal_entity_amount_cents", UNSET)

        effective_on = d.pop("effective_on", UNSET)

        exchange_rate = d.pop("exchange_rate", UNSET)

        status = d.pop("status", UNSET)

        project_management_expense_record = cls(
            id=id,
            project_worker_id=project_worker_id,
            expense_id=expense_id,
            subproject_id=subproject_id,
            original_amount_currency=original_amount_currency,
            original_amount_cents=original_amount_cents,
            legal_entity_amount_currency=legal_entity_amount_currency,
            legal_entity_amount_cents=legal_entity_amount_cents,
            effective_on=effective_on,
            exchange_rate=exchange_rate,
            status=status,
        )

        project_management_expense_record.additional_properties = d
        return project_management_expense_record

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
