from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar(
    "T", bound="GetApi20261001ResourcesPerformanceReviewEvaluationsWithTargetsManagedByFilter"
)


@_attrs_define
class GetApi20261001ResourcesPerformanceReviewEvaluationsWithTargetsManagedByFilter:
    """Only evaluations where the participant is managed by the specified employee ID

    Example:
        {'manager_employee_id': 1, 'only_direct_reports': False}

    """

    manager_employee_id: str
    only_direct_reports: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        manager_employee_id = self.manager_employee_id

        only_direct_reports = self.only_direct_reports

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "manager_employee_id": manager_employee_id,
                "only_direct_reports": only_direct_reports,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        manager_employee_id = d.pop("manager_employee_id")

        only_direct_reports = d.pop("only_direct_reports")

        get_api_20261001_resources_performance_review_evaluations_with_targets_managed_by_filter = (
            cls(
                manager_employee_id=manager_employee_id,
                only_direct_reports=only_direct_reports,
            )
        )

        get_api_20261001_resources_performance_review_evaluations_with_targets_managed_by_filter.additional_properties = d
        return (
            get_api_20261001_resources_performance_review_evaluations_with_targets_managed_by_filter
        )

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
