from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="JobCatalogLevel")


@_attrs_define
class JobCatalogLevel:
    id: str
    """ identifier for the job catalog level. """
    role_id: str
    """ identifier for the job catalog role. """
    name: str
    """ Level name. """
    role_name: str
    """ Role name. """
    order: int
    """ Sort order of the level within its role (lower is more junior). """
    archived: bool
    """ Whether this level is archived. """
    is_default: bool
    """ Shows if the level is the default one. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        role_id = self.role_id

        name = self.name

        role_name = self.role_name

        order = self.order

        archived = self.archived

        is_default = self.is_default

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "role_id": role_id,
                "name": name,
                "role_name": role_name,
                "order": order,
                "archived": archived,
                "is_default": is_default,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        role_id = d.pop("role_id")

        name = d.pop("name")

        role_name = d.pop("role_name")

        order = d.pop("order")

        archived = d.pop("archived")

        is_default = d.pop("is_default")

        job_catalog_level = cls(
            id=id,
            role_id=role_id,
            name=name,
            role_name=role_name,
            order=order,
            archived=archived,
            is_default=is_default,
        )

        job_catalog_level.additional_properties = d
        return job_catalog_level

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
