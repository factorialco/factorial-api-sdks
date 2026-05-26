from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PutApi20260401ResourcesTimeSettingsBreakConfigurationsIdBody")


@_attrs_define
class PutApi20260401ResourcesTimeSettingsBreakConfigurationsIdBody:
    id: int
    name: str | Unset = UNSET
    paid: bool | Unset = UNSET
    archived: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        paid = self.paid

        archived = self.archived

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if paid is not UNSET:
            field_dict["paid"] = paid
        if archived is not UNSET:
            field_dict["archived"] = archived

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name", UNSET)

        paid = d.pop("paid", UNSET)

        archived = d.pop("archived", UNSET)

        put_api_20260401_resources_time_settings_break_configurations_id_body = cls(
            id=id,
            name=name,
            paid=paid,
            archived=archived,
        )

        put_api_20260401_resources_time_settings_break_configurations_id_body.additional_properties = d
        return put_api_20260401_resources_time_settings_break_configurations_id_body

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
