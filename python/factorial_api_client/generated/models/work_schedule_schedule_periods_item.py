from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WorkScheduleSchedulePeriodsItem")


@_attrs_define
class WorkScheduleSchedulePeriodsItem:
    id: str
    default: bool
    schedule_id: str
    start_month: int
    start_day: int
    end_month: int
    end_day: int
    start_date: str
    end_date: str
    schedule_type: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        default = self.default

        schedule_id = self.schedule_id

        start_month = self.start_month

        start_day = self.start_day

        end_month = self.end_month

        end_day = self.end_day

        start_date = self.start_date

        end_date = self.end_date

        schedule_type = self.schedule_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "default": default,
                "schedule_id": schedule_id,
                "start_month": start_month,
                "start_day": start_day,
                "end_month": end_month,
                "end_day": end_day,
                "start_date": start_date,
                "end_date": end_date,
                "schedule_type": schedule_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        default = d.pop("default")

        schedule_id = d.pop("schedule_id")

        start_month = d.pop("start_month")

        start_day = d.pop("start_day")

        end_month = d.pop("end_month")

        end_day = d.pop("end_day")

        start_date = d.pop("start_date")

        end_date = d.pop("end_date")

        schedule_type = d.pop("schedule_type")

        work_schedule_schedule_periods_item = cls(
            id=id,
            default=default,
            schedule_id=schedule_id,
            start_month=start_month,
            start_day=start_day,
            end_month=end_month,
            end_day=end_day,
            start_date=start_date,
            end_date=end_date,
            schedule_type=schedule_type,
        )

        work_schedule_schedule_periods_item.additional_properties = d
        return work_schedule_schedule_periods_item

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
