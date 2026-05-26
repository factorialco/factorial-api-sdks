from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TimeoffPolicy")


@_attrs_define
class TimeoffPolicy:
    id: int
    """ The policy id. """
    name: str
    """ Policy name. """
    company_id: int
    """ The company id. """
    main: bool | Unset = UNSET
    """ Is the main policy? It will return true if it's the main policy if not it will return false. """
    description: str | Unset = UNSET
    """ The policy description. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        company_id = self.company_id

        main = self.main

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "company_id": company_id,
            }
        )
        if main is not UNSET:
            field_dict["main"] = main
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        company_id = d.pop("company_id")

        main = d.pop("main", UNSET)

        description = d.pop("description", UNSET)

        timeoff_policy = cls(
            id=id,
            name=name,
            company_id=company_id,
            main=main,
            description=description,
        )

        timeoff_policy.additional_properties = d
        return timeoff_policy

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
