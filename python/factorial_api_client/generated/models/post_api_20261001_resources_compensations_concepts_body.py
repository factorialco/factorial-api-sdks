from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_api_20261001_resources_compensations_concepts_body_category import (
    PostApi20261001ResourcesCompensationsConceptsBodyCategory,
)
from ..models.post_api_20261001_resources_compensations_concepts_body_unit_type import (
    PostApi20261001ResourcesCompensationsConceptsBodyUnitType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20261001ResourcesCompensationsConceptsBody")


@_attrs_define
class PostApi20261001ResourcesCompensationsConceptsBody:
    category: PostApi20261001ResourcesCompensationsConceptsBodyCategory
    """ Concept category """
    company_id: str
    """ Company id that owns the concept """
    label: str
    """ Display label """
    description: str | Unset = UNSET
    """ Concept description """
    unit_type: PostApi20261001ResourcesCompensationsConceptsBodyUnitType | Unset = UNSET
    """ Unit type """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category = self.category.value

        company_id = self.company_id

        label = self.label

        description = self.description

        unit_type: str | Unset = UNSET
        if not isinstance(self.unit_type, Unset):
            unit_type = self.unit_type.value if self.unit_type is not None else None

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "category": category,
                "company_id": company_id,
                "label": label,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if unit_type is not UNSET:
            field_dict["unit_type"] = unit_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        category = PostApi20261001ResourcesCompensationsConceptsBodyCategory(d.pop("category"))

        company_id = d.pop("company_id")

        label = d.pop("label")

        description = d.pop("description", UNSET)

        _unit_type = d.pop("unit_type", UNSET)
        unit_type: PostApi20261001ResourcesCompensationsConceptsBodyUnitType | Unset
        if isinstance(_unit_type, Unset):
            unit_type = UNSET
        else:
            unit_type = PostApi20261001ResourcesCompensationsConceptsBodyUnitType(_unit_type) if _unit_type is not None else None

        post_api_20261001_resources_compensations_concepts_body = cls(
            category=category,
            company_id=company_id,
            label=label,
            description=description,
            unit_type=unit_type,
        )

        post_api_20261001_resources_compensations_concepts_body.additional_properties = d
        return post_api_20261001_resources_compensations_concepts_body

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
