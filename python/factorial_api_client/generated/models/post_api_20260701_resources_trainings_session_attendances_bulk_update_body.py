from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20260701ResourcesTrainingsSessionAttendancesBulkUpdateBody")


@_attrs_define
class PostApi20260701ResourcesTrainingsSessionAttendancesBulkUpdateBody:
    ids: list[str]
    """ List of session attendance IDs to update """
    status: str | Unset = UNSET
    """ New status for the session attendances """
    completed_duration: str | Unset = UNSET
    """ Completed duration in hours (decimal format, e.g. 1.5 means 1h 30m) """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ids = self.ids

        status = self.status

        completed_duration = self.completed_duration

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ids": ids,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status
        if completed_duration is not UNSET:
            field_dict["completed_duration"] = completed_duration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ids = cast(list[str], d.pop("ids"))

        status = d.pop("status", UNSET)

        completed_duration = d.pop("completed_duration", UNSET)

        post_api_20260701_resources_trainings_session_attendances_bulk_update_body = cls(
            ids=ids,
            status=status,
            completed_duration=completed_duration,
        )

        post_api_20260701_resources_trainings_session_attendances_bulk_update_body.additional_properties = d
        return post_api_20260701_resources_trainings_session_attendances_bulk_update_body

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
