from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_api_20261001_resources_timeoff_allowances_body_accrued_units_availability import (
    PostApi20261001ResourcesTimeoffAllowancesBodyAccruedUnitsAvailability,
)
from ..models.post_api_20261001_resources_timeoff_allowances_body_allowance_type import (
    PostApi20261001ResourcesTimeoffAllowancesBodyAllowanceType,
)
from ..models.post_api_20261001_resources_timeoff_allowances_body_available_days import (
    PostApi20261001ResourcesTimeoffAllowancesBodyAvailableDays,
)
from ..models.post_api_20261001_resources_timeoff_allowances_body_cycle_start import (
    PostApi20261001ResourcesTimeoffAllowancesBodyCycleStart,
)
from ..models.post_api_20261001_resources_timeoff_allowances_body_days_type import (
    PostApi20261001ResourcesTimeoffAllowancesBodyDaysType,
)
from ..models.post_api_20261001_resources_timeoff_allowances_body_frequency import (
    PostApi20261001ResourcesTimeoffAllowancesBodyFrequency,
)
from ..models.post_api_20261001_resources_timeoff_allowances_body_negative_counter_type import (
    PostApi20261001ResourcesTimeoffAllowancesBodyNegativeCounterType,
)
from ..models.post_api_20261001_resources_timeoff_allowances_body_proration_type import (
    PostApi20261001ResourcesTimeoffAllowancesBodyProrationType,
)
from ..models.post_api_20261001_resources_timeoff_allowances_body_range_type import (
    PostApi20261001ResourcesTimeoffAllowancesBodyRangeType,
)
from ..models.post_api_20261001_resources_timeoff_allowances_body_rounding import (
    PostApi20261001ResourcesTimeoffAllowancesBodyRounding,
)
from ..models.post_api_20261001_resources_timeoff_allowances_body_source_units import (
    PostApi20261001ResourcesTimeoffAllowancesBodySourceUnits,
)
from ..models.post_api_20261001_resources_timeoff_allowances_body_tenure_period_transition import (
    PostApi20261001ResourcesTimeoffAllowancesBodyTenurePeriodTransition,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_api_20261001_resources_timeoff_allowances_body_tenure_periods_item import (
        PostApi20261001ResourcesTimeoffAllowancesBodyTenurePeriodsItem,
    )


T = TypeVar("T", bound="PostApi20261001ResourcesTimeoffAllowancesBody")


@_attrs_define
class PostApi20261001ResourcesTimeoffAllowancesBody:
    accrued_units_availability: (
        PostApi20261001ResourcesTimeoffAllowancesBodyAccruedUnitsAvailability
    )
    """ When can the accrued units be spent. """
    allowance_type: PostApi20261001ResourcesTimeoffAllowancesBodyAllowanceType
    """ Sets the allowance units. Can be "days" or "hours" """
    available_days: PostApi20261001ResourcesTimeoffAllowancesBodyAvailableDays
    """ Indicates how the allowance units are accrued. For example all_days means all allowance days are given on
    the first day of the cycle. """
    count_holiday_as_workable: bool
    """ This setting flags if units taken during a bank holiday should be deducted or not from allowance. """
    cycle_start: PostApi20261001ResourcesTimeoffAllowancesBodyCycleStart
    """ When does the cycle start. """
    days_type: PostApi20261001ResourcesTimeoffAllowancesBodyDaysType
    """ Indicates if the allowance is based on working on calendar days. """
    holiday_allowance_in_cents: int
    """ Base amount of holiday allowance units multiplied by 100 """
    leave_type_ids: list[str]
    """ An array of leave type ids associated with that allowance """
    name: str
    """ Allowance name set by the user """
    negative_counter_type: PostApi20261001ResourcesTimeoffAllowancesBodyNegativeCounterType
    """ Whether the allowance allows to request more days than available. """
    proration_type: PostApi20261001ResourcesTimeoffAllowancesBodyProrationType
    """ Whether the allowance has proration enabled or not. """
    pto_proratio_enabled: bool
    """ Whether the allowance days are prorated or not """
    rounding: PostApi20261001ResourcesTimeoffAllowancesBodyRounding
    """ How the accrued units of the allowance are rounded. It depends if the allowance is set in hours or days. """
    source_units: PostApi20261001ResourcesTimeoffAllowancesBodySourceUnits
    """ This field configures the type of allowance (fixed balance, based on worked time) """
    tenure_periods: list[PostApi20261001ResourcesTimeoffAllowancesBodyTenurePeriodsItem]
    """ The tenure periods associated with the allowance. """
    timeoff_policy_id: str
    """ The Id of the policy to which the allowance belongs to """
    unlimited_accrued_hours: bool
    """ Flag to indicate if there is unlimited accrual. """
    unlimited_carry_over: bool
    """ Flag to indicate if there is unlimited carry over. """
    unlimited_carry_over_expiration: bool
    """ Boolean to flag if carryover does not expire """
    unlimited_holidays: bool
    """ Flag to indicate that the allowance has unlimited available days """
    accrued_denominator_in_cents: int | Unset = UNSET
    """ Only for Allowances based on worked time. It represents how many units you need to work to be granted
    allowance units """
    accrued_factor_in_cents: int | Unset = UNSET
    """ Only for Allowances based on worked time. It represents how many units you are given per unit of time worked
    """
    carry_over_units_in_cents: int | Unset = UNSET
    """ How many units can carry over between cycles multiplied by 100 """
    cycle_length: int | Unset = UNSET
    """ How many months does each allowance cycle last """
    expire_in_months: int | Unset = UNSET
    """ When does the carryover expire in months. """
    frequency: PostApi20261001ResourcesTimeoffAllowancesBodyFrequency | Unset = UNSET
    """ Defines duration of the allowance cycles. Can be "yearly", "monthly_flexible" or "lifetime" """
    maximum_amount_in_cents: int | Unset = UNSET
    """ Maximum the allowance can reach on accrued """
    position: int | Unset = UNSET
    """ Indicates the position in the allowance when rendering them in UI """
    range_type: PostApi20261001ResourcesTimeoffAllowancesBodyRangeType | Unset = UNSET
    """ Configures how leaves duration is handled. """
    tenure_period_transition: (
        PostApi20261001ResourcesTimeoffAllowancesBodyTenurePeriodTransition | Unset
    ) = UNSET
    """ In case the allowance has tenure periods, when is this tenure applied. """
    tenure_periods_enabled: bool | Unset = UNSET
    """ Whether the allowance has tenure periods enabled or not. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accrued_units_availability = self.accrued_units_availability.value

        allowance_type = self.allowance_type.value

        available_days = self.available_days.value

        count_holiday_as_workable = self.count_holiday_as_workable

        cycle_start = self.cycle_start.value

        days_type = self.days_type.value

        holiday_allowance_in_cents = self.holiday_allowance_in_cents

        leave_type_ids = self.leave_type_ids

        name = self.name

        negative_counter_type = self.negative_counter_type.value

        proration_type = self.proration_type.value

        pto_proratio_enabled = self.pto_proratio_enabled

        rounding = self.rounding.value

        source_units = self.source_units.value

        tenure_periods = []
        for tenure_periods_item_data in self.tenure_periods:
            tenure_periods_item = tenure_periods_item_data.to_dict()
            tenure_periods.append(tenure_periods_item)

        timeoff_policy_id = self.timeoff_policy_id

        unlimited_accrued_hours = self.unlimited_accrued_hours

        unlimited_carry_over = self.unlimited_carry_over

        unlimited_carry_over_expiration = self.unlimited_carry_over_expiration

        unlimited_holidays = self.unlimited_holidays

        accrued_denominator_in_cents = self.accrued_denominator_in_cents

        accrued_factor_in_cents = self.accrued_factor_in_cents

        carry_over_units_in_cents = self.carry_over_units_in_cents

        cycle_length = self.cycle_length

        expire_in_months = self.expire_in_months

        frequency: str | Unset = UNSET
        if not isinstance(self.frequency, Unset):
            frequency = self.frequency.value if self.frequency is not None else None

        maximum_amount_in_cents = self.maximum_amount_in_cents

        position = self.position

        range_type: str | Unset = UNSET
        if not isinstance(self.range_type, Unset):
            range_type = self.range_type.value if self.range_type is not None else None

        tenure_period_transition: str | Unset = UNSET
        if not isinstance(self.tenure_period_transition, Unset):
            tenure_period_transition = self.tenure_period_transition.value if self.tenure_period_transition is not None else None

        tenure_periods_enabled = self.tenure_periods_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accrued_units_availability": accrued_units_availability,
                "allowance_type": allowance_type,
                "available_days": available_days,
                "count_holiday_as_workable": count_holiday_as_workable,
                "cycle_start": cycle_start,
                "days_type": days_type,
                "holiday_allowance_in_cents": holiday_allowance_in_cents,
                "leave_type_ids": leave_type_ids,
                "name": name,
                "negative_counter_type": negative_counter_type,
                "proration_type": proration_type,
                "pto_proratio_enabled": pto_proratio_enabled,
                "rounding": rounding,
                "source_units": source_units,
                "tenure_periods": tenure_periods,
                "timeoff_policy_id": timeoff_policy_id,
                "unlimited_accrued_hours": unlimited_accrued_hours,
                "unlimited_carry_over": unlimited_carry_over,
                "unlimited_carry_over_expiration": unlimited_carry_over_expiration,
                "unlimited_holidays": unlimited_holidays,
            }
        )
        if accrued_denominator_in_cents is not UNSET:
            field_dict["accrued_denominator_in_cents"] = accrued_denominator_in_cents
        if accrued_factor_in_cents is not UNSET:
            field_dict["accrued_factor_in_cents"] = accrued_factor_in_cents
        if carry_over_units_in_cents is not UNSET:
            field_dict["carry_over_units_in_cents"] = carry_over_units_in_cents
        if cycle_length is not UNSET:
            field_dict["cycle_length"] = cycle_length
        if expire_in_months is not UNSET:
            field_dict["expire_in_months"] = expire_in_months
        if frequency is not UNSET:
            field_dict["frequency"] = frequency
        if maximum_amount_in_cents is not UNSET:
            field_dict["maximum_amount_in_cents"] = maximum_amount_in_cents
        if position is not UNSET:
            field_dict["position"] = position
        if range_type is not UNSET:
            field_dict["range_type"] = range_type
        if tenure_period_transition is not UNSET:
            field_dict["tenure_period_transition"] = tenure_period_transition
        if tenure_periods_enabled is not UNSET:
            field_dict["tenure_periods_enabled"] = tenure_periods_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_api_20261001_resources_timeoff_allowances_body_tenure_periods_item import (
            PostApi20261001ResourcesTimeoffAllowancesBodyTenurePeriodsItem,
        )

        d = dict(src_dict)
        accrued_units_availability = (
            PostApi20261001ResourcesTimeoffAllowancesBodyAccruedUnitsAvailability(
                d.pop("accrued_units_availability")
            )
        )

        allowance_type = PostApi20261001ResourcesTimeoffAllowancesBodyAllowanceType(
            d.pop("allowance_type")
        )

        available_days = PostApi20261001ResourcesTimeoffAllowancesBodyAvailableDays(
            d.pop("available_days")
        )

        count_holiday_as_workable = d.pop("count_holiday_as_workable")

        cycle_start = PostApi20261001ResourcesTimeoffAllowancesBodyCycleStart(d.pop("cycle_start"))

        days_type = PostApi20261001ResourcesTimeoffAllowancesBodyDaysType(d.pop("days_type"))

        holiday_allowance_in_cents = d.pop("holiday_allowance_in_cents")

        leave_type_ids = cast(list[str], d.pop("leave_type_ids"))

        name = d.pop("name")

        negative_counter_type = PostApi20261001ResourcesTimeoffAllowancesBodyNegativeCounterType(
            d.pop("negative_counter_type")
        )

        proration_type = PostApi20261001ResourcesTimeoffAllowancesBodyProrationType(
            d.pop("proration_type")
        )

        pto_proratio_enabled = d.pop("pto_proratio_enabled")

        rounding = PostApi20261001ResourcesTimeoffAllowancesBodyRounding(d.pop("rounding"))

        source_units = PostApi20261001ResourcesTimeoffAllowancesBodySourceUnits(
            d.pop("source_units")
        )

        tenure_periods = []
        _tenure_periods = d.pop("tenure_periods")
        for tenure_periods_item_data in _tenure_periods:
            tenure_periods_item = (
                PostApi20261001ResourcesTimeoffAllowancesBodyTenurePeriodsItem.from_dict(
                    tenure_periods_item_data
                )
            )

            tenure_periods.append(tenure_periods_item)

        timeoff_policy_id = d.pop("timeoff_policy_id")

        unlimited_accrued_hours = d.pop("unlimited_accrued_hours")

        unlimited_carry_over = d.pop("unlimited_carry_over")

        unlimited_carry_over_expiration = d.pop("unlimited_carry_over_expiration")

        unlimited_holidays = d.pop("unlimited_holidays")

        accrued_denominator_in_cents = d.pop("accrued_denominator_in_cents", UNSET)

        accrued_factor_in_cents = d.pop("accrued_factor_in_cents", UNSET)

        carry_over_units_in_cents = d.pop("carry_over_units_in_cents", UNSET)

        cycle_length = d.pop("cycle_length", UNSET)

        expire_in_months = d.pop("expire_in_months", UNSET)

        _frequency = d.pop("frequency", UNSET)
        frequency: PostApi20261001ResourcesTimeoffAllowancesBodyFrequency | Unset
        if isinstance(_frequency, Unset):
            frequency = UNSET
        else:
            frequency = PostApi20261001ResourcesTimeoffAllowancesBodyFrequency(_frequency) if _frequency is not None else None

        maximum_amount_in_cents = d.pop("maximum_amount_in_cents", UNSET)

        position = d.pop("position", UNSET)

        _range_type = d.pop("range_type", UNSET)
        range_type: PostApi20261001ResourcesTimeoffAllowancesBodyRangeType | Unset
        if isinstance(_range_type, Unset):
            range_type = UNSET
        else:
            range_type = PostApi20261001ResourcesTimeoffAllowancesBodyRangeType(_range_type) if _range_type is not None else None

        _tenure_period_transition = d.pop("tenure_period_transition", UNSET)
        tenure_period_transition: (
            PostApi20261001ResourcesTimeoffAllowancesBodyTenurePeriodTransition | Unset
        )
        if isinstance(_tenure_period_transition, Unset):
            tenure_period_transition = UNSET
        else:
            tenure_period_transition = (
                PostApi20261001ResourcesTimeoffAllowancesBodyTenurePeriodTransition(
                    _tenure_period_transition
                ) if _tenure_period_transition is not None else None
            )

        tenure_periods_enabled = d.pop("tenure_periods_enabled", UNSET)

        post_api_20261001_resources_timeoff_allowances_body = cls(
            accrued_units_availability=accrued_units_availability,
            allowance_type=allowance_type,
            available_days=available_days,
            count_holiday_as_workable=count_holiday_as_workable,
            cycle_start=cycle_start,
            days_type=days_type,
            holiday_allowance_in_cents=holiday_allowance_in_cents,
            leave_type_ids=leave_type_ids,
            name=name,
            negative_counter_type=negative_counter_type,
            proration_type=proration_type,
            pto_proratio_enabled=pto_proratio_enabled,
            rounding=rounding,
            source_units=source_units,
            tenure_periods=tenure_periods,
            timeoff_policy_id=timeoff_policy_id,
            unlimited_accrued_hours=unlimited_accrued_hours,
            unlimited_carry_over=unlimited_carry_over,
            unlimited_carry_over_expiration=unlimited_carry_over_expiration,
            unlimited_holidays=unlimited_holidays,
            accrued_denominator_in_cents=accrued_denominator_in_cents,
            accrued_factor_in_cents=accrued_factor_in_cents,
            carry_over_units_in_cents=carry_over_units_in_cents,
            cycle_length=cycle_length,
            expire_in_months=expire_in_months,
            frequency=frequency,
            maximum_amount_in_cents=maximum_amount_in_cents,
            position=position,
            range_type=range_type,
            tenure_period_transition=tenure_period_transition,
            tenure_periods_enabled=tenure_periods_enabled,
        )

        post_api_20261001_resources_timeoff_allowances_body.additional_properties = d
        return post_api_20261001_resources_timeoff_allowances_body

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
