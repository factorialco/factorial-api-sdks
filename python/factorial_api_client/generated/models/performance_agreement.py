from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.performance_agreement_status import PerformanceAgreementStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.performance_agreement_conclusions import PerformanceAgreementConclusions
    from ..models.performance_agreement_manager_comments_item import (
        PerformanceAgreementManagerCommentsItem,
    )
    from ..models.performance_agreement_self_comments_item import (
        PerformanceAgreementSelfCommentsItem,
    )


T = TypeVar("T", bound="PerformanceAgreement")


@_attrs_define
class PerformanceAgreement:
    id: str
    """ Action plan ID """
    process_id: str
    """ Review process ID """
    target_id: str
    """ Review process target ID """
    status: PerformanceAgreementStatus
    """ Action plan status """
    locked: bool
    """ When the action plan cannot be edited anymore. Locked when both manager and employee signed it. """
    self_comments: list[PerformanceAgreementSelfCommentsItem]
    """ Self comments by question """
    manager_comments: list[PerformanceAgreementManagerCommentsItem]
    """ Manager comments by question """
    signer_id: str | Unset = UNSET
    """ Manager access ID who signed the action plan """
    reviewer_id: str | Unset = UNSET
    """ Manager employee ID """
    manager_signed_at: str | Unset = UNSET
    """ Date when the manager signed the action plan """
    target_signed_at: str | Unset = UNSET
    """ Date when the employee signed the action plan """
    agreement_signed_at: str | Unset = UNSET
    """ Date when the action plan was last signed """
    last_modified_at: str | Unset = UNSET
    """ Date when the action plan was last modified """
    conclusions: PerformanceAgreementConclusions | Unset = UNSET
    """ Conclusions of the action plan """
    self_evaluation_id: str | Unset = UNSET
    """ Self review evaluation ID """
    manager_evaluation_id: str | Unset = UNSET
    """ Manager review evaluation ID """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        process_id = self.process_id

        target_id = self.target_id

        status = self.status.value

        locked = self.locked

        self_comments = []
        for self_comments_item_data in self.self_comments:
            self_comments_item = self_comments_item_data.to_dict()
            self_comments.append(self_comments_item)

        manager_comments = []
        for manager_comments_item_data in self.manager_comments:
            manager_comments_item = manager_comments_item_data.to_dict()
            manager_comments.append(manager_comments_item)

        signer_id = self.signer_id

        reviewer_id = self.reviewer_id

        manager_signed_at = self.manager_signed_at

        target_signed_at = self.target_signed_at

        agreement_signed_at = self.agreement_signed_at

        last_modified_at = self.last_modified_at

        conclusions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.conclusions, Unset):
            conclusions = self.conclusions.to_dict()

        self_evaluation_id = self.self_evaluation_id

        manager_evaluation_id = self.manager_evaluation_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "process_id": process_id,
                "target_id": target_id,
                "status": status,
                "locked": locked,
                "self_comments": self_comments,
                "manager_comments": manager_comments,
            }
        )
        if signer_id is not UNSET:
            field_dict["signer_id"] = signer_id
        if reviewer_id is not UNSET:
            field_dict["reviewer_id"] = reviewer_id
        if manager_signed_at is not UNSET:
            field_dict["manager_signed_at"] = manager_signed_at
        if target_signed_at is not UNSET:
            field_dict["target_signed_at"] = target_signed_at
        if agreement_signed_at is not UNSET:
            field_dict["agreement_signed_at"] = agreement_signed_at
        if last_modified_at is not UNSET:
            field_dict["last_modified_at"] = last_modified_at
        if conclusions is not UNSET:
            field_dict["conclusions"] = conclusions
        if self_evaluation_id is not UNSET:
            field_dict["self_evaluation_id"] = self_evaluation_id
        if manager_evaluation_id is not UNSET:
            field_dict["manager_evaluation_id"] = manager_evaluation_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.performance_agreement_conclusions import PerformanceAgreementConclusions
        from ..models.performance_agreement_manager_comments_item import (
            PerformanceAgreementManagerCommentsItem,
        )
        from ..models.performance_agreement_self_comments_item import (
            PerformanceAgreementSelfCommentsItem,
        )

        d = dict(src_dict)
        id = d.pop("id")

        process_id = d.pop("process_id")

        target_id = d.pop("target_id")

        status = PerformanceAgreementStatus(d.pop("status"))

        locked = d.pop("locked")

        self_comments = []
        _self_comments = d.pop("self_comments")
        for self_comments_item_data in _self_comments:
            self_comments_item = PerformanceAgreementSelfCommentsItem.from_dict(
                self_comments_item_data
            )

            self_comments.append(self_comments_item)

        manager_comments = []
        _manager_comments = d.pop("manager_comments")
        for manager_comments_item_data in _manager_comments:
            manager_comments_item = PerformanceAgreementManagerCommentsItem.from_dict(
                manager_comments_item_data
            )

            manager_comments.append(manager_comments_item)

        signer_id = d.pop("signer_id", UNSET)

        reviewer_id = d.pop("reviewer_id", UNSET)

        manager_signed_at = d.pop("manager_signed_at", UNSET)

        target_signed_at = d.pop("target_signed_at", UNSET)

        agreement_signed_at = d.pop("agreement_signed_at", UNSET)

        last_modified_at = d.pop("last_modified_at", UNSET)

        _conclusions = d.pop("conclusions", UNSET)
        conclusions: PerformanceAgreementConclusions | Unset
        if isinstance(_conclusions, Unset):
            conclusions = UNSET
        else:
            conclusions = PerformanceAgreementConclusions.from_dict(_conclusions)

        self_evaluation_id = d.pop("self_evaluation_id", UNSET)

        manager_evaluation_id = d.pop("manager_evaluation_id", UNSET)

        performance_agreement = cls(
            id=id,
            process_id=process_id,
            target_id=target_id,
            status=status,
            locked=locked,
            self_comments=self_comments,
            manager_comments=manager_comments,
            signer_id=signer_id,
            reviewer_id=reviewer_id,
            manager_signed_at=manager_signed_at,
            target_signed_at=target_signed_at,
            agreement_signed_at=agreement_signed_at,
            last_modified_at=last_modified_at,
            conclusions=conclusions,
            self_evaluation_id=self_evaluation_id,
            manager_evaluation_id=manager_evaluation_id,
        )

        performance_agreement.additional_properties = d
        return performance_agreement

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
