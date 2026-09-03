from __future__ import annotations

import json
from collections.abc import Mapping
from io import BytesIO
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.post_api_20261001_resources_finance_financial_documents_body_document_type import (
    PostApi20261001ResourcesFinanceFinancialDocumentsBodyDocumentType,
)
from ..types import UNSET, File, Unset

if TYPE_CHECKING:
    from ..models.post_api_20261001_resources_finance_financial_documents_body_line_items_item import (
        PostApi20261001ResourcesFinanceFinancialDocumentsBodyLineItemsItem,
    )


T = TypeVar("T", bound="PostApi20261001ResourcesFinanceFinancialDocumentsBody")


@_attrs_define
class PostApi20261001ResourcesFinanceFinancialDocumentsBody:
    company_id: str
    """ Company identifier, refers to /api/me endpoint. """
    document_type: PostApi20261001ResourcesFinanceFinancialDocumentsBodyDocumentType
    """ Type of the financial document. One of `invoice`, `credit_note`, `receipt`. """
    file: File
    """ The document file to upload, the binary file. Required for purchase documents. """
    vendor_id: str | Unset = UNSET
    """ Vendor identifier (Finance contact). """
    legal_entity_id: str | Unset = UNSET
    """ Legal entity identifier of the financial document. """
    invoice_number: str | Unset = UNSET
    """ Document number. Must be unique per vendor for purchases; a duplicate returns a 422 with a machine-readable
    invoice_number error. """
    invoice_date: str | Unset = UNSET
    """ Document date. """
    due_date: str | Unset = UNSET
    """ Due date. """
    currency: str | Unset = UNSET
    """ Document currency (ISO 4217). """
    total_amount_cents: int | Unset = UNSET
    """ Total amount in cents. Ignored when line_items are provided, since the line items own the totals. """
    additional_information: str | Unset = UNSET
    """ Free-text internal notes about the financial document. """
    parent_financial_document_id: str | Unset = UNSET
    """ For credit notes, the referenced original document by internal id (exposed as parent_financial_document_id
    to match the read contract). Provide this or original_invoice_number. """
    original_invoice_number: str | Unset = UNSET
    """ For credit notes, the referenced original document by invoice number (resolved together with the vendor).
    """
    line_items: list[PostApi20261001ResourcesFinanceFinancialDocumentsBodyLineItemsItem] | Unset = (
        UNSET
    )
    """ Purchase-invoice line items. When present they own the document totals. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company_id = self.company_id

        document_type = self.document_type.value

        file = self.file.to_tuple()

        vendor_id = self.vendor_id

        legal_entity_id = self.legal_entity_id

        invoice_number = self.invoice_number

        invoice_date = self.invoice_date

        due_date = self.due_date

        currency = self.currency

        total_amount_cents = self.total_amount_cents

        additional_information = self.additional_information

        parent_financial_document_id = self.parent_financial_document_id

        original_invoice_number = self.original_invoice_number

        line_items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.line_items, Unset):
            line_items = []
            for line_items_item_data in self.line_items:
                line_items_item = line_items_item_data.to_dict()
                line_items.append(line_items_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "company_id": company_id,
                "document_type": document_type,
                "file": file,
            }
        )
        if vendor_id is not UNSET:
            field_dict["vendor_id"] = vendor_id
        if legal_entity_id is not UNSET:
            field_dict["legal_entity_id"] = legal_entity_id
        if invoice_number is not UNSET:
            field_dict["invoice_number"] = invoice_number
        if invoice_date is not UNSET:
            field_dict["invoice_date"] = invoice_date
        if due_date is not UNSET:
            field_dict["due_date"] = due_date
        if currency is not UNSET:
            field_dict["currency"] = currency
        if total_amount_cents is not UNSET:
            field_dict["total_amount_cents"] = total_amount_cents
        if additional_information is not UNSET:
            field_dict["additional_information"] = additional_information
        if parent_financial_document_id is not UNSET:
            field_dict["parent_financial_document_id"] = parent_financial_document_id
        if original_invoice_number is not UNSET:
            field_dict["original_invoice_number"] = original_invoice_number
        if line_items is not UNSET:
            field_dict["line_items[]"] = line_items

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("company_id", (None, str(self.company_id).encode(), "text/plain")))

        files.append(
            ("document_type", (None, str(self.document_type.value).encode(), "text/plain"))
        )

        files.append(("file", self.file.to_tuple()))

        if not isinstance(self.vendor_id, Unset):
            files.append(("vendor_id", (None, str(self.vendor_id).encode(), "text/plain")))

        if not isinstance(self.legal_entity_id, Unset):
            files.append(
                ("legal_entity_id", (None, str(self.legal_entity_id).encode(), "text/plain"))
            )

        if not isinstance(self.invoice_number, Unset):
            files.append(
                ("invoice_number", (None, str(self.invoice_number).encode(), "text/plain"))
            )

        if not isinstance(self.invoice_date, Unset):
            files.append(("invoice_date", (None, str(self.invoice_date).encode(), "text/plain")))

        if not isinstance(self.due_date, Unset):
            files.append(("due_date", (None, str(self.due_date).encode(), "text/plain")))

        if not isinstance(self.currency, Unset):
            files.append(("currency", (None, str(self.currency).encode(), "text/plain")))

        if not isinstance(self.total_amount_cents, Unset):
            files.append(
                ("total_amount_cents", (None, str(self.total_amount_cents).encode(), "text/plain"))
            )

        if not isinstance(self.additional_information, Unset):
            files.append(
                (
                    "additional_information",
                    (None, str(self.additional_information).encode(), "text/plain"),
                )
            )

        if not isinstance(self.parent_financial_document_id, Unset):
            files.append(
                (
                    "parent_financial_document_id",
                    (None, str(self.parent_financial_document_id).encode(), "text/plain"),
                )
            )

        if not isinstance(self.original_invoice_number, Unset):
            files.append(
                (
                    "original_invoice_number",
                    (None, str(self.original_invoice_number).encode(), "text/plain"),
                )
            )

        if not isinstance(self.line_items, Unset):
            for line_items_item_element in self.line_items:
                files.append(
                    (
                        "line_items[]",
                        (
                            None,
                            json.dumps(line_items_item_element.to_dict()).encode(),
                            "application/json",
                        ),
                    )
                )

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_api_20261001_resources_finance_financial_documents_body_line_items_item import (
            PostApi20261001ResourcesFinanceFinancialDocumentsBodyLineItemsItem,
        )

        d = dict(src_dict)
        company_id = d.pop("company_id")

        document_type = PostApi20261001ResourcesFinanceFinancialDocumentsBodyDocumentType(
            d.pop("document_type")
        )

        file = File(payload=BytesIO(d.pop("file")))

        vendor_id = d.pop("vendor_id", UNSET)

        legal_entity_id = d.pop("legal_entity_id", UNSET)

        invoice_number = d.pop("invoice_number", UNSET)

        invoice_date = d.pop("invoice_date", UNSET)

        due_date = d.pop("due_date", UNSET)

        currency = d.pop("currency", UNSET)

        total_amount_cents = d.pop("total_amount_cents", UNSET)

        additional_information = d.pop("additional_information", UNSET)

        parent_financial_document_id = d.pop("parent_financial_document_id", UNSET)

        original_invoice_number = d.pop("original_invoice_number", UNSET)

        _line_items = d.pop("line_items[]", UNSET)
        line_items: (
            list[PostApi20261001ResourcesFinanceFinancialDocumentsBodyLineItemsItem] | Unset
        ) = UNSET
        if _line_items is not UNSET:
            line_items = []
            for line_items_item_data in _line_items:
                line_items_item = (
                    PostApi20261001ResourcesFinanceFinancialDocumentsBodyLineItemsItem.from_dict(
                        line_items_item_data
                    )
                )

                line_items.append(line_items_item)

        post_api_20261001_resources_finance_financial_documents_body = cls(
            company_id=company_id,
            document_type=document_type,
            file=file,
            vendor_id=vendor_id,
            legal_entity_id=legal_entity_id,
            invoice_number=invoice_number,
            invoice_date=invoice_date,
            due_date=due_date,
            currency=currency,
            total_amount_cents=total_amount_cents,
            additional_information=additional_information,
            parent_financial_document_id=parent_financial_document_id,
            original_invoice_number=original_invoice_number,
            line_items=line_items,
        )

        post_api_20261001_resources_finance_financial_documents_body.additional_properties = d
        return post_api_20261001_resources_finance_financial_documents_body

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
