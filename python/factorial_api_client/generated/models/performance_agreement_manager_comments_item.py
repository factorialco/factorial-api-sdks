from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PerformanceAgreementManagerCommentsItem")


@_attrs_define
class PerformanceAgreementManagerCommentsItem:
    question_uuid: str
    author_access_id: str
    text: str
    updated_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        question_uuid = self.question_uuid

        author_access_id = self.author_access_id

        text = self.text

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "question_uuid": question_uuid,
                "author_access_id": author_access_id,
                "text": text,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        question_uuid = d.pop("question_uuid")

        author_access_id = d.pop("author_access_id")

        text = d.pop("text")

        updated_at = d.pop("updated_at")

        performance_agreement_manager_comments_item = cls(
            question_uuid=question_uuid,
            author_access_id=author_access_id,
            text=text,
            updated_at=updated_at,
        )

        performance_agreement_manager_comments_item.additional_properties = d
        return performance_agreement_manager_comments_item

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
