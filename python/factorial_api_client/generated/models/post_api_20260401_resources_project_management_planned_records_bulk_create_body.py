from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20260401ResourcesProjectManagementPlannedRecordsBulkCreateBody")


@_attrs_define
class PostApi20260401ResourcesProjectManagementPlannedRecordsBulkCreateBody:
    project_worker_ids: list[int]
    """ The project worker ids to create the planned records for """
    start_date: str
    """ The start date to create the planned records for """
    end_date: str
    """ The end date to create the planned records for """
    daily_minutes: int
    """ The daily minutes to create the planned records for """
    subproject_id: int | Unset = UNSET
    """ The subproject id to create the planned records for """
    week_days: list[int] | Unset = UNSET
    """ The week days to create the planned records for, start in Sunday 0 and end in Saturday 6 """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_worker_ids = self.project_worker_ids

        start_date = self.start_date

        end_date = self.end_date

        daily_minutes = self.daily_minutes

        subproject_id = self.subproject_id

        week_days: list[int] | Unset = UNSET
        if not isinstance(self.week_days, Unset):
            week_days = self.week_days

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "project_worker_ids": project_worker_ids,
                "start_date": start_date,
                "end_date": end_date,
                "daily_minutes": daily_minutes,
            }
        )
        if subproject_id is not UNSET:
            field_dict["subproject_id"] = subproject_id
        if week_days is not UNSET:
            field_dict["week_days"] = week_days

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        project_worker_ids = cast(list[int], d.pop("project_worker_ids"))

        start_date = d.pop("start_date")

        end_date = d.pop("end_date")

        daily_minutes = d.pop("daily_minutes")

        subproject_id = d.pop("subproject_id", UNSET)

        week_days = cast(list[int], d.pop("week_days", UNSET))

        post_api_20260401_resources_project_management_planned_records_bulk_create_body = cls(
            project_worker_ids=project_worker_ids,
            start_date=start_date,
            end_date=end_date,
            daily_minutes=daily_minutes,
            subproject_id=subproject_id,
            week_days=week_days,
        )

        post_api_20260401_resources_project_management_planned_records_bulk_create_body.additional_properties = d
        return post_api_20260401_resources_project_management_planned_records_bulk_create_body

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
