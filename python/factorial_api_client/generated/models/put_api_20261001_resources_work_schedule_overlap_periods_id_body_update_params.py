from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PutApi20261001ResourcesWorkScheduleOverlapPeriodsIdBodyUpdateParams")


@_attrs_define
class PutApi20261001ResourcesWorkScheduleOverlapPeriodsIdBodyUpdateParams:
    """Attributes to update on the overlap period (start/end day and month)

    Example:
        {'start_day': 15, 'start_month': 12, 'end_day': 31, 'end_month': 12}

    """

    start_day: int | Unset = UNSET
    start_month: int | Unset = UNSET
    end_day: int | Unset = UNSET
    end_month: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start_day = self.start_day

        start_month = self.start_month

        end_day = self.end_day

        end_month = self.end_month

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if start_day is not UNSET:
            field_dict["start_day"] = start_day
        if start_month is not UNSET:
            field_dict["start_month"] = start_month
        if end_day is not UNSET:
            field_dict["end_day"] = end_day
        if end_month is not UNSET:
            field_dict["end_month"] = end_month

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        start_day = d.pop("start_day", UNSET)

        start_month = d.pop("start_month", UNSET)

        end_day = d.pop("end_day", UNSET)

        end_month = d.pop("end_month", UNSET)

        put_api_20261001_resources_work_schedule_overlap_periods_id_body_update_params = cls(
            start_day=start_day,
            start_month=start_month,
            end_day=end_day,
            end_month=end_month,
        )

        put_api_20261001_resources_work_schedule_overlap_periods_id_body_update_params.additional_properties = d
        return put_api_20261001_resources_work_schedule_overlap_periods_id_body_update_params

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
