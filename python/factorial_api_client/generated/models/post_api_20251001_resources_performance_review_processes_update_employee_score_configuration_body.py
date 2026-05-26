from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar(
    "T",
    bound="PostApi20251001ResourcesPerformanceReviewProcessesUpdateEmployeeScoreConfigurationBody",
)


@_attrs_define
class PostApi20251001ResourcesPerformanceReviewProcessesUpdateEmployeeScoreConfigurationBody:
    id: int
    """ Review process ID """
    enabled: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        enabled = self.enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "enabled": enabled,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        enabled = d.pop("enabled")

        post_api_20251001_resources_performance_review_processes_update_employee_score_configuration_body = cls(
            id=id,
            enabled=enabled,
        )

        post_api_20251001_resources_performance_review_processes_update_employee_score_configuration_body.additional_properties = d
        return post_api_20251001_resources_performance_review_processes_update_employee_score_configuration_body

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
