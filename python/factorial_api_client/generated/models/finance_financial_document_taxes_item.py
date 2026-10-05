from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.finance_financial_document_taxes_item_type import (
    FinanceFinancialDocumentTaxesItemType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.finance_financial_document_taxes_item_tax_rates_item import (
        FinanceFinancialDocumentTaxesItemTaxRatesItem,
    )


T = TypeVar("T", bound="FinanceFinancialDocumentTaxesItem")


@_attrs_define
class FinanceFinancialDocumentTaxesItem:
    amount_cents: int | Unset = UNSET
    percentage: float | Unset = UNSET
    base_amount_cents: int | Unset = UNSET
    type_: FinanceFinancialDocumentTaxesItemType | Unset = UNSET
    tax_type_id: str | Unset = UNSET
    tax_type_name: str | Unset = UNSET
    tax_rates: list[FinanceFinancialDocumentTaxesItemTaxRatesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount_cents = self.amount_cents

        percentage = self.percentage

        base_amount_cents = self.base_amount_cents

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value if self.type_ is not None else None

        tax_type_id = self.tax_type_id

        tax_type_name = self.tax_type_name

        tax_rates: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tax_rates, Unset):
            tax_rates = []
            for tax_rates_item_data in self.tax_rates:
                tax_rates_item = tax_rates_item_data.to_dict()
                tax_rates.append(tax_rates_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount_cents is not UNSET:
            field_dict["amount_cents"] = amount_cents
        if percentage is not UNSET:
            field_dict["percentage"] = percentage
        if base_amount_cents is not UNSET:
            field_dict["base_amount_cents"] = base_amount_cents
        if type_ is not UNSET:
            field_dict["type"] = type_
        if tax_type_id is not UNSET:
            field_dict["tax_type_id"] = tax_type_id
        if tax_type_name is not UNSET:
            field_dict["tax_type_name"] = tax_type_name
        if tax_rates is not UNSET:
            field_dict["tax_rates"] = tax_rates

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.finance_financial_document_taxes_item_tax_rates_item import (
            FinanceFinancialDocumentTaxesItemTaxRatesItem,
        )

        d = dict(src_dict)
        amount_cents = d.pop("amount_cents", UNSET)

        percentage = d.pop("percentage", UNSET)

        base_amount_cents = d.pop("base_amount_cents", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: FinanceFinancialDocumentTaxesItemType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = FinanceFinancialDocumentTaxesItemType(_type_) if _type_ is not None else None

        tax_type_id = d.pop("tax_type_id", UNSET)

        tax_type_name = d.pop("tax_type_name", UNSET)

        _tax_rates = d.pop("tax_rates", UNSET)
        tax_rates: list[FinanceFinancialDocumentTaxesItemTaxRatesItem] | Unset = UNSET
        if _tax_rates is not UNSET:
            tax_rates = []
            for tax_rates_item_data in _tax_rates:
                tax_rates_item = FinanceFinancialDocumentTaxesItemTaxRatesItem.from_dict(
                    tax_rates_item_data
                )

                tax_rates.append(tax_rates_item)

        finance_financial_document_taxes_item = cls(
            amount_cents=amount_cents,
            percentage=percentage,
            base_amount_cents=base_amount_cents,
            type_=type_,
            tax_type_id=tax_type_id,
            tax_type_name=tax_type_name,
            tax_rates=tax_rates,
        )

        finance_financial_document_taxes_item.additional_properties = d
        return finance_financial_document_taxes_item

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
