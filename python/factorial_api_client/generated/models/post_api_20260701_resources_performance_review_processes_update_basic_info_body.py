from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20260701ResourcesPerformanceReviewProcessesUpdateBasicInfoBody")


@_attrs_define
class PostApi20260701ResourcesPerformanceReviewProcessesUpdateBasicInfoBody:
    id: str
    """ Review process ID """
    name: str | Unset = UNSET
    """ New name of the review process """
    description: str | Unset = UNSET
    """ New description of the review process """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        post_api_20260701_resources_performance_review_processes_update_basic_info_body = cls(
            id=id,
            name=name,
            description=description,
        )

        post_api_20260701_resources_performance_review_processes_update_basic_info_body.additional_properties = d
        return post_api_20260701_resources_performance_review_processes_update_basic_info_body

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
