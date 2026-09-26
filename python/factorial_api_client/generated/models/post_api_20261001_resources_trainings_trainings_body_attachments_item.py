from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, File, Unset

T = TypeVar("T", bound="PostApi20261001ResourcesTrainingsTrainingsBodyAttachmentsItem")


@_attrs_define
class PostApi20261001ResourcesTrainingsTrainingsBodyAttachmentsItem:
    author_id: str
    file: File
    visibility: bool
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        author_id = self.author_id

        file = self.file.to_tuple()

        visibility = self.visibility

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "author_id": author_id,
                "file": file,
                "visibility": visibility,
            }
        )
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        author_id = d.pop("author_id")

        file = File(payload=BytesIO(d.pop("file")))

        visibility = d.pop("visibility")

        title = d.pop("title", UNSET)

        post_api_20261001_resources_trainings_trainings_body_attachments_item = cls(
            author_id=author_id,
            file=file,
            visibility=visibility,
            title=title,
        )

        post_api_20261001_resources_trainings_trainings_body_attachments_item.additional_properties = d
        return post_api_20261001_resources_trainings_trainings_body_attachments_item

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
