from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_api_20261001_resources_timeoff_allowances_body_tenure_periods_item_balance_type import (
    PostApi20261001ResourcesTimeoffAllowancesBodyTenurePeriodsItemBalanceType,
)
from ..models.post_api_20261001_resources_timeoff_allowances_body_tenure_periods_item_period_type import (
    PostApi20261001ResourcesTimeoffAllowancesBodyTenurePeriodsItemPeriodType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20261001ResourcesTimeoffAllowancesBodyTenurePeriodsItem")


@_attrs_define
class PostApi20261001ResourcesTimeoffAllowancesBodyTenurePeriodsItem:
    balance_type: PostApi20261001ResourcesTimeoffAllowancesBodyTenurePeriodsItemBalanceType
    period_length: int
    period_type: PostApi20261001ResourcesTimeoffAllowancesBodyTenurePeriodsItemPeriodType
    adjustment_in_cents: int | Unset = UNSET
    max_cap_in_cents: int | Unset = UNSET
    temp_id: str | Unset = UNSET
    time_worked_based_hours_accrued_in_cents: int | Unset = UNSET
    time_worked_based_per_hours_worked_in_cents: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        balance_type = self.balance_type.value

        period_length = self.period_length

        period_type = self.period_type.value

        adjustment_in_cents = self.adjustment_in_cents

        max_cap_in_cents = self.max_cap_in_cents

        temp_id = self.temp_id

        time_worked_based_hours_accrued_in_cents = self.time_worked_based_hours_accrued_in_cents

        time_worked_based_per_hours_worked_in_cents = (
            self.time_worked_based_per_hours_worked_in_cents
        )

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "balance_type": balance_type,
                "period_length": period_length,
                "period_type": period_type,
            }
        )
        if adjustment_in_cents is not UNSET:
            field_dict["adjustment_in_cents"] = adjustment_in_cents
        if max_cap_in_cents is not UNSET:
            field_dict["max_cap_in_cents"] = max_cap_in_cents
        if temp_id is not UNSET:
            field_dict["temp_id"] = temp_id
        if time_worked_based_hours_accrued_in_cents is not UNSET:
            field_dict["time_worked_based_hours_accrued_in_cents"] = (
                time_worked_based_hours_accrued_in_cents
            )
        if time_worked_based_per_hours_worked_in_cents is not UNSET:
            field_dict["time_worked_based_per_hours_worked_in_cents"] = (
                time_worked_based_per_hours_worked_in_cents
            )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        balance_type = PostApi20261001ResourcesTimeoffAllowancesBodyTenurePeriodsItemBalanceType(
            d.pop("balance_type")
        )

        period_length = d.pop("period_length")

        period_type = PostApi20261001ResourcesTimeoffAllowancesBodyTenurePeriodsItemPeriodType(
            d.pop("period_type")
        )

        adjustment_in_cents = d.pop("adjustment_in_cents", UNSET)

        max_cap_in_cents = d.pop("max_cap_in_cents", UNSET)

        temp_id = d.pop("temp_id", UNSET)

        time_worked_based_hours_accrued_in_cents = d.pop(
            "time_worked_based_hours_accrued_in_cents", UNSET
        )

        time_worked_based_per_hours_worked_in_cents = d.pop(
            "time_worked_based_per_hours_worked_in_cents", UNSET
        )

        post_api_20261001_resources_timeoff_allowances_body_tenure_periods_item = cls(
            balance_type=balance_type,
            period_length=period_length,
            period_type=period_type,
            adjustment_in_cents=adjustment_in_cents,
            max_cap_in_cents=max_cap_in_cents,
            temp_id=temp_id,
            time_worked_based_hours_accrued_in_cents=time_worked_based_hours_accrued_in_cents,
            time_worked_based_per_hours_worked_in_cents=time_worked_based_per_hours_worked_in_cents,
        )

        post_api_20261001_resources_timeoff_allowances_body_tenure_periods_item.additional_properties = d
        return post_api_20261001_resources_timeoff_allowances_body_tenure_periods_item

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
