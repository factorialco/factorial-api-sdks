from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.project_management_project_employees_assignment import (
    ProjectManagementProjectEmployeesAssignment,
)
from ..models.project_management_project_status import ProjectManagementProjectStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectManagementProject")


@_attrs_define
class ProjectManagementProject:
    id: int
    """ The id of the project """
    name: str
    """ The name of the project """
    status: ProjectManagementProjectStatus
    """ The status of the project """
    employees_assignment: ProjectManagementProjectEmployeesAssignment
    """ The employees assigment of the project """
    is_billable: bool
    """ Check if the projects is billable """
    legal_entity_id: int
    """ The legal entity id of the project """
    code: str | Unset = UNSET
    """ The code of the project """
    description: str | Unset = UNSET
    """ The description of the project """
    start_date: str | Unset = UNSET
    """ The start date of the project """
    due_date: str | Unset = UNSET
    """ The end date of the project """
    inputed_minutes: int | Unset = UNSET
    """ The total minutes tracked in the project (if requested) """
    fixed_cost_cents: int | Unset = UNSET
    """ Total fixed costs in cents """
    labor_cost_cents: int | Unset = UNSET
    """ Total labor costs in cents """
    spending_cost_cents: int | Unset = UNSET
    """ Total spending costs in cents """
    client_id: int | Unset = UNSET
    """ The client of the project, refers to finance/contacts. """
    total_cost_cents: int | Unset = UNSET
    """ Total Cost in cents """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        status = self.status.value

        employees_assignment = self.employees_assignment.value

        is_billable = self.is_billable

        legal_entity_id = self.legal_entity_id

        code = self.code

        description = self.description

        start_date = self.start_date

        due_date = self.due_date

        inputed_minutes = self.inputed_minutes

        fixed_cost_cents = self.fixed_cost_cents

        labor_cost_cents = self.labor_cost_cents

        spending_cost_cents = self.spending_cost_cents

        client_id = self.client_id

        total_cost_cents = self.total_cost_cents

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "status": status,
                "employees_assignment": employees_assignment,
                "is_billable": is_billable,
                "legal_entity_id": legal_entity_id,
            }
        )
        if code is not UNSET:
            field_dict["code"] = code
        if description is not UNSET:
            field_dict["description"] = description
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if due_date is not UNSET:
            field_dict["due_date"] = due_date
        if inputed_minutes is not UNSET:
            field_dict["inputed_minutes"] = inputed_minutes
        if fixed_cost_cents is not UNSET:
            field_dict["fixed_cost_cents"] = fixed_cost_cents
        if labor_cost_cents is not UNSET:
            field_dict["labor_cost_cents"] = labor_cost_cents
        if spending_cost_cents is not UNSET:
            field_dict["spending_cost_cents"] = spending_cost_cents
        if client_id is not UNSET:
            field_dict["client_id"] = client_id
        if total_cost_cents is not UNSET:
            field_dict["total_cost_cents"] = total_cost_cents

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        status = ProjectManagementProjectStatus(d.pop("status"))

        employees_assignment = ProjectManagementProjectEmployeesAssignment(
            d.pop("employees_assignment")
        )

        is_billable = d.pop("is_billable")

        legal_entity_id = d.pop("legal_entity_id")

        code = d.pop("code", UNSET)

        description = d.pop("description", UNSET)

        start_date = d.pop("start_date", UNSET)

        due_date = d.pop("due_date", UNSET)

        inputed_minutes = d.pop("inputed_minutes", UNSET)

        fixed_cost_cents = d.pop("fixed_cost_cents", UNSET)

        labor_cost_cents = d.pop("labor_cost_cents", UNSET)

        spending_cost_cents = d.pop("spending_cost_cents", UNSET)

        client_id = d.pop("client_id", UNSET)

        total_cost_cents = d.pop("total_cost_cents", UNSET)

        project_management_project = cls(
            id=id,
            name=name,
            status=status,
            employees_assignment=employees_assignment,
            is_billable=is_billable,
            legal_entity_id=legal_entity_id,
            code=code,
            description=description,
            start_date=start_date,
            due_date=due_date,
            inputed_minutes=inputed_minutes,
            fixed_cost_cents=fixed_cost_cents,
            labor_cost_cents=labor_cost_cents,
            spending_cost_cents=spending_cost_cents,
            client_id=client_id,
            total_cost_cents=total_cost_cents,
        )

        project_management_project.additional_properties = d
        return project_management_project

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
