from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.post_api_20251001_resources_project_management_project_tasks_body_status import (
    PostApi20251001ResourcesProjectManagementProjectTasksBodyStatus,
)
from ..types import UNSET, File, FileTypes, Unset

T = TypeVar("T", bound="PostApi20251001ResourcesProjectManagementProjectTasksBody")


@_attrs_define
class PostApi20251001ResourcesProjectManagementProjectTasksBody:
    name: str
    """ The name of the project task """
    project_id: int
    """ The ID of the project where the task belongs """
    status: PostApi20251001ResourcesProjectManagementProjectTasksBodyStatus
    """ The status of the project task """
    content: str | Unset = UNSET
    """ The content/description of the project task """
    starts_on: str | Unset = UNSET
    """ The date when the project task starts """
    follow_up: bool | Unset = UNSET
    """ If true, status changes related to the project will notify the author """
    due_on: str | Unset = UNSET
    """ The date when the project task will be due """
    assignee_employee_ids: list[int] | Unset = UNSET
    """ The value of the assignee employee ids of the project task """
    subproject_id: int | Unset = UNSET
    """ The ID of the subproject where the project task belongs """
    files: list[File] | Unset = UNSET
    """ Array of files that will be attached to the project task """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        project_id = self.project_id

        status = self.status.value

        content = self.content

        starts_on = self.starts_on

        follow_up = self.follow_up

        due_on = self.due_on

        assignee_employee_ids: list[int] | Unset = UNSET
        if not isinstance(self.assignee_employee_ids, Unset):
            assignee_employee_ids = self.assignee_employee_ids

        subproject_id = self.subproject_id

        files: list[FileTypes] | Unset = UNSET
        if not isinstance(self.files, Unset):
            files = []
            for files_item_data in self.files:
                files_item = files_item_data.to_tuple()

                files.append(files_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "project_id": project_id,
                "status": status,
            }
        )
        if content is not UNSET:
            field_dict["content"] = content
        if starts_on is not UNSET:
            field_dict["starts_on"] = starts_on
        if follow_up is not UNSET:
            field_dict["follow_up"] = follow_up
        if due_on is not UNSET:
            field_dict["due_on"] = due_on
        if assignee_employee_ids is not UNSET:
            field_dict["assignee_employee_ids[]"] = assignee_employee_ids
        if subproject_id is not UNSET:
            field_dict["subproject_id"] = subproject_id
        if files is not UNSET:
            field_dict["files[]"] = files

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("name", (None, str(self.name).encode(), "text/plain")))

        files.append(("project_id", (None, str(self.project_id).encode(), "text/plain")))

        files.append(("status", (None, str(self.status.value).encode(), "text/plain")))

        if not isinstance(self.content, Unset):
            files.append(("content", (None, str(self.content).encode(), "text/plain")))

        if not isinstance(self.starts_on, Unset):
            files.append(("starts_on", (None, str(self.starts_on).encode(), "text/plain")))

        if not isinstance(self.follow_up, Unset):
            files.append(("follow_up", (None, str(self.follow_up).encode(), "text/plain")))

        if not isinstance(self.due_on, Unset):
            files.append(("due_on", (None, str(self.due_on).encode(), "text/plain")))

        if not isinstance(self.assignee_employee_ids, Unset):
            for assignee_employee_ids_item_element in self.assignee_employee_ids:
                files.append(
                    (
                        "assignee_employee_ids[]",
                        (None, str(assignee_employee_ids_item_element).encode(), "text/plain"),
                    )
                )

        if not isinstance(self.subproject_id, Unset):
            files.append(("subproject_id", (None, str(self.subproject_id).encode(), "text/plain")))

        if not isinstance(self.files, Unset):
            for files_item_element in self.files:
                files.append(("files[]", files_item_element.to_tuple()))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        project_id = d.pop("project_id")

        status = PostApi20251001ResourcesProjectManagementProjectTasksBodyStatus(d.pop("status"))

        content = d.pop("content", UNSET)

        starts_on = d.pop("starts_on", UNSET)

        follow_up = d.pop("follow_up", UNSET)

        due_on = d.pop("due_on", UNSET)

        assignee_employee_ids = cast(list[int], d.pop("assignee_employee_ids[]", UNSET))

        subproject_id = d.pop("subproject_id", UNSET)

        _files = d.pop("files[]", UNSET)
        files: list[File] | Unset = UNSET
        if _files is not UNSET:
            files = []
            for files_item_data in _files:
                files_item = File(payload=BytesIO(files_item_data))

                files.append(files_item)

        post_api_20251001_resources_project_management_project_tasks_body = cls(
            name=name,
            project_id=project_id,
            status=status,
            content=content,
            starts_on=starts_on,
            follow_up=follow_up,
            due_on=due_on,
            assignee_employee_ids=assignee_employee_ids,
            subproject_id=subproject_id,
            files=files,
        )

        post_api_20251001_resources_project_management_project_tasks_body.additional_properties = d
        return post_api_20251001_resources_project_management_project_tasks_body

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
