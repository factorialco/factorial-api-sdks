from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20251001ResourcesProjectManagementProjectsBody")


@_attrs_define
class PostApi20251001ResourcesProjectManagementProjectsBody:
    name: str
    """ Mandatory to pass a name of the project. """
    code: str | Unset = UNSET
    """ Optional unique code for the project to be identifiable and searchable. """
    description: str | Unset = UNSET
    """ Description of the project. """
    start_date: str | Unset = UNSET
    """ Optional start date for the project. If given must be in iso-8601 format (YYYY-MM-DD). """
    due_date: str | Unset = UNSET
    """ Optional due date for the project. If given must be in iso-8601 format (YYYY-MM-DD). """
    status: str | Unset = UNSET
    """ Project status. Can be `active` or `closed` """
    employees_assignment: str | Unset = UNSET
    """ Optional param to define the kind of assignation the project has. Can be `manual` or `company` """
    project_admins: list[int] | Unset = UNSET
    """ Array of employee IDs who are project administrators """
    project_managers: list[int] | Unset = UNSET
    """ Array of employee IDs who are project managers """
    is_billable: bool | Unset = UNSET
    """ Whether the project is billable to clients """
    fixed_cost_cents: int | Unset = UNSET
    """ Fixed cost of the project in cents """
    budget_allocation: int | Unset = UNSET
    """ Budget allocation in minutes for the project, it's exclusive of the budget_allocation_cents """
    legal_entity_id: int | Unset = UNSET
    """ The legal entity ID associated with the project """
    budget_allocation_cents: int | Unset = UNSET
    """ Budget allocation amount in cents, it's exclusive of the budget_allocation """
    fee_amount_cents: int | Unset = UNSET
    """ Fee amount in cents for the project """
    client_id: int | Unset = UNSET
    """ Client associated to the project, refers to finance/contacts. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        code = self.code

        description = self.description

        start_date = self.start_date

        due_date = self.due_date

        status = self.status

        employees_assignment = self.employees_assignment

        project_admins: list[int] | Unset = UNSET
        if not isinstance(self.project_admins, Unset):
            project_admins = self.project_admins

        project_managers: list[int] | Unset = UNSET
        if not isinstance(self.project_managers, Unset):
            project_managers = self.project_managers

        is_billable = self.is_billable

        fixed_cost_cents = self.fixed_cost_cents

        budget_allocation = self.budget_allocation

        legal_entity_id = self.legal_entity_id

        budget_allocation_cents = self.budget_allocation_cents

        fee_amount_cents = self.fee_amount_cents

        client_id = self.client_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
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
        if status is not UNSET:
            field_dict["status"] = status
        if employees_assignment is not UNSET:
            field_dict["employees_assignment"] = employees_assignment
        if project_admins is not UNSET:
            field_dict["project_admins"] = project_admins
        if project_managers is not UNSET:
            field_dict["project_managers"] = project_managers
        if is_billable is not UNSET:
            field_dict["is_billable"] = is_billable
        if fixed_cost_cents is not UNSET:
            field_dict["fixed_cost_cents"] = fixed_cost_cents
        if budget_allocation is not UNSET:
            field_dict["budget_allocation"] = budget_allocation
        if legal_entity_id is not UNSET:
            field_dict["legal_entity_id"] = legal_entity_id
        if budget_allocation_cents is not UNSET:
            field_dict["budget_allocation_cents"] = budget_allocation_cents
        if fee_amount_cents is not UNSET:
            field_dict["fee_amount_cents"] = fee_amount_cents
        if client_id is not UNSET:
            field_dict["client_id"] = client_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        code = d.pop("code", UNSET)

        description = d.pop("description", UNSET)

        start_date = d.pop("start_date", UNSET)

        due_date = d.pop("due_date", UNSET)

        status = d.pop("status", UNSET)

        employees_assignment = d.pop("employees_assignment", UNSET)

        project_admins = cast(list[int], d.pop("project_admins", UNSET))

        project_managers = cast(list[int], d.pop("project_managers", UNSET))

        is_billable = d.pop("is_billable", UNSET)

        fixed_cost_cents = d.pop("fixed_cost_cents", UNSET)

        budget_allocation = d.pop("budget_allocation", UNSET)

        legal_entity_id = d.pop("legal_entity_id", UNSET)

        budget_allocation_cents = d.pop("budget_allocation_cents", UNSET)

        fee_amount_cents = d.pop("fee_amount_cents", UNSET)

        client_id = d.pop("client_id", UNSET)

        post_api_20251001_resources_project_management_projects_body = cls(
            name=name,
            code=code,
            description=description,
            start_date=start_date,
            due_date=due_date,
            status=status,
            employees_assignment=employees_assignment,
            project_admins=project_admins,
            project_managers=project_managers,
            is_billable=is_billable,
            fixed_cost_cents=fixed_cost_cents,
            budget_allocation=budget_allocation,
            legal_entity_id=legal_entity_id,
            budget_allocation_cents=budget_allocation_cents,
            fee_amount_cents=fee_amount_cents,
            client_id=client_id,
        )

        post_api_20251001_resources_project_management_projects_body.additional_properties = d
        return post_api_20251001_resources_project_management_projects_body

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
