from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.timeoff_allowance_accrued_units_availability import (
    TimeoffAllowanceAccruedUnitsAvailability,
)
from ..models.timeoff_allowance_allowance_type import TimeoffAllowanceAllowanceType
from ..models.timeoff_allowance_available_days import TimeoffAllowanceAvailableDays
from ..models.timeoff_allowance_days_type import TimeoffAllowanceDaysType
from ..models.timeoff_allowance_frequency import TimeoffAllowanceFrequency
from ..models.timeoff_allowance_negative_counter_type import TimeoffAllowanceNegativeCounterType
from ..models.timeoff_allowance_proration_type import TimeoffAllowanceProrationType
from ..models.timeoff_allowance_range_type import TimeoffAllowanceRangeType
from ..models.timeoff_allowance_rounding import TimeoffAllowanceRounding
from ..models.timeoff_allowance_source_units import TimeoffAllowanceSourceUnits
from ..models.timeoff_allowance_tenure_period_transition import (
    TimeoffAllowanceTenurePeriodTransition,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="TimeoffAllowance")


@_attrs_define
class TimeoffAllowance:
    id: int
    """ Unique identifier of the allowance """
    allowance_type: TimeoffAllowanceAllowanceType
    """ Sets the allowance units. Can be "days" or "hours" """
    available_days: TimeoffAllowanceAvailableDays
    """ Indicates how the allowance units are accrued. For example all_days means all allowance days are given on
    the first day of the cycle. """
    count_holiday_as_workable: bool
    """ This setting flags if units taken during a bank holiday should be deducted or not from allowance. """
    leave_type_ids: list[int]
    """ An array of leave type ids associated with that allowance """
    name: str
    """ Allowance name set by the user """
    proration_type: TimeoffAllowanceProrationType
    """ Whether the allowance has proration enabled or not. """
    rounding: TimeoffAllowanceRounding
    """ How the accrued units of the allowance are rounded. It depends if the allowance is set in hours or days. """
    tenure_periods: list[Any]
    """ The tenure periods associated with the allowance. """
    timeoff_cycle: str
    """ Value to indicate how the allowance cycle is configured. Its an abbreviation of the first and last month.
    """
    timeoff_policy_id: int
    """ The Id of the policy to which the allowance belongs to """
    accrued_denominator_in_cents: int | Unset = UNSET
    """ Only for Allowances based on worked time. It represents how many units you need to work to be granted
    allowance units """
    accrued_factor_in_cents: int | Unset = UNSET
    """ Only for Allowances based on worked time. It represents how many units you are given per unit of time worked
    """
    accrued_units_availability: TimeoffAllowanceAccruedUnitsAvailability | Unset = UNSET
    """ When can the acrrued units be spent. """
    carry_over_days: int | Unset = UNSET
    """ How many units can carry over between cycles """
    carry_over_units_in_cents: int | Unset = UNSET
    """ How many units can carry over between cycles multiplied by 100 """
    cycle_length: int | Unset = UNSET
    """ How many months does each allowance cycle last """
    cycle_start: str | Unset = UNSET
    """ When does the cycle start. """
    days_type: TimeoffAllowanceDaysType | Unset = UNSET
    """ Indicates if the allowance is based on working on calendar days. """
    employee_carry_over_starting_year: int | Unset = UNSET
    """ When does the carryover start """
    expire_in_months: int | Unset = UNSET
    """ When does the carryover expire in months. """
    frequency: TimeoffAllowanceFrequency | Unset = UNSET
    """ Defines duration of the allowance cycles. Can be "yearly", "monthly_flexible" or "lifetime" """
    holiday_allowance_in_cents: int | Unset = UNSET
    """ Base amount of holiday allowance units multiplied by 100 """
    maximum_amount_in_cents: int | Unset = UNSET
    """ Maximum the allowance can reach on accrued """
    negative_counter_type: TimeoffAllowanceNegativeCounterType | Unset = UNSET
    """ Whether the allowance allows to request more days than available """
    position: int | Unset = UNSET
    """ Indicates the position in the allowance when rendering them in UI """
    pto_proratio_enabled: bool | Unset = UNSET
    """ Whether the allowance days are prorrated or not """
    range_type: TimeoffAllowanceRangeType | Unset = UNSET
    """ Configures how leaves duration is handled. """
    send_notification: bool | Unset = UNSET
    source_units: TimeoffAllowanceSourceUnits | Unset = UNSET
    """ This field configures the type of allowance (fixed balance, based on worked time) """
    tenure_period_transition: TimeoffAllowanceTenurePeriodTransition | Unset = UNSET
    """ In case the allowance has tenure periods, when is this tenure applied. """
    tenure_periods_enabled: bool | Unset = UNSET
    """ Whether the allowance has tenure periods enabled or not. """
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

        allowance_type = self.allowance_type.value

        available_days = self.available_days.value

        count_holiday_as_workable = self.count_holiday_as_workable

        leave_type_ids = self.leave_type_ids

        name = self.name

        proration_type = self.proration_type.value

        rounding = self.rounding.value

        tenure_periods = self.tenure_periods

        timeoff_cycle = self.timeoff_cycle

        timeoff_policy_id = self.timeoff_policy_id

        accrued_denominator_in_cents = self.accrued_denominator_in_cents

        accrued_factor_in_cents = self.accrued_factor_in_cents

        accrued_units_availability: str | Unset = UNSET
        if not isinstance(self.accrued_units_availability, Unset):
            accrued_units_availability = self.accrued_units_availability.value

        carry_over_days = self.carry_over_days

        carry_over_units_in_cents = self.carry_over_units_in_cents

        cycle_length = self.cycle_length

        cycle_start = self.cycle_start

        days_type: str | Unset = UNSET
        if not isinstance(self.days_type, Unset):
            days_type = self.days_type.value

        employee_carry_over_starting_year = self.employee_carry_over_starting_year

        expire_in_months = self.expire_in_months

        frequency: str | Unset = UNSET
        if not isinstance(self.frequency, Unset):
            frequency = self.frequency.value

        holiday_allowance_in_cents = self.holiday_allowance_in_cents

        maximum_amount_in_cents = self.maximum_amount_in_cents

        negative_counter_type: str | Unset = UNSET
        if not isinstance(self.negative_counter_type, Unset):
            negative_counter_type = self.negative_counter_type.value

        position = self.position

        pto_proratio_enabled = self.pto_proratio_enabled

        range_type: str | Unset = UNSET
        if not isinstance(self.range_type, Unset):
            range_type = self.range_type.value

        send_notification = self.send_notification

        source_units: str | Unset = UNSET
        if not isinstance(self.source_units, Unset):
            source_units = self.source_units.value

        tenure_period_transition: str | Unset = UNSET
        if not isinstance(self.tenure_period_transition, Unset):
            tenure_period_transition = self.tenure_period_transition.value

        tenure_periods_enabled = self.tenure_periods_enabled

        unlimited_accrued_hours = self.unlimited_accrued_hours

        unlimited_carry_over = self.unlimited_carry_over

        unlimited_carry_over_expiration = self.unlimited_carry_over_expiration

        unlimited_holidays = self.unlimited_holidays

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "allowance_type": allowance_type,
                "available_days": available_days,
                "count_holiday_as_workable": count_holiday_as_workable,
                "leave_type_ids": leave_type_ids,
                "name": name,
                "proration_type": proration_type,
                "rounding": rounding,
                "tenure_periods": tenure_periods,
                "timeoff_cycle": timeoff_cycle,
                "timeoff_policy_id": timeoff_policy_id,
            }
        )
        if accrued_denominator_in_cents is not UNSET:
            field_dict["accrued_denominator_in_cents"] = accrued_denominator_in_cents
        if accrued_factor_in_cents is not UNSET:
            field_dict["accrued_factor_in_cents"] = accrued_factor_in_cents
        if accrued_units_availability is not UNSET:
            field_dict["accrued_units_availability"] = accrued_units_availability
        if carry_over_days is not UNSET:
            field_dict["carry_over_days"] = carry_over_days
        if carry_over_units_in_cents is not UNSET:
            field_dict["carry_over_units_in_cents"] = carry_over_units_in_cents
        if cycle_length is not UNSET:
            field_dict["cycle_length"] = cycle_length
        if cycle_start is not UNSET:
            field_dict["cycle_start"] = cycle_start
        if days_type is not UNSET:
            field_dict["days_type"] = days_type
        if employee_carry_over_starting_year is not UNSET:
            field_dict["employee_carry_over_starting_year"] = employee_carry_over_starting_year
        if expire_in_months is not UNSET:
            field_dict["expire_in_months"] = expire_in_months
        if frequency is not UNSET:
            field_dict["frequency"] = frequency
        if holiday_allowance_in_cents is not UNSET:
            field_dict["holiday_allowance_in_cents"] = holiday_allowance_in_cents
        if maximum_amount_in_cents is not UNSET:
            field_dict["maximum_amount_in_cents"] = maximum_amount_in_cents
        if negative_counter_type is not UNSET:
            field_dict["negative_counter_type"] = negative_counter_type
        if position is not UNSET:
            field_dict["position"] = position
        if pto_proratio_enabled is not UNSET:
            field_dict["pto_proratio_enabled"] = pto_proratio_enabled
        if range_type is not UNSET:
            field_dict["range_type"] = range_type
        if send_notification is not UNSET:
            field_dict["send_notification"] = send_notification
        if source_units is not UNSET:
            field_dict["source_units"] = source_units
        if tenure_period_transition is not UNSET:
            field_dict["tenure_period_transition"] = tenure_period_transition
        if tenure_periods_enabled is not UNSET:
            field_dict["tenure_periods_enabled"] = tenure_periods_enabled
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

        allowance_type = TimeoffAllowanceAllowanceType(d.pop("allowance_type"))

        available_days = TimeoffAllowanceAvailableDays(d.pop("available_days"))

        count_holiday_as_workable = d.pop("count_holiday_as_workable")

        leave_type_ids = cast(list[int], d.pop("leave_type_ids"))

        name = d.pop("name")

        proration_type = TimeoffAllowanceProrationType(d.pop("proration_type"))

        rounding = TimeoffAllowanceRounding(d.pop("rounding"))

        tenure_periods = cast(list[Any], d.pop("tenure_periods"))

        timeoff_cycle = d.pop("timeoff_cycle")

        timeoff_policy_id = d.pop("timeoff_policy_id")

        accrued_denominator_in_cents = d.pop("accrued_denominator_in_cents", UNSET)

        accrued_factor_in_cents = d.pop("accrued_factor_in_cents", UNSET)

        _accrued_units_availability = d.pop("accrued_units_availability", UNSET)
        accrued_units_availability: TimeoffAllowanceAccruedUnitsAvailability | Unset
        if isinstance(_accrued_units_availability, Unset):
            accrued_units_availability = UNSET
        else:
            accrued_units_availability = TimeoffAllowanceAccruedUnitsAvailability(
                _accrued_units_availability
            )

        carry_over_days = d.pop("carry_over_days", UNSET)

        carry_over_units_in_cents = d.pop("carry_over_units_in_cents", UNSET)

        cycle_length = d.pop("cycle_length", UNSET)

        cycle_start = d.pop("cycle_start", UNSET)

        _days_type = d.pop("days_type", UNSET)
        days_type: TimeoffAllowanceDaysType | Unset
        if isinstance(_days_type, Unset):
            days_type = UNSET
        else:
            days_type = TimeoffAllowanceDaysType(_days_type) if _days_type is not None else None

        employee_carry_over_starting_year = d.pop("employee_carry_over_starting_year", UNSET)

        expire_in_months = d.pop("expire_in_months", UNSET)

        _frequency = d.pop("frequency", UNSET)
        frequency: TimeoffAllowanceFrequency | Unset
        if isinstance(_frequency, Unset):
            frequency = UNSET
        else:
            frequency = TimeoffAllowanceFrequency(_frequency) if _frequency is not None else None

        holiday_allowance_in_cents = d.pop("holiday_allowance_in_cents", UNSET)

        maximum_amount_in_cents = d.pop("maximum_amount_in_cents", UNSET)

        _negative_counter_type = d.pop("negative_counter_type", UNSET)
        negative_counter_type: TimeoffAllowanceNegativeCounterType | Unset
        if isinstance(_negative_counter_type, Unset):
            negative_counter_type = UNSET
        else:
            negative_counter_type = TimeoffAllowanceNegativeCounterType(_negative_counter_type) if _negative_counter_type is not None else None

        position = d.pop("position", UNSET)

        pto_proratio_enabled = d.pop("pto_proratio_enabled", UNSET)

        _range_type = d.pop("range_type", UNSET)
        range_type: TimeoffAllowanceRangeType | Unset
        if isinstance(_range_type, Unset):
            range_type = UNSET
        else:
            range_type = TimeoffAllowanceRangeType(_range_type) if _range_type is not None else None

        send_notification = d.pop("send_notification", UNSET)

        _source_units = d.pop("source_units", UNSET)
        source_units: TimeoffAllowanceSourceUnits | Unset
        if isinstance(_source_units, Unset):
            source_units = UNSET
        else:
            source_units = TimeoffAllowanceSourceUnits(_source_units) if _source_units is not None else None

        _tenure_period_transition = d.pop("tenure_period_transition", UNSET)
        tenure_period_transition: TimeoffAllowanceTenurePeriodTransition | Unset
        if isinstance(_tenure_period_transition, Unset):
            tenure_period_transition = UNSET
        else:
            tenure_period_transition = TimeoffAllowanceTenurePeriodTransition(
                _tenure_period_transition
            )

        tenure_periods_enabled = d.pop("tenure_periods_enabled", UNSET)

        unlimited_accrued_hours = d.pop("unlimited_accrued_hours", UNSET)

        unlimited_carry_over = d.pop("unlimited_carry_over", UNSET)

        unlimited_carry_over_expiration = d.pop("unlimited_carry_over_expiration", UNSET)

        unlimited_holidays = d.pop("unlimited_holidays", UNSET)

        timeoff_allowance = cls(
            id=id,
            allowance_type=allowance_type,
            available_days=available_days,
            count_holiday_as_workable=count_holiday_as_workable,
            leave_type_ids=leave_type_ids,
            name=name,
            proration_type=proration_type,
            rounding=rounding,
            tenure_periods=tenure_periods,
            timeoff_cycle=timeoff_cycle,
            timeoff_policy_id=timeoff_policy_id,
            accrued_denominator_in_cents=accrued_denominator_in_cents,
            accrued_factor_in_cents=accrued_factor_in_cents,
            accrued_units_availability=accrued_units_availability,
            carry_over_days=carry_over_days,
            carry_over_units_in_cents=carry_over_units_in_cents,
            cycle_length=cycle_length,
            cycle_start=cycle_start,
            days_type=days_type,
            employee_carry_over_starting_year=employee_carry_over_starting_year,
            expire_in_months=expire_in_months,
            frequency=frequency,
            holiday_allowance_in_cents=holiday_allowance_in_cents,
            maximum_amount_in_cents=maximum_amount_in_cents,
            negative_counter_type=negative_counter_type,
            position=position,
            pto_proratio_enabled=pto_proratio_enabled,
            range_type=range_type,
            send_notification=send_notification,
            source_units=source_units,
            tenure_period_transition=tenure_period_transition,
            tenure_periods_enabled=tenure_periods_enabled,
            unlimited_accrued_hours=unlimited_accrued_hours,
            unlimited_carry_over=unlimited_carry_over,
            unlimited_carry_over_expiration=unlimited_carry_over_expiration,
            unlimited_holidays=unlimited_holidays,
        )

        timeoff_allowance.additional_properties = d
        return timeoff_allowance

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
