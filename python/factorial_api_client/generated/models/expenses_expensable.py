from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.expenses_expensable_reimbursement_method import ExpensesExpensableReimbursementMethod
from ..models.expenses_expensable_status import ExpensesExpensableStatus
from ..models.expenses_expensable_type import ExpensesExpensableType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExpensesExpensable")


@_attrs_define
class ExpensesExpensable:
    id: int
    """ Unique identifier for the expensable """
    type_: ExpensesExpensableType
    """ Type of the expensable. Can be either "expense" or "mileage" or "perdiem" """
    company_id: int
    """ The ID of the company that owns the expensable """
    employee_id: int
    """ The ID of the employee that owns the expensable """
    created_at: str
    """ The date and time when the expensable was created """
    currency: str
    """ The currency code in ISO 4217 format """
    status: ExpensesExpensableStatus
    """ The status of the expensable. Can be pending, approved, paid, archived, in_review, rejected, reversed,
    draft, or in_payroll """
    status_updated_at: str
    """ The optional date and time when the status was last updated """
    updated_at: str
    """ The date and time when the expensable was last updated """
    cost_center_ids: list[int]
    """ The ids of the cost centers """
    group_id: int | Unset = UNSET
    """ The optional ID of the group that the expensable belongs to """
    legal_entity_id: int | Unset = UNSET
    """ The optional ID of the legal entity that the expensable belongs to """
    amount: int | Unset = UNSET
    """ The optional amount in cents """
    description: str | Unset = UNSET
    """ The optional description of the expensable """
    reporter_id: int | Unset = UNSET
    """ The optional ID of the employee that reported the expensable """
    effective_on: str | Unset = UNSET
    """ The optional date and time when the expensable was effective """
    review_request_at: str | Unset = UNSET
    """ The optional date and time when the expensable was requested for review """
    paid_at: str | Unset = UNSET
    """ The optional date and time when the expensable was set as paid """
    reimbursable_amount: int | Unset = UNSET
    """ The optional reimbursable amount in cents """
    reimbursable_currency: str | Unset = UNSET
    """ The optional reimbursable currency code in ISO 4217 format """
    reimbursement_method: ExpensesExpensableReimbursementMethod | Unset = UNSET
    """ The optional reimbursement method """
    internal_reference: str | Unset = UNSET
    """ The optional internal reference of the expensable """
    expense_id: int | Unset = UNSET
    """ The optional ID of the expense that the expensable belongs to """
    mileage_id: int | Unset = UNSET
    """ The optional ID of the mileage that the expensable belongs to """
    per_diem_id: int | Unset = UNSET
    """ The optional ID of the per_diem that the expensable belongs to """
    budget_id: int | Unset = UNSET
    """ The id of the budget """
    project_id: int | Unset = UNSET
    """ The id of the project """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_.value

        company_id = self.company_id

        employee_id = self.employee_id

        created_at = self.created_at

        currency = self.currency

        status = self.status.value

        status_updated_at = self.status_updated_at

        updated_at = self.updated_at

        cost_center_ids = self.cost_center_ids

        group_id = self.group_id

        legal_entity_id = self.legal_entity_id

        amount = self.amount

        description = self.description

        reporter_id = self.reporter_id

        effective_on = self.effective_on

        review_request_at = self.review_request_at

        paid_at = self.paid_at

        reimbursable_amount = self.reimbursable_amount

        reimbursable_currency = self.reimbursable_currency

        reimbursement_method: str | Unset = UNSET
        if not isinstance(self.reimbursement_method, Unset):
            reimbursement_method = self.reimbursement_method.value if self.reimbursement_method is not None else None

        internal_reference = self.internal_reference

        expense_id = self.expense_id

        mileage_id = self.mileage_id

        per_diem_id = self.per_diem_id

        budget_id = self.budget_id

        project_id = self.project_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
                "company_id": company_id,
                "employee_id": employee_id,
                "created_at": created_at,
                "currency": currency,
                "status": status,
                "status_updated_at": status_updated_at,
                "updated_at": updated_at,
                "cost_center_ids": cost_center_ids,
            }
        )
        if group_id is not UNSET:
            field_dict["group_id"] = group_id
        if legal_entity_id is not UNSET:
            field_dict["legal_entity_id"] = legal_entity_id
        if amount is not UNSET:
            field_dict["amount"] = amount
        if description is not UNSET:
            field_dict["description"] = description
        if reporter_id is not UNSET:
            field_dict["reporter_id"] = reporter_id
        if effective_on is not UNSET:
            field_dict["effective_on"] = effective_on
        if review_request_at is not UNSET:
            field_dict["review_request_at"] = review_request_at
        if paid_at is not UNSET:
            field_dict["paid_at"] = paid_at
        if reimbursable_amount is not UNSET:
            field_dict["reimbursable_amount"] = reimbursable_amount
        if reimbursable_currency is not UNSET:
            field_dict["reimbursable_currency"] = reimbursable_currency
        if reimbursement_method is not UNSET:
            field_dict["reimbursement_method"] = reimbursement_method
        if internal_reference is not UNSET:
            field_dict["internal_reference"] = internal_reference
        if expense_id is not UNSET:
            field_dict["expense_id"] = expense_id
        if mileage_id is not UNSET:
            field_dict["mileage_id"] = mileage_id
        if per_diem_id is not UNSET:
            field_dict["per_diem_id"] = per_diem_id
        if budget_id is not UNSET:
            field_dict["budget_id"] = budget_id
        if project_id is not UNSET:
            field_dict["project_id"] = project_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        type_ = ExpensesExpensableType(d.pop("type"))

        company_id = d.pop("company_id")

        employee_id = d.pop("employee_id")

        created_at = d.pop("created_at")

        currency = d.pop("currency")

        status = ExpensesExpensableStatus(d.pop("status"))

        status_updated_at = d.pop("status_updated_at")

        updated_at = d.pop("updated_at")

        cost_center_ids = cast(list[int], d.pop("cost_center_ids"))

        group_id = d.pop("group_id", UNSET)

        legal_entity_id = d.pop("legal_entity_id", UNSET)

        amount = d.pop("amount", UNSET)

        description = d.pop("description", UNSET)

        reporter_id = d.pop("reporter_id", UNSET)

        effective_on = d.pop("effective_on", UNSET)

        review_request_at = d.pop("review_request_at", UNSET)

        paid_at = d.pop("paid_at", UNSET)

        reimbursable_amount = d.pop("reimbursable_amount", UNSET)

        reimbursable_currency = d.pop("reimbursable_currency", UNSET)

        _reimbursement_method = d.pop("reimbursement_method", UNSET)
        reimbursement_method: ExpensesExpensableReimbursementMethod | Unset
        if isinstance(_reimbursement_method, Unset):
            reimbursement_method = UNSET
        else:
            reimbursement_method = ExpensesExpensableReimbursementMethod(_reimbursement_method) if _reimbursement_method is not None else None

        internal_reference = d.pop("internal_reference", UNSET)

        expense_id = d.pop("expense_id", UNSET)

        mileage_id = d.pop("mileage_id", UNSET)

        per_diem_id = d.pop("per_diem_id", UNSET)

        budget_id = d.pop("budget_id", UNSET)

        project_id = d.pop("project_id", UNSET)

        expenses_expensable = cls(
            id=id,
            type_=type_,
            company_id=company_id,
            employee_id=employee_id,
            created_at=created_at,
            currency=currency,
            status=status,
            status_updated_at=status_updated_at,
            updated_at=updated_at,
            cost_center_ids=cost_center_ids,
            group_id=group_id,
            legal_entity_id=legal_entity_id,
            amount=amount,
            description=description,
            reporter_id=reporter_id,
            effective_on=effective_on,
            review_request_at=review_request_at,
            paid_at=paid_at,
            reimbursable_amount=reimbursable_amount,
            reimbursable_currency=reimbursable_currency,
            reimbursement_method=reimbursement_method,
            internal_reference=internal_reference,
            expense_id=expense_id,
            mileage_id=mileage_id,
            per_diem_id=per_diem_id,
            budget_id=budget_id,
            project_id=project_id,
        )

        expenses_expensable.additional_properties = d
        return expenses_expensable

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
