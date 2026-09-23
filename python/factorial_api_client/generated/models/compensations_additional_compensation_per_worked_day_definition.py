from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CompensationsAdditionalCompensationPerWorkedDayDefinition")


@_attrs_define
class CompensationsAdditionalCompensationPerWorkedDayDefinition:
    """Definition object populated for PerWorkedDay strategies. Carries `calculation_source`, `reference_time`,
    `minimum_amount_of_hours_in_minutes`, `work_locations`, `timeoff_leave_type_ids`, and `eligible_days`. `null` for
    Fixed / Variable strategies.

    """

    calculation_source: str
    reference_time: str
    minimum_amount_of_hours_in_minutes: int | Unset = UNSET
    work_locations: list[str] | Unset = UNSET
    timeoff_leave_type_ids: list[str] | Unset = UNSET
    eligible_days: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        calculation_source = self.calculation_source

        reference_time = self.reference_time

        minimum_amount_of_hours_in_minutes = self.minimum_amount_of_hours_in_minutes

        work_locations: list[str] | Unset = UNSET
        if not isinstance(self.work_locations, Unset):
            work_locations = self.work_locations

        timeoff_leave_type_ids: list[str] | Unset = UNSET
        if not isinstance(self.timeoff_leave_type_ids, Unset):
            timeoff_leave_type_ids = self.timeoff_leave_type_ids

        eligible_days: list[str] | Unset = UNSET
        if not isinstance(self.eligible_days, Unset):
            eligible_days = self.eligible_days

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "calculation_source": calculation_source,
                "reference_time": reference_time,
            }
        )
        if minimum_amount_of_hours_in_minutes is not UNSET:
            field_dict["minimum_amount_of_hours_in_minutes"] = minimum_amount_of_hours_in_minutes
        if work_locations is not UNSET:
            field_dict["work_locations"] = work_locations
        if timeoff_leave_type_ids is not UNSET:
            field_dict["timeoff_leave_type_ids"] = timeoff_leave_type_ids
        if eligible_days is not UNSET:
            field_dict["eligible_days"] = eligible_days

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        calculation_source = d.pop("calculation_source")

        reference_time = d.pop("reference_time")

        minimum_amount_of_hours_in_minutes = d.pop("minimum_amount_of_hours_in_minutes", UNSET)

        work_locations = cast(list[str], d.pop("work_locations", UNSET))

        timeoff_leave_type_ids = cast(list[str], d.pop("timeoff_leave_type_ids", UNSET))

        eligible_days = cast(list[str], d.pop("eligible_days", UNSET))

        compensations_additional_compensation_per_worked_day_definition = cls(
            calculation_source=calculation_source,
            reference_time=reference_time,
            minimum_amount_of_hours_in_minutes=minimum_amount_of_hours_in_minutes,
            work_locations=work_locations,
            timeoff_leave_type_ids=timeoff_leave_type_ids,
            eligible_days=eligible_days,
        )

        compensations_additional_compensation_per_worked_day_definition.additional_properties = d
        return compensations_additional_compensation_per_worked_day_definition

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
