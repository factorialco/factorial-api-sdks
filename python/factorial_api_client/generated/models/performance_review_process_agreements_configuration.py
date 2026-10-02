from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PerformanceReviewProcessAgreementsConfiguration")


@_attrs_define
class PerformanceReviewProcessAgreementsConfiguration:
    """Action plans help track goal progress, and facilitate performance review discussions.

    Example:
        {'enabled': True}

    """

    enabled: bool
    esignature_enabled: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        esignature_enabled = self.esignature_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enabled": enabled,
                "esignature_enabled": esignature_enabled,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("enabled")

        esignature_enabled = d.pop("esignature_enabled")

        performance_review_process_agreements_configuration = cls(
            enabled=enabled,
            esignature_enabled=esignature_enabled,
        )

        performance_review_process_agreements_configuration.additional_properties = d
        return performance_review_process_agreements_configuration

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
