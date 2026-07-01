from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20260701ResourcesTrainingsSessionAccessMembershipsBulkCreateBody")


@_attrs_define
class PostApi20260701ResourcesTrainingsSessionAccessMembershipsBulkCreateBody:
    session_id: str
    notify: bool
    access_ids: list[str] | Unset = UNSET
    employee_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        session_id = self.session_id

        notify = self.notify

        access_ids: list[str] | Unset = UNSET
        if not isinstance(self.access_ids, Unset):
            access_ids = self.access_ids

        employee_ids: list[str] | Unset = UNSET
        if not isinstance(self.employee_ids, Unset):
            employee_ids = self.employee_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "session_id": session_id,
                "notify": notify,
            }
        )
        if access_ids is not UNSET:
            field_dict["access_ids"] = access_ids
        if employee_ids is not UNSET:
            field_dict["employee_ids"] = employee_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        session_id = d.pop("session_id")

        notify = d.pop("notify")

        access_ids = cast(list[str], d.pop("access_ids", UNSET))

        employee_ids = cast(list[str], d.pop("employee_ids", UNSET))

        post_api_20260701_resources_trainings_session_access_memberships_bulk_create_body = cls(
            session_id=session_id,
            notify=notify,
            access_ids=access_ids,
            employee_ids=employee_ids,
        )

        post_api_20260701_resources_trainings_session_access_memberships_bulk_create_body.additional_properties = d
        return post_api_20260701_resources_trainings_session_access_memberships_bulk_create_body

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
