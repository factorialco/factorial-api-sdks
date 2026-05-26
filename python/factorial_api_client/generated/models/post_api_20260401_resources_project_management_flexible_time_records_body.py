from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20260401ResourcesProjectManagementFlexibleTimeRecordsBody")


@_attrs_define
class PostApi20260401ResourcesProjectManagementFlexibleTimeRecordsBody:
    project_worker_id: int
    date: str
    imputed_minutes: int
    subproject_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_worker_id = self.project_worker_id

        date = self.date

        imputed_minutes = self.imputed_minutes

        subproject_id = self.subproject_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "project_worker_id": project_worker_id,
                "date": date,
                "imputed_minutes": imputed_minutes,
            }
        )
        if subproject_id is not UNSET:
            field_dict["subproject_id"] = subproject_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        project_worker_id = d.pop("project_worker_id")

        date = d.pop("date")

        imputed_minutes = d.pop("imputed_minutes")

        subproject_id = d.pop("subproject_id", UNSET)

        post_api_20260401_resources_project_management_flexible_time_records_body = cls(
            project_worker_id=project_worker_id,
            date=date,
            imputed_minutes=imputed_minutes,
            subproject_id=subproject_id,
        )

        post_api_20260401_resources_project_management_flexible_time_records_body.additional_properties = d
        return post_api_20260401_resources_project_management_flexible_time_records_body

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
