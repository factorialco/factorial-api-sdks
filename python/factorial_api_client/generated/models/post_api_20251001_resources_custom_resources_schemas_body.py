from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20251001ResourcesCustomResourcesSchemasBody")


@_attrs_define
class PostApi20251001ResourcesCustomResourcesSchemasBody:
    name: str
    """ Schema name """
    company_id: int
    """ Company identifier where this schema belongs """
    hidden: bool
    """ Manages visibility of the schema """
    effective_at_id: int | Unset = UNSET
    """ Custom field identifier """
    position: int | Unset = UNSET
    """ Schema position within employee profile """
    usage_group_slug: str | Unset = UNSET
    """ Schema slug """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        company_id = self.company_id

        hidden = self.hidden

        effective_at_id = self.effective_at_id

        position = self.position

        usage_group_slug = self.usage_group_slug

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "company_id": company_id,
                "hidden": hidden,
            }
        )
        if effective_at_id is not UNSET:
            field_dict["effective_at_id"] = effective_at_id
        if position is not UNSET:
            field_dict["position"] = position
        if usage_group_slug is not UNSET:
            field_dict["usage_group_slug"] = usage_group_slug

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        company_id = d.pop("company_id")

        hidden = d.pop("hidden")

        effective_at_id = d.pop("effective_at_id", UNSET)

        position = d.pop("position", UNSET)

        usage_group_slug = d.pop("usage_group_slug", UNSET)

        post_api_20251001_resources_custom_resources_schemas_body = cls(
            name=name,
            company_id=company_id,
            hidden=hidden,
            effective_at_id=effective_at_id,
            position=position,
            usage_group_slug=usage_group_slug,
        )

        post_api_20251001_resources_custom_resources_schemas_body.additional_properties = d
        return post_api_20251001_resources_custom_resources_schemas_body

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
