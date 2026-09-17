from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.put_api_20261001_resources_finance_financial_documents_id_body_document_type import (
    PutApi20261001ResourcesFinanceFinancialDocumentsIdBodyDocumentType,
)
from ..models.put_api_20261001_resources_finance_financial_documents_id_body_status import (
    PutApi20261001ResourcesFinanceFinancialDocumentsIdBodyStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.put_api_20261001_resources_finance_financial_documents_id_body_line_items_item import (
        PutApi20261001ResourcesFinanceFinancialDocumentsIdBodyLineItemsItem,
    )
    from ..models.put_api_20261001_resources_finance_financial_documents_id_body_taxes_item import (
        PutApi20261001ResourcesFinanceFinancialDocumentsIdBodyTaxesItem,
    )


T = TypeVar("T", bound="PutApi20261001ResourcesFinanceFinancialDocumentsIdBody")


@_attrs_define
class PutApi20261001ResourcesFinanceFinancialDocumentsIdBody:
    company_id: str
    """ Company identifier, as returned by the credentials endpoint (`/resources/api_public/credentials`). """
    id: str
    """ Identifier of the financial document to update. """
    status: PutApi20261001ResourcesFinanceFinancialDocumentsIdBodyStatus
    """ Status of the document. Transitions have real side effects: `sent_to_pay` enqueues a payment request in
    Factorial, and `paid` marks the document as paid (manual payment). Once a document is `sent_to_pay`, its payment
    lifecycle is owned by the payment flow in Factorial — do not set `paid` manually on it; the payment
    reconciliation does. """
    taxes: list[PutApi20261001ResourcesFinanceFinancialDocumentsIdBodyTaxesItem]
    """ Tax breakdown, as returned by the read endpoint — send back what you read (adjusted to your changes).
    Replaced as sent; ignored when line_items are provided, since the line items own the totals. """
    currency: str | Unset = UNSET
    """ Document currency (ISO 4217). """
    total_amount_cents: int | Unset = UNSET
    """ Total amount in cents. Ignored when line_items are provided, since the line items own the totals. """
    document_number: str | Unset = UNSET
    """ Document number. Must be unique per vendor for purchases; a duplicate returns a 409 with the same machine-
    readable invoice_number error key as the create endpoint. """
    document_date: str | Unset = UNSET
    """ Document date. """
    due_date: str | Unset = UNSET
    """ Due date. """
    validated_at: str | Unset = UNSET
    """ Validation timestamp, as returned by the read endpoint (e.g. `2020-01-01T00:00:00.000Z`). Setting it on a
    not-yet-validated document validates it: the strict required-field set (currency, amounts, document number,
    dates, vendor, legal entity) is enforced on that transition, not before. """
    line_items: (
        list[PutApi20261001ResourcesFinanceFinancialDocumentsIdBodyLineItemsItem] | Unset
    ) = UNSET
    """ Purchase-invoice line items. Rows are addressed by id, never by position: rows carrying an id update the
    matching line item, rows without an id create new ones, and persisted rows missing from the set are deleted.
    Send an empty array to remove all line items, or omit the field entirely to leave them untouched. When present
    they own the document totals. """
    legal_entity_id: str | Unset = UNSET
    """ Legal entity identifier of the financial document. """
    vendor_id: str | Unset = UNSET
    """ Vendor identifier (Finance contact). """
    document_type: PutApi20261001ResourcesFinanceFinancialDocumentsIdBodyDocumentType | Unset = (
        UNSET
    )
    """ Type of the financial document. One of `invoice`, `credit_note`, `receipt`. """
    parent_financial_document_id: str | Unset = UNSET
    """ For credit notes, the referenced original document by internal id (e.g. `135`). """
    additional_information: str | Unset = UNSET
    """ Free-text internal notes about the financial document. Kept unchanged when the field is absent. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company_id = self.company_id

        id = self.id

        status = self.status.value

        taxes = []
        for taxes_item_data in self.taxes:
            taxes_item = taxes_item_data.to_dict()
            taxes.append(taxes_item)

        currency = self.currency

        total_amount_cents = self.total_amount_cents

        document_number = self.document_number

        document_date = self.document_date

        due_date = self.due_date

        validated_at = self.validated_at

        line_items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.line_items, Unset):
            line_items = []
            for line_items_item_data in self.line_items:
                line_items_item = line_items_item_data.to_dict()
                line_items.append(line_items_item)

        legal_entity_id = self.legal_entity_id

        vendor_id = self.vendor_id

        document_type: str | Unset = UNSET
        if not isinstance(self.document_type, Unset):
            document_type = self.document_type.value if self.document_type is not None else None

        parent_financial_document_id = self.parent_financial_document_id

        additional_information = self.additional_information

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "company_id": company_id,
                "id": id,
                "status": status,
                "taxes": taxes,
            }
        )
        if currency is not UNSET:
            field_dict["currency"] = currency
        if total_amount_cents is not UNSET:
            field_dict["total_amount_cents"] = total_amount_cents
        if document_number is not UNSET:
            field_dict["document_number"] = document_number
        if document_date is not UNSET:
            field_dict["document_date"] = document_date
        if due_date is not UNSET:
            field_dict["due_date"] = due_date
        if validated_at is not UNSET:
            field_dict["validated_at"] = validated_at
        if line_items is not UNSET:
            field_dict["line_items"] = line_items
        if legal_entity_id is not UNSET:
            field_dict["legal_entity_id"] = legal_entity_id
        if vendor_id is not UNSET:
            field_dict["vendor_id"] = vendor_id
        if document_type is not UNSET:
            field_dict["document_type"] = document_type
        if parent_financial_document_id is not UNSET:
            field_dict["parent_financial_document_id"] = parent_financial_document_id
        if additional_information is not UNSET:
            field_dict["additional_information"] = additional_information

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.put_api_20261001_resources_finance_financial_documents_id_body_line_items_item import (
            PutApi20261001ResourcesFinanceFinancialDocumentsIdBodyLineItemsItem,
        )
        from ..models.put_api_20261001_resources_finance_financial_documents_id_body_taxes_item import (
            PutApi20261001ResourcesFinanceFinancialDocumentsIdBodyTaxesItem,
        )

        d = dict(src_dict)
        company_id = d.pop("company_id")

        id = d.pop("id")

        status = PutApi20261001ResourcesFinanceFinancialDocumentsIdBodyStatus(d.pop("status"))

        taxes = []
        _taxes = d.pop("taxes")
        for taxes_item_data in _taxes:
            taxes_item = PutApi20261001ResourcesFinanceFinancialDocumentsIdBodyTaxesItem.from_dict(
                taxes_item_data
            )

            taxes.append(taxes_item)

        currency = d.pop("currency", UNSET)

        total_amount_cents = d.pop("total_amount_cents", UNSET)

        document_number = d.pop("document_number", UNSET)

        document_date = d.pop("document_date", UNSET)

        due_date = d.pop("due_date", UNSET)

        validated_at = d.pop("validated_at", UNSET)

        _line_items = d.pop("line_items", UNSET)
        line_items: (
            list[PutApi20261001ResourcesFinanceFinancialDocumentsIdBodyLineItemsItem] | Unset
        ) = UNSET
        if _line_items is not UNSET:
            line_items = []
            for line_items_item_data in _line_items:
                line_items_item = (
                    PutApi20261001ResourcesFinanceFinancialDocumentsIdBodyLineItemsItem.from_dict(
                        line_items_item_data
                    )
                )

                line_items.append(line_items_item)

        legal_entity_id = d.pop("legal_entity_id", UNSET)

        vendor_id = d.pop("vendor_id", UNSET)

        _document_type = d.pop("document_type", UNSET)
        document_type: PutApi20261001ResourcesFinanceFinancialDocumentsIdBodyDocumentType | Unset
        if isinstance(_document_type, Unset):
            document_type = UNSET
        else:
            document_type = PutApi20261001ResourcesFinanceFinancialDocumentsIdBodyDocumentType(
                _document_type
            ) if _document_type is not None else None

        parent_financial_document_id = d.pop("parent_financial_document_id", UNSET)

        additional_information = d.pop("additional_information", UNSET)

        put_api_20261001_resources_finance_financial_documents_id_body = cls(
            company_id=company_id,
            id=id,
            status=status,
            taxes=taxes,
            currency=currency,
            total_amount_cents=total_amount_cents,
            document_number=document_number,
            document_date=document_date,
            due_date=due_date,
            validated_at=validated_at,
            line_items=line_items,
            legal_entity_id=legal_entity_id,
            vendor_id=vendor_id,
            document_type=document_type,
            parent_financial_document_id=parent_financial_document_id,
            additional_information=additional_information,
        )

        put_api_20261001_resources_finance_financial_documents_id_body.additional_properties = d
        return put_api_20261001_resources_finance_financial_documents_id_body

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
