from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.expenses_per_diem_payment import ExpensesPerDiemPayment
from ..models.expenses_per_diem_status import ExpensesPerDiemStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.expenses_per_diem_category import ExpensesPerDiemCategory


T = TypeVar("T", bound="ExpensesPerDiem")


@_attrs_define
class ExpensesPerDiem:
    id: int
    """ The ID of the per diem. """
    company_id: int
    """ The ID of the company the per diem is for. """
    currency: str
    """ The currency for the reimbursable amount. """
    payment: ExpensesPerDiemPayment
    """ The payment method for the per diem. """
    files: list[Any]
    """ The files attached to the per diem. """
    status: ExpensesPerDiemStatus
    """ The status of the per diem. """
    rates: list[Any]
    """ The rates for the per diem. """
    employee_id: int | Unset = UNSET
    """ The ID of the employee the per diem is for. """
    expenses_expensable_id: int | Unset = UNSET
    """ The ID of the expensable the per diem is for. """
    end_date: str | Unset = UNSET
    """ The end date of the per diem. """
    start_date: str | Unset = UNSET
    """ The start date of the per diem. """
    from_: str | Unset = UNSET
    """ The location the per diem is from. """
    to: str | Unset = UNSET
    """ The location the per diem is to. """
    ledger_account_id: int | Unset = UNSET
    """ The ID of the ledger account the per diem is for. """
    amount: int | Unset = UNSET
    """ The amount of the per diem. """
    reimbursable_amount: int | Unset = UNSET
    """ The amount to be reimbursed by the per diem in cents. """
    reimbursable_currency: str | Unset = UNSET
    """ The currency for the reimbursable amount. """
    paid_at: str | Unset = UNSET
    """ The date the per diem was paid. """
    review_request_at: str | Unset = UNSET
    """ The date the per diem was requested for review. """
    effective_on: str | Unset = UNSET
    """ The date the per diem is effective on. """
    description: str | Unset = UNSET
    """ The description of the per diem. """
    category: ExpensesPerDiemCategory | Unset = UNSET
    """ The category of the per diem. """
    subcategory: str | Unset = UNSET
    """ The subcategory of the per diem. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        company_id = self.company_id

        currency = self.currency

        payment = self.payment.value

        files = self.files

        status = self.status.value

        rates = self.rates

        employee_id = self.employee_id

        expenses_expensable_id = self.expenses_expensable_id

        end_date = self.end_date

        start_date = self.start_date

        from_ = self.from_

        to = self.to

        ledger_account_id = self.ledger_account_id

        amount = self.amount

        reimbursable_amount = self.reimbursable_amount

        reimbursable_currency = self.reimbursable_currency

        paid_at = self.paid_at

        review_request_at = self.review_request_at

        effective_on = self.effective_on

        description = self.description

        category: dict[str, Any] | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.to_dict()

        subcategory = self.subcategory

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "company_id": company_id,
                "currency": currency,
                "payment": payment,
                "files": files,
                "status": status,
                "rates": rates,
            }
        )
        if employee_id is not UNSET:
            field_dict["employee_id"] = employee_id
        if expenses_expensable_id is not UNSET:
            field_dict["expenses_expensable_id"] = expenses_expensable_id
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to
        if ledger_account_id is not UNSET:
            field_dict["ledger_account_id"] = ledger_account_id
        if amount is not UNSET:
            field_dict["amount"] = amount
        if reimbursable_amount is not UNSET:
            field_dict["reimbursable_amount"] = reimbursable_amount
        if reimbursable_currency is not UNSET:
            field_dict["reimbursable_currency"] = reimbursable_currency
        if paid_at is not UNSET:
            field_dict["paid_at"] = paid_at
        if review_request_at is not UNSET:
            field_dict["review_request_at"] = review_request_at
        if effective_on is not UNSET:
            field_dict["effective_on"] = effective_on
        if description is not UNSET:
            field_dict["description"] = description
        if category is not UNSET:
            field_dict["category"] = category
        if subcategory is not UNSET:
            field_dict["subcategory"] = subcategory

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.expenses_per_diem_category import ExpensesPerDiemCategory

        d = dict(src_dict)
        id = d.pop("id")

        company_id = d.pop("company_id")

        currency = d.pop("currency")

        payment = ExpensesPerDiemPayment(d.pop("payment"))

        files = cast(list[Any], d.pop("files"))

        status = ExpensesPerDiemStatus(d.pop("status"))

        rates = cast(list[Any], d.pop("rates"))

        employee_id = d.pop("employee_id", UNSET)

        expenses_expensable_id = d.pop("expenses_expensable_id", UNSET)

        end_date = d.pop("end_date", UNSET)

        start_date = d.pop("start_date", UNSET)

        from_ = d.pop("from", UNSET)

        to = d.pop("to", UNSET)

        ledger_account_id = d.pop("ledger_account_id", UNSET)

        amount = d.pop("amount", UNSET)

        reimbursable_amount = d.pop("reimbursable_amount", UNSET)

        reimbursable_currency = d.pop("reimbursable_currency", UNSET)

        paid_at = d.pop("paid_at", UNSET)

        review_request_at = d.pop("review_request_at", UNSET)

        effective_on = d.pop("effective_on", UNSET)

        description = d.pop("description", UNSET)

        _category = d.pop("category", UNSET)
        category: ExpensesPerDiemCategory | Unset
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = ExpensesPerDiemCategory.from_dict(_category)

        subcategory = d.pop("subcategory", UNSET)

        expenses_per_diem = cls(
            id=id,
            company_id=company_id,
            currency=currency,
            payment=payment,
            files=files,
            status=status,
            rates=rates,
            employee_id=employee_id,
            expenses_expensable_id=expenses_expensable_id,
            end_date=end_date,
            start_date=start_date,
            from_=from_,
            to=to,
            ledger_account_id=ledger_account_id,
            amount=amount,
            reimbursable_amount=reimbursable_amount,
            reimbursable_currency=reimbursable_currency,
            paid_at=paid_at,
            review_request_at=review_request_at,
            effective_on=effective_on,
            description=description,
            category=category,
            subcategory=subcategory,
        )

        expenses_per_diem.additional_properties = d
        return expenses_per_diem

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
