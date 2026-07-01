from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20260701ResourcesShiftManagementShiftsBulkCreateBody")


@_attrs_define
class PostApi20260701ResourcesShiftManagementShiftsBulkCreateBody:
    shifts: list[Any]
    """ Array of shift objects to create. Each shift object represents a scheduled work period for an employee """
    planned_breaks: list[Any] | Unset = UNSET
    """ An array of planned breaks to be added to the shifts created. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        shifts = self.shifts

        planned_breaks: list[Any] | Unset = UNSET
        if not isinstance(self.planned_breaks, Unset):
            planned_breaks = self.planned_breaks

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "shifts": shifts,
            }
        )
        if planned_breaks is not UNSET:
            field_dict["planned_breaks"] = planned_breaks

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        shifts = cast(list[Any], d.pop("shifts"))

        planned_breaks = cast(list[Any], d.pop("planned_breaks", UNSET))

        post_api_20260701_resources_shift_management_shifts_bulk_create_body = cls(
            shifts=shifts,
            planned_breaks=planned_breaks,
        )

        post_api_20260701_resources_shift_management_shifts_bulk_create_body.additional_properties = d
        return post_api_20260701_resources_shift_management_shifts_bulk_create_body

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
