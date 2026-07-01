from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.put_api_20260701_resources_timeoff_allowances_id_body_available_days import (
    PutApi20260701ResourcesTimeoffAllowancesIdBodyAvailableDays,
)
from ..models.put_api_20260701_resources_timeoff_allowances_id_body_days_type import (
    PutApi20260701ResourcesTimeoffAllowancesIdBodyDaysType,
)
from ..models.put_api_20260701_resources_timeoff_allowances_id_body_frequency import (
    PutApi20260701ResourcesTimeoffAllowancesIdBodyFrequency,
)
from ..models.put_api_20260701_resources_timeoff_allowances_id_body_negative_counter_type import (
    PutApi20260701ResourcesTimeoffAllowancesIdBodyNegativeCounterType,
)
from ..models.put_api_20260701_resources_timeoff_allowances_id_body_proration_type import (
    PutApi20260701ResourcesTimeoffAllowancesIdBodyProrationType,
)
from ..models.put_api_20260701_resources_timeoff_allowances_id_body_range_type import (
    PutApi20260701ResourcesTimeoffAllowancesIdBodyRangeType,
)
from ..models.put_api_20260701_resources_timeoff_allowances_id_body_rounding import (
    PutApi20260701ResourcesTimeoffAllowancesIdBodyRounding,
)
from ..models.put_api_20260701_resources_timeoff_allowances_id_body_tenure_period_transition import (
    PutApi20260701ResourcesTimeoffAllowancesIdBodyTenurePeriodTransition,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PutApi20260701ResourcesTimeoffAllowancesIdBody")


@_attrs_define
class PutApi20260701ResourcesTimeoffAllowancesIdBody:
    id: str
    accrued_denominator_in_cents: int | Unset = UNSET
    """ Only for Allowances based on worked time. It represents how many units you need to work to be granted
    allowance units """
    accrued_factor_in_cents: int | Unset = UNSET
    """ Only for Allowances based on worked time. It represents how many units you are given per unit of time worked
    """
    available_days: PutApi20260701ResourcesTimeoffAllowancesIdBodyAvailableDays | Unset = UNSET
    """ Indicates how the allowance units are accrued. For example all_days means all allowance days are given on
    the first day of the cycle. """
    carry_over_units_in_cents: int | Unset = UNSET
    """ How many units can carry over between cycles multiplied by 100 """
    count_holiday_as_workable: bool | Unset = UNSET
    """ This setting flags if units taken during a bank holiday should be deducted or not from allowance. """
    days_type: PutApi20260701ResourcesTimeoffAllowancesIdBodyDaysType | Unset = UNSET
    """ Indicates if the allowance is based on working on calendar days. """
    expire_in_months: int | Unset = UNSET
    """ When does the carryover expire in months. """
    frequency: PutApi20260701ResourcesTimeoffAllowancesIdBodyFrequency | Unset = UNSET
    """ Defines duration of the allowance cycles. Can be "yearly", "monthly_flexible" or "lifetime" """
    holiday_allowance_in_cents: int | Unset = UNSET
    """ Base amount of holiday allowance units multiplied by 100 """
    leave_type_ids: list[str] | Unset = UNSET
    """ An array of leave type ids associated with that allowance """
    maximum_amount_in_cents: int | Unset = UNSET
    """ Maximum the allowance can reach on accrued """
    name: str | Unset = UNSET
    """ Allowance name set by the user """
    negative_counter_type: (
        PutApi20260701ResourcesTimeoffAllowancesIdBodyNegativeCounterType | Unset
    ) = UNSET
    """ Whether the allowance allows to request more days than available. """
    position: int | Unset = UNSET
    """ Indicates the position in the allowance when rendering them in UI """
    proration_type: PutApi20260701ResourcesTimeoffAllowancesIdBodyProrationType | Unset = UNSET
    """ Whether the allowance has proration enabled or not. """
    pto_proratio_enabled: bool | Unset = UNSET
    """ Whether the allowance days are prorated or not """
    range_type: PutApi20260701ResourcesTimeoffAllowancesIdBodyRangeType | Unset = UNSET
    """ Configures how leaves duration is handled. """
    rounding: PutApi20260701ResourcesTimeoffAllowancesIdBodyRounding | Unset = UNSET
    """ How the accrued units of the allowance are rounded. It depends if the allowance is set in hours or days. """
    tenure_period_transition: (
        PutApi20260701ResourcesTimeoffAllowancesIdBodyTenurePeriodTransition | Unset
    ) = UNSET
    """ In case the allowance has tenure periods, when is this tenure applied. """
    tenure_periods_enabled: bool | Unset = UNSET
    """ Whether the allowance has tenure periods enabled or not. """
    tenure_periods: list[Any] | Unset = UNSET
    """ The tenure periods associated with the allowance. """
    unlimited_accrued_hours: bool | Unset = UNSET
    """ Flag to indicate if there is unlimited accrual. """
    unlimited_carry_over: bool | Unset = UNSET
    """ Flag to indicate if there is unlimited carry over. """
    unlimited_carry_over_expiration: bool | Unset = UNSET
    """ Boolean to flag if carryover does not expire """
    unlimited_holidays: bool | Unset = UNSET
    """ Flag to indicate that the allowance has unlimited available days """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        accrued_denominator_in_cents = self.accrued_denominator_in_cents

        accrued_factor_in_cents = self.accrued_factor_in_cents

        available_days: str | Unset = UNSET
        if not isinstance(self.available_days, Unset):
            available_days = self.available_days.value

        carry_over_units_in_cents = self.carry_over_units_in_cents

        count_holiday_as_workable = self.count_holiday_as_workable

        days_type: str | Unset = UNSET
        if not isinstance(self.days_type, Unset):
            days_type = self.days_type.value

        expire_in_months = self.expire_in_months

        frequency: str | Unset = UNSET
        if not isinstance(self.frequency, Unset):
            frequency = self.frequency.value

        holiday_allowance_in_cents = self.holiday_allowance_in_cents

        leave_type_ids: list[str] | Unset = UNSET
        if not isinstance(self.leave_type_ids, Unset):
            leave_type_ids = self.leave_type_ids

        maximum_amount_in_cents = self.maximum_amount_in_cents

        name = self.name

        negative_counter_type: str | Unset = UNSET
        if not isinstance(self.negative_counter_type, Unset):
            negative_counter_type = self.negative_counter_type.value

        position = self.position

        proration_type: str | Unset = UNSET
        if not isinstance(self.proration_type, Unset):
            proration_type = self.proration_type.value

        pto_proratio_enabled = self.pto_proratio_enabled

        range_type: str | Unset = UNSET
        if not isinstance(self.range_type, Unset):
            range_type = self.range_type.value

        rounding: str | Unset = UNSET
        if not isinstance(self.rounding, Unset):
            rounding = self.rounding.value

        tenure_period_transition: str | Unset = UNSET
        if not isinstance(self.tenure_period_transition, Unset):
            tenure_period_transition = self.tenure_period_transition.value

        tenure_periods_enabled = self.tenure_periods_enabled

        tenure_periods: list[Any] | Unset = UNSET
        if not isinstance(self.tenure_periods, Unset):
            tenure_periods = self.tenure_periods

        unlimited_accrued_hours = self.unlimited_accrued_hours

        unlimited_carry_over = self.unlimited_carry_over

        unlimited_carry_over_expiration = self.unlimited_carry_over_expiration

        unlimited_holidays = self.unlimited_holidays

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if accrued_denominator_in_cents is not UNSET:
            field_dict["accrued_denominator_in_cents"] = accrued_denominator_in_cents
        if accrued_factor_in_cents is not UNSET:
            field_dict["accrued_factor_in_cents"] = accrued_factor_in_cents
        if available_days is not UNSET:
            field_dict["available_days"] = available_days
        if carry_over_units_in_cents is not UNSET:
            field_dict["carry_over_units_in_cents"] = carry_over_units_in_cents
        if count_holiday_as_workable is not UNSET:
            field_dict["count_holiday_as_workable"] = count_holiday_as_workable
        if days_type is not UNSET:
            field_dict["days_type"] = days_type
        if expire_in_months is not UNSET:
            field_dict["expire_in_months"] = expire_in_months
        if frequency is not UNSET:
            field_dict["frequency"] = frequency
        if holiday_allowance_in_cents is not UNSET:
            field_dict["holiday_allowance_in_cents"] = holiday_allowance_in_cents
        if leave_type_ids is not UNSET:
            field_dict["leave_type_ids"] = leave_type_ids
        if maximum_amount_in_cents is not UNSET:
            field_dict["maximum_amount_in_cents"] = maximum_amount_in_cents
        if name is not UNSET:
            field_dict["name"] = name
        if negative_counter_type is not UNSET:
            field_dict["negative_counter_type"] = negative_counter_type
        if position is not UNSET:
            field_dict["position"] = position
        if proration_type is not UNSET:
            field_dict["proration_type"] = proration_type
        if pto_proratio_enabled is not UNSET:
            field_dict["pto_proratio_enabled"] = pto_proratio_enabled
        if range_type is not UNSET:
            field_dict["range_type"] = range_type
        if rounding is not UNSET:
            field_dict["rounding"] = rounding
        if tenure_period_transition is not UNSET:
            field_dict["tenure_period_transition"] = tenure_period_transition
        if tenure_periods_enabled is not UNSET:
            field_dict["tenure_periods_enabled"] = tenure_periods_enabled
        if tenure_periods is not UNSET:
            field_dict["tenure_periods"] = tenure_periods
        if unlimited_accrued_hours is not UNSET:
            field_dict["unlimited_accrued_hours"] = unlimited_accrued_hours
        if unlimited_carry_over is not UNSET:
            field_dict["unlimited_carry_over"] = unlimited_carry_over
        if unlimited_carry_over_expiration is not UNSET:
            field_dict["unlimited_carry_over_expiration"] = unlimited_carry_over_expiration
        if unlimited_holidays is not UNSET:
            field_dict["unlimited_holidays"] = unlimited_holidays

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        accrued_denominator_in_cents = d.pop("accrued_denominator_in_cents", UNSET)

        accrued_factor_in_cents = d.pop("accrued_factor_in_cents", UNSET)

        _available_days = d.pop("available_days", UNSET)
        available_days: PutApi20260701ResourcesTimeoffAllowancesIdBodyAvailableDays | Unset
        if isinstance(_available_days, Unset):
            available_days = UNSET
        else:
            available_days = PutApi20260701ResourcesTimeoffAllowancesIdBodyAvailableDays(
                _available_days
            )

        carry_over_units_in_cents = d.pop("carry_over_units_in_cents", UNSET)

        count_holiday_as_workable = d.pop("count_holiday_as_workable", UNSET)

        _days_type = d.pop("days_type", UNSET)
        days_type: PutApi20260701ResourcesTimeoffAllowancesIdBodyDaysType | Unset
        if isinstance(_days_type, Unset):
            days_type = UNSET
        else:
            days_type = PutApi20260701ResourcesTimeoffAllowancesIdBodyDaysType(_days_type) if _days_type is not None else None

        expire_in_months = d.pop("expire_in_months", UNSET)

        _frequency = d.pop("frequency", UNSET)
        frequency: PutApi20260701ResourcesTimeoffAllowancesIdBodyFrequency | Unset
        if isinstance(_frequency, Unset):
            frequency = UNSET
        else:
            frequency = PutApi20260701ResourcesTimeoffAllowancesIdBodyFrequency(_frequency) if _frequency is not None else None

        holiday_allowance_in_cents = d.pop("holiday_allowance_in_cents", UNSET)

        leave_type_ids = cast(list[str], d.pop("leave_type_ids", UNSET))

        maximum_amount_in_cents = d.pop("maximum_amount_in_cents", UNSET)

        name = d.pop("name", UNSET)

        _negative_counter_type = d.pop("negative_counter_type", UNSET)
        negative_counter_type: (
            PutApi20260701ResourcesTimeoffAllowancesIdBodyNegativeCounterType | Unset
        )
        if isinstance(_negative_counter_type, Unset):
            negative_counter_type = UNSET
        else:
            negative_counter_type = (
                PutApi20260701ResourcesTimeoffAllowancesIdBodyNegativeCounterType(
                    _negative_counter_type
                )
            )

        position = d.pop("position", UNSET)

        _proration_type = d.pop("proration_type", UNSET)
        proration_type: PutApi20260701ResourcesTimeoffAllowancesIdBodyProrationType | Unset
        if isinstance(_proration_type, Unset):
            proration_type = UNSET
        else:
            proration_type = PutApi20260701ResourcesTimeoffAllowancesIdBodyProrationType(
                _proration_type
            )

        pto_proratio_enabled = d.pop("pto_proratio_enabled", UNSET)

        _range_type = d.pop("range_type", UNSET)
        range_type: PutApi20260701ResourcesTimeoffAllowancesIdBodyRangeType | Unset
        if isinstance(_range_type, Unset):
            range_type = UNSET
        else:
            range_type = PutApi20260701ResourcesTimeoffAllowancesIdBodyRangeType(_range_type) if _range_type is not None else None

        _rounding = d.pop("rounding", UNSET)
        rounding: PutApi20260701ResourcesTimeoffAllowancesIdBodyRounding | Unset
        if isinstance(_rounding, Unset):
            rounding = UNSET
        else:
            rounding = PutApi20260701ResourcesTimeoffAllowancesIdBodyRounding(_rounding) if _rounding is not None else None

        _tenure_period_transition = d.pop("tenure_period_transition", UNSET)
        tenure_period_transition: (
            PutApi20260701ResourcesTimeoffAllowancesIdBodyTenurePeriodTransition | Unset
        )
        if isinstance(_tenure_period_transition, Unset):
            tenure_period_transition = UNSET
        else:
            tenure_period_transition = (
                PutApi20260701ResourcesTimeoffAllowancesIdBodyTenurePeriodTransition(
                    _tenure_period_transition
                )
            )

        tenure_periods_enabled = d.pop("tenure_periods_enabled", UNSET)

        tenure_periods = cast(list[Any], d.pop("tenure_periods", UNSET))

        unlimited_accrued_hours = d.pop("unlimited_accrued_hours", UNSET)

        unlimited_carry_over = d.pop("unlimited_carry_over", UNSET)

        unlimited_carry_over_expiration = d.pop("unlimited_carry_over_expiration", UNSET)

        unlimited_holidays = d.pop("unlimited_holidays", UNSET)

        put_api_20260701_resources_timeoff_allowances_id_body = cls(
            id=id,
            accrued_denominator_in_cents=accrued_denominator_in_cents,
            accrued_factor_in_cents=accrued_factor_in_cents,
            available_days=available_days,
            carry_over_units_in_cents=carry_over_units_in_cents,
            count_holiday_as_workable=count_holiday_as_workable,
            days_type=days_type,
            expire_in_months=expire_in_months,
            frequency=frequency,
            holiday_allowance_in_cents=holiday_allowance_in_cents,
            leave_type_ids=leave_type_ids,
            maximum_amount_in_cents=maximum_amount_in_cents,
            name=name,
            negative_counter_type=negative_counter_type,
            position=position,
            proration_type=proration_type,
            pto_proratio_enabled=pto_proratio_enabled,
            range_type=range_type,
            rounding=rounding,
            tenure_period_transition=tenure_period_transition,
            tenure_periods_enabled=tenure_periods_enabled,
            tenure_periods=tenure_periods,
            unlimited_accrued_hours=unlimited_accrued_hours,
            unlimited_carry_over=unlimited_carry_over,
            unlimited_carry_over_expiration=unlimited_carry_over_expiration,
            unlimited_holidays=unlimited_holidays,
        )

        put_api_20260701_resources_timeoff_allowances_id_body.additional_properties = d
        return put_api_20260701_resources_timeoff_allowances_id_body

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
