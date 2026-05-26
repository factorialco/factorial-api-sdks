from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostsPost")


@_attrs_define
class PostsPost:
    id: int
    """ identifiers of the post """
    allow_comments_and_reactions: bool
    """ allow comments and reactions on the post """
    published_at: str
    """ date when the post has been published """
    created_at: str
    """ date when the post has been created """
    updated_at: str
    """ date when the post has been updated """
    visits_count: int
    """ number of visits of the post """
    comments_count: int
    title: str | Unset = UNSET
    """ title of the post """
    description: str | Unset = UNSET
    """ description of the post """
    cover_image_url: str | Unset = UNSET
    """ url of the cover image """
    posts_group_id: int | Unset = UNSET
    """ group identifier of the post, references to posts/groups endpoint """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        allow_comments_and_reactions = self.allow_comments_and_reactions

        published_at = self.published_at

        created_at = self.created_at

        updated_at = self.updated_at

        visits_count = self.visits_count

        comments_count = self.comments_count

        title = self.title

        description = self.description

        cover_image_url = self.cover_image_url

        posts_group_id = self.posts_group_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "allow_comments_and_reactions": allow_comments_and_reactions,
                "published_at": published_at,
                "created_at": created_at,
                "updated_at": updated_at,
                "visits_count": visits_count,
                "comments_count": comments_count,
            }
        )
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if cover_image_url is not UNSET:
            field_dict["cover_image_url"] = cover_image_url
        if posts_group_id is not UNSET:
            field_dict["posts_group_id"] = posts_group_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        allow_comments_and_reactions = d.pop("allow_comments_and_reactions")

        published_at = d.pop("published_at")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        visits_count = d.pop("visits_count")

        comments_count = d.pop("comments_count")

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        cover_image_url = d.pop("cover_image_url", UNSET)

        posts_group_id = d.pop("posts_group_id", UNSET)

        posts_post = cls(
            id=id,
            allow_comments_and_reactions=allow_comments_and_reactions,
            published_at=published_at,
            created_at=created_at,
            updated_at=updated_at,
            visits_count=visits_count,
            comments_count=comments_count,
            title=title,
            description=description,
            cover_image_url=cover_image_url,
            posts_group_id=posts_group_id,
        )

        posts_post.additional_properties = d
        return posts_post

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
