from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PutApi20261001ResourcesTimeoffPoliciesIdBody")


@_attrs_define
class PutApi20261001ResourcesTimeoffPoliciesIdBody:
    id: str
    """ Id of the policy to update. """
    name: str | Unset = UNSET
    """ The name of the policy. """
    description: str | Unset = UNSET
    """ Policy description. """
    main: bool | Unset = UNSET
    """ If the policy is the main policy. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        main = self.main

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if main is not UNSET:
            field_dict["main"] = main

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        main = d.pop("main", UNSET)

        put_api_20261001_resources_timeoff_policies_id_body = cls(
            id=id,
            name=name,
            description=description,
            main=main,
        )

        put_api_20261001_resources_timeoff_policies_id_body.additional_properties = d
        return put_api_20261001_resources_timeoff_policies_id_body

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
