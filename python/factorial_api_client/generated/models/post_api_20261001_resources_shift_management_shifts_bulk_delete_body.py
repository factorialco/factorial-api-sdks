from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20261001ResourcesShiftManagementShiftsBulkDeleteBody")


@_attrs_define
class PostApi20261001ResourcesShiftManagementShiftsBulkDeleteBody:
    author_id: str
    """ Identifier of the user/access who is performing the bulk delete operation. Used for audit purposes and
    tracking who deleted the shifts """
    ids: list[str] | Unset = UNSET
    """ Filter shifts by their unique identifiers. Deletes only shifts matching the provided IDs. If not provided,
    uses other filters to determine which shifts to delete """
    start_at: str | Unset = UNSET
    """ Filter shifts that end on or after this date. Only the date (calendar day) is used; the time part is ignored
    (treated as start of day, 00:00:00). Shifts are included if their end time is at or after the start of the
    specified day """
    end_at: str | Unset = UNSET
    """ Filter shifts that start before this date. Only the date (calendar day) is used; the time part is ignored
    (treated as end of day, 23:59:59). Shifts are included if their start time is before the end of the specified
    day """
    employee_ids: list[str] | Unset = UNSET
    """ Filter shifts by employee identifiers. Deletes only shifts assigned to the specified employees. Can be
    combined with start_at and end_at for precise bulk deletion """
    destroy_backup_shifts: bool | Unset = UNSET
    """ Also destroys shifts with status backup when true, which by default are being kept """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        author_id = self.author_id

        ids: list[str] | Unset = UNSET
        if not isinstance(self.ids, Unset):
            ids = self.ids

        start_at = self.start_at

        end_at = self.end_at

        employee_ids: list[str] | Unset = UNSET
        if not isinstance(self.employee_ids, Unset):
            employee_ids = self.employee_ids

        destroy_backup_shifts = self.destroy_backup_shifts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "author_id": author_id,
            }
        )
        if ids is not UNSET:
            field_dict["ids"] = ids
        if start_at is not UNSET:
            field_dict["start_at"] = start_at
        if end_at is not UNSET:
            field_dict["end_at"] = end_at
        if employee_ids is not UNSET:
            field_dict["employee_ids"] = employee_ids
        if destroy_backup_shifts is not UNSET:
            field_dict["destroy_backup_shifts"] = destroy_backup_shifts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        author_id = d.pop("author_id")

        ids = cast(list[str], d.pop("ids", UNSET))

        start_at = d.pop("start_at", UNSET)

        end_at = d.pop("end_at", UNSET)

        employee_ids = cast(list[str], d.pop("employee_ids", UNSET))

        destroy_backup_shifts = d.pop("destroy_backup_shifts", UNSET)

        post_api_20261001_resources_shift_management_shifts_bulk_delete_body = cls(
            author_id=author_id,
            ids=ids,
            start_at=start_at,
            end_at=end_at,
            employee_ids=employee_ids,
            destroy_backup_shifts=destroy_backup_shifts,
        )

        post_api_20261001_resources_shift_management_shifts_bulk_delete_body.additional_properties = d
        return post_api_20261001_resources_shift_management_shifts_bulk_delete_body

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
