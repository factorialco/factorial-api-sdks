from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostApi20251001ResourcesPerformanceReviewProcessTargetsBulkCreateBody")


@_attrs_define
class PostApi20251001ResourcesPerformanceReviewProcessTargetsBulkCreateBody:
    performance_review_process_id: int
    """ Review process ID """
    targets_access_ids: list[int]
    """ List of access IDs to be added as participants """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        performance_review_process_id = self.performance_review_process_id

        targets_access_ids = self.targets_access_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "performance_review_process_id": performance_review_process_id,
                "targets_access_ids": targets_access_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        performance_review_process_id = d.pop("performance_review_process_id")

        targets_access_ids = cast(list[int], d.pop("targets_access_ids"))

        post_api_20251001_resources_performance_review_process_targets_bulk_create_body = cls(
            performance_review_process_id=performance_review_process_id,
            targets_access_ids=targets_access_ids,
        )

        post_api_20251001_resources_performance_review_process_targets_bulk_create_body.additional_properties = d
        return post_api_20251001_resources_performance_review_process_targets_bulk_create_body

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
