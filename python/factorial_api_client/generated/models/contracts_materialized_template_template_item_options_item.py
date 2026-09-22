from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ContractsMaterializedTemplateTemplateItemOptionsItem")


@_attrs_define
class ContractsMaterializedTemplateTemplateItemOptionsItem:
    id: str
    option_id: str
    fragment_id: str
    label: str
    default: bool
    raw_label: str | Unset = UNSET
    translation_string: str | Unset = UNSET
    archived_at: str | Unset = UNSET
    integration_source: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        option_id = self.option_id

        fragment_id = self.fragment_id

        label = self.label

        default = self.default

        raw_label = self.raw_label

        translation_string = self.translation_string

        archived_at = self.archived_at

        integration_source = self.integration_source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "option_id": option_id,
                "fragment_id": fragment_id,
                "label": label,
                "default": default,
            }
        )
        if raw_label is not UNSET:
            field_dict["raw_label"] = raw_label
        if translation_string is not UNSET:
            field_dict["translation_string"] = translation_string
        if archived_at is not UNSET:
            field_dict["archived_at"] = archived_at
        if integration_source is not UNSET:
            field_dict["integration_source"] = integration_source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        option_id = d.pop("option_id")

        fragment_id = d.pop("fragment_id")

        label = d.pop("label")

        default = d.pop("default")

        raw_label = d.pop("raw_label", UNSET)

        translation_string = d.pop("translation_string", UNSET)

        archived_at = d.pop("archived_at", UNSET)

        integration_source = d.pop("integration_source", UNSET)

        contracts_materialized_template_template_item_options_item = cls(
            id=id,
            option_id=option_id,
            fragment_id=fragment_id,
            label=label,
            default=default,
            raw_label=raw_label,
            translation_string=translation_string,
            archived_at=archived_at,
            integration_source=integration_source,
        )

        contracts_materialized_template_template_item_options_item.additional_properties = d
        return contracts_materialized_template_template_item_options_item

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
