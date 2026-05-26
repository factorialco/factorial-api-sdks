from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EmployeeUpdatesSummary")


@_attrs_define
class EmployeeUpdatesSummary:
    id: int
    legal_entity_id: int
    status: str
    type_: str
    created_at: str
    employee_id: int | Unset = UNSET
    starts_on: str | Unset = UNSET
    ends_on: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        legal_entity_id = self.legal_entity_id

        status = self.status

        type_ = self.type_

        created_at = self.created_at

        employee_id = self.employee_id

        starts_on = self.starts_on

        ends_on = self.ends_on

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "legal_entity_id": legal_entity_id,
                "status": status,
                "type": type_,
                "created_at": created_at,
            }
        )
        if employee_id is not UNSET:
            field_dict["employee_id"] = employee_id
        if starts_on is not UNSET:
            field_dict["starts_on"] = starts_on
        if ends_on is not UNSET:
            field_dict["ends_on"] = ends_on

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        legal_entity_id = d.pop("legal_entity_id")

        status = d.pop("status")

        type_ = d.pop("type")

        created_at = d.pop("created_at")

        employee_id = d.pop("employee_id", UNSET)

        starts_on = d.pop("starts_on", UNSET)

        ends_on = d.pop("ends_on", UNSET)

        employee_updates_summary = cls(
            id=id,
            legal_entity_id=legal_entity_id,
            status=status,
            type_=type_,
            created_at=created_at,
            employee_id=employee_id,
            starts_on=starts_on,
            ends_on=ends_on,
        )

        employee_updates_summary.additional_properties = d
        return employee_updates_summary

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
