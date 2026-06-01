from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectManagementPlannedRecord")


@_attrs_define
class ProjectManagementPlannedRecord:
    id: int
    """ The id of the planned record """
    daily_minutes: int
    """ The daily minutes of the planned record """
    start_date: str
    """ The start date of the planned record """
    end_date: str
    """ The end date of the planned record """
    project_worker_id: int
    """ The project worker id of the planned record """
    week_days: list[int]
    """ The week days of the planned record, start in Sunday 0 and end in Saturday 6 """
    subproject_id: int | Unset = UNSET
    """ The subproject id of the planned record """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        daily_minutes = self.daily_minutes

        start_date = self.start_date

        end_date = self.end_date

        project_worker_id = self.project_worker_id

        week_days = self.week_days

        subproject_id = self.subproject_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "daily_minutes": daily_minutes,
                "start_date": start_date,
                "end_date": end_date,
                "project_worker_id": project_worker_id,
                "week_days": week_days,
            }
        )
        if subproject_id is not UNSET:
            field_dict["subproject_id"] = subproject_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        daily_minutes = d.pop("daily_minutes")

        start_date = d.pop("start_date")

        end_date = d.pop("end_date")

        project_worker_id = d.pop("project_worker_id")

        week_days = cast(list[int], d.pop("week_days"))

        subproject_id = d.pop("subproject_id", UNSET)

        project_management_planned_record = cls(
            id=id,
            daily_minutes=daily_minutes,
            start_date=start_date,
            end_date=end_date,
            project_worker_id=project_worker_id,
            week_days=week_days,
            subproject_id=subproject_id,
        )

        project_management_planned_record.additional_properties = d
        return project_management_planned_record

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
