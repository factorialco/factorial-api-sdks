from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20251001ResourcesShiftManagementShiftsBulkDeleteBody")


@_attrs_define
class PostApi20251001ResourcesShiftManagementShiftsBulkDeleteBody:
    author_id: int
    """ Access identifier of the author fo the bulk delete action """
    ids: list[int] | Unset = UNSET
    """ List of shift identifiers """
    start_at: str | Unset = UNSET
    """ Start date for the shift list """
    end_at: str | Unset = UNSET
    """ End date for the shift list """
    employee_ids: list[int] | Unset = UNSET
    """ Lsit of the employee identifiers """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        author_id = self.author_id

        ids: list[int] | Unset = UNSET
        if not isinstance(self.ids, Unset):
            ids = self.ids

        start_at = self.start_at

        end_at = self.end_at

        employee_ids: list[int] | Unset = UNSET
        if not isinstance(self.employee_ids, Unset):
            employee_ids = self.employee_ids

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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        author_id = d.pop("author_id")

        ids = cast(list[int], d.pop("ids", UNSET))

        start_at = d.pop("start_at", UNSET)

        end_at = d.pop("end_at", UNSET)

        employee_ids = cast(list[int], d.pop("employee_ids", UNSET))

        post_api_20251001_resources_shift_management_shifts_bulk_delete_body = cls(
            author_id=author_id,
            ids=ids,
            start_at=start_at,
            end_at=end_at,
            employee_ids=employee_ids,
        )

        post_api_20251001_resources_shift_management_shifts_bulk_delete_body.additional_properties = d
        return post_api_20251001_resources_shift_management_shifts_bulk_delete_body

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
