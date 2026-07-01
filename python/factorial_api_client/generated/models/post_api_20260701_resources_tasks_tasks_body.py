from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_api_20260701_resources_tasks_tasks_body_status import (
    PostApi20260701ResourcesTasksTasksBodyStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20260701ResourcesTasksTasksBody")


@_attrs_define
class PostApi20260701ResourcesTasksTasksBody:
    name: str
    """ name of the task. """
    status: PostApi20260701ResourcesTasksTasksBodyStatus
    """ status of the task (todo | in_progress | done | discarded). """
    content: str | Unset = UNSET
    """ description of the task """
    due_on: str | Unset = UNSET
    """ expiration date of the task. """
    assignee_ids: list[str] | Unset = UNSET
    """ Employees assigned to the task, assignee_id references to access_id. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        status = self.status.value

        content = self.content

        due_on = self.due_on

        assignee_ids: list[str] | Unset = UNSET
        if not isinstance(self.assignee_ids, Unset):
            assignee_ids = self.assignee_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "status": status,
            }
        )
        if content is not UNSET:
            field_dict["content"] = content
        if due_on is not UNSET:
            field_dict["due_on"] = due_on
        if assignee_ids is not UNSET:
            field_dict["assignee_ids"] = assignee_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        status = PostApi20260701ResourcesTasksTasksBodyStatus(d.pop("status"))

        content = d.pop("content", UNSET)

        due_on = d.pop("due_on", UNSET)

        assignee_ids = cast(list[str], d.pop("assignee_ids", UNSET))

        post_api_20260701_resources_tasks_tasks_body = cls(
            name=name,
            status=status,
            content=content,
            due_on=due_on,
            assignee_ids=assignee_ids,
        )

        post_api_20260701_resources_tasks_tasks_body.additional_properties = d
        return post_api_20260701_resources_tasks_tasks_body

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
