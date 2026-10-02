from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.expenses_expense_taxes_item_type import ExpensesExpenseTaxesItemType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExpensesExpenseTaxesItem")


@_attrs_define
class ExpensesExpenseTaxesItem:
    type_: ExpensesExpenseTaxesItemType
    amount: int | Unset = UNSET
    percentage: float | Unset = UNSET
    base_amount: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        amount = self.amount

        percentage = self.percentage

        base_amount = self.base_amount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if amount is not UNSET:
            field_dict["amount"] = amount
        if percentage is not UNSET:
            field_dict["percentage"] = percentage
        if base_amount is not UNSET:
            field_dict["base_amount"] = base_amount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = ExpensesExpenseTaxesItemType(d.pop("type"))

        amount = d.pop("amount", UNSET)

        percentage = d.pop("percentage", UNSET)

        base_amount = d.pop("base_amount", UNSET)

        expenses_expense_taxes_item = cls(
            type_=type_,
            amount=amount,
            percentage=percentage,
            base_amount=base_amount,
        )

        expenses_expense_taxes_item.additional_properties = d
        return expenses_expense_taxes_item

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
