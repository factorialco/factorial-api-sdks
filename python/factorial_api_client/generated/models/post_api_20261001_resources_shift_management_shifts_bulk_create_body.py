from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_api_20261001_resources_shift_management_shifts_bulk_create_body_planned_breaks_item import (
        PostApi20261001ResourcesShiftManagementShiftsBulkCreateBodyPlannedBreaksItem,
    )
    from ..models.post_api_20261001_resources_shift_management_shifts_bulk_create_body_shifts_item import (
        PostApi20261001ResourcesShiftManagementShiftsBulkCreateBodyShiftsItem,
    )


T = TypeVar("T", bound="PostApi20261001ResourcesShiftManagementShiftsBulkCreateBody")


@_attrs_define
class PostApi20261001ResourcesShiftManagementShiftsBulkCreateBody:
    shifts: list[PostApi20261001ResourcesShiftManagementShiftsBulkCreateBodyShiftsItem]
    """ Array of shift objects to create. Each shift object represents a scheduled work period for an employee """
    planned_breaks: (
        list[PostApi20261001ResourcesShiftManagementShiftsBulkCreateBodyPlannedBreaksItem] | Unset
    ) = UNSET
    """ An array of planned breaks to be added to the shifts created. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        shifts = []
        for shifts_item_data in self.shifts:
            shifts_item = shifts_item_data.to_dict()
            shifts.append(shifts_item)

        planned_breaks: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.planned_breaks, Unset):
            planned_breaks = []
            for planned_breaks_item_data in self.planned_breaks:
                planned_breaks_item = planned_breaks_item_data.to_dict()
                planned_breaks.append(planned_breaks_item)

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
        from ..models.post_api_20261001_resources_shift_management_shifts_bulk_create_body_planned_breaks_item import (
            PostApi20261001ResourcesShiftManagementShiftsBulkCreateBodyPlannedBreaksItem,
        )
        from ..models.post_api_20261001_resources_shift_management_shifts_bulk_create_body_shifts_item import (
            PostApi20261001ResourcesShiftManagementShiftsBulkCreateBodyShiftsItem,
        )

        d = dict(src_dict)
        shifts = []
        _shifts = d.pop("shifts")
        for shifts_item_data in _shifts:
            shifts_item = (
                PostApi20261001ResourcesShiftManagementShiftsBulkCreateBodyShiftsItem.from_dict(
                    shifts_item_data
                )
            )

            shifts.append(shifts_item)

        _planned_breaks = d.pop("planned_breaks", UNSET)
        planned_breaks: (
            list[PostApi20261001ResourcesShiftManagementShiftsBulkCreateBodyPlannedBreaksItem]
            | Unset
        ) = UNSET
        if _planned_breaks is not UNSET:
            planned_breaks = []
            for planned_breaks_item_data in _planned_breaks:
                planned_breaks_item = PostApi20261001ResourcesShiftManagementShiftsBulkCreateBodyPlannedBreaksItem.from_dict(
                    planned_breaks_item_data
                )

                planned_breaks.append(planned_breaks_item)

        post_api_20261001_resources_shift_management_shifts_bulk_create_body = cls(
            shifts=shifts,
            planned_breaks=planned_breaks,
        )

        post_api_20261001_resources_shift_management_shifts_bulk_create_body.additional_properties = d
        return post_api_20261001_resources_shift_management_shifts_bulk_create_body

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
