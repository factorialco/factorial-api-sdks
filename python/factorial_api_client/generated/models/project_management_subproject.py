from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.project_management_subproject_status import ProjectManagementSubprojectStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectManagementSubproject")


@_attrs_define
class ProjectManagementSubproject:
    name: str
    """ The name of the subproject """
    project_id: str
    """ The id of the project """
    status: ProjectManagementSubprojectStatus
    """ The status of the subproject """
    id: str | Unset = UNSET
    """ The id of the subproject """
    inputed_minutes: int | Unset = UNSET
    """ The total minutes tracked in the subproject (if requested) """
    labor_cost_cents: int | Unset = UNSET
    """ The total labor cost of the subproject in cents (if requested) """
    description: str | Unset = UNSET
    """ The description of the subproject """
    code: str | Unset = UNSET
    """ The code of the subproject """
    start_date: str | Unset = UNSET
    """ The start date of the subproject """
    due_date: str | Unset = UNSET
    """ The due date of the subproject """
    is_billable: bool | Unset = UNSET
    """ Whether the subproject is billable """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        project_id = self.project_id

        status = self.status.value

        id = self.id

        inputed_minutes = self.inputed_minutes

        labor_cost_cents = self.labor_cost_cents

        description = self.description

        code = self.code

        start_date = self.start_date

        due_date = self.due_date

        is_billable = self.is_billable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "project_id": project_id,
                "status": status,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if inputed_minutes is not UNSET:
            field_dict["inputed_minutes"] = inputed_minutes
        if labor_cost_cents is not UNSET:
            field_dict["labor_cost_cents"] = labor_cost_cents
        if description is not UNSET:
            field_dict["description"] = description
        if code is not UNSET:
            field_dict["code"] = code
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if due_date is not UNSET:
            field_dict["due_date"] = due_date
        if is_billable is not UNSET:
            field_dict["is_billable"] = is_billable

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        project_id = d.pop("project_id")

        status = ProjectManagementSubprojectStatus(d.pop("status"))

        id = d.pop("id", UNSET)

        inputed_minutes = d.pop("inputed_minutes", UNSET)

        labor_cost_cents = d.pop("labor_cost_cents", UNSET)

        description = d.pop("description", UNSET)

        code = d.pop("code", UNSET)

        start_date = d.pop("start_date", UNSET)

        due_date = d.pop("due_date", UNSET)

        is_billable = d.pop("is_billable", UNSET)

        project_management_subproject = cls(
            name=name,
            project_id=project_id,
            status=status,
            id=id,
            inputed_minutes=inputed_minutes,
            labor_cost_cents=labor_cost_cents,
            description=description,
            code=code,
            start_date=start_date,
            due_date=due_date,
            is_billable=is_billable,
        )

        project_management_subproject.additional_properties = d
        return project_management_subproject

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
