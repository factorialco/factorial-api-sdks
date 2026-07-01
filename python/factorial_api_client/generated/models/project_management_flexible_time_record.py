from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectManagementFlexibleTimeRecord")


@_attrs_define
class ProjectManagementFlexibleTimeRecord:
    id: str
    """ The unique identifier of the flexible time record. """
    date: str
    """ The date on which the time was imputed. """
    imputed_minutes: int
    """ The amount of time imputed to the project, in minutes. """
    project_worker_id: str
    """ The ID of the project worker associated with this flexible time record. """
    subproject_id: str | Unset = UNSET
    """ The ID of the subproject worked on, if any. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        date = self.date

        imputed_minutes = self.imputed_minutes

        project_worker_id = self.project_worker_id

        subproject_id = self.subproject_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "date": date,
                "imputed_minutes": imputed_minutes,
                "project_worker_id": project_worker_id,
            }
        )
        if subproject_id is not UNSET:
            field_dict["subproject_id"] = subproject_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        date = d.pop("date")

        imputed_minutes = d.pop("imputed_minutes")

        project_worker_id = d.pop("project_worker_id")

        subproject_id = d.pop("subproject_id", UNSET)

        project_management_flexible_time_record = cls(
            id=id,
            date=date,
            imputed_minutes=imputed_minutes,
            project_worker_id=project_worker_id,
            subproject_id=subproject_id,
        )

        project_management_flexible_time_record.additional_properties = d
        return project_management_flexible_time_record

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
