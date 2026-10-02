from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PerformanceAgreementConclusions")


@_attrs_define
class PerformanceAgreementConclusions:
    """Conclusions of the action plan

    Example:
        {'text': 'The employee is doing well.', 'last_updated_at': '2024-01-01T00:00:00Z'}

    """

    text: str
    last_updated_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        text = self.text

        last_updated_at = self.last_updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "text": text,
                "last_updated_at": last_updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        text = d.pop("text")

        last_updated_at = d.pop("last_updated_at")

        performance_agreement_conclusions = cls(
            text=text,
            last_updated_at=last_updated_at,
        )

        performance_agreement_conclusions.additional_properties = d
        return performance_agreement_conclusions

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
