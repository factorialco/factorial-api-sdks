from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PerformanceReviewVisibilitySetting")


@_attrs_define
class PerformanceReviewVisibilitySetting:
    id: str
    """ Review process ID """
    performance_review_process_id: str
    """ Review process ID """
    restrict_answers_visibility_to_reportees: bool
    """ Employees don't have access to their results when enabled """
    early_access_to_answers_for_managers: bool
    """ Managers can access the results of their reports before deadline when enabled """
    anonymous_peer_evaluation_for_target: bool
    """ Peer evaluations are anonymous when enabled, so employees don't know who reviewed them """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        performance_review_process_id = self.performance_review_process_id

        restrict_answers_visibility_to_reportees = self.restrict_answers_visibility_to_reportees

        early_access_to_answers_for_managers = self.early_access_to_answers_for_managers

        anonymous_peer_evaluation_for_target = self.anonymous_peer_evaluation_for_target

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "performance_review_process_id": performance_review_process_id,
                "restrict_answers_visibility_to_reportees": restrict_answers_visibility_to_reportees,
                "early_access_to_answers_for_managers": early_access_to_answers_for_managers,
                "anonymous_peer_evaluation_for_target": anonymous_peer_evaluation_for_target,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        performance_review_process_id = d.pop("performance_review_process_id")

        restrict_answers_visibility_to_reportees = d.pop("restrict_answers_visibility_to_reportees")

        early_access_to_answers_for_managers = d.pop("early_access_to_answers_for_managers")

        anonymous_peer_evaluation_for_target = d.pop("anonymous_peer_evaluation_for_target")

        performance_review_visibility_setting = cls(
            id=id,
            performance_review_process_id=performance_review_process_id,
            restrict_answers_visibility_to_reportees=restrict_answers_visibility_to_reportees,
            early_access_to_answers_for_managers=early_access_to_answers_for_managers,
            anonymous_peer_evaluation_for_target=anonymous_peer_evaluation_for_target,
        )

        performance_review_visibility_setting.additional_properties = d
        return performance_review_visibility_setting

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
