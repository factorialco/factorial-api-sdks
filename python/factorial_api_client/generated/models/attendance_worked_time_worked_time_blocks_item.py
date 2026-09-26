from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.attendance_worked_time_worked_time_blocks_item_pool_type import (
    AttendanceWorkedTimeWorkedTimeBlocksItemPoolType,
)
from ..models.attendance_worked_time_worked_time_blocks_item_time_type import (
    AttendanceWorkedTimeWorkedTimeBlocksItemTimeType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="AttendanceWorkedTimeWorkedTimeBlocksItem")


@_attrs_define
class AttendanceWorkedTimeWorkedTimeBlocksItem:
    minutes: int
    time_type: AttendanceWorkedTimeWorkedTimeBlocksItemTimeType
    extra_hour: bool
    complementary_hour: bool
    raw_minutes_in_cents: int
    equivalent_minutes_in_cents: int
    pool_type: AttendanceWorkedTimeWorkedTimeBlocksItemPoolType
    date: str
    approved: bool
    workable: bool
    in_schedule: bool
    employee_id: str
    time_range_category_id: str | Unset = UNSET
    time_settings_break_configuration_id: str | Unset = UNSET
    time_range_category_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        minutes = self.minutes

        time_type = self.time_type.value

        extra_hour = self.extra_hour

        complementary_hour = self.complementary_hour

        raw_minutes_in_cents = self.raw_minutes_in_cents

        equivalent_minutes_in_cents = self.equivalent_minutes_in_cents

        pool_type = self.pool_type.value

        date = self.date

        approved = self.approved

        workable = self.workable

        in_schedule = self.in_schedule

        employee_id = self.employee_id

        time_range_category_id = self.time_range_category_id

        time_settings_break_configuration_id = self.time_settings_break_configuration_id

        time_range_category_name = self.time_range_category_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "minutes": minutes,
                "time_type": time_type,
                "extra_hour": extra_hour,
                "complementary_hour": complementary_hour,
                "raw_minutes_in_cents": raw_minutes_in_cents,
                "equivalent_minutes_in_cents": equivalent_minutes_in_cents,
                "pool_type": pool_type,
                "date": date,
                "approved": approved,
                "workable": workable,
                "in_schedule": in_schedule,
                "employee_id": employee_id,
            }
        )
        if time_range_category_id is not UNSET:
            field_dict["time_range_category_id"] = time_range_category_id
        if time_settings_break_configuration_id is not UNSET:
            field_dict["time_settings_break_configuration_id"] = (
                time_settings_break_configuration_id
            )
        if time_range_category_name is not UNSET:
            field_dict["time_range_category_name"] = time_range_category_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        minutes = d.pop("minutes")

        time_type = AttendanceWorkedTimeWorkedTimeBlocksItemTimeType(d.pop("time_type"))

        extra_hour = d.pop("extra_hour")

        complementary_hour = d.pop("complementary_hour")

        raw_minutes_in_cents = d.pop("raw_minutes_in_cents")

        equivalent_minutes_in_cents = d.pop("equivalent_minutes_in_cents")

        pool_type = AttendanceWorkedTimeWorkedTimeBlocksItemPoolType(d.pop("pool_type"))

        date = d.pop("date")

        approved = d.pop("approved")

        workable = d.pop("workable")

        in_schedule = d.pop("in_schedule")

        employee_id = d.pop("employee_id")

        time_range_category_id = d.pop("time_range_category_id", UNSET)

        time_settings_break_configuration_id = d.pop("time_settings_break_configuration_id", UNSET)

        time_range_category_name = d.pop("time_range_category_name", UNSET)

        attendance_worked_time_worked_time_blocks_item = cls(
            minutes=minutes,
            time_type=time_type,
            extra_hour=extra_hour,
            complementary_hour=complementary_hour,
            raw_minutes_in_cents=raw_minutes_in_cents,
            equivalent_minutes_in_cents=equivalent_minutes_in_cents,
            pool_type=pool_type,
            date=date,
            approved=approved,
            workable=workable,
            in_schedule=in_schedule,
            employee_id=employee_id,
            time_range_category_id=time_range_category_id,
            time_settings_break_configuration_id=time_settings_break_configuration_id,
            time_range_category_name=time_range_category_name,
        )

        attendance_worked_time_worked_time_blocks_item.additional_properties = d
        return attendance_worked_time_worked_time_blocks_item

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
