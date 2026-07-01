from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PerformanceReviewProcessTarget")


@_attrs_define
class PerformanceReviewProcessTarget:
    id: str
    """ Review process target ID (composed with performance_review_process_id and access_id) """
    access_id: str
    """ Participant access ID """
    performance_review_process_id: str
    """ Review process ID """
    materialized_process_target_id: str
    """ Materialized review process target ID """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        access_id = self.access_id

        performance_review_process_id = self.performance_review_process_id

        materialized_process_target_id = self.materialized_process_target_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "access_id": access_id,
                "performance_review_process_id": performance_review_process_id,
                "materialized_process_target_id": materialized_process_target_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        access_id = d.pop("access_id")

        performance_review_process_id = d.pop("performance_review_process_id")

        materialized_process_target_id = d.pop("materialized_process_target_id")

        performance_review_process_target = cls(
            id=id,
            access_id=access_id,
            performance_review_process_id=performance_review_process_id,
            materialized_process_target_id=materialized_process_target_id,
        )

        performance_review_process_target.additional_properties = d
        return performance_review_process_target

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
