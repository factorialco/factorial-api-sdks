from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomResourcesValue")


@_attrs_define
class CustomResourcesValue:
    id: int
    """ Value identifier """
    field_id: int
    """ Identifier of the field this value belongs to """
    long_text_value: str | Unset = UNSET
    """ When the field's type is long_text_value, value for schema long_text_value custom field """
    date_value: str | Unset = UNSET
    """ When the field's type is date_value, value for schema date_value custom field """
    text_value: str | Unset = UNSET
    """ When the field's type is text_value, value for schema text_value custom field """
    number_value: int | Unset = UNSET
    """ When the field's type is number_value, value for schema number_value custom field """
    option_value: str | Unset = UNSET
    """ When the field's type is option_value, selected value for schema option_value custom field """
    cents_value: int | Unset = UNSET
    """ When the field's type is cents_value, value for schema cents_value custom field """
    boolean_value: bool | Unset = UNSET
    """ When the field's type is boolean_value, value for schema boolean_value custom field """
    single_choice_value: str | Unset = UNSET
    """ When the field's type is single_choice_value, selected value for schema single_choice_value custom field """
    multiple_choice_value: list[str] | Unset = UNSET
    """ When the field's type is multiple_choice_value,selected values for schema multiple_choice_value custom field
    """
    attachable_id: int | Unset = UNSET
    """ The id of the attached resource like an employee """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        field_id = self.field_id

        long_text_value = self.long_text_value

        date_value = self.date_value

        text_value = self.text_value

        number_value = self.number_value

        option_value = self.option_value

        cents_value = self.cents_value

        boolean_value = self.boolean_value

        single_choice_value = self.single_choice_value

        multiple_choice_value: list[str] | Unset = UNSET
        if not isinstance(self.multiple_choice_value, Unset):
            multiple_choice_value = self.multiple_choice_value

        attachable_id = self.attachable_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "field_id": field_id,
            }
        )
        if long_text_value is not UNSET:
            field_dict["long_text_value"] = long_text_value
        if date_value is not UNSET:
            field_dict["date_value"] = date_value
        if text_value is not UNSET:
            field_dict["text_value"] = text_value
        if number_value is not UNSET:
            field_dict["number_value"] = number_value
        if option_value is not UNSET:
            field_dict["option_value"] = option_value
        if cents_value is not UNSET:
            field_dict["cents_value"] = cents_value
        if boolean_value is not UNSET:
            field_dict["boolean_value"] = boolean_value
        if single_choice_value is not UNSET:
            field_dict["single_choice_value"] = single_choice_value
        if multiple_choice_value is not UNSET:
            field_dict["multiple_choice_value"] = multiple_choice_value
        if attachable_id is not UNSET:
            field_dict["attachable_id"] = attachable_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        field_id = d.pop("field_id")

        long_text_value = d.pop("long_text_value", UNSET)

        date_value = d.pop("date_value", UNSET)

        text_value = d.pop("text_value", UNSET)

        number_value = d.pop("number_value", UNSET)

        option_value = d.pop("option_value", UNSET)

        cents_value = d.pop("cents_value", UNSET)

        boolean_value = d.pop("boolean_value", UNSET)

        single_choice_value = d.pop("single_choice_value", UNSET)

        multiple_choice_value = cast(list[str], d.pop("multiple_choice_value", UNSET))

        attachable_id = d.pop("attachable_id", UNSET)

        custom_resources_value = cls(
            id=id,
            field_id=field_id,
            long_text_value=long_text_value,
            date_value=date_value,
            text_value=text_value,
            number_value=number_value,
            option_value=option_value,
            cents_value=cents_value,
            boolean_value=boolean_value,
            single_choice_value=single_choice_value,
            multiple_choice_value=multiple_choice_value,
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
