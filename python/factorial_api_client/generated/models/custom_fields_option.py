from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomFieldsOption")


@_attrs_define
class CustomFieldsOption:
    id: str
    """ Option identifier """
    label: str | Unset = UNSET
    """ Title for option """
    value: str | Unset = UNSET
    """ Option value """
    is_active: bool | Unset = UNSET
    """ Flag to make the option available """
    field_id: str | Unset = UNSET
    """ Custom Fields identifier """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        label = self.label

        value = self.value

        is_active = self.is_active

        field_id = self.field_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if label is not UNSET:
            field_dict["label"] = label
        if value is not UNSET:
            field_dict["value"] = value
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if field_id is not UNSET:
            field_dict["field_id"] = field_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        label = d.pop("label", UNSET)

        value = d.pop("value", UNSET)

        is_active = d.pop("is_active", UNSET)

        field_id = d.pop("field_id", UNSET)

        custom_fields_option = cls(
            id=id,
            label=label,
            value=value,
            is_active=is_active,
            field_id=field_id,
        )

        custom_fields_option.additional_properties = d
        return custom_fields_option

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
