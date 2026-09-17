from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ats_message_attachments_item import AtsMessageAttachmentsItem


T = TypeVar("T", bound="AtsMessage")


@_attrs_define
class AtsMessage:
    id: str
    content: str
    ats_conversation_id: str
    sent_by_id: str
    sent_by_type: str
    created_at: str
    attachments: list[AtsMessageAttachmentsItem]
    topic: str
    delayed_until: str | Unset = UNSET
    sent_at: str | Unset = UNSET
    delivered_at: str | Unset = UNSET
    opened_at: str | Unset = UNSET
    last_error_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        content = self.content

        ats_conversation_id = self.ats_conversation_id

        sent_by_id = self.sent_by_id

        sent_by_type = self.sent_by_type

        created_at = self.created_at

        attachments = []
        for attachments_item_data in self.attachments:
            attachments_item = attachments_item_data.to_dict()
            attachments.append(attachments_item)

        topic = self.topic

        delayed_until = self.delayed_until

        sent_at = self.sent_at

        delivered_at = self.delivered_at

        opened_at = self.opened_at

        last_error_at = self.last_error_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "content": content,
                "ats_conversation_id": ats_conversation_id,
                "sent_by_id": sent_by_id,
                "sent_by_type": sent_by_type,
                "created_at": created_at,
                "attachments": attachments,
                "topic": topic,
            }
        )
        if delayed_until is not UNSET:
            field_dict["delayed_until"] = delayed_until
        if sent_at is not UNSET:
            field_dict["sent_at"] = sent_at
        if delivered_at is not UNSET:
            field_dict["delivered_at"] = delivered_at
        if opened_at is not UNSET:
            field_dict["opened_at"] = opened_at
        if last_error_at is not UNSET:
            field_dict["last_error_at"] = last_error_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ats_message_attachments_item import AtsMessageAttachmentsItem

        d = dict(src_dict)
        id = d.pop("id")

        content = d.pop("content")

        ats_conversation_id = d.pop("ats_conversation_id")

        sent_by_id = d.pop("sent_by_id")

        sent_by_type = d.pop("sent_by_type")

        created_at = d.pop("created_at")

        attachments = []
        _attachments = d.pop("attachments")
        for attachments_item_data in _attachments:
            attachments_item = AtsMessageAttachmentsItem.from_dict(attachments_item_data)

            attachments.append(attachments_item)

        topic = d.pop("topic")

        delayed_until = d.pop("delayed_until", UNSET)

        sent_at = d.pop("sent_at", UNSET)

        delivered_at = d.pop("delivered_at", UNSET)

        opened_at = d.pop("opened_at", UNSET)

        last_error_at = d.pop("last_error_at", UNSET)

        ats_message = cls(
            id=id,
            content=content,
            ats_conversation_id=ats_conversation_id,
            sent_by_id=sent_by_id,
            sent_by_type=sent_by_type,
            created_at=created_at,
            attachments=attachments,
            topic=topic,
            delayed_until=delayed_until,
            sent_at=sent_at,
            delivered_at=delivered_at,
            opened_at=opened_at,
            last_error_at=last_error_at,
        )

        ats_message.additional_properties = d
        return ats_message

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
