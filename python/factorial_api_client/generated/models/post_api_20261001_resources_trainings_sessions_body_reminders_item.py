from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_api_20261001_resources_trainings_sessions_body_reminders_item_timeframe import (
    PostApi20261001ResourcesTrainingsSessionsBodyRemindersItemTimeframe,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20261001ResourcesTrainingsSessionsBodyRemindersItem")


@_attrs_define
class PostApi20261001ResourcesTrainingsSessionsBodyRemindersItem:
    name: str
    session_id: str | Unset = UNSET
    content: str | Unset = UNSET
    scheduled_at: str | Unset = UNSET
    timeframe: PostApi20261001ResourcesTrainingsSessionsBodyRemindersItemTimeframe | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        session_id = self.session_id

        content = self.content

        scheduled_at = self.scheduled_at

        timeframe: str | Unset = UNSET
        if not isinstance(self.timeframe, Unset):
            timeframe = self.timeframe.value if self.timeframe is not None else None

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if session_id is not UNSET:
            field_dict["session_id"] = session_id
        if content is not UNSET:
            field_dict["content"] = content
        if scheduled_at is not UNSET:
            field_dict["scheduled_at"] = scheduled_at
        if timeframe is not UNSET:
            field_dict["timeframe"] = timeframe

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        session_id = d.pop("session_id", UNSET)

        content = d.pop("content", UNSET)

        scheduled_at = d.pop("scheduled_at", UNSET)

        _timeframe = d.pop("timeframe", UNSET)
        timeframe: PostApi20261001ResourcesTrainingsSessionsBodyRemindersItemTimeframe | Unset
        if isinstance(_timeframe, Unset):
            timeframe = UNSET
        else:
            timeframe = PostApi20261001ResourcesTrainingsSessionsBodyRemindersItemTimeframe(
                _timeframe
            ) if _timeframe is not None else None

        post_api_20261001_resources_trainings_sessions_body_reminders_item = cls(
            name=name,
            session_id=session_id,
            content=content,
            scheduled_at=scheduled_at,
            timeframe=timeframe,
        )

        post_api_20261001_resources_trainings_sessions_body_reminders_item.additional_properties = d
        return post_api_20261001_resources_trainings_sessions_body_reminders_item

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
