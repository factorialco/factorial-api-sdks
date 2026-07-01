from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.custom_fields_field_field_type import CustomFieldsFieldFieldType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomFieldsField")


@_attrs_define
class CustomFieldsField:
    id: str
    """ Field identifier """
    field_type: CustomFieldsFieldFieldType
    """ The type of the field's value """
    label_text: str
    """ Field label """
    position: int | Unset = UNSET
    """ Field position within employee profile """
    required: bool | Unset = UNSET
    """ Requirement to fill this field """
    min_value: int | Unset = UNSET
    """ Minimum value in range field type """
    max_value: int | Unset = UNSET
    """ Maximum value in range field type """
    legal_entity_name: str | Unset = UNSET
    """ Legal entity name where this field belongs """
    legal_entity_id: str | Unset = UNSET
    """ Legal entity id where this field belongs """
    slug: str | Unset = UNSET
    """ Custom field slug """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        field_type = self.field_type.value

        label_text = self.label_text

        position = self.position

        required = self.required

        min_value = self.min_value

        max_value = self.max_value

        legal_entity_name = self.legal_entity_name

        legal_entity_id = self.legal_entity_id

        slug = self.slug

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "field_type": field_type,
                "label_text": label_text,
            }
        )
        if position is not UNSET:
            field_dict["position"] = position
        if required is not UNSET:
            field_dict["required"] = required
        if min_value is not UNSET:
            field_dict["min_value"] = min_value
        if max_value is not UNSET:
            field_dict["max_value"] = max_value
        if legal_entity_name is not UNSET:
            field_dict["legal_entity_name"] = legal_entity_name
        if legal_entity_id is not UNSET:
            field_dict["legal_entity_id"] = legal_entity_id
        if slug is not UNSET:
            field_dict["slug"] = slug

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        field_type = CustomFieldsFieldFieldType(d.pop("field_type"))

        label_text = d.pop("label_text")

        position = d.pop("position", UNSET)

        required = d.pop("required", UNSET)

        min_value = d.pop("min_value", UNSET)

        max_value = d.pop("max_value", UNSET)

        legal_entity_name = d.pop("legal_entity_name", UNSET)

        legal_entity_id = d.pop("legal_entity_id", UNSET)

        slug = d.pop("slug", UNSET)

        custom_fields_field = cls(
            id=id,
            field_type=field_type,
            label_text=label_text,
            position=position,
            required=required,
            min_value=min_value,
            max_value=max_value,
            legal_entity_name=legal_entity_name,
            legal_entity_id=legal_entity_id,
            slug=slug,
        )

        custom_fields_field.additional_properties = d
        return custom_fields_field

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
