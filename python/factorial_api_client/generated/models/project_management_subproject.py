from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectManagementSubproject")


@_attrs_define
class ProjectManagementSubproject:
    name: str
    """ The name of the subproject """
    project_id: int
    """ The id of the project """
    id: int | Unset = UNSET
    """ The id of the subproject """
    inputed_minutes: int | Unset = UNSET
    """ The total minutes tracked in the subproject (if requested) """
    labor_cost_cents: int | Unset = UNSET
    """ The total labor cost of the subproject in cents (if requested) """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        project_id = self.project_id

        id = self.id

        inputed_minutes = self.inputed_minutes

        labor_cost_cents = self.labor_cost_cents

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "project_id": project_id,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if inputed_minutes is not UNSET:
            field_dict["inputed_minutes"] = inputed_minutes
        if labor_cost_cents is not UNSET:
            field_dict["labor_cost_cents"] = labor_cost_cents

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        project_id = d.pop("project_id")

        id = d.pop("id", UNSET)

        inputed_minutes = d.pop("inputed_minutes", UNSET)

        labor_cost_cents = d.pop("labor_cost_cents", UNSET)

        project_management_subproject = cls(
            name=name,
            project_id=project_id,
            id=id,
            inputed_minutes=inputed_minutes,
            labor_cost_cents=labor_cost_cents,
        )

        project_management_subproject.additional_properties = d
        return project_management_subproject

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
