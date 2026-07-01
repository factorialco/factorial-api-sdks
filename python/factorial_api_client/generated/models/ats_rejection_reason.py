from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ats_rejection_reason_decision_maker import AtsRejectionReasonDecisionMaker

T = TypeVar("T", bound="AtsRejectionReason")


@_attrs_define
class AtsRejectionReason:
    id: str
    """ Rejection reason identifier """
    company_id: str
    """ Company identifier of the rejection reason """
    decision_maker: AtsRejectionReasonDecisionMaker
    """ Decision maker of the rejection reason """
    reason: str
    """ Reason of the rejection """
    created_at: str
    """ Rejection reason created date """
    updated_at: str
    """ Rejection reason updated date """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        company_id = self.company_id

        decision_maker = self.decision_maker.value

        reason = self.reason

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "company_id": company_id,
                "decision_maker": decision_maker,
                "reason": reason,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        company_id = d.pop("company_id")

        decision_maker = AtsRejectionReasonDecisionMaker(d.pop("decision_maker"))

        reason = d.pop("reason")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        ats_rejection_reason = cls(
            id=id,
            company_id=company_id,
            decision_maker=decision_maker,
            reason=reason,
            created_at=created_at,
            updated_at=updated_at,
        )

        ats_rejection_reason.additional_properties = d
        return ats_rejection_reason

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
