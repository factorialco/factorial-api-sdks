from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PutApi20261001ResourcesAtsQuestionsIdBodyOptionsItem")


@_attrs_define
class PutApi20261001ResourcesAtsQuestionsIdBodyOptionsItem:
    text: str
    disqualifies: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        text = self.text

        disqualifies = self.disqualifies

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "text": text,
            }
        )
        if disqualifies is not UNSET:
            field_dict["disqualifies"] = disqualifies

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        text = d.pop("text")

        disqualifies = d.pop("disqualifies", UNSET)

        put_api_20261001_resources_ats_questions_id_body_options_item = cls(
            text=text,
            disqualifies=disqualifies,
        )

        put_api_20261001_resources_ats_questions_id_body_options_item.additional_properties = d
        return put_api_20261001_resources_ats_questions_id_body_options_item

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
