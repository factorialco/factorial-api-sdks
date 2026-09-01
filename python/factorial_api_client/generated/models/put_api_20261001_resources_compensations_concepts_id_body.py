from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.put_api_20261001_resources_compensations_concepts_id_body_category import (
    PutApi20261001ResourcesCompensationsConceptsIdBodyCategory,
)
from ..models.put_api_20261001_resources_compensations_concepts_id_body_unit_type import (
    PutApi20261001ResourcesCompensationsConceptsIdBodyUnitType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PutApi20261001ResourcesCompensationsConceptsIdBody")


@_attrs_define
class PutApi20261001ResourcesCompensationsConceptsIdBody:
    id: str
    """ The identifier of the concept to update """
    category: PutApi20261001ResourcesCompensationsConceptsIdBodyCategory | Unset = UNSET
    """ Concept category (custom concepts only) """
    description: str | Unset = UNSET
    """ Concept description (custom concepts only) """
    label: str | Unset = UNSET
    """ Display label (custom concepts only) """
    unit_type: PutApi20261001ResourcesCompensationsConceptsIdBodyUnitType | Unset = UNSET
    """ Unit type (custom concepts only) """
    labor_cost: bool | Unset = UNSET
    """ Marks the concept as labor cost (custom concepts only) """
    enabled: bool | Unset = UNSET
    """ Activates / deactivates the concept (default and custom concepts) """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        category: str | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.value if self.category is not None else None

        description = self.description

        label = self.label

        unit_type: str | Unset = UNSET
        if not isinstance(self.unit_type, Unset):
            unit_type = self.unit_type.value if self.unit_type is not None else None

        labor_cost = self.labor_cost

        enabled = self.enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if category is not UNSET:
            field_dict["category"] = category
        if description is not UNSET:
            field_dict["description"] = description
        if label is not UNSET:
            field_dict["label"] = label
        if unit_type is not UNSET:
            field_dict["unit_type"] = unit_type
        if labor_cost is not UNSET:
            field_dict["labor_cost"] = labor_cost
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        _category = d.pop("category", UNSET)
        category: PutApi20261001ResourcesCompensationsConceptsIdBodyCategory | Unset
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = PutApi20261001ResourcesCompensationsConceptsIdBodyCategory(_category) if _category is not None else None

        description = d.pop("description", UNSET)

        label = d.pop("label", UNSET)

        _unit_type = d.pop("unit_type", UNSET)
        unit_type: PutApi20261001ResourcesCompensationsConceptsIdBodyUnitType | Unset
        if isinstance(_unit_type, Unset):
            unit_type = UNSET
        else:
            unit_type = PutApi20261001ResourcesCompensationsConceptsIdBodyUnitType(_unit_type) if _unit_type is not None else None

        labor_cost = d.pop("labor_cost", UNSET)

        enabled = d.pop("enabled", UNSET)

        put_api_20261001_resources_compensations_concepts_id_body = cls(
            id=id,
            category=category,
            description=description,
            label=label,
            unit_type=unit_type,
            labor_cost=labor_cost,
            enabled=enabled,
        )

        put_api_20261001_resources_compensations_concepts_id_body.additional_properties = d
        return put_api_20261001_resources_compensations_concepts_id_body

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
