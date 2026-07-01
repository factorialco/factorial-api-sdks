from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar(
    "T", bound="PostApi20260701ResourcesApprovalsMaterializedApprovalsFlowsApproveResourceBody"
)


@_attrs_define
class PostApi20260701ResourcesApprovalsMaterializedApprovalsFlowsApproveResourceBody:
    resource_id: str
    """ Id of the resource to approve. """
    resource_type: str
    """ Type of the resource to approve (e.g. Timeoff::Leave). """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resource_id = self.resource_id

        resource_type = self.resource_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resource_id": resource_id,
                "resource_type": resource_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        resource_id = d.pop("resource_id")

        resource_type = d.pop("resource_type")

        post_api_20260701_resources_approvals_materialized_approvals_flows_approve_resource_body = (
            cls(
                resource_id=resource_id,
                resource_type=resource_type,
            )
        )

        post_api_20260701_resources_approvals_materialized_approvals_flows_approve_resource_body.additional_properties = d
        return (
            post_api_20260701_resources_approvals_materialized_approvals_flows_approve_resource_body
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
