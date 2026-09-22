from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_api_20261001_resources_custom_fields_fields_body_editable import (
    PostApi20261001ResourcesCustomFieldsFieldsBodyEditable,
)
from ..models.post_api_20261001_resources_custom_fields_fields_body_field_type import (
    PostApi20261001ResourcesCustomFieldsFieldsBodyFieldType,
)
from ..models.post_api_20261001_resources_custom_fields_fields_body_visible import (
    PostApi20261001ResourcesCustomFieldsFieldsBodyVisible,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20261001ResourcesCustomFieldsFieldsBody")


@_attrs_define
class PostApi20261001ResourcesCustomFieldsFieldsBody:
    company_id: str
    """ Company identifier where this field belongs """
    field_type: PostApi20261001ResourcesCustomFieldsFieldsBodyFieldType
    editable: PostApi20261001ResourcesCustomFieldsFieldsBodyEditable | Unset = UNSET
    """ Group of employees that can edit the field """
    visible: PostApi20261001ResourcesCustomFieldsFieldsBodyVisible | Unset = UNSET
    """ Group of employees that can see the field """
    label: str | Unset = UNSET
    """ Field label """
    min_value: int | Unset = UNSET
    """ Minimum value in range field type """
    max_value: int | Unset = UNSET
    """ Maximum value in range field type """
    required: bool | Unset = UNSET
    """ Requirement to fill this field """
    options: list[str] | Unset = UNSET
    """ Array of options """
    position: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company_id = self.company_id

        field_type = self.field_type.value

        editable: str | Unset = UNSET
        if not isinstance(self.editable, Unset):
            editable = self.editable.value if self.editable is not None else None

        visible: str | Unset = UNSET
        if not isinstance(self.visible, Unset):
            visible = self.visible.value if self.visible is not None else None

        label = self.label

        min_value = self.min_value

        max_value = self.max_value

        required = self.required

        options: list[str] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = self.options

        position = self.position

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "company_id": company_id,
                "field_type": field_type,
            }
        )
        if editable is not UNSET:
            field_dict["editable"] = editable
        if visible is not UNSET:
            field_dict["visible"] = visible
        if label is not UNSET:
            field_dict["label"] = label
        if min_value is not UNSET:
            field_dict["min_value"] = min_value
        if max_value is not UNSET:
            field_dict["max_value"] = max_value
        if required is not UNSET:
            field_dict["required"] = required
        if options is not UNSET:
            field_dict["options"] = options
        if position is not UNSET:
            field_dict["position"] = position

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        company_id = d.pop("company_id")

        field_type = PostApi20261001ResourcesCustomFieldsFieldsBodyFieldType(d.pop("field_type"))

        _editable = d.pop("editable", UNSET)
        editable: PostApi20261001ResourcesCustomFieldsFieldsBodyEditable | Unset
        if isinstance(_editable, Unset):
            editable = UNSET
        else:
            editable = PostApi20261001ResourcesCustomFieldsFieldsBodyEditable(_editable) if _editable is not None else None

        _visible = d.pop("visible", UNSET)
        visible: PostApi20261001ResourcesCustomFieldsFieldsBodyVisible | Unset
        if isinstance(_visible, Unset):
            visible = UNSET
        else:
            visible = PostApi20261001ResourcesCustomFieldsFieldsBodyVisible(_visible) if _visible is not None else None

        label = d.pop("label", UNSET)

        min_value = d.pop("min_value", UNSET)

        max_value = d.pop("max_value", UNSET)

        required = d.pop("required", UNSET)

        options = cast(list[str], d.pop("options", UNSET))

        position = d.pop("position", UNSET)

        post_api_20261001_resources_custom_fields_fields_body = cls(
            company_id=company_id,
            field_type=field_type,
            editable=editable,
            visible=visible,
            label=label,
            min_value=min_value,
            max_value=max_value,
            required=required,
            options=options,
            position=position,
        )

        post_api_20261001_resources_custom_fields_fields_body.additional_properties = d
        return post_api_20261001_resources_custom_fields_fields_body

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
