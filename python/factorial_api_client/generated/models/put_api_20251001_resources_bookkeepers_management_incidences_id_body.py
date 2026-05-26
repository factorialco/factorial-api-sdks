from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PutApi20251001ResourcesBookkeepersManagementIncidencesIdBody")


@_attrs_define
class PutApi20251001ResourcesBookkeepersManagementIncidencesIdBody:
    id: int
    """ incidence (aka employee update) identifier to update. """
    status: str | Unset = UNSET
    """ status of the incidence (aka employee update). It can be any of 'in-preparation', 'to-do', 'doing', 'done',
    'discarded' """
    has_message: bool | Unset = UNSET
    """ Boolean that indicates is the incidence (aka employee update) has message """
    message_from: str | Unset = UNSET
    read_at: str | Unset = UNSET
    """ Date in which the  incidence (aka employee update) was read """
    mark_as_read: bool | Unset = UNSET
    """ Boolean that indicate if the incidence is read """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        status = self.status

        has_message = self.has_message

        message_from = self.message_from

        read_at = self.read_at

        mark_as_read = self.mark_as_read

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status
        if has_message is not UNSET:
            field_dict["has_message"] = has_message
        if message_from is not UNSET:
            field_dict["message_from"] = message_from
        if read_at is not UNSET:
            field_dict["read_at"] = read_at
        if mark_as_read is not UNSET:
            field_dict["mark_as_read"] = mark_as_read

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        status = d.pop("status", UNSET)

        has_message = d.pop("has_message", UNSET)

        message_from = d.pop("message_from", UNSET)

        read_at = d.pop("read_at", UNSET)

        mark_as_read = d.pop("mark_as_read", UNSET)

        put_api_20251001_resources_bookkeepers_management_incidences_id_body = cls(
            id=id,
            status=status,
            has_message=has_message,
            message_from=message_from,
            read_at=read_at,
            mark_as_read=mark_as_read,
        )

        put_api_20251001_resources_bookkeepers_management_incidences_id_body.additional_properties = d
        return put_api_20251001_resources_bookkeepers_management_incidences_id_body

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
