from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FinanceCategory")


@_attrs_define
class FinanceCategory:
    id: int
    """ Unique identifier for the category """
    label: str
    """ Custom label for the category """
    default_label: str
    """ Default translated label for the category """
    identifier: str
    """ System identifier for the category """
    visible: bool
    """ Whether the category is visible """
    enabled: bool
    """ Whether the category is enabled """
    parent_category_id: int | Unset = UNSET
    """ Parent category ID (null for main categories) """
    position: int | Unset = UNSET
    """ Display position of the category """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        label = self.label

        default_label = self.default_label

        identifier = self.identifier

        visible = self.visible

        enabled = self.enabled

        parent_category_id = self.parent_category_id

        position = self.position

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "label": label,
                "default_label": default_label,
                "identifier": identifier,
                "visible": visible,
                "enabled": enabled,
            }
        )
        if parent_category_id is not UNSET:
            field_dict["parent_category_id"] = parent_category_id
        if position is not UNSET:
            field_dict["position"] = position

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        label = d.pop("label")

        default_label = d.pop("default_label")

        identifier = d.pop("identifier")

        visible = d.pop("visible")

        enabled = d.pop("enabled")

        parent_category_id = d.pop("parent_category_id", UNSET)

        position = d.pop("position", UNSET)

        finance_category = cls(
            id=id,
            label=label,
            default_label=default_label,
            identifier=identifier,
            visible=visible,
            enabled=enabled,
            parent_category_id=parent_category_id,
            position=position,
        )

        finance_category.additional_properties = d
        return finance_category

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
