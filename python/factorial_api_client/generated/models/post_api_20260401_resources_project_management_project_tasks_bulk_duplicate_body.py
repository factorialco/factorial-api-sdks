from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20260401ResourcesProjectManagementProjectTasksBulkDuplicateBody")


@_attrs_define
class PostApi20260401ResourcesProjectManagementProjectTasksBulkDuplicateBody:
    ids: list[int]
    """ Task ids to be duplicated """
    project_id: int | Unset = UNSET
    """ Project id where the tasks will be duplicated """
    subproject_id: int | Unset = UNSET
    """ Subproject id where the tasks will be duplicated """
    exclude_assignees: bool | Unset = UNSET
    """ Set this to true if you want to exclude assignees from the duplicated tasks """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ids = self.ids

        project_id = self.project_id

        subproject_id = self.subproject_id

        exclude_assignees = self.exclude_assignees

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ids": ids,
            }
        )
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if subproject_id is not UNSET:
            field_dict["subproject_id"] = subproject_id
        if exclude_assignees is not UNSET:
            field_dict["exclude_assignees"] = exclude_assignees

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ids = cast(list[int], d.pop("ids"))

        project_id = d.pop("project_id", UNSET)

        subproject_id = d.pop("subproject_id", UNSET)

        exclude_assignees = d.pop("exclude_assignees", UNSET)

        post_api_20260401_resources_project_management_project_tasks_bulk_duplicate_body = cls(
            ids=ids,
            project_id=project_id,
            subproject_id=subproject_id,
            exclude_assignees=exclude_assignees,
        )

        post_api_20260401_resources_project_management_project_tasks_bulk_duplicate_body.additional_properties = d
        return post_api_20260401_resources_project_management_project_tasks_bulk_duplicate_body

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
