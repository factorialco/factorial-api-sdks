from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostApi20261001ResourcesProjectManagementProjectsChangeAssignmentBody")


@_attrs_define
class PostApi20261001ResourcesProjectManagementProjectsChangeAssignmentBody:
    id: str
    employees_assignment: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        employees_assignment = self.employees_assignment

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "employees_assignment": employees_assignment,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        employees_assignment = d.pop("employees_assignment")

        post_api_20261001_resources_project_management_projects_change_assignment_body = cls(
            id=id,
            employees_assignment=employees_assignment,
        )

        post_api_20261001_resources_project_management_projects_change_assignment_body.additional_properties = d
        return post_api_20261001_resources_project_management_projects_change_assignment_body

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
