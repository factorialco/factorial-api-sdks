from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkScheduleSchedule")


@_attrs_define
class WorkScheduleSchedule:
    id: int
    name: str
    company_id: int
    created_at: str
    updated_at: str
    employee_ids: list[int]
    periods: list[Any]
    archived_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        company_id = self.company_id

        created_at = self.created_at

        updated_at = self.updated_at

        employee_ids = self.employee_ids

        periods = self.periods

        archived_at = self.archived_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "company_id": company_id,
                "created_at": created_at,
                "updated_at": updated_at,
                "employee_ids": employee_ids,
                "periods": periods,
            }
        )
        if archived_at is not UNSET:
            field_dict["archived_at"] = archived_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        company_id = d.pop("company_id")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        employee_ids = cast(list[int], d.pop("employee_ids"))

        periods = cast(list[Any], d.pop("periods"))

        archived_at = d.pop("archived_at", UNSET)

        work_schedule_schedule = cls(
            id=id,
            name=name,
            company_id=company_id,
            created_at=created_at,
            updated_at=updated_at,
            employee_ids=employee_ids,
            periods=periods,
            archived_at=archived_at,
        )

        work_schedule_schedule.additional_properties = d
        return work_schedule_schedule

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
