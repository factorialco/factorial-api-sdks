from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_api_20260701_resources_custom_fields_resource_fields_body_editable import (
    PostApi20260701ResourcesCustomFieldsResourceFieldsBodyEditable,
)
from ..models.post_api_20260701_resources_custom_fields_resource_fields_body_field_type import (
    PostApi20260701ResourcesCustomFieldsResourceFieldsBodyFieldType,
)
from ..models.post_api_20260701_resources_custom_fields_resource_fields_body_visible import (
    PostApi20260701ResourcesCustomFieldsResourceFieldsBodyVisible,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20260701ResourcesCustomFieldsResourceFieldsBody")


@_attrs_define
class PostApi20260701ResourcesCustomFieldsResourceFieldsBody:
    schema_id: str
    """ Schema identifier """
    company_id: str
    """ Company identifier """
    field_type: PostApi20260701ResourcesCustomFieldsResourceFieldsBodyFieldType
    """ Type of the value for the resource field """
    required: bool
    """ Requirement to fill this resource field """
    editable: PostApi20260701ResourcesCustomFieldsResourceFieldsBodyEditable
    """ Group for which this field is editable """
    visible: PostApi20260701ResourcesCustomFieldsResourceFieldsBodyVisible
    """ Group for which this field is visible """
    label: str | Unset = UNSET
    """ Resource field label """
    max_value: int | Unset = UNSET
    """ Maximum value for range field type """
    min_value: int | Unset = UNSET
    """ Minimum value for range field type """
    position: int | Unset = UNSET
    """ Field position within schema """
    options: list[str] | Unset = UNSET
    """ Array of options to choose from """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        schema_id = self.schema_id

        company_id = self.company_id

        field_type = self.field_type.value

        required = self.required

        editable = self.editable.value

        visible = self.visible.value

        label = self.label

        max_value = self.max_value

        min_value = self.min_value

        position = self.position

        options: list[str] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = self.options

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "schema_id": schema_id,
                "company_id": company_id,
                "field_type": field_type,
                "required": required,
                "editable": editable,
                "visible": visible,
            }
        )
        if label is not UNSET:
            field_dict["label"] = label
        if max_value is not UNSET:
            field_dict["max_value"] = max_value
        if min_value is not UNSET:
            field_dict["min_value"] = min_value
        if position is not UNSET:
            field_dict["position"] = position
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        schema_id = d.pop("schema_id")

        company_id = d.pop("company_id")

        field_type = PostApi20260701ResourcesCustomFieldsResourceFieldsBodyFieldType(
            d.pop("field_type")
        )

        required = d.pop("required")

        editable = PostApi20260701ResourcesCustomFieldsResourceFieldsBodyEditable(d.pop("editable"))

        visible = PostApi20260701ResourcesCustomFieldsResourceFieldsBodyVisible(d.pop("visible"))

        label = d.pop("label", UNSET)

        max_value = d.pop("max_value", UNSET)

        min_value = d.pop("min_value", UNSET)

        position = d.pop("position", UNSET)

        options = cast(list[str], d.pop("options", UNSET))

        post_api_20260701_resources_custom_fields_resource_fields_body = cls(
            schema_id=schema_id,
            company_id=company_id,
            field_type=field_type,
            required=required,
            editable=editable,
            visible=visible,
            label=label,
            max_value=max_value,
            min_value=min_value,
            position=position,
            options=options,
        )

        post_api_20260701_resources_custom_fields_resource_fields_body.additional_properties = d
        return post_api_20260701_resources_custom_fields_resource_fields_body

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
