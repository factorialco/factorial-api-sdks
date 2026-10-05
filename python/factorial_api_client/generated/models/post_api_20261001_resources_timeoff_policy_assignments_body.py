from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostApi20261001ResourcesTimeoffPolicyAssignmentsBody")


@_attrs_define
class PostApi20261001ResourcesTimeoffPolicyAssignmentsBody:
    timeoff_policy_id: str
    """ The time off policy id """
    employee_id: str
    """ The employee id """
    effective_at: str
    """ The effective date of the policy assignment """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timeoff_policy_id = self.timeoff_policy_id

        employee_id = self.employee_id

        effective_at = self.effective_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timeoff_policy_id": timeoff_policy_id,
                "employee_id": employee_id,
                "effective_at": effective_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        timeoff_policy_id = d.pop("timeoff_policy_id")

        employee_id = d.pop("employee_id")

        effective_at = d.pop("effective_at")

        post_api_20261001_resources_timeoff_policy_assignments_body = cls(
            timeoff_policy_id=timeoff_policy_id,
            employee_id=employee_id,
            effective_at=effective_at,
        )

        post_api_20261001_resources_timeoff_policy_assignments_body.additional_properties = d
        return post_api_20261001_resources_timeoff_policy_assignments_body

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
