from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PerformanceReviewProcessCustomTemplateVisibilitySettings")


@_attrs_define
class PerformanceReviewProcessCustomTemplateVisibilitySettings:
    """Visibility settings for the custom template

    Example:
        {'early_access_to_answers_for_managers': True, 'restrict_answers_visibility_to_reportees': False,
            'anonymous_peer_evaluation_for_target': False}

    """

    restrict_answers_visibility_to_reportees: bool
    early_access_to_answers_for_managers: bool
    anonymous_peer_evaluation_for_target: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        restrict_answers_visibility_to_reportees = self.restrict_answers_visibility_to_reportees

        early_access_to_answers_for_managers = self.early_access_to_answers_for_managers

        anonymous_peer_evaluation_for_target = self.anonymous_peer_evaluation_for_target

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "restrict_answers_visibility_to_reportees": restrict_answers_visibility_to_reportees,
                "early_access_to_answers_for_managers": early_access_to_answers_for_managers,
                "anonymous_peer_evaluation_for_target": anonymous_peer_evaluation_for_target,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        restrict_answers_visibility_to_reportees = d.pop("restrict_answers_visibility_to_reportees")

        early_access_to_answers_for_managers = d.pop("early_access_to_answers_for_managers")

        anonymous_peer_evaluation_for_target = d.pop("anonymous_peer_evaluation_for_target")

        performance_review_process_custom_template_visibility_settings = cls(
            restrict_answers_visibility_to_reportees=restrict_answers_visibility_to_reportees,
            early_access_to_answers_for_managers=early_access_to_answers_for_managers,
            anonymous_peer_evaluation_for_target=anonymous_peer_evaluation_for_target,
        )

        performance_review_process_custom_template_visibility_settings.additional_properties = d
        return performance_review_process_custom_template_visibility_settings

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
