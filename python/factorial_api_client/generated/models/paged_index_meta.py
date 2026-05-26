from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PagedIndexMeta")


@_attrs_define
class PagedIndexMeta:
    has_previous_page: bool
    has_next_page: bool
    limit: int
    total: int
    start_cursor: str | Unset = UNSET
    end_cursor: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        has_previous_page = self.has_previous_page

        has_next_page = self.has_next_page

        limit = self.limit

        total = self.total

        start_cursor = self.start_cursor

        end_cursor = self.end_cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "has_previous_page": has_previous_page,
                "has_next_page": has_next_page,
                "limit": limit,
                "total": total,
            }
        )
        if start_cursor is not UNSET:
            field_dict["start_cursor"] = start_cursor
        if end_cursor is not UNSET:
            field_dict["end_cursor"] = end_cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        has_previous_page = d.pop("has_previous_page")

        has_next_page = d.pop("has_next_page")

        limit = d.pop("limit")

        total = d.pop("total")

        start_cursor = d.pop("start_cursor", UNSET)

        end_cursor = d.pop("end_cursor", UNSET)

        paged_index_meta = cls(
            has_previous_page=has_previous_page,
            has_next_page=has_next_page,
            limit=limit,
            total=total,
            start_cursor=start_cursor,
            end_cursor=end_cursor,
        )

        paged_index_meta.additional_properties = d
        return paged_index_meta

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
