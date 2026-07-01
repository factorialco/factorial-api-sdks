from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PutApi20260701ResourcesProjectManagementPlannedRecordsIdBody")


@_attrs_define
class PutApi20260701ResourcesProjectManagementPlannedRecordsIdBody:
    id: str
    """ The id of the planned record to update """
    start_date: str
    """ The start date to update the planned record for """
    end_date: str
    """ The end date to update the planned record for """
    daily_minutes: int
    """ The daily minutes to update the planned record for """
    project_worker_id: str | Unset = UNSET
    """ The project worker id to update the planned record for """
    week_days: list[int] | Unset = UNSET
    """ The week days to update the planned record for, start in Sunday 0 and end in Saturday 6 """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        start_date = self.start_date

        end_date = self.end_date

        daily_minutes = self.daily_minutes

        project_worker_id = self.project_worker_id

        week_days: list[int] | Unset = UNSET
        if not isinstance(self.week_days, Unset):
            week_days = self.week_days

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "start_date": start_date,
                "end_date": end_date,
                "daily_minutes": daily_minutes,
            }
        )
        if project_worker_id is not UNSET:
            field_dict["project_worker_id"] = project_worker_id
        if week_days is not UNSET:
            field_dict["week_days"] = week_days

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        start_date = d.pop("start_date")

        end_date = d.pop("end_date")

        daily_minutes = d.pop("daily_minutes")

        project_worker_id = d.pop("project_worker_id", UNSET)

        week_days = cast(list[int], d.pop("week_days", UNSET))

        put_api_20260701_resources_project_management_planned_records_id_body = cls(
            id=id,
            start_date=start_date,
            end_date=end_date,
            daily_minutes=daily_minutes,
            project_worker_id=project_worker_id,
            week_days=week_days,
        )

        put_api_20260701_resources_project_management_planned_records_id_body.additional_properties = d
        return put_api_20260701_resources_project_management_planned_records_id_body

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
