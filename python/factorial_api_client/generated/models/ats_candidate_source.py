from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ats_candidate_source_category import AtsCandidateSourceCategory

T = TypeVar("T", bound="AtsCandidateSource")


@_attrs_define
class AtsCandidateSource:
    id: int
    """ identifier of the source. """
    company_id: int
    """ identifier of the company. """
    category: AtsCandidateSourceCategory
    """ category of the source. """
    name: str
    """ name of the source. """
    label: str
    """ Translated label of the source if it is a default one, or name otherwise """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        company_id = self.company_id

        category = self.category.value

        name = self.name

        label = self.label

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "company_id": company_id,
                "category": category,
                "name": name,
                "label": label,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        company_id = d.pop("company_id")

        category = AtsCandidateSourceCategory(d.pop("category"))

        name = d.pop("name")

        label = d.pop("label")

        ats_candidate_source = cls(
            id=id,
            company_id=company_id,
            category=category,
            name=name,
            label=label,
        )

        ats_candidate_source.additional_properties = d
        return ats_candidate_source

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
