from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectManagementExportableProject")


@_attrs_define
class ProjectManagementExportableProject:
    id: str
    """ The id of the project """
    project_name: str
    """ The name of the project """
    project_status: str
    """ The status of the project """
    inputed_time: str
    """ The time imputed by the employee """
    date: str | Unset = UNSET
    """ The date of imputed time """
    project_code: str | Unset = UNSET
    """ The code of the project """
    project_start_date: str | Unset = UNSET
    """ The start date of the project """
    project_due_date: str | Unset = UNSET
    """ The due date of the project """
    subproject_name: str | Unset = UNSET
    """ The name of the subproject """
    employee_name: str | Unset = UNSET
    """ The name of the employee """
    employee_id: str | Unset = UNSET
    """ The id of the employee """
    client_id: str | Unset = UNSET
    """ The client id of the project """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        project_name = self.project_name

        project_status = self.project_status

        inputed_time = self.inputed_time

        date = self.date

        project_code = self.project_code

        project_start_date = self.project_start_date

        project_due_date = self.project_due_date

        subproject_name = self.subproject_name

        employee_name = self.employee_name

        employee_id = self.employee_id

        client_id = self.client_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "project_name": project_name,
                "project_status": project_status,
                "inputed_time": inputed_time,
            }
        )
        if date is not UNSET:
            field_dict["date"] = date
        if project_code is not UNSET:
            field_dict["project_code"] = project_code
        if project_start_date is not UNSET:
            field_dict["project_start_date"] = project_start_date
        if project_due_date is not UNSET:
            field_dict["project_due_date"] = project_due_date
        if subproject_name is not UNSET:
            field_dict["subproject_name"] = subproject_name
        if employee_name is not UNSET:
            field_dict["employee_name"] = employee_name
        if employee_id is not UNSET:
            field_dict["employee_id"] = employee_id
        if client_id is not UNSET:
            field_dict["client_id"] = client_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        project_name = d.pop("project_name")

        project_status = d.pop("project_status")

        inputed_time = d.pop("inputed_time")

        date = d.pop("date", UNSET)

        project_code = d.pop("project_code", UNSET)

        project_start_date = d.pop("project_start_date", UNSET)

        project_due_date = d.pop("project_due_date", UNSET)

        subproject_name = d.pop("subproject_name", UNSET)

        employee_name = d.pop("employee_name", UNSET)

        employee_id = d.pop("employee_id", UNSET)

        client_id = d.pop("client_id", UNSET)

        project_management_exportable_project = cls(
            id=id,
            project_name=project_name,
            project_status=project_status,
            inputed_time=inputed_time,
            date=date,
            project_code=project_code,
            project_start_date=project_start_date,
            project_due_date=project_due_date,
            subproject_name=subproject_name,
            employee_name=employee_name,
            employee_id=employee_id,
            client_id=client_id,
        )

        project_management_exportable_project.additional_properties = d
        return project_management_exportable_project

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
