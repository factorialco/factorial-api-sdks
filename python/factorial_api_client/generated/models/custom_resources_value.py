from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomResourcesValue")


@_attrs_define
class CustomResourcesValue:
    id: str
    """ Value identifier """
    resource_id: str
    """ The identifier of the resource that owns the resource value """
    attachable_id: str | Unset = UNSET
    """ The id of the attached resource like an employee """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        resource_id = self.resource_id

        attachable_id = self.attachable_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "resource_id": resource_id,
            }
        )
        if attachable_id is not UNSET:
            field_dict["attachable_id"] = attachable_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        resource_id = d.pop("resource_id")

        attachable_id = d.pop("attachable_id", UNSET)

        custom_resources_value = cls(
            id=id,
            resource_id=resource_id,
            attachable_id=attachable_id,
        )

        custom_resources_value.additional_properties = d
        return custom_resources_value

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
