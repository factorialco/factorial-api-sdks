from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.expenses_expense_creation_type import ExpensesExpenseCreationType
from ..models.expenses_expense_payment import ExpensesExpensePayment
from ..models.expenses_expense_status import ExpensesExpenseStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.expenses_expense_card import ExpensesExpenseCard
    from ..models.expenses_expense_category import ExpensesExpenseCategory
    from ..models.expenses_expense_signed_document import ExpensesExpenseSignedDocument


T = TypeVar("T", bound="ExpensesExpense")


@_attrs_define
class ExpensesExpense:
    company_id: int
    """ The id of the expense's company """
    creation_type: ExpensesExpenseCreationType
    """ How the expense was created, one of 'manual', 'automatic' or 'travelperk' """
    currency: str
    """ The currency of the expense """
    status: ExpensesExpenseStatus
    """ The status of the expense """
    effective_on: str
    """ The date when the expense was made """
    status_updated_at: str
    """ The date and time when the status was updated """
    files: list[Any]
    """ The files of the expense """
    taxes: list[Any]
    """ The taxes of the expense """
    id: int | Unset = UNSET
    """ The id of the expense """
    employee_id: int | Unset = UNSET
    """ The id of the expense's owner """
    card_payment_id: int | Unset = UNSET
    """ The id of the card payment """
    dispute_id: int | Unset = UNSET
    """ The id of the dispute """
    expenses_expensable_id: int | Unset = UNSET
    """ The id of the expensable """
    merchant_name: str | Unset = UNSET
    """ The name of the merchant """
    user_merchant: str | Unset = UNSET
    """ The user merchant of the expense """
    merchant_tin: str | Unset = UNSET
    """ The tax identification number of the merchant """
    category: ExpensesExpenseCategory | Unset = UNSET
    """ The category of the expense """
    subcategory: str | Unset = UNSET
    """ The subcategory of the expense """
    reference: str | Unset = UNSET
    """ The reference of the expense """
    amount: int | Unset = UNSET
    """ The optional amount in cents """
    description: str | Unset = UNSET
    """ The description of the expense """
    review_request_at: str | Unset = UNSET
    """ The date and time when the expense was reviewed """
    external_authorization_id: str | Unset = UNSET
    """ The id of the external authorization """
    expenses_card_id: int | Unset = UNSET
    """ The id of the card """
    card: ExpensesExpenseCard | Unset = UNSET
    """ The card of the expense """
    document_id: int | Unset = UNSET
    """ The id of the document """
    signed_document: ExpensesExpenseSignedDocument | Unset = UNSET
    """ The signed document of the expense """
    access_token: str | Unset = UNSET
    """ The access token of the expense """
    paid_at: str | Unset = UNSET
    """ The date and time when the expense was paid """
    document_number: str | Unset = UNSET
    """ Number of the financial document associated to the expense """
    document_type: str | Unset = UNSET
    """ Type of the financial document associated to the expense """
    payment: ExpensesExpensePayment | Unset = UNSET
    """ The payment of the expense """
    payment_method: str | Unset = UNSET
    """ The method of the payment """
    exchange_rate: float | Unset = UNSET
    """ The exchange rate of the payment """
    reimbursable_currency: str | Unset = UNSET
    """ The currency of the reimbursable amount """
    reimbursable_amount: int | Unset = UNSET
    """ The optional reimbursable amount in cents """
    category_id: int | Unset = UNSET
    """ The id of the category """
    ledger_account_id: int | Unset = UNSET
    """ The id of the ledger account """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company_id = self.company_id

        creation_type = self.creation_type.value

        currency = self.currency

        status = self.status.value

        effective_on = self.effective_on

        status_updated_at = self.status_updated_at

        files = self.files

        taxes = self.taxes

        id = self.id

        employee_id = self.employee_id

        card_payment_id = self.card_payment_id

        dispute_id = self.dispute_id

        expenses_expensable_id = self.expenses_expensable_id

        merchant_name = self.merchant_name

        user_merchant = self.user_merchant

        merchant_tin = self.merchant_tin

        category: dict[str, Any] | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.to_dict()

        subcategory = self.subcategory

        reference = self.reference

        amount = self.amount

        description = self.description

        review_request_at = self.review_request_at

        external_authorization_id = self.external_authorization_id

        expenses_card_id = self.expenses_card_id

        card: dict[str, Any] | Unset = UNSET
        if not isinstance(self.card, Unset):
            card = self.card.to_dict()

        document_id = self.document_id

        signed_document: dict[str, Any] | Unset = UNSET
        if not isinstance(self.signed_document, Unset):
            signed_document = self.signed_document.to_dict()

        access_token = self.access_token

        paid_at = self.paid_at

        document_number = self.document_number

        document_type = self.document_type

        payment: str | Unset = UNSET
        if not isinstance(self.payment, Unset):
            payment = self.payment.value

        payment_method = self.payment_method

        exchange_rate = self.exchange_rate

        reimbursable_currency = self.reimbursable_currency

        reimbursable_amount = self.reimbursable_amount

        category_id = self.category_id

        ledger_account_id = self.ledger_account_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "company_id": company_id,
                "creation_type": creation_type,
                "currency": currency,
                "status": status,
                "effective_on": effective_on,
                "status_updated_at": status_updated_at,
                "files": files,
                "taxes": taxes,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if employee_id is not UNSET:
            field_dict["employee_id"] = employee_id
        if card_payment_id is not UNSET:
            field_dict["card_payment_id"] = card_payment_id
        if dispute_id is not UNSET:
            field_dict["dispute_id"] = dispute_id
        if expenses_expensable_id is not UNSET:
            field_dict["expenses_expensable_id"] = expenses_expensable_id
        if merchant_name is not UNSET:
            field_dict["merchant_name"] = merchant_name
        if user_merchant is not UNSET:
            field_dict["user_merchant"] = user_merchant
        if merchant_tin is not UNSET:
            field_dict["merchant_tin"] = merchant_tin
        if category is not UNSET:
            field_dict["category"] = category
        if subcategory is not UNSET:
            field_dict["subcategory"] = subcategory
        if reference is not UNSET:
            field_dict["reference"] = reference
        if amount is not UNSET:
            field_dict["amount"] = amount
        if description is not UNSET:
            field_dict["description"] = description
        if review_request_at is not UNSET:
            field_dict["review_request_at"] = review_request_at
        if external_authorization_id is not UNSET:
            field_dict["external_authorization_id"] = external_authorization_id
        if expenses_card_id is not UNSET:
            field_dict["expenses_card_id"] = expenses_card_id
        if card is not UNSET:
            field_dict["card"] = card
        if document_id is not UNSET:
            field_dict["document_id"] = document_id
        if signed_document is not UNSET:
            field_dict["signed_document"] = signed_document
        if access_token is not UNSET:
            field_dict["access_token"] = access_token
        if paid_at is not UNSET:
            field_dict["paid_at"] = paid_at
        if document_number is not UNSET:
            field_dict["document_number"] = document_number
        if document_type is not UNSET:
            field_dict["document_type"] = document_type
        if payment is not UNSET:
            field_dict["payment"] = payment
        if payment_method is not UNSET:
            field_dict["payment_method"] = payment_method
        if exchange_rate is not UNSET:
            field_dict["exchange_rate"] = exchange_rate
        if reimbursable_currency is not UNSET:
            field_dict["reimbursable_currency"] = reimbursable_currency
        if reimbursable_amount is not UNSET:
            field_dict["reimbursable_amount"] = reimbursable_amount
        if category_id is not UNSET:
            field_dict["category_id"] = category_id
        if ledger_account_id is not UNSET:
            field_dict["ledger_account_id"] = ledger_account_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.expenses_expense_card import ExpensesExpenseCard
        from ..models.expenses_expense_category import ExpensesExpenseCategory
        from ..models.expenses_expense_signed_document import ExpensesExpenseSignedDocument

        d = dict(src_dict)
        company_id = d.pop("company_id")

        creation_type = ExpensesExpenseCreationType(d.pop("creation_type"))

        currency = d.pop("currency")

        status = ExpensesExpenseStatus(d.pop("status"))

        effective_on = d.pop("effective_on")

        status_updated_at = d.pop("status_updated_at")

        files = cast(list[Any], d.pop("files"))

        taxes = cast(list[Any], d.pop("taxes"))

        id = d.pop("id", UNSET)

        employee_id = d.pop("employee_id", UNSET)

        card_payment_id = d.pop("card_payment_id", UNSET)

        dispute_id = d.pop("dispute_id", UNSET)

        expenses_expensable_id = d.pop("expenses_expensable_id", UNSET)

        merchant_name = d.pop("merchant_name", UNSET)

        user_merchant = d.pop("user_merchant", UNSET)

        merchant_tin = d.pop("merchant_tin", UNSET)

        _category = d.pop("category", UNSET)
        category: ExpensesExpenseCategory | Unset
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = ExpensesExpenseCategory.from_dict(_category)

        subcategory = d.pop("subcategory", UNSET)

        reference = d.pop("reference", UNSET)

        amount = d.pop("amount", UNSET)

        description = d.pop("description", UNSET)

        review_request_at = d.pop("review_request_at", UNSET)

        external_authorization_id = d.pop("external_authorization_id", UNSET)

        expenses_card_id = d.pop("expenses_card_id", UNSET)

        _card = d.pop("card", UNSET)
        card: ExpensesExpenseCard | Unset
        if isinstance(_card, Unset):
            card = UNSET
        else:
            card = ExpensesExpenseCard.from_dict(_card)

        document_id = d.pop("document_id", UNSET)

        _signed_document = d.pop("signed_document", UNSET)
        signed_document: ExpensesExpenseSignedDocument | Unset
        if isinstance(_signed_document, Unset):
            signed_document = UNSET
        else:
            signed_document = ExpensesExpenseSignedDocument.from_dict(_signed_document)

        access_token = d.pop("access_token", UNSET)

        paid_at = d.pop("paid_at", UNSET)

        document_number = d.pop("document_number", UNSET)

        document_type = d.pop("document_type", UNSET)

        _payment = d.pop("payment", UNSET)
        payment: ExpensesExpensePayment | Unset
        if isinstance(_payment, Unset):
            payment = UNSET
        else:
            payment = ExpensesExpensePayment(_payment) if _payment is not None else None

        payment_method = d.pop("payment_method", UNSET)

        exchange_rate = d.pop("exchange_rate", UNSET)

        reimbursable_currency = d.pop("reimbursable_currency", UNSET)

        reimbursable_amount = d.pop("reimbursable_amount", UNSET)

        category_id = d.pop("category_id", UNSET)

        ledger_account_id = d.pop("ledger_account_id", UNSET)

        expenses_expense = cls(
            company_id=company_id,
            creation_type=creation_type,
            currency=currency,
            status=status,
            effective_on=effective_on,
            status_updated_at=status_updated_at,
            files=files,
            taxes=taxes,
            id=id,
            employee_id=employee_id,
            card_payment_id=card_payment_id,
            dispute_id=dispute_id,
            expenses_expensable_id=expenses_expensable_id,
            merchant_name=merchant_name,
            user_merchant=user_merchant,
            merchant_tin=merchant_tin,
            category=category,
            subcategory=subcategory,
            reference=reference,
            amount=amount,
            description=description,
            review_request_at=review_request_at,
            external_authorization_id=external_authorization_id,
            expenses_card_id=expenses_card_id,
            card=card,
            document_id=document_id,
            signed_document=signed_document,
            access_token=access_token,
            paid_at=paid_at,
            document_number=document_number,
            document_type=document_type,
            payment=payment,
            payment_method=payment_method,
            exchange_rate=exchange_rate,
            reimbursable_currency=reimbursable_currency,
            reimbursable_amount=reimbursable_amount,
            category_id=category_id,
            ledger_account_id=ledger_account_id,
        )

        expenses_expense.additional_properties = d
        return expenses_expense

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
