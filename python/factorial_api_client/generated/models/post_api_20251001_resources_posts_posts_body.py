from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20251001ResourcesPostsPostsBody")


@_attrs_define
class PostApi20251001ResourcesPostsPostsBody:
    title: str
    """ title of the post """
    description: str
    """ description of the post """
    post_group_id: int
    """ group identifier of the post, references to posts/groups endpoint """
    allow_comments_and_reactions: bool | Unset = UNSET
    """ allow comments and reactions on the post """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        description = self.description

        post_group_id = self.post_group_id

        allow_comments_and_reactions = self.allow_comments_and_reactions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "description": description,
                "post_group_id": post_group_id,
            }
        )
        if allow_comments_and_reactions is not UNSET:
            field_dict["allow_comments_and_reactions"] = allow_comments_and_reactions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title")

        description = d.pop("description")

        post_group_id = d.pop("post_group_id")

        allow_comments_and_reactions = d.pop("allow_comments_and_reactions", UNSET)

        post_api_20251001_resources_posts_posts_body = cls(
            title=title,
            description=description,
            post_group_id=post_group_id,
            allow_comments_and_reactions=allow_comments_and_reactions,
        )

        post_api_20251001_resources_posts_posts_body.additional_properties = d
        return post_api_20251001_resources_posts_posts_body

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
