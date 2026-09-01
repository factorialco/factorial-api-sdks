from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.timeoff_allowance_tenure_periods_item_balance_type import (
    TimeoffAllowanceTenurePeriodsItemBalanceType,
)
from ..models.timeoff_allowance_tenure_periods_item_period_type import (
    TimeoffAllowanceTenurePeriodsItemPeriodType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="TimeoffAllowanceTenurePeriodsItem")


@_attrs_define
class TimeoffAllowanceTenurePeriodsItem:
    id: str
    period_type: TimeoffAllowanceTenurePeriodsItemPeriodType
    balance_type: TimeoffAllowanceTenurePeriodsItemBalanceType
    period_length: int | Unset = UNSET
    adjustment_in_cents: int | Unset = UNSET
    time_worked_based_hours_accrued_in_cents: int | Unset = UNSET
    time_worked_based_per_hours_worked_in_cents: int | Unset = UNSET
    max_cap_in_cents: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        period_type = self.period_type.value

        balance_type = self.balance_type.value

        period_length = self.period_length

        adjustment_in_cents = self.adjustment_in_cents

        time_worked_based_hours_accrued_in_cents = self.time_worked_based_hours_accrued_in_cents

        time_worked_based_per_hours_worked_in_cents = (
            self.time_worked_based_per_hours_worked_in_cents
        )

        max_cap_in_cents = self.max_cap_in_cents

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "period_type": period_type,
                "balance_type": balance_type,
            }
        )
        if period_length is not UNSET:
            field_dict["period_length"] = period_length
        if adjustment_in_cents is not UNSET:
            field_dict["adjustment_in_cents"] = adjustment_in_cents
        if time_worked_based_hours_accrued_in_cents is not UNSET:
            field_dict["time_worked_based_hours_accrued_in_cents"] = (
                time_worked_based_hours_accrued_in_cents
            )
        if time_worked_based_per_hours_worked_in_cents is not UNSET:
            field_dict["time_worked_based_per_hours_worked_in_cents"] = (
                time_worked_based_per_hours_worked_in_cents
            )
        if max_cap_in_cents is not UNSET:
            field_dict["max_cap_in_cents"] = max_cap_in_cents

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        period_type = TimeoffAllowanceTenurePeriodsItemPeriodType(d.pop("period_type"))

        balance_type = TimeoffAllowanceTenurePeriodsItemBalanceType(d.pop("balance_type"))

        period_length = d.pop("period_length", UNSET)

        adjustment_in_cents = d.pop("adjustment_in_cents", UNSET)

        time_worked_based_hours_accrued_in_cents = d.pop(
            "time_worked_based_hours_accrued_in_cents", UNSET
        )

        time_worked_based_per_hours_worked_in_cents = d.pop(
            "time_worked_based_per_hours_worked_in_cents", UNSET
        )

        max_cap_in_cents = d.pop("max_cap_in_cents", UNSET)

        timeoff_allowance_tenure_periods_item = cls(
            id=id,
            period_type=period_type,
            balance_type=balance_type,
            period_length=period_length,
            adjustment_in_cents=adjustment_in_cents,
            time_worked_based_hours_accrued_in_cents=time_worked_based_hours_accrued_in_cents,
            time_worked_based_per_hours_worked_in_cents=time_worked_based_per_hours_worked_in_cents,
            max_cap_in_cents=max_cap_in_cents,
        )

        timeoff_allowance_tenure_periods_item.additional_properties = d
        return timeoff_allowance_tenure_periods_item

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
