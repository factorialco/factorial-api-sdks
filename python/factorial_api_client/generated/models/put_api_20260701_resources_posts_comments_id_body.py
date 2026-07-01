from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PutApi20260701ResourcesPostsCommentsIdBody")


@_attrs_define
class PutApi20260701ResourcesPostsCommentsIdBody:
    id: str
    """ identifier of the comment """
    post_id: str
    """ identifier of the post """
    text: str
    """ Text of the comment """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        post_id = self.post_id

        text = self.text

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "post_id": post_id,
                "text": text,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        post_id = d.pop("post_id")

        text = d.pop("text")

        put_api_20260701_resources_posts_comments_id_body = cls(
            id=id,
            post_id=post_id,
            text=text,
        )

        put_api_20260701_resources_posts_comments_id_body.additional_properties = d
        return put_api_20260701_resources_posts_comments_id_body

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
