from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.approvals_materialized_approvals_flow_status import (
    ApprovalsMaterializedApprovalsFlowStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApprovalsMaterializedApprovalsFlow")


@_attrs_define
class ApprovalsMaterializedApprovalsFlow:
    id: int
    author_id: int
    owner_id: int
    resource_type: str
    resource_id: int
    resource_url: str
    status: ApprovalsMaterializedApprovalsFlowStatus
    expires_at: str
    approval_flow_id: int
    approvers: list[Any]
    email_detail_blocks: list[str]
    author_employee_id: int | Unset = UNSET
    owner_employee_id: int | Unset = UNSET
    final_decision_at: str | Unset = UNSET
    override_approver_id: int | Unset = UNSET
    override_approver_employee_id: int | Unset = UNSET
    rules_decision: str | Unset = UNSET
    auto_approval_description: str | Unset = UNSET
    action_type: str | Unset = UNSET
    reason: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        author_id = self.author_id

        owner_id = self.owner_id

        resource_type = self.resource_type

        resource_id = self.resource_id

        resource_url = self.resource_url

        status = self.status.value

        expires_at = self.expires_at

        approval_flow_id = self.approval_flow_id

        approvers = self.approvers

        email_detail_blocks = self.email_detail_blocks

        author_employee_id = self.author_employee_id

        owner_employee_id = self.owner_employee_id

        final_decision_at = self.final_decision_at

        override_approver_id = self.override_approver_id

        override_approver_employee_id = self.override_approver_employee_id

        rules_decision = self.rules_decision

        auto_approval_description = self.auto_approval_description

        action_type = self.action_type

        reason = self.reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "author_id": author_id,
                "owner_id": owner_id,
                "resource_type": resource_type,
                "resource_id": resource_id,
                "resource_url": resource_url,
                "status": status,
                "expires_at": expires_at,
                "approval_flow_id": approval_flow_id,
                "approvers": approvers,
                "email_detail_blocks": email_detail_blocks,
            }
        )
        if author_employee_id is not UNSET:
            field_dict["author_employee_id"] = author_employee_id
        if owner_employee_id is not UNSET:
            field_dict["owner_employee_id"] = owner_employee_id
        if final_decision_at is not UNSET:
            field_dict["final_decision_at"] = final_decision_at
        if override_approver_id is not UNSET:
            field_dict["override_approver_id"] = override_approver_id
        if override_approver_employee_id is not UNSET:
            field_dict["override_approver_employee_id"] = override_approver_employee_id
        if rules_decision is not UNSET:
            field_dict["rules_decision"] = rules_decision
        if auto_approval_description is not UNSET:
            field_dict["auto_approval_description"] = auto_approval_description
        if action_type is not UNSET:
            field_dict["action_type"] = action_type
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        author_id = d.pop("author_id")

        owner_id = d.pop("owner_id")

        resource_type = d.pop("resource_type")

        resource_id = d.pop("resource_id")

        resource_url = d.pop("resource_url")

        status = ApprovalsMaterializedApprovalsFlowStatus(d.pop("status"))

        expires_at = d.pop("expires_at")

        approval_flow_id = d.pop("approval_flow_id")

        approvers = cast(list[Any], d.pop("approvers"))

        email_detail_blocks = cast(list[str], d.pop("email_detail_blocks"))

        author_employee_id = d.pop("author_employee_id", UNSET)

        owner_employee_id = d.pop("owner_employee_id", UNSET)

        final_decision_at = d.pop("final_decision_at", UNSET)

        override_approver_id = d.pop("override_approver_id", UNSET)

        override_approver_employee_id = d.pop("override_approver_employee_id", UNSET)

        rules_decision = d.pop("rules_decision", UNSET)

        auto_approval_description = d.pop("auto_approval_description", UNSET)

        action_type = d.pop("action_type", UNSET)

        reason = d.pop("reason", UNSET)

        approvals_materialized_approvals_flow = cls(
            id=id,
            author_id=author_id,
            owner_id=owner_id,
            resource_type=resource_type,
            resource_id=resource_id,
            resource_url=resource_url,
            status=status,
            expires_at=expires_at,
            approval_flow_id=approval_flow_id,
            approvers=approvers,
            email_detail_blocks=email_detail_blocks,
            author_employee_id=author_employee_id,
            owner_employee_id=owner_employee_id,
            final_decision_at=final_decision_at,
            override_approver_id=override_approver_id,
            override_approver_employee_id=override_approver_employee_id,
            rules_decision=rules_decision,
            auto_approval_description=auto_approval_description,
            action_type=action_type,
            reason=reason,
        )

        approvals_materialized_approvals_flow.additional_properties = d
        return approvals_materialized_approvals_flow

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
