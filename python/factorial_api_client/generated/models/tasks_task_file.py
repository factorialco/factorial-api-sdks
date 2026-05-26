from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TasksTaskFile")


@_attrs_define
class TasksTaskFile:
    id: int
    """ identifier of the file. """
    task_id: int
    """ identifier of the task. """
    filename: str
    """ name of the file. """
    path: str
    """ path of the file, for downloading the file you need to concat api_url/path. """
    created_at: str
    """ creation date of the file. """
    content_type: str | Unset = UNSET
    """ content type of the file. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        task_id = self.task_id

        filename = self.filename

        path = self.path

        created_at = self.created_at

        content_type = self.content_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "task_id": task_id,
                "filename": filename,
                "path": path,
                "created_at": created_at,
            }
        )
        if content_type is not UNSET:
            field_dict["content_type"] = content_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        task_id = d.pop("task_id")

        filename = d.pop("filename")

        path = d.pop("path")

        created_at = d.pop("created_at")

        content_type = d.pop("content_type", UNSET)

        tasks_task_file = cls(
            id=id,
            task_id=task_id,
            filename=filename,
            path=path,
            created_at=created_at,
            content_type=content_type,
        )

        tasks_task_file.additional_properties = d
        return tasks_task_file

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
