from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.put_api_20261001_resources_timeoff_allowances_id_body_tenure_periods_item_balance_type import (
    PutApi20261001ResourcesTimeoffAllowancesIdBodyTenurePeriodsItemBalanceType,
)
from ..models.put_api_20261001_resources_timeoff_allowances_id_body_tenure_periods_item_period_type import (
    PutApi20261001ResourcesTimeoffAllowancesIdBodyTenurePeriodsItemPeriodType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PutApi20261001ResourcesTimeoffAllowancesIdBodyTenurePeriodsItem")


@_attrs_define
class PutApi20261001ResourcesTimeoffAllowancesIdBodyTenurePeriodsItem:
    id: str | Unset = UNSET
    adjustment_in_cents: int | Unset = UNSET
    balance_type: (
        PutApi20261001ResourcesTimeoffAllowancesIdBodyTenurePeriodsItemBalanceType | Unset
    ) = UNSET
    max_cap_in_cents: int | Unset = UNSET
    period_length: int | Unset = UNSET
    period_type: (
        PutApi20261001ResourcesTimeoffAllowancesIdBodyTenurePeriodsItemPeriodType | Unset
    ) = UNSET
    temp_id: str | Unset = UNSET
    time_worked_based_hours_accrued_in_cents: int | Unset = UNSET
    time_worked_based_per_hours_worked_in_cents: int | Unset = UNSET
    field_destroy: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        adjustment_in_cents = self.adjustment_in_cents

        balance_type: str | Unset = UNSET
        if not isinstance(self.balance_type, Unset):
            balance_type = self.balance_type.value if self.balance_type is not None else None

        max_cap_in_cents = self.max_cap_in_cents

        period_length = self.period_length

        period_type: str | Unset = UNSET
        if not isinstance(self.period_type, Unset):
            period_type = self.period_type.value if self.period_type is not None else None

        temp_id = self.temp_id

        time_worked_based_hours_accrued_in_cents = self.time_worked_based_hours_accrued_in_cents

        time_worked_based_per_hours_worked_in_cents = (
            self.time_worked_based_per_hours_worked_in_cents
        )

        field_destroy = self.field_destroy

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if adjustment_in_cents is not UNSET:
            field_dict["adjustment_in_cents"] = adjustment_in_cents
        if balance_type is not UNSET:
            field_dict["balance_type"] = balance_type
        if max_cap_in_cents is not UNSET:
            field_dict["max_cap_in_cents"] = max_cap_in_cents
        if period_length is not UNSET:
            field_dict["period_length"] = period_length
        if period_type is not UNSET:
            field_dict["period_type"] = period_type
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
        if field_destroy is not UNSET:
            field_dict["_destroy"] = field_destroy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        adjustment_in_cents = d.pop("adjustment_in_cents", UNSET)

        _balance_type = d.pop("balance_type", UNSET)
        balance_type: (
            PutApi20261001ResourcesTimeoffAllowancesIdBodyTenurePeriodsItemBalanceType | Unset
        )
        if isinstance(_balance_type, Unset):
            balance_type = UNSET
        else:
            balance_type = (
                PutApi20261001ResourcesTimeoffAllowancesIdBodyTenurePeriodsItemBalanceType(
                    _balance_type
                ) if _balance_type is not None else None
            )

        max_cap_in_cents = d.pop("max_cap_in_cents", UNSET)

        period_length = d.pop("period_length", UNSET)

        _period_type = d.pop("period_type", UNSET)
        period_type: (
            PutApi20261001ResourcesTimeoffAllowancesIdBodyTenurePeriodsItemPeriodType | Unset
        )
        if isinstance(_period_type, Unset):
            period_type = UNSET
        else:
            period_type = PutApi20261001ResourcesTimeoffAllowancesIdBodyTenurePeriodsItemPeriodType(
                _period_type
            ) if _period_type is not None else None

        temp_id = d.pop("temp_id", UNSET)

        time_worked_based_hours_accrued_in_cents = d.pop(
            "time_worked_based_hours_accrued_in_cents", UNSET
        )

        time_worked_based_per_hours_worked_in_cents = d.pop(
            "time_worked_based_per_hours_worked_in_cents", UNSET
        )

        field_destroy = d.pop("_destroy", UNSET)

        put_api_20261001_resources_timeoff_allowances_id_body_tenure_periods_item = cls(
            id=id,
            adjustment_in_cents=adjustment_in_cents,
            balance_type=balance_type,
            max_cap_in_cents=max_cap_in_cents,
            period_length=period_length,
            period_type=period_type,
            temp_id=temp_id,
            time_worked_based_hours_accrued_in_cents=time_worked_based_hours_accrued_in_cents,
            time_worked_based_per_hours_worked_in_cents=time_worked_based_per_hours_worked_in_cents,
            field_destroy=field_destroy,
        )

        put_api_20261001_resources_timeoff_allowances_id_body_tenure_periods_item.additional_properties = d
        return put_api_20261001_resources_timeoff_allowances_id_body_tenure_periods_item

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
