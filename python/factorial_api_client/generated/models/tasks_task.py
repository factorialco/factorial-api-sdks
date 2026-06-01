from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.tasks_task_status import TasksTaskStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="TasksTask")


@_attrs_define
class TasksTask:
    id: int
    """ Identifier of the task """
    name: str
    """ Name of the task """
    company_id: int
    """ Company identifier of the author of the task """
    assignee_ids: list[int]
    """ Employees assigned to the task, assignee_id references to access_id """
    created_at: str
    updated_at: str
    """ Updated at date of the task """
    content: str | Unset = UNSET
    """ Content of the task """
    due_on: str | Unset = UNSET
    """ Due on date of the task """
    author_employee_id: int | Unset = UNSET
    """ Employee id of the author of the task """
    completed_at: str | Unset = UNSET
    """ Completed at date of the task """
    completed_by_id: int | Unset = UNSET
    """ Completed by identifier """
    status: TasksTaskStatus | Unset = UNSET
    """ Status of the task """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        company_id = self.company_id

        assignee_ids = self.assignee_ids

        created_at = self.created_at

        updated_at = self.updated_at

        content = self.content

        due_on = self.due_on

        author_employee_id = self.author_employee_id

        completed_at = self.completed_at

        completed_by_id = self.completed_by_id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "company_id": company_id,
                "assignee_ids": assignee_ids,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if content is not UNSET:
            field_dict["content"] = content
        if due_on is not UNSET:
            field_dict["due_on"] = due_on
        if author_employee_id is not UNSET:
            field_dict["author_employee_id"] = author_employee_id
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at
        if completed_by_id is not UNSET:
            field_dict["completed_by_id"] = completed_by_id
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        company_id = d.pop("company_id")

        assignee_ids = cast(list[int], d.pop("assignee_ids"))

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        content = d.pop("content", UNSET)

        due_on = d.pop("due_on", UNSET)

        author_employee_id = d.pop("author_employee_id", UNSET)

        completed_at = d.pop("completed_at", UNSET)

        completed_by_id = d.pop("completed_by_id", UNSET)

        _status = d.pop("status", UNSET)
        status: TasksTaskStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = TasksTaskStatus(_status) if _status is not None else None

        tasks_task = cls(
            id=id,
            name=name,
            company_id=company_id,
            assignee_ids=assignee_ids,
            created_at=created_at,
            updated_at=updated_at,
            content=content,
            due_on=due_on,
            author_employee_id=author_employee_id,
            completed_at=completed_at,
            completed_by_id=completed_by_id,
            status=status,
        )

        tasks_task.additional_properties = d
        return tasks_task

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
