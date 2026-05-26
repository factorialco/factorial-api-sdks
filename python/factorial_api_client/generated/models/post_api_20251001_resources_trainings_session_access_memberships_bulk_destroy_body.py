from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostApi20251001ResourcesTrainingsSessionAccessMembershipsBulkDestroyBody")


@_attrs_define
class PostApi20251001ResourcesTrainingsSessionAccessMembershipsBulkDestroyBody:
    ids: list[int]
    notify: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ids = self.ids

        notify = self.notify

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ids": ids,
                "notify": notify,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ids = cast(list[int], d.pop("ids"))

        notify = d.pop("notify")

        post_api_20251001_resources_trainings_session_access_memberships_bulk_destroy_body = cls(
            ids=ids,
            notify=notify,
        )

        post_api_20251001_resources_trainings_session_access_memberships_bulk_destroy_body.additional_properties = d
        return post_api_20251001_resources_trainings_session_access_memberships_bulk_destroy_body

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
