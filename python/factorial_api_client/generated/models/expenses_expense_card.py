from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExpensesExpenseCard")


@_attrs_define
class ExpensesExpenseCard:
    """The card of the expense"""

    card_type: str
    last4: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        card_type = self.card_type

        last4 = self.last4

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "card_type": card_type,
            }
        )
        if last4 is not UNSET:
            field_dict["last4"] = last4

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        card_type = d.pop("card_type")

        last4 = d.pop("last4", UNSET)

        expenses_expense_card = cls(
            card_type=card_type,
            last4=last4,
        )

        expenses_expense_card.additional_properties = d
        return expenses_expense_card

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
