from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.put_api_20251001_resources_tasks_tasks_id_body_status import (
    PutApi20251001ResourcesTasksTasksIdBodyStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PutApi20251001ResourcesTasksTasksIdBody")


@_attrs_define
class PutApi20251001ResourcesTasksTasksIdBody:
    id: int
    """ id of a task. """
    name: str | Unset = UNSET
    """ name of  task. """
    content: str | Unset = UNSET
    """ description of the task. """
    due_on: str | Unset = UNSET
    """ expiration date of the task. """
    assignee_ids: list[int] | Unset = UNSET
    """ employees assigned to the task, assignee_id references to access_id. """
    status: PutApi20251001ResourcesTasksTasksIdBodyStatus | Unset = UNSET
    """ status of the task (todo | in_progress | done | discarded). """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        content = self.content

        due_on = self.due_on

        assignee_ids: list[int] | Unset = UNSET
        if not isinstance(self.assignee_ids, Unset):
            assignee_ids = self.assignee_ids

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if content is not UNSET:
            field_dict["content"] = content
        if due_on is not UNSET:
            field_dict["due_on"] = due_on
        if assignee_ids is not UNSET:
            field_dict["assignee_ids"] = assignee_ids
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name", UNSET)

        content = d.pop("content", UNSET)

        due_on = d.pop("due_on", UNSET)

        assignee_ids = cast(list[int], d.pop("assignee_ids", UNSET))

        _status = d.pop("status", UNSET)
        status: PutApi20251001ResourcesTasksTasksIdBodyStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = PutApi20251001ResourcesTasksTasksIdBodyStatus(_status) if _status is not None else None

        put_api_20251001_resources_tasks_tasks_id_body = cls(
            id=id,
            name=name,
            content=content,
            due_on=due_on,
            assignee_ids=assignee_ids,
            status=status,
        )

        put_api_20251001_resources_tasks_tasks_id_body.additional_properties = d
        return put_api_20251001_resources_tasks_tasks_id_body

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
