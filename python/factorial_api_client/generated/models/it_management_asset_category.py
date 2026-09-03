from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ItManagementAssetCategory")


@_attrs_define
class ItManagementAssetCategory:
    id: str
    """ Asset category identifier """
    key: str
    """ Unique catalog key (e.g. 'it', 'it.laptop') """
    name: str
    """ Human-readable name """
    created_at: str
    updated_at: str
    parent_id: str | Unset = UNSET
    """ Parent category identifier. NULL for top-level groups. """
    position: int | Unset = UNSET
    """ Display order within its parent """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        key = self.key

        name = self.name

        created_at = self.created_at

        updated_at = self.updated_at

        parent_id = self.parent_id

        position = self.position

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "key": key,
                "name": name,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if parent_id is not UNSET:
            field_dict["parent_id"] = parent_id
        if position is not UNSET:
            field_dict["position"] = position

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        key = d.pop("key")

        name = d.pop("name")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        parent_id = d.pop("parent_id", UNSET)

        position = d.pop("position", UNSET)

        it_management_asset_category = cls(
            id=id,
            key=key,
            name=name,
            created_at=created_at,
            updated_at=updated_at,
            parent_id=parent_id,
            position=position,
        )

        it_management_asset_category.additional_properties = d
        return it_management_asset_category

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
