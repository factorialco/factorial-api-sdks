from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PutApi20260701ResourcesWorkScheduleOverlapPeriodsIdBody")


@_attrs_define
class PutApi20260701ResourcesWorkScheduleOverlapPeriodsIdBody:
    author: str
    id: str
    update_params: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        author = self.author

        id = self.id

        update_params = self.update_params

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "author": author,
                "id": id,
                "update_params": update_params,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        author = d.pop("author")

        id = d.pop("id")

        update_params = d.pop("update_params")

        put_api_20260701_resources_work_schedule_overlap_periods_id_body = cls(
            author=author,
            id=id,
            update_params=update_params,
        )

        put_api_20260701_resources_work_schedule_overlap_periods_id_body.additional_properties = d
        return put_api_20260701_resources_work_schedule_overlap_periods_id_body

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
