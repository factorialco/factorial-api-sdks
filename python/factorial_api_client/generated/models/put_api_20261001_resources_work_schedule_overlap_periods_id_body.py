from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.put_api_20261001_resources_work_schedule_overlap_periods_id_body_update_params import (
        PutApi20261001ResourcesWorkScheduleOverlapPeriodsIdBodyUpdateParams,
    )


T = TypeVar("T", bound="PutApi20261001ResourcesWorkScheduleOverlapPeriodsIdBody")


@_attrs_define
class PutApi20261001ResourcesWorkScheduleOverlapPeriodsIdBody:
    id: str
    """ Identifier of the overlap period to update """
    update_params: PutApi20261001ResourcesWorkScheduleOverlapPeriodsIdBodyUpdateParams | Unset = (
        UNSET
    )
    """ Attributes to update on the overlap period (start/end day and month) """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        update_params: dict[str, Any] | Unset = UNSET
        if not isinstance(self.update_params, Unset):
            update_params = self.update_params.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if update_params is not UNSET:
            field_dict["update_params"] = update_params

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.put_api_20261001_resources_work_schedule_overlap_periods_id_body_update_params import (
            PutApi20261001ResourcesWorkScheduleOverlapPeriodsIdBodyUpdateParams,
        )

        d = dict(src_dict)
        id = d.pop("id")

        _update_params = d.pop("update_params", UNSET)
        update_params: PutApi20261001ResourcesWorkScheduleOverlapPeriodsIdBodyUpdateParams | Unset
        if isinstance(_update_params, Unset):
            update_params = UNSET
        else:
            update_params = (
                PutApi20261001ResourcesWorkScheduleOverlapPeriodsIdBodyUpdateParams.from_dict(
                    _update_params
                )
            )

        put_api_20261001_resources_work_schedule_overlap_periods_id_body = cls(
            id=id,
            update_params=update_params,
        )

        put_api_20261001_resources_work_schedule_overlap_periods_id_body.additional_properties = d
        return put_api_20261001_resources_work_schedule_overlap_periods_id_body

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
