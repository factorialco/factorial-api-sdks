from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectManagementProjectTask")


@_attrs_define
class ProjectManagementProjectTask:
    id: str
    project_id: str
    """ The ID of the project linked to the project task """
    task_id: str
    """ The ID of the task linked to the project task """
    follow_up: bool
    """ If true, status changes related to the project will notify the author """
    subproject_id: str | Unset = UNSET
    """ The ID of the subproject linked to the project task """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        project_id = self.project_id

        task_id = self.task_id

        follow_up = self.follow_up

        subproject_id = self.subproject_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "project_id": project_id,
                "task_id": task_id,
                "follow_up": follow_up,
            }
        )
        if subproject_id is not UNSET:
            field_dict["subproject_id"] = subproject_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        project_id = d.pop("project_id")

        task_id = d.pop("task_id")

        follow_up = d.pop("follow_up")

        subproject_id = d.pop("subproject_id", UNSET)

        project_management_project_task = cls(
            id=id,
            project_id=project_id,
            task_id=task_id,
            follow_up=follow_up,
            subproject_id=subproject_id,
        )

        project_management_project_task.additional_properties = d
        return project_management_project_task

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
