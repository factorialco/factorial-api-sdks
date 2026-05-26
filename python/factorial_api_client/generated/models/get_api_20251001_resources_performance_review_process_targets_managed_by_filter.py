from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetApi20251001ResourcesPerformanceReviewProcessTargetsManagedByFilter")


@_attrs_define
class GetApi20251001ResourcesPerformanceReviewProcessTargetsManagedByFilter:
    """Only participants managed by the specified employee ID

    Example:
        {'manager_employee_id': 1, 'only_direct_reports': False}

    """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        get_api_20251001_resources_performance_review_process_targets_managed_by_filter = cls()

        get_api_20251001_resources_performance_review_process_targets_managed_by_filter.additional_properties = d
        return get_api_20251001_resources_performance_review_process_targets_managed_by_filter

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
