from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostApi20261001ResourcesWorkScheduleOverlapPeriodsBodyCreateParams")


@_attrs_define
class PostApi20261001ResourcesWorkScheduleOverlapPeriodsBodyCreateParams:
    """Attributes for the new overlap period (default flag, start/end day and month, and schedule type)

    Example:
        {'default': False, 'start_day': 15, 'start_month': 12, 'end_day': 31, 'end_month': 12, 'schedule_type':
            'flexible'}

    """

    default: bool
    start_day: int
    start_month: int
    end_day: int
    end_month: int
    schedule_type: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        default = self.default

        start_day = self.start_day

        start_month = self.start_month

        end_day = self.end_day

        end_month = self.end_month

        schedule_type = self.schedule_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "default": default,
                "start_day": start_day,
                "start_month": start_month,
                "end_day": end_day,
                "end_month": end_month,
                "schedule_type": schedule_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        default = d.pop("default")

        start_day = d.pop("start_day")

        start_month = d.pop("start_month")

        end_day = d.pop("end_day")

        end_month = d.pop("end_month")

        schedule_type = d.pop("schedule_type")

        post_api_20261001_resources_work_schedule_overlap_periods_body_create_params = cls(
            default=default,
            start_day=start_day,
            start_month=start_month,
            end_day=end_day,
            end_month=end_month,
            schedule_type=schedule_type,
        )

        post_api_20261001_resources_work_schedule_overlap_periods_body_create_params.additional_properties = d
        return post_api_20261001_resources_work_schedule_overlap_periods_body_create_params

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
