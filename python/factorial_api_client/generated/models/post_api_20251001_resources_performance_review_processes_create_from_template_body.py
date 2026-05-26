from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_api_20251001_resources_performance_review_processes_create_from_template_body_template_type import (
    PostApi20251001ResourcesPerformanceReviewProcessesCreateFromTemplateBodyTemplateType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20251001ResourcesPerformanceReviewProcessesCreateFromTemplateBody")


@_attrs_define
class PostApi20251001ResourcesPerformanceReviewProcessesCreateFromTemplateBody:
    author_access_id: int
    """ Access ID to be set as author of the new review process """
    template_id: int
    """ Review process template ID """
    template_type: (
        PostApi20251001ResourcesPerformanceReviewProcessesCreateFromTemplateBodyTemplateType
    )
    """ Type of the template, custom or predefined """
    name: str | Unset = UNSET
    """ Name of the new review process """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        author_access_id = self.author_access_id

        template_id = self.template_id

        template_type = self.template_type.value

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "author_access_id": author_access_id,
                "template_id": template_id,
                "template_type": template_type,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        author_access_id = d.pop("author_access_id")

        template_id = d.pop("template_id")

        template_type = (
            PostApi20251001ResourcesPerformanceReviewProcessesCreateFromTemplateBodyTemplateType(
                d.pop("template_type")
            )
        )

        name = d.pop("name", UNSET)

        post_api_20251001_resources_performance_review_processes_create_from_template_body = cls(
            author_access_id=author_access_id,
            template_id=template_id,
            template_type=template_type,
            name=name,
        )

        post_api_20251001_resources_performance_review_processes_create_from_template_body.additional_properties = d
        return post_api_20251001_resources_performance_review_processes_create_from_template_body

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
