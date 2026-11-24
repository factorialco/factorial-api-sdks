from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostApi20270101ResourcesProjectManagementSubprojectWorkersBulkAssignBody")


@_attrs_define
class PostApi20270101ResourcesProjectManagementSubprojectWorkersBulkAssignBody:
    subproject_id: str
    """ The id of the subproject whose assignment is being replaced. """
    employee_ids: list[str]
    """ Set of employee_ids that must be **assigned** to the subproject after execution. All the employees in the
    list will be assigned and all others will be unassigned. Every employee must be an assigned project worker of
    the project owning the subproject. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        subproject_id = self.subproject_id

        employee_ids = self.employee_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "subproject_id": subproject_id,
                "employee_ids": employee_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        subproject_id = d.pop("subproject_id")

        employee_ids = cast(list[str], d.pop("employee_ids"))

        post_api_20270101_resources_project_management_subproject_workers_bulk_assign_body = cls(
            subproject_id=subproject_id,
            employee_ids=employee_ids,
        )

        post_api_20270101_resources_project_management_subproject_workers_bulk_assign_body.additional_properties = d
        return post_api_20270101_resources_project_management_subproject_workers_bulk_assign_body

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
