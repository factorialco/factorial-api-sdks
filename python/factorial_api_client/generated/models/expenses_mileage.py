from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.expenses_mileage_payment import ExpensesMileagePayment
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.expenses_mileage_category import ExpensesMileageCategory


T = TypeVar("T", bound="ExpensesMileage")


@_attrs_define
class ExpensesMileage:
    id: int
    company_id: int
    currency: str
    status: str
    files: list[Any]
    payment: ExpensesMileagePayment
    employee_id: int | Unset = UNSET
    expenses_expensable_id: int | Unset = UNSET
    category: ExpensesMileageCategory | Unset = UNSET
    subcategory: str | Unset = UNSET
    category_id: int | Unset = UNSET
    amount: int | Unset = UNSET
    reimbursable_amount: int | Unset = UNSET
    """ The amount to be reimbursed for the mileage in cents. """
    reimbursable_currency: str | Unset = UNSET
    """ The currency for the reimbursable amount. """
    mileage: int | Unset = UNSET
    units: str | Unset = UNSET
    rate: str | Unset = UNSET
    from_: str | Unset = UNSET
    to: str | Unset = UNSET
    description: str | Unset = UNSET
    effective_on: str | Unset = UNSET
    review_request_at: str | Unset = UNSET
    paid_at: str | Unset = UNSET
    ledger_account_id: int | Unset = UNSET
    round_trip: bool | Unset = UNSET
    """ Indicates if the mileage is a round trip """
    origin_longitude: str | Unset = UNSET
    """ The longitude of the origin of the mileage """
    origin_latitude: str | Unset = UNSET
    """ The latitude of the origin of the mileage """
    destination_longitude: str | Unset = UNSET
    """ The longitude of the destination of the mileage """
    destination_latitude: str | Unset = UNSET
    """ The latitude of the destination of the mileage """
    calculated_mileage: int | Unset = UNSET
    """ The calculated mileage between origin and destination in decameters/10-milers """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        company_id = self.company_id

        currency = self.currency

        status = self.status

        files = self.files

        payment = self.payment.value

        employee_id = self.employee_id

        expenses_expensable_id = self.expenses_expensable_id

        category: dict[str, Any] | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.to_dict()

        subcategory = self.subcategory

        category_id = self.category_id

        amount = self.amount

        reimbursable_amount = self.reimbursable_amount

        reimbursable_currency = self.reimbursable_currency

        mileage = self.mileage

        units = self.units

        rate = self.rate

        from_ = self.from_

        to = self.to

        description = self.description

        effective_on = self.effective_on

        review_request_at = self.review_request_at

        paid_at = self.paid_at

        ledger_account_id = self.ledger_account_id

        round_trip = self.round_trip

        origin_longitude = self.origin_longitude

        origin_latitude = self.origin_latitude

        destination_longitude = self.destination_longitude

        destination_latitude = self.destination_latitude

        calculated_mileage = self.calculated_mileage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "company_id": company_id,
                "currency": currency,
                "status": status,
                "files": files,
                "payment": payment,
            }
        )
        if employee_id is not UNSET:
            field_dict["employee_id"] = employee_id
        if expenses_expensable_id is not UNSET:
            field_dict["expenses_expensable_id"] = expenses_expensable_id
        if category is not UNSET:
            field_dict["category"] = category
        if subcategory is not UNSET:
            field_dict["subcategory"] = subcategory
        if category_id is not UNSET:
            field_dict["category_id"] = category_id
        if amount is not UNSET:
            field_dict["amount"] = amount
        if reimbursable_amount is not UNSET:
            field_dict["reimbursable_amount"] = reimbursable_amount
        if reimbursable_currency is not UNSET:
            field_dict["reimbursable_currency"] = reimbursable_currency
        if mileage is not UNSET:
            field_dict["mileage"] = mileage
        if units is not UNSET:
            field_dict["units"] = units
        if rate is not UNSET:
            field_dict["rate"] = rate
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to
        if description is not UNSET:
            field_dict["description"] = description
        if effective_on is not UNSET:
            field_dict["effective_on"] = effective_on
        if review_request_at is not UNSET:
            field_dict["review_request_at"] = review_request_at
        if paid_at is not UNSET:
            field_dict["paid_at"] = paid_at
        if ledger_account_id is not UNSET:
            field_dict["ledger_account_id"] = ledger_account_id
        if round_trip is not UNSET:
            field_dict["round_trip"] = round_trip
        if origin_longitude is not UNSET:
            field_dict["origin_longitude"] = origin_longitude
        if origin_latitude is not UNSET:
            field_dict["origin_latitude"] = origin_latitude
        if destination_longitude is not UNSET:
            field_dict["destination_longitude"] = destination_longitude
        if destination_latitude is not UNSET:
            field_dict["destination_latitude"] = destination_latitude
        if calculated_mileage is not UNSET:
            field_dict["calculated_mileage"] = calculated_mileage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.expenses_mileage_category import ExpensesMileageCategory

        d = dict(src_dict)
        id = d.pop("id")

        company_id = d.pop("company_id")

        currency = d.pop("currency")

        status = d.pop("status")

        files = cast(list[Any], d.pop("files"))

        payment = ExpensesMileagePayment(d.pop("payment"))

        employee_id = d.pop("employee_id", UNSET)

        expenses_expensable_id = d.pop("expenses_expensable_id", UNSET)

        _category = d.pop("category", UNSET)
        category: ExpensesMileageCategory | Unset
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = ExpensesMileageCategory.from_dict(_category)

        subcategory = d.pop("subcategory", UNSET)

        category_id = d.pop("category_id", UNSET)

        amount = d.pop("amount", UNSET)

        reimbursable_amount = d.pop("reimbursable_amount", UNSET)

        reimbursable_currency = d.pop("reimbursable_currency", UNSET)

        mileage = d.pop("mileage", UNSET)

        units = d.pop("units", UNSET)

        rate = d.pop("rate", UNSET)

        from_ = d.pop("from", UNSET)

        to = d.pop("to", UNSET)

        description = d.pop("description", UNSET)

        effective_on = d.pop("effective_on", UNSET)

        review_request_at = d.pop("review_request_at", UNSET)

        paid_at = d.pop("paid_at", UNSET)

        ledger_account_id = d.pop("ledger_account_id", UNSET)

        round_trip = d.pop("round_trip", UNSET)

        origin_longitude = d.pop("origin_longitude", UNSET)

        origin_latitude = d.pop("origin_latitude", UNSET)

        destination_longitude = d.pop("destination_longitude", UNSET)

        destination_latitude = d.pop("destination_latitude", UNSET)

        calculated_mileage = d.pop("calculated_mileage", UNSET)

        expenses_mileage = cls(
            id=id,
            company_id=company_id,
            currency=currency,
            status=status,
            files=files,
            payment=payment,
            employee_id=employee_id,
            expenses_expensable_id=expenses_expensable_id,
            category=category,
            subcategory=subcategory,
            category_id=category_id,
            amount=amount,
            reimbursable_amount=reimbursable_amount,
            reimbursable_currency=reimbursable_currency,
            mileage=mileage,
            units=units,
            rate=rate,
            from_=from_,
            to=to,
            description=description,
            effective_on=effective_on,
            review_request_at=review_request_at,
            paid_at=paid_at,
            ledger_account_id=ledger_account_id,
            round_trip=round_trip,
            origin_longitude=origin_longitude,
            origin_latitude=origin_latitude,
            destination_longitude=destination_longitude,
            destination_latitude=destination_latitude,
            calculated_mileage=calculated_mileage,
        )

        expenses_mileage.additional_properties = d
        return expenses_mileage

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
