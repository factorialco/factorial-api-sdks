from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ats_hiring_stage_name import AtsHiringStageName

T = TypeVar("T", bound="AtsHiringStage")


@_attrs_define
class AtsHiringStage:
    id: str
    """ Identifier of the hiring stage """
    name: AtsHiringStageName
    """ Name of the hiring stage """
    label: str
    """ Label of the hiring stage """
    company_id: str
    """ Company identifier of the hiring stage """
    position: int
    """ Position of the hiring stage """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name.value

        label = self.label

        company_id = self.company_id

        position = self.position

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "label": label,
                "company_id": company_id,
                "position": position,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = AtsHiringStageName(d.pop("name"))

        label = d.pop("label")

        company_id = d.pop("company_id")

        position = d.pop("position")

        ats_hiring_stage = cls(
            id=id,
            name=name,
            label=label,
            company_id=company_id,
            position=position,
        )

        ats_hiring_stage.additional_properties = d
        return ats_hiring_stage

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
