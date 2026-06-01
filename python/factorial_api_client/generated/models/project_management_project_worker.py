from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectManagementProjectWorker")


@_attrs_define
class ProjectManagementProjectWorker:
    id: int
    """ id of the project worker. """
    project_id: int
    """ id of the project. """
    employee_id: int
    """ id of the employee. """
    assigned: bool
    """ true if the employee is assigned to the project, false otherwise. """
    inputed_minutes: int | Unset = UNSET
    """ total inmputed minutes of the employee in the project. """
    labor_cost_cents: int | Unset = UNSET
    """ total project currency labor cost of the employee in the project. """
    company_labor_cost_cents: int | Unset = UNSET
    """ total company currency labor cost of the employee in the project. """
    spending_cost_cents: int | Unset = UNSET
    """ total spending cost of the employee in the project. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        project_id = self.project_id

        employee_id = self.employee_id

        assigned = self.assigned

        inputed_minutes = self.inputed_minutes

        labor_cost_cents = self.labor_cost_cents

        company_labor_cost_cents = self.company_labor_cost_cents

        spending_cost_cents = self.spending_cost_cents

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "project_id": project_id,
                "employee_id": employee_id,
                "assigned": assigned,
            }
        )
        if inputed_minutes is not UNSET:
            field_dict["inputed_minutes"] = inputed_minutes
        if labor_cost_cents is not UNSET:
            field_dict["labor_cost_cents"] = labor_cost_cents
        if company_labor_cost_cents is not UNSET:
            field_dict["company_labor_cost_cents"] = company_labor_cost_cents
        if spending_cost_cents is not UNSET:
            field_dict["spending_cost_cents"] = spending_cost_cents

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        project_id = d.pop("project_id")

        employee_id = d.pop("employee_id")

        assigned = d.pop("assigned")

        inputed_minutes = d.pop("inputed_minutes", UNSET)

        labor_cost_cents = d.pop("labor_cost_cents", UNSET)

        company_labor_cost_cents = d.pop("company_labor_cost_cents", UNSET)

        spending_cost_cents = d.pop("spending_cost_cents", UNSET)

        project_management_project_worker = cls(
            id=id,
            project_id=project_id,
            employee_id=employee_id,
            assigned=assigned,
            inputed_minutes=inputed_minutes,
            labor_cost_cents=labor_cost_cents,
            company_labor_cost_cents=company_labor_cost_cents,
            spending_cost_cents=spending_cost_cents,
        )

        project_management_project_worker.additional_properties = d
        return project_management_project_worker

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
