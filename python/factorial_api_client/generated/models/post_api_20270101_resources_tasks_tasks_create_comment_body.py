from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20270101ResourcesTasksTasksCreateCommentBody")


@_attrs_define
class PostApi20270101ResourcesTasksTasksCreateCommentBody:
    content: str
    """ body of the comment. """
    resource_id: str
    """ id of the task the comment is written on. """
    company_id: str
    """ id of the company the task belongs to. """
    author_id: str | Unset = UNSET
    """ deprecated, use author_employee_id instead. Access that authors the comment. """
    author_employee_id: str | Unset = UNSET
    """ employee that authors the comment. """
    mentioned_access_ids: list[str] | Unset = UNSET
    """ deprecated, use mentioned_employee_ids instead. Accesses mentioned in the comment. """
    mentioned_employee_ids: list[str] | Unset = UNSET
    """ employees mentioned in the comment. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content = self.content

        resource_id = self.resource_id

        company_id = self.company_id

        author_id = self.author_id

        author_employee_id = self.author_employee_id

        mentioned_access_ids: list[str] | Unset = UNSET
        if not isinstance(self.mentioned_access_ids, Unset):
            mentioned_access_ids = self.mentioned_access_ids

        mentioned_employee_ids: list[str] | Unset = UNSET
        if not isinstance(self.mentioned_employee_ids, Unset):
            mentioned_employee_ids = self.mentioned_employee_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content": content,
                "resource_id": resource_id,
                "company_id": company_id,
            }
        )
        if author_id is not UNSET:
            field_dict["author_id"] = author_id
        if author_employee_id is not UNSET:
            field_dict["author_employee_id"] = author_employee_id
        if mentioned_access_ids is not UNSET:
            field_dict["mentioned_access_ids"] = mentioned_access_ids
        if mentioned_employee_ids is not UNSET:
            field_dict["mentioned_employee_ids"] = mentioned_employee_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        content = d.pop("content")

        resource_id = d.pop("resource_id")

        company_id = d.pop("company_id")

        author_id = d.pop("author_id", UNSET)

        author_employee_id = d.pop("author_employee_id", UNSET)

        mentioned_access_ids = cast(list[str], d.pop("mentioned_access_ids", UNSET))

        mentioned_employee_ids = cast(list[str], d.pop("mentioned_employee_ids", UNSET))

        post_api_20270101_resources_tasks_tasks_create_comment_body = cls(
            content=content,
            resource_id=resource_id,
            company_id=company_id,
            author_id=author_id,
            author_employee_id=author_employee_id,
            mentioned_access_ids=mentioned_access_ids,
            mentioned_employee_ids=mentioned_employee_ids,
        )

        post_api_20270101_resources_tasks_tasks_create_comment_body.additional_properties = d
        return post_api_20270101_resources_tasks_tasks_create_comment_body

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
