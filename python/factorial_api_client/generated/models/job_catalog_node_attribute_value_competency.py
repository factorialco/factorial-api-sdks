from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.job_catalog_node_attribute_value_competency_level import (
        JobCatalogNodeAttributeValueCompetencyLevel,
    )


T = TypeVar("T", bound="JobCatalogNodeAttributeValueCompetency")


@_attrs_define
class JobCatalogNodeAttributeValueCompetency:
    """Competency payload including name, short description and optional level metadata

    Example:
        {"name":"Design Fundamentals","description":"Core visual principles","level":{"id":1,"name":"Level
            1","description":"Understands basics"}}

    """

    name: str | Unset = UNSET
    description: str | Unset = UNSET
    level: JobCatalogNodeAttributeValueCompetencyLevel | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        level: dict[str, Any] | Unset = UNSET
        if not isinstance(self.level, Unset):
            level = self.level.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if level is not UNSET:
            field_dict["level"] = level

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.job_catalog_node_attribute_value_competency_level import (
            JobCatalogNodeAttributeValueCompetencyLevel,
        )

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _level = d.pop("level", UNSET)
        level: JobCatalogNodeAttributeValueCompetencyLevel | Unset
        if isinstance(_level, Unset):
            level = UNSET
        else:
            level = JobCatalogNodeAttributeValueCompetencyLevel.from_dict(_level)

        job_catalog_node_attribute_value_competency = cls(
            name=name,
            description=description,
            level=level,
        )

        job_catalog_node_attribute_value_competency.additional_properties = d
        return job_catalog_node_attribute_value_competency

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
