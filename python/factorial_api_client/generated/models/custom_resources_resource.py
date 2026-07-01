from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CustomResourcesResource")


@_attrs_define
class CustomResourcesResource:
    id: str
    """ The id of the Resource """
    schema_id: str
    """ The id of the Schema this resource belongs to """
    attachable_type: str
    """ Attachable type (the type of the attachable) """
    attachable_id: str
    """ The id of the Attachable """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        schema_id = self.schema_id

        attachable_type = self.attachable_type

        attachable_id = self.attachable_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "schema_id": schema_id,
                "attachable_type": attachable_type,
                "attachable_id": attachable_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        schema_id = d.pop("schema_id")

        attachable_type = d.pop("attachable_type")

        attachable_id = d.pop("attachable_id")

        custom_resources_resource = cls(
            id=id,
            schema_id=schema_id,
            attachable_type=attachable_type,
            attachable_id=attachable_id,
        )

        custom_resources_resource.additional_properties = d
        return custom_resources_resource

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
