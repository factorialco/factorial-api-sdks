from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_api_20261001_resources_tasks_tasks_bulk_update_body_tasks_item_identifier import (
    PostApi20261001ResourcesTasksTasksBulkUpdateBodyTasksItemIdentifier,
)
from ..models.post_api_20261001_resources_tasks_tasks_bulk_update_body_tasks_item_status import (
    PostApi20261001ResourcesTasksTasksBulkUpdateBodyTasksItemStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20261001ResourcesTasksTasksBulkUpdateBodyTasksItem")


@_attrs_define
class PostApi20261001ResourcesTasksTasksBulkUpdateBodyTasksItem:
    id: str
    name: str | Unset = UNSET
    content: str | Unset = UNSET
    starts_on: str | Unset = UNSET
    due_on: str | Unset = UNSET
    assignee_ids: list[str] | Unset = UNSET
    identifier: PostApi20261001ResourcesTasksTasksBulkUpdateBodyTasksItemIdentifier | Unset = UNSET
    status: PostApi20261001ResourcesTasksTasksBulkUpdateBodyTasksItemStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        content = self.content

        starts_on = self.starts_on

        due_on = self.due_on

        assignee_ids: list[str] | Unset = UNSET
        if not isinstance(self.assignee_ids, Unset):
            assignee_ids = self.assignee_ids

        identifier: str | Unset = UNSET
        if not isinstance(self.identifier, Unset):
            identifier = self.identifier.value if self.identifier is not None else None

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value if self.status is not None else None

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
        if starts_on is not UNSET:
            field_dict["starts_on"] = starts_on
        if due_on is not UNSET:
            field_dict["due_on"] = due_on
        if assignee_ids is not UNSET:
            field_dict["assignee_ids"] = assignee_ids
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name", UNSET)

        content = d.pop("content", UNSET)

        starts_on = d.pop("starts_on", UNSET)

        due_on = d.pop("due_on", UNSET)

        assignee_ids = cast(list[str], d.pop("assignee_ids", UNSET))

        _identifier = d.pop("identifier", UNSET)
        identifier: PostApi20261001ResourcesTasksTasksBulkUpdateBodyTasksItemIdentifier | Unset
        if isinstance(_identifier, Unset):
            identifier = UNSET
        else:
            identifier = PostApi20261001ResourcesTasksTasksBulkUpdateBodyTasksItemIdentifier(
                _identifier
            ) if _identifier is not None else None

        _status = d.pop("status", UNSET)
        status: PostApi20261001ResourcesTasksTasksBulkUpdateBodyTasksItemStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = PostApi20261001ResourcesTasksTasksBulkUpdateBodyTasksItemStatus(_status) if _status is not None else None

        post_api_20261001_resources_tasks_tasks_bulk_update_body_tasks_item = cls(
            id=id,
            name=name,
            content=content,
            starts_on=starts_on,
            due_on=due_on,
            assignee_ids=assignee_ids,
            identifier=identifier,
            status=status,
        )

        post_api_20261001_resources_tasks_tasks_bulk_update_body_tasks_item.additional_properties = d
        return post_api_20261001_resources_tasks_tasks_bulk_update_body_tasks_item

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
