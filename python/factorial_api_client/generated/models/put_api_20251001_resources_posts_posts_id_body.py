from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PutApi20251001ResourcesPostsPostsIdBody")


@_attrs_define
class PutApi20251001ResourcesPostsPostsIdBody:
    id: int
    """ identifier of the post """
    title: str | Unset = UNSET
    """ title of the post """
    description: str | Unset = UNSET
    """ description of the post """
    post_group_id: int | Unset = UNSET
    """ group identifier of the post, references to posts/groups endpoint """
    allow_comments_and_reactions: bool | Unset = UNSET
    """ allow comments and reactions on the post """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        description = self.description

        post_group_id = self.post_group_id

        allow_comments_and_reactions = self.allow_comments_and_reactions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if post_group_id is not UNSET:
            field_dict["post_group_id"] = post_group_id
        if allow_comments_and_reactions is not UNSET:
            field_dict["allow_comments_and_reactions"] = allow_comments_and_reactions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        post_group_id = d.pop("post_group_id", UNSET)

        allow_comments_and_reactions = d.pop("allow_comments_and_reactions", UNSET)

        put_api_20251001_resources_posts_posts_id_body = cls(
            id=id,
            title=title,
            description=description,
            post_group_id=post_group_id,
            allow_comments_and_reactions=allow_comments_and_reactions,
        )

        put_api_20251001_resources_posts_posts_id_body.additional_properties = d
        return put_api_20251001_resources_posts_posts_id_body

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
