from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ProjectManagementSubprojectWorker")


@_attrs_define
class ProjectManagementSubprojectWorker:
    id: str
    """ id of the subproject worker. """
    subproject_id: str
    """ id of the subproject (phase). """
    project_id: str
    """ id of the project owning the subproject. """
    project_worker_id: str
    """ id of the project worker. """
    employee_id: str
    """ id of the employee. """
    assigned: bool
    """ true if the employee is assigned to the subproject, false otherwise. """
    company_id: str
    """ id of the company that owns the subproject worker. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        subproject_id = self.subproject_id

        project_id = self.project_id

        project_worker_id = self.project_worker_id

        employee_id = self.employee_id

        assigned = self.assigned

        company_id = self.company_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "subproject_id": subproject_id,
                "project_id": project_id,
                "project_worker_id": project_worker_id,
                "employee_id": employee_id,
                "assigned": assigned,
                "company_id": company_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        subproject_id = d.pop("subproject_id")

        project_id = d.pop("project_id")

        project_worker_id = d.pop("project_worker_id")

        employee_id = d.pop("employee_id")

        assigned = d.pop("assigned")

        company_id = d.pop("company_id")

        project_management_subproject_worker = cls(
            id=id,
            subproject_id=subproject_id,
            project_id=project_id,
            project_worker_id=project_worker_id,
            employee_id=employee_id,
            assigned=assigned,
            company_id=company_id,
        )

        project_management_subproject_worker.additional_properties = d
        return project_management_subproject_worker

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
