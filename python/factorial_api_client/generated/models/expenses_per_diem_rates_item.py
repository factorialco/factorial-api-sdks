from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExpensesPerDiemRatesItem")


@_attrs_define
class ExpensesPerDiemRatesItem:
    expenses_per_diem_id: str
    rate_configuration_id: str
    id: str | Unset = UNSET
    total_days: int | Unset = UNSET
    total_amount_cents: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        expenses_per_diem_id = self.expenses_per_diem_id

        rate_configuration_id = self.rate_configuration_id

        id = self.id

        total_days = self.total_days

        total_amount_cents = self.total_amount_cents

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "expenses_per_diem_id": expenses_per_diem_id,
                "rate_configuration_id": rate_configuration_id,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if total_days is not UNSET:
            field_dict["total_days"] = total_days
        if total_amount_cents is not UNSET:
            field_dict["total_amount_cents"] = total_amount_cents

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        expenses_per_diem_id = d.pop("expenses_per_diem_id")

        rate_configuration_id = d.pop("rate_configuration_id")

        id = d.pop("id", UNSET)

        total_days = d.pop("total_days", UNSET)

        total_amount_cents = d.pop("total_amount_cents", UNSET)

        expenses_per_diem_rates_item = cls(
            expenses_per_diem_id=expenses_per_diem_id,
            rate_configuration_id=rate_configuration_id,
            id=id,
            total_days=total_days,
            total_amount_cents=total_amount_cents,
        )

        expenses_per_diem_rates_item.additional_properties = d
        return expenses_per_diem_rates_item

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
