from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.compensations_concept_category import CompensationsConceptCategory
from ..models.compensations_concept_unit_type import CompensationsConceptUnitType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CompensationsConcept")


@_attrs_define
class CompensationsConcept:
    id: int
    """ The identifier of the concept """
    company_id: int
    """ The company identifier of the concept """
    default: bool
    """ Whether the concept is a default or a custom concept """
    description: str
    """ The description of the concept """
    label: str
    """ The label of the concept """
    name: str
    """ The name of the concept """
    translated_name: str
    """ The translated name of the concept if it is a default concept. """
    category: CompensationsConceptCategory | Unset = UNSET
    """ The category of the concept """
    unit_name: str | Unset = UNSET
    """ The name of the unit of the concept """
    unit_type: CompensationsConceptUnitType | Unset = UNSET
    """ The type of the unit of the concept """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        company_id = self.company_id

        default = self.default

        description = self.description

        label = self.label

        name = self.name

        translated_name = self.translated_name

        category: str | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.value

        unit_name = self.unit_name

        unit_type: str | Unset = UNSET
        if not isinstance(self.unit_type, Unset):
            unit_type = self.unit_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "company_id": company_id,
                "default": default,
                "description": description,
                "label": label,
                "name": name,
                "translated_name": translated_name,
            }
        )
        if category is not UNSET:
            field_dict["category"] = category
        if unit_name is not UNSET:
            field_dict["unit_name"] = unit_name
        if unit_type is not UNSET:
            field_dict["unit_type"] = unit_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        company_id = d.pop("company_id")

        default = d.pop("default")

        description = d.pop("description")

        label = d.pop("label")

        name = d.pop("name")

        translated_name = d.pop("translated_name")

        _category = d.pop("category", UNSET)
        category: CompensationsConceptCategory | Unset
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = CompensationsConceptCategory(_category) if _category is not None else None

        unit_name = d.pop("unit_name", UNSET)

        _unit_type = d.pop("unit_type", UNSET)
        unit_type: CompensationsConceptUnitType | Unset
        if isinstance(_unit_type, Unset):
            unit_type = UNSET
        else:
            unit_type = CompensationsConceptUnitType(_unit_type) if _unit_type is not None else None

        compensations_concept = cls(
            id=id,
            company_id=company_id,
            default=default,
            description=description,
            label=label,
            name=name,
            translated_name=translated_name,
            category=category,
            unit_name=unit_name,
            unit_type=unit_type,
        )

        compensations_concept.additional_properties = d
        return compensations_concept

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
