from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FinanceFinancialDocumentLineItem")


@_attrs_define
class FinanceFinancialDocumentLineItem:
    id: str
    """ Line item identifier. """
    financial_document_id: str
    """ The financial document this line belongs to. """
    description: str
    """ What the line charges for. """
    quantity: float
    """ Number of units. """
    discount_percentage: float
    """ Discount applied to the line, as a fraction (0.1 is 10%). """
    subtotal_price_cents: int
    """ Line amount after discount, before taxes, in cents. """
    total_price_cents: int
    """ Line amount after discount and taxes, in cents. """
    unit_price_cents: int | Unset = UNSET
    """ Price per unit in cents, before discount and taxes. """
    tax_rate_id: str | Unset = UNSET
    """ The tax rate applied to the line, when the company has it configured. """
    tax_rate_percentage: float | Unset = UNSET
    """ The tax rate applied to the line, as a fraction (0.21 is 21%). """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        financial_document_id = self.financial_document_id

        description = self.description

        quantity = self.quantity

        discount_percentage = self.discount_percentage

        subtotal_price_cents = self.subtotal_price_cents

        total_price_cents = self.total_price_cents

        unit_price_cents = self.unit_price_cents

        tax_rate_id = self.tax_rate_id

        tax_rate_percentage = self.tax_rate_percentage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "financial_document_id": financial_document_id,
                "description": description,
                "quantity": quantity,
                "discount_percentage": discount_percentage,
                "subtotal_price_cents": subtotal_price_cents,
                "total_price_cents": total_price_cents,
            }
        )
        if unit_price_cents is not UNSET:
            field_dict["unit_price_cents"] = unit_price_cents
        if tax_rate_id is not UNSET:
            field_dict["tax_rate_id"] = tax_rate_id
        if tax_rate_percentage is not UNSET:
            field_dict["tax_rate_percentage"] = tax_rate_percentage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        financial_document_id = d.pop("financial_document_id")

        description = d.pop("description")

        quantity = d.pop("quantity")

        discount_percentage = d.pop("discount_percentage")

        subtotal_price_cents = d.pop("subtotal_price_cents")

        total_price_cents = d.pop("total_price_cents")

        unit_price_cents = d.pop("unit_price_cents", UNSET)

        tax_rate_id = d.pop("tax_rate_id", UNSET)

        tax_rate_percentage = d.pop("tax_rate_percentage", UNSET)

        finance_financial_document_line_item = cls(
            id=id,
            financial_document_id=financial_document_id,
            description=description,
            quantity=quantity,
            discount_percentage=discount_percentage,
            subtotal_price_cents=subtotal_price_cents,
            total_price_cents=total_price_cents,
            unit_price_cents=unit_price_cents,
            tax_rate_id=tax_rate_id,
            tax_rate_percentage=tax_rate_percentage,
        )

        finance_financial_document_line_item.additional_properties = d
        return finance_financial_document_line_item

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
