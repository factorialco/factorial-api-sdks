from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_api_20261001_resources_work_schedule_overlap_periods_body_create_params import (
        PostApi20261001ResourcesWorkScheduleOverlapPeriodsBodyCreateParams,
    )


T = TypeVar("T", bound="PostApi20261001ResourcesWorkScheduleOverlapPeriodsBody")


@_attrs_define
class PostApi20261001ResourcesWorkScheduleOverlapPeriodsBody:
    schedule_id: str
    """ Identifier of the schedule this overlap period belongs to """
    create_params: PostApi20261001ResourcesWorkScheduleOverlapPeriodsBodyCreateParams | Unset = (
        UNSET
    )
    """ Attributes for the new overlap period (default flag, start/end day and month, and schedule type) """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        schedule_id = self.schedule_id

        create_params: dict[str, Any] | Unset = UNSET
        if not isinstance(self.create_params, Unset):
            create_params = self.create_params.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "schedule_id": schedule_id,
            }
        )
        if create_params is not UNSET:
            field_dict["create_params"] = create_params

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_api_20261001_resources_work_schedule_overlap_periods_body_create_params import (
            PostApi20261001ResourcesWorkScheduleOverlapPeriodsBodyCreateParams,
        )

        d = dict(src_dict)
        schedule_id = d.pop("schedule_id")

        _create_params = d.pop("create_params", UNSET)
        create_params: PostApi20261001ResourcesWorkScheduleOverlapPeriodsBodyCreateParams | Unset
        if isinstance(_create_params, Unset):
            create_params = UNSET
        else:
            create_params = (
                PostApi20261001ResourcesWorkScheduleOverlapPeriodsBodyCreateParams.from_dict(
                    _create_params
                )
            )

        post_api_20261001_resources_work_schedule_overlap_periods_body = cls(
            schedule_id=schedule_id,
            create_params=create_params,
        )

        post_api_20261001_resources_work_schedule_overlap_periods_body.additional_properties = d
        return post_api_20261001_resources_work_schedule_overlap_periods_body

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
