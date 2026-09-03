from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20261001ResourcesCustomFieldsOptionsBody")


@_attrs_define
class PostApi20261001ResourcesCustomFieldsOptionsBody:
    label: str
    """ Title for option """
    field_id: str
    """ Custom Fields identifier """
    is_active: bool | Unset = UNSET
    """ Flag to make the option available """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        label = self.label

        field_id = self.field_id

        is_active = self.is_active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "label": label,
                "field_id": field_id,
            }
        )
        if is_active is not UNSET:
            field_dict["is_active"] = is_active

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        label = d.pop("label")

        field_id = d.pop("field_id")

        is_active = d.pop("is_active", UNSET)

        post_api_20261001_resources_custom_fields_options_body = cls(
            label=label,
            field_id=field_id,
            is_active=is_active,
        )

        post_api_20261001_resources_custom_fields_options_body.additional_properties = d
        return post_api_20261001_resources_custom_fields_options_body

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
