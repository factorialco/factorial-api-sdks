from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkScheduleDayConfiguration")


@_attrs_define
class WorkScheduleDayConfiguration:
    id: int
    overlap_period_id: int
    weekday: str
    duration_in_seconds: int
    start_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        overlap_period_id = self.overlap_period_id

        weekday = self.weekday

        duration_in_seconds = self.duration_in_seconds

        start_at = self.start_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "overlap_period_id": overlap_period_id,
                "weekday": weekday,
                "duration_in_seconds": duration_in_seconds,
            }
        )
        if start_at is not UNSET:
            field_dict["start_at"] = start_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        overlap_period_id = d.pop("overlap_period_id")

        weekday = d.pop("weekday")

        duration_in_seconds = d.pop("duration_in_seconds")

        start_at = d.pop("start_at", UNSET)

        work_schedule_day_configuration = cls(
            id=id,
            overlap_period_id=overlap_period_id,
            weekday=weekday,
            duration_in_seconds=duration_in_seconds,
            start_at=start_at,
        )

        work_schedule_day_configuration.additional_properties = d
        return work_schedule_day_configuration

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
