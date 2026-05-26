from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostApi20251001ResourcesTimeoffAllowancesDeleteWithAltAllowanceBody")


@_attrs_define
class PostApi20251001ResourcesTimeoffAllowancesDeleteWithAltAllowanceBody:
    id: int
    alt_allowance_id: int
    """ Allowance id sent to migrate existing incidences from the deleted allowance to the alternative allowance """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        alt_allowance_id = self.alt_allowance_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "alt_allowance_id": alt_allowance_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        alt_allowance_id = d.pop("alt_allowance_id")

        post_api_20251001_resources_timeoff_allowances_delete_with_alt_allowance_body = cls(
            id=id,
            alt_allowance_id=alt_allowance_id,
        )

        post_api_20251001_resources_timeoff_allowances_delete_with_alt_allowance_body.additional_properties = d
        return post_api_20251001_resources_timeoff_allowances_delete_with_alt_allowance_body

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
