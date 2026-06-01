from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectManagementExportableExpense")


@_attrs_define
class ProjectManagementExportableExpense:
    employee_name: str
    date: str | Unset = UNSET
    project_name: str | Unset = UNSET
    subproject_name: str | Unset = UNSET
    preferred_name: str | Unset = UNSET
    amount: str | Unset = UNSET
    currency: str | Unset = UNSET
    expense_category: str | Unset = UNSET
    expense_subcategory: str | Unset = UNSET
    expense_status: str | Unset = UNSET
    expense_link: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        employee_name = self.employee_name

        date = self.date

        project_name = self.project_name

        subproject_name = self.subproject_name

        preferred_name = self.preferred_name

        amount = self.amount

        currency = self.currency

        expense_category = self.expense_category

        expense_subcategory = self.expense_subcategory

        expense_status = self.expense_status

        expense_link = self.expense_link

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "employee_name": employee_name,
            }
        )
        if date is not UNSET:
            field_dict["date"] = date
        if project_name is not UNSET:
            field_dict["project_name"] = project_name
        if subproject_name is not UNSET:
            field_dict["subproject_name"] = subproject_name
        if preferred_name is not UNSET:
            field_dict["preferred_name"] = preferred_name
        if amount is not UNSET:
            field_dict["amount"] = amount
        if currency is not UNSET:
            field_dict["currency"] = currency
        if expense_category is not UNSET:
            field_dict["expense_category"] = expense_category
        if expense_subcategory is not UNSET:
            field_dict["expense_subcategory"] = expense_subcategory
        if expense_status is not UNSET:
            field_dict["expense_status"] = expense_status
        if expense_link is not UNSET:
            field_dict["expense_link"] = expense_link

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        employee_name = d.pop("employee_name")

        date = d.pop("date", UNSET)

        project_name = d.pop("project_name", UNSET)

        subproject_name = d.pop("subproject_name", UNSET)

        preferred_name = d.pop("preferred_name", UNSET)

        amount = d.pop("amount", UNSET)

        currency = d.pop("currency", UNSET)

        expense_category = d.pop("expense_category", UNSET)

        expense_subcategory = d.pop("expense_subcategory", UNSET)

        expense_status = d.pop("expense_status", UNSET)

        expense_link = d.pop("expense_link", UNSET)

        project_management_exportable_expense = cls(
            employee_name=employee_name,
            date=date,
            project_name=project_name,
            subproject_name=subproject_name,
            preferred_name=preferred_name,
            amount=amount,
            currency=currency,
            expense_category=expense_category,
            expense_subcategory=expense_subcategory,
            expense_status=expense_status,
            expense_link=expense_link,
        )

        project_management_exportable_expense.additional_properties = d
        return project_management_exportable_expense

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
