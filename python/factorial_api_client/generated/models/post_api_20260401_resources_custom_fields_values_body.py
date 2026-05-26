from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostApi20260401ResourcesCustomFieldsValuesBody")


@_attrs_define
class PostApi20260401ResourcesCustomFieldsValuesBody:
    field_id: int
    """ Custom Fields identifier """
    valuable_type: str
    """ Type of the object that the custom field is attached to: 'Document' | 'Employee' |
    'Contracts::ContractVersion' | 'CustomResources::Value'  """
    valuable_id: int
    """ Identifier of the object that the custom field is attached to """
    value: str
    """ Custom Fields value """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_id = self.field_id

        valuable_type = self.valuable_type

        valuable_id = self.valuable_id

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "field_id": field_id,
                "valuable_type": valuable_type,
                "valuable_id": valuable_id,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_id = d.pop("field_id")

        valuable_type = d.pop("valuable_type")

        valuable_id = d.pop("valuable_id")

        value = d.pop("value")

        post_api_20260401_resources_custom_fields_values_body = cls(
            field_id=field_id,
            valuable_type=valuable_type,
            valuable_id=valuable_id,
            value=value,
        )

        post_api_20260401_resources_custom_fields_values_body.additional_properties = d
        return post_api_20260401_resources_custom_fields_values_body

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
