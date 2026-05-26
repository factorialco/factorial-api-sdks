from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomFieldsValue")


@_attrs_define
class CustomFieldsValue:
    id: int
    """ Unique identifier for the custom field value """
    custom_field_identifier: str
    """ The unique identifier of the custom field """
    valuable_id: int
    """ The identifier of the object that owns this custom field value """
    field_id: int
    """ The identifier of the custom field """
    valuable_type: str
    """ The type of the object that owns this custom field value """
    value: str | Unset = UNSET
    """ Custom Fields value """
    long_text_value: str | Unset = UNSET
    """ Custom field text value """
    date_value: str | Unset = UNSET
    """ Custom field date value """
    single_choice_value: str | Unset = UNSET
    """ Custom field single choice value """
    cents_value: int | Unset = UNSET
    """ Custom field number value """
    label: str | Unset = UNSET
    """ The label of the custom field """
    required: bool | Unset = UNSET
    """ Whether the custom field is required """
    usage_group_id: int | Unset = UNSET
    """ The identifier of the usage group """
    usage_group_slug: str | Unset = UNSET
    """ The slug of the usage group """
    updated_at: str | Unset = UNSET
    """ The date and time the custom field value was last updated. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        custom_field_identifier = self.custom_field_identifier

        valuable_id = self.valuable_id

        field_id = self.field_id

        valuable_type = self.valuable_type

        value = self.value

        long_text_value = self.long_text_value

        date_value = self.date_value

        single_choice_value = self.single_choice_value

        cents_value = self.cents_value

        label = self.label

        required = self.required

        usage_group_id = self.usage_group_id

        usage_group_slug = self.usage_group_slug

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "custom_field_identifier": custom_field_identifier,
                "valuable_id": valuable_id,
                "field_id": field_id,
                "valuable_type": valuable_type,
            }
        )
        if value is not UNSET:
            field_dict["value"] = value
        if long_text_value is not UNSET:
            field_dict["long_text_value"] = long_text_value
        if date_value is not UNSET:
            field_dict["date_value"] = date_value
        if single_choice_value is not UNSET:
            field_dict["single_choice_value"] = single_choice_value
        if cents_value is not UNSET:
            field_dict["cents_value"] = cents_value
        if label is not UNSET:
            field_dict["label"] = label
        if required is not UNSET:
            field_dict["required"] = required
        if usage_group_id is not UNSET:
            field_dict["usage_group_id"] = usage_group_id
        if usage_group_slug is not UNSET:
            field_dict["usage_group_slug"] = usage_group_slug
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        custom_field_identifier = d.pop("custom_field_identifier")

        valuable_id = d.pop("valuable_id")

        field_id = d.pop("field_id")

        valuable_type = d.pop("valuable_type")

        value = d.pop("value", UNSET)

        long_text_value = d.pop("long_text_value", UNSET)

        date_value = d.pop("date_value", UNSET)

        single_choice_value = d.pop("single_choice_value", UNSET)

        cents_value = d.pop("cents_value", UNSET)

        label = d.pop("label", UNSET)

        required = d.pop("required", UNSET)

        usage_group_id = d.pop("usage_group_id", UNSET)

        usage_group_slug = d.pop("usage_group_slug", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        custom_fields_value = cls(
            id=id,
            custom_field_identifier=custom_field_identifier,
            valuable_id=valuable_id,
            field_id=field_id,
            valuable_type=valuable_type,
            value=value,
            long_text_value=long_text_value,
            date_value=date_value,
            single_choice_value=single_choice_value,
            cents_value=cents_value,
            label=label,
            required=required,
            usage_group_id=usage_group_id,
            usage_group_slug=usage_group_slug,
            updated_at=updated_at,
        )

        custom_fields_value.additional_properties = d
        return custom_fields_value

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
