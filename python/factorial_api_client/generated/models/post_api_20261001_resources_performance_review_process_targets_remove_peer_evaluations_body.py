from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar(
    "T", bound="PostApi20261001ResourcesPerformanceReviewProcessTargetsRemovePeerEvaluationsBody"
)


@_attrs_define
class PostApi20261001ResourcesPerformanceReviewProcessTargetsRemovePeerEvaluationsBody:
    id: str
    evaluation_ids: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        evaluation_ids = self.evaluation_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "evaluation_ids": evaluation_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        evaluation_ids = cast(list[str], d.pop("evaluation_ids"))

        post_api_20261001_resources_performance_review_process_targets_remove_peer_evaluations_body = cls(
            id=id,
            evaluation_ids=evaluation_ids,
        )

        post_api_20261001_resources_performance_review_process_targets_remove_peer_evaluations_body.additional_properties = d
        return post_api_20261001_resources_performance_review_process_targets_remove_peer_evaluations_body

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
