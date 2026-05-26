from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostApi20251001ResourcesCustomResourcesValuesBody")


@_attrs_define
class PostApi20251001ResourcesCustomResourcesValuesBody:
    schema_id: int
    """ Identifier of the schema this value belongs to """
    employee_id: int
    field_id: int
    """ Identifier of the field this value belongs to """
    value: str
    """ Value for schema custom field """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        schema_id = self.schema_id

        employee_id = self.employee_id

        field_id = self.field_id

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "schema_id": schema_id,
                "employee_id": employee_id,
                "field_id": field_id,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        schema_id = d.pop("schema_id")

        employee_id = d.pop("employee_id")

        field_id = d.pop("field_id")

        value = d.pop("value")

        post_api_20251001_resources_custom_resources_values_body = cls(
            schema_id=schema_id,
            employee_id=employee_id,
            field_id=field_id,
            value=value,
        )

        post_api_20251001_resources_custom_resources_values_body.additional_properties = d
        return post_api_20251001_resources_custom_resources_values_body

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
