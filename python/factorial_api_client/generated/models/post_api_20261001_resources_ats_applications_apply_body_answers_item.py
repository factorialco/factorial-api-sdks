from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20261001ResourcesAtsApplicationsApplyBodyAnswersItem")


@_attrs_define
class PostApi20261001ResourcesAtsApplicationsApplyBodyAnswersItem:
    ats_question_id: str
    value: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ats_question_id = self.ats_question_id

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ats_question_id": ats_question_id,
            }
        )
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ats_question_id = d.pop("ats_question_id")

        value = d.pop("value", UNSET)

        post_api_20261001_resources_ats_applications_apply_body_answers_item = cls(
            ats_question_id=ats_question_id,
            value=value,
        )

        post_api_20261001_resources_ats_applications_apply_body_answers_item.additional_properties = d
        return post_api_20261001_resources_ats_applications_apply_body_answers_item

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
