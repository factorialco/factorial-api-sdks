from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.approvals_materialized_approvals_flow_approvers_item_status import (
    ApprovalsMaterializedApprovalsFlowApproversItemStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApprovalsMaterializedApprovalsFlowApproversItem")


@_attrs_define
class ApprovalsMaterializedApprovalsFlowApproversItem:
    id: str
    materialized_approval_step_id: str
    approval_step_approver_id: str
    status: ApprovalsMaterializedApprovalsFlowApproversItemStatus
    updated_at: str
    access_id: str | Unset = UNSET
    employee_id: str | Unset = UNSET
    selection_criteria: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        materialized_approval_step_id = self.materialized_approval_step_id

        approval_step_approver_id = self.approval_step_approver_id

        status = self.status.value

        updated_at = self.updated_at

        access_id = self.access_id

        employee_id = self.employee_id

        selection_criteria = self.selection_criteria

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "materialized_approval_step_id": materialized_approval_step_id,
                "approval_step_approver_id": approval_step_approver_id,
                "status": status,
                "updated_at": updated_at,
            }
        )
        if access_id is not UNSET:
            field_dict["access_id"] = access_id
        if employee_id is not UNSET:
            field_dict["employee_id"] = employee_id
        if selection_criteria is not UNSET:
            field_dict["selection_criteria"] = selection_criteria

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        materialized_approval_step_id = d.pop("materialized_approval_step_id")

        approval_step_approver_id = d.pop("approval_step_approver_id")

        status = ApprovalsMaterializedApprovalsFlowApproversItemStatus(d.pop("status"))

        updated_at = d.pop("updated_at")

        access_id = d.pop("access_id", UNSET)

        employee_id = d.pop("employee_id", UNSET)

        selection_criteria = d.pop("selection_criteria", UNSET)

        approvals_materialized_approvals_flow_approvers_item = cls(
            id=id,
            materialized_approval_step_id=materialized_approval_step_id,
            approval_step_approver_id=approval_step_approver_id,
            status=status,
            updated_at=updated_at,
            access_id=access_id,
            employee_id=employee_id,
            selection_criteria=selection_criteria,
        )

        approvals_materialized_approvals_flow_approvers_item.additional_properties = d
        return approvals_materialized_approvals_flow_approvers_item

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
