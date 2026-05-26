from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.post_api_20251001_resources_ats_messages_body_sent_by_type import (
    PostApi20251001ResourcesAtsMessagesBodySentByType,
)
from ..types import UNSET, File, Unset

T = TypeVar("T", bound="PostApi20251001ResourcesAtsMessagesBody")


@_attrs_define
class PostApi20251001ResourcesAtsMessagesBody:
    content: str
    sent_by_id: int
    sent_by_type: PostApi20251001ResourcesAtsMessagesBodySentByType
    ats_application_id: int
    attachments: list[File]
    topic: str
    send_as_corporate_email: bool
    delayed_until: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content = self.content

        sent_by_id = self.sent_by_id

        sent_by_type = self.sent_by_type.value

        ats_application_id = self.ats_application_id

        attachments = []
        for attachments_item_data in self.attachments:
            attachments_item = attachments_item_data.to_tuple()

            attachments.append(attachments_item)

        topic = self.topic

        send_as_corporate_email = self.send_as_corporate_email

        delayed_until = self.delayed_until

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content": content,
                "sent_by_id": sent_by_id,
                "sent_by_type": sent_by_type,
                "ats_application_id": ats_application_id,
                "attachments[]": attachments,
                "topic": topic,
                "send_as_corporate_email": send_as_corporate_email,
            }
        )
        if delayed_until is not UNSET:
            field_dict["delayed_until"] = delayed_until

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("content", (None, str(self.content).encode(), "text/plain")))

        files.append(("sent_by_id", (None, str(self.sent_by_id).encode(), "text/plain")))

        files.append(("sent_by_type", (None, str(self.sent_by_type.value).encode(), "text/plain")))

        files.append(
            ("ats_application_id", (None, str(self.ats_application_id).encode(), "text/plain"))
        )

        for attachments_item_element in self.attachments:
            files.append(("attachments[]", attachments_item_element.to_tuple()))

        files.append(("topic", (None, str(self.topic).encode(), "text/plain")))

        files.append(
            (
                "send_as_corporate_email",
                (None, str(self.send_as_corporate_email).encode(), "text/plain"),
            )
        )

        if not isinstance(self.delayed_until, Unset):
            files.append(("delayed_until", (None, str(self.delayed_until).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        content = d.pop("content")

        sent_by_id = d.pop("sent_by_id")

        sent_by_type = PostApi20251001ResourcesAtsMessagesBodySentByType(d.pop("sent_by_type"))

        ats_application_id = d.pop("ats_application_id")

        attachments = []
        _attachments = d.pop("attachments[]")
        for attachments_item_data in _attachments:
            attachments_item = File(payload=BytesIO(attachments_item_data))

            attachments.append(attachments_item)

        topic = d.pop("topic")

        send_as_corporate_email = d.pop("send_as_corporate_email")

        delayed_until = d.pop("delayed_until", UNSET)

        post_api_20251001_resources_ats_messages_body = cls(
            content=content,
            sent_by_id=sent_by_id,
            sent_by_type=sent_by_type,
            ats_application_id=ats_application_id,
            attachments=attachments,
            topic=topic,
            send_as_corporate_email=send_as_corporate_email,
            delayed_until=delayed_until,
        )

        post_api_20251001_resources_ats_messages_body.additional_properties = d
        return post_api_20251001_resources_ats_messages_body

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
