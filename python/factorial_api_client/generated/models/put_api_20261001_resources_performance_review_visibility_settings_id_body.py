from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PutApi20261001ResourcesPerformanceReviewVisibilitySettingsIdBody")


@_attrs_define
class PutApi20261001ResourcesPerformanceReviewVisibilitySettingsIdBody:
    restrict_answers_visibility_to_reportees: bool
    """ When enabled, employees don't have access to their results """
    early_access_to_answers_for_managers: bool
    """ When enabled, managers can access the results of their reports before deadline """
    anonymous_peer_evaluation_for_target: bool
    """ When enabled, peer evaluations are anonymous so employees don't know who reviewed them """
    id: str | Unset = UNSET
    """ Review process ID """
    performance_review_process_id: str | Unset = UNSET
    """ Review process ID """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        restrict_answers_visibility_to_reportees = self.restrict_answers_visibility_to_reportees

        early_access_to_answers_for_managers = self.early_access_to_answers_for_managers

        anonymous_peer_evaluation_for_target = self.anonymous_peer_evaluation_for_target

        id = self.id

        performance_review_process_id = self.performance_review_process_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "restrict_answers_visibility_to_reportees": restrict_answers_visibility_to_reportees,
                "early_access_to_answers_for_managers": early_access_to_answers_for_managers,
                "anonymous_peer_evaluation_for_target": anonymous_peer_evaluation_for_target,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if performance_review_process_id is not UNSET:
            field_dict["performance_review_process_id"] = performance_review_process_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        restrict_answers_visibility_to_reportees = d.pop("restrict_answers_visibility_to_reportees")

        early_access_to_answers_for_managers = d.pop("early_access_to_answers_for_managers")

        anonymous_peer_evaluation_for_target = d.pop("anonymous_peer_evaluation_for_target")

        id = d.pop("id", UNSET)

        performance_review_process_id = d.pop("performance_review_process_id", UNSET)

        put_api_20261001_resources_performance_review_visibility_settings_id_body = cls(
            restrict_answers_visibility_to_reportees=restrict_answers_visibility_to_reportees,
            early_access_to_answers_for_managers=early_access_to_answers_for_managers,
            anonymous_peer_evaluation_for_target=anonymous_peer_evaluation_for_target,
            id=id,
            performance_review_process_id=performance_review_process_id,
        )

        put_api_20261001_resources_performance_review_visibility_settings_id_body.additional_properties = d
        return put_api_20261001_resources_performance_review_visibility_settings_id_body

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
